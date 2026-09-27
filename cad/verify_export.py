import adsk.core,adsk.fusion,json,os
OUT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..')) # Or set your output folder explicitly for MCP.
def run(_context: str):
 app=adsk.core.Application.get();d=adsk.fusion.Design.cast(app.activeProduct);r=d.rootComponent;tm=adsk.fusion.TemporaryBRepManager.get()
 bs=[b for b in r.bRepBodies if not b.name.startswith('REF_') and 'coupon' not in b.name]
 collisions=[]
 for i,a in enumerate(bs):
  for b in bs[i+1:]:
   if not a.boundingBox.intersects(b.boundingBox):continue
   c=tm.copy(a)
   ok=tm.booleanOperation(c,tm.copy(b),adsk.fusion.BooleanTypes.IntersectionBooleanType)
   if ok and c and c.volume>1e-6:collisions.append([a.name,b.name,round(c.volume*1000,4)])
 inventory=[{'name':b.name,'solid':b.isSolid,'volume_mm3':b.volume*1000,'bounds_mm':[[p.x*10,p.y*10,p.z*10] for p in [b.boundingBox.minPoint,b.boundingBox.maxPoint]]} for b in r.bRepBodies]
 open(os.path.join(OUT,'validation','fusion_checks.json'),'w').write(json.dumps({'neutral_intersections_mm3':collisions,'inventory':inventory},indent=2))
 results={}
 results['f3d']=d.exportManager.execute(d.exportManager.createFusionArchiveExportOptions(os.path.join(OUT,'cad','Mechanical_Switch_v01.f3d')))
 results['step']=d.exportManager.execute(d.exportManager.createSTEPExportOptions(os.path.join(OUT,'cad','Mechanical_Switch_v01.step')))
 if not results['step'] and os.path.exists(os.path.join(OUT,'cad','Mechanical_Switch_v01.step')):os.remove(os.path.join(OUT,'cad','Mechanical_Switch_v01.step'))
 open(os.path.join(OUT,'validation','exports.json'),'w').write(json.dumps(results,indent=2))

