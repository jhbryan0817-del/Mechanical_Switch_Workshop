import pathlib,struct,json,collections,math
root=pathlib.Path(__file__).resolve().parents[1]
results=[]
for path in sorted((root/'stl').glob('*.stl')):
 data=path.read_bytes();n=struct.unpack_from('<I',data,80)[0];assert len(data)==84+50*n
 edges=collections.Counter();verts=set();vol=0;mins=[math.inf]*3;maxs=[-math.inf]*3
 for i in range(n):
  v=struct.unpack_from('<12fH',data,84+50*i)[3:12];p=[tuple(v[j:j+3]) for j in [0,3,6]];q=[tuple(round(x,4) for x in a) for a in p]
  for a in q:
   verts.add(a)
   for k,x in enumerate(a):mins[k]=min(mins[k],x);maxs[k]=max(maxs[k],x)
  for j in range(3):edges[tuple(sorted((q[j],q[(j+1)%3])))]+=1
  a,b,c=p;vol+=(a[0]*(b[1]*c[2]-b[2]*c[1])+a[1]*(b[2]*c[0]-b[0]*c[2])+a[2]*(b[0]*c[1]-b[1]*c[0]))/6
 bad=sum(v!=2 for v in edges.values())
 results.append({'file':path.name,'triangles':n,'closed_edge_check':bad==0,'nonmanifold_or_boundary_edges':bad,'positive_volume':vol>0,'volume_mm3':round(vol,3),'size_mm':[round(maxs[k]-mins[k],3) for k in range(3)]})
(root/'validation'/'stl_checks.json').write_text(json.dumps(results,indent=2))
print(json.dumps({'files':len(results),'all_closed':all(r['closed_edge_check'] for r in results),'all_positive_volume':all(r['positive_volume'] for r in results),'failures':[r for r in results if not r['closed_edge_check'] or not r['positive_volume']]},indent=2))
