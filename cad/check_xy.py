import adsk.core,adsk.fusion,json,os
OUT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..')) # Or set your output folder explicitly for MCP.
def run(_context: str):
 d=adsk.fusion.Design.cast(adsk.core.Application.get().activeProduct);r=d.rootComponent;tm=adsk.fusion.TemporaryBRepManager.get()
 bs=[b for b in r.bRepBodies if not b.name.startswith('REF_') and 'coupon' not in b.name]
 results=[]
 for x in [-28.5,0,28.5]:
  for y in [-12,0,12]:
   bodies=[]
   for b in bs:
    t=tm.copy(b);mat=adsk.core.Matrix3D.create()
    fixed=b.name.startswith(('01_','12_'))
    mat.translation=adsk.core.Vector3D.create(0 if fixed else x/10,0 if fixed or b.name.startswith('02_') else y/10,0)
    tm.transform(t,mat);bodies.append((b.name,t))
   hits=[]
   for i,(an,a) in enumerate(bodies):
    for bn,b in bodies[i+1:]:
     if not a.boundingBox.intersects(b.boundingBox):continue
     c=tm.copy(a);ok=tm.booleanOperation(c,tm.copy(b),adsk.fusion.BooleanTypes.IntersectionBooleanType)
     if ok and c and c.volume>1e-6:hits.append([an,bn,round(c.volume*1000,4)])
   results.append({'x_offset_mm':x,'y_offset_mm':y,'intersections_mm3':hits})
 open(os.path.join(OUT,'validation','xy_sample_checks.json'),'w').write(json.dumps(results,indent=2))

