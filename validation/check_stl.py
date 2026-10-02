"""Validate current binary STLs against their Fusion export manifest (stdlib only)."""
import collections
import hashlib
import json
import math
import pathlib
import struct

ROOT = pathlib.Path(__file__).resolve().parents[1]

def check(path, source):
    data = path.read_bytes()
    count = struct.unpack_from('<I', data, 80)[0]
    assert len(data) == 84 + 50*count, f'Invalid binary STL length: {path.name}'
    edges = collections.defaultdict(list)
    adjacent = [set() for _ in range(count)]
    volume = 0.0
    mins, maxs = [math.inf]*3, [-math.inf]*3
    degenerates = 0
    finite = True
    normals_match = True
    for i in range(count):
        values = struct.unpack_from('<12fH', data, 84+50*i)
        normal = values[:3]
        a,b,c = points = [tuple(values[j:j+3]) for j in (3,6,9)]
        finite &= all(math.isfinite(x) for x in values[:12])
        u = [b[k]-a[k] for k in range(3)]
        v = [c[k]-a[k] for k in range(3)]
        cross = (u[1]*v[2]-u[2]*v[1], u[2]*v[0]-u[0]*v[2], u[0]*v[1]-u[1]*v[0])
        degenerates += sum(x*x for x in cross) < 1e-16
        normals_match &= sum(normal[k]*cross[k] for k in range(3)) > 0
        for p in points:
            for k in range(3):
                mins[k], maxs[k] = min(mins[k],p[k]), max(maxs[k],p[k])
        for j in range(3):
            p,q = points[j], points[(j+1)%3]
            edges[tuple(sorted((p,q)))].append((i,p<q))
        volume += (a[0]*(b[1]*c[2]-b[2]*c[1])+a[1]*(b[2]*c[0]-b[0]*c[2])+a[2]*(b[0]*c[1]-b[1]*c[0]))/6
    bad_edges = sum(len(rows)!=2 for rows in edges.values())
    winding_errors = sum(len(rows)==2 and rows[0][1]==rows[1][1] for rows in edges.values())
    for rows in edges.values():
        if len(rows)==2:
            a,b = rows[0][0],rows[1][0]
            adjacent[a].add(b); adjacent[b].add(a)
    remaining = set(range(count))
    shells = 0
    while remaining:
        shells += 1
        stack = [remaining.pop()]
        while stack:
            for neighbor in adjacent[stack.pop()]:
                if neighbor in remaining:
                    remaining.remove(neighbor); stack.append(neighbor)
    dimensions = [maxs[k]-mins[k] for k in range(3)]
    volume_error = abs(volume-source['cad_volume_mm3'])/source['cad_volume_mm3']*100
    cad_bounds = source['assembly_bounds_mm']
    cad_size = [cad_bounds[1][k]-cad_bounds[0][k] for k in range(3)]
    rotated_cad_size = [sum(abs(row[j])*cad_size[j] for j in range(3)) for row in source['rotation_matrix']]
    dimension_match = all(abs(dimensions[k]-rotated_cad_size[k])<0.01 for k in range(3))
    digest = hashlib.sha256(data).hexdigest()
    passed = finite and not degenerates and not bad_edges and not winding_errors and normals_match and shells==1 and volume>0 and volume_error<1 and dimension_match and abs(mins[2])<0.001 and digest==source['sha256']
    return dict(file=path.name,passed=passed,triangles=count,finite_coordinates=finite,degenerate_triangles=degenerates,nonmanifold_or_boundary_edges=bad_edges,winding_errors=winding_errors,normals_match_winding=normals_match,connected_shells=shells,volume_mm3=round(volume,5),cad_volume_error_percent=round(volume_error,5),size_mm=[round(x,5) for x in dimensions],minimum_z_mm=mins[2],dimensions_match_manifest=dimension_match,sha256=digest)

if __name__ == '__main__':
    manifest = json.loads((ROOT/'validation'/'exports.json').read_text())
    sources = {p['file']:p for p in manifest['parts']}
    files = sorted((ROOT/'stl').glob('*.stl'))
    assert {p.name for p in files} == set(sources), 'Current STL directory must match the three manifest entries'
    results = [check(p,sources[p.name]) for p in files]
    report = dict(export_date=manifest['export_date'],all_passed=all(p['passed'] for p in results),checks=results,limits='No self-intersection analysis, slicing, support analysis or physical print/fit validation.')
    (ROOT/'validation'/'stl_checks.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(report,indent=2))
    raise SystemExit(0 if report['all_passed'] else 1)
