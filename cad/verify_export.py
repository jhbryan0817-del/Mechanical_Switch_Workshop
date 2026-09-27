"""Geometry checks and exports. Run after build transaction completes."""
import adsk.core,adsk.fusion,os,json,math
OUT=os.path.abspath(os.path.join(os.path.dirname(__file__),'..'))
def run(_context: str):
 app=adsk.core.Application.get();doc=next(doc for doc in app.documents if doc.name=='Mechanical Switch');doc.activate()
 d=adsk.fusion.Design.cast(doc.products.itemByProductType('DesignProductType'));r=d.rootComponent;tm=adsk.fusion.TemporaryBRepManager.get()
 for o in r.occurrences:
  assert all(abs(a-b)<1e-9 for a,b in zip(o.transform2.asArray(),adsk.core.Matrix3D.create().asArray())), 'Verifier requires identity component transforms'
 allbs=[b for o in r.occurrences for b in o.component.bRepBodies]
 def group(b):return b.attributes.itemByName('MechanicalSwitch','group').value
 bs=[b for b in allbs if group(b) not in ('optional','keepout')]
 def intersect(a,b):
  if not a.boundingBox.intersects(b.boundingBox):return 0
  c=tm.copy(a);ok=tm.booleanOperation(c,tm.copy(b),adsk.fusion.BooleanTypes.IntersectionBooleanType)
  return c.volume*1000 if ok and c else 0
 def moved(b,x=0,angle=0):
  c=tm.copy(b);m=adsk.core.Matrix3D.create()
  if angle:m.setToRotation(math.radians(angle),adsk.core.Vector3D.create(1,0,0),adsk.core.Point3D.create(0,0,1.6))
  tm.transform(c,m)
  if x:
   m=adsk.core.Matrix3D.create();m.translation=adsk.core.Vector3D.create(x/10,0,0);tm.transform(c,m)
  return c
 hits=[]
 for i,a in enumerate(bs):
  for b in bs[i+1:]:
   vol=intersect(a,b)
   if vol>0.001:hits.append([a.name,b.name,round(vol,4)])
 adjustment=[]
 fixed=[b for b in bs if group(b)=='fixed']
 for x in range(-26,27,2):
  for b in bs:
   if group(b) in ('fixed','switch'):continue
   c=moved(b,x)
   for a in fixed:
    vol=intersect(a,c)
    if vol>0.001:adjustment.append({'x_mm':x,'a':a.name,'b':b.name,'overlap_mm3':round(vol,4)})
 sweep=[];contacts=[]
 rotor=[b for b in bs if group(b)=='rotor']
 static=[b for b in bs if group(b)!='rotor']
 for angle in range(-30,31,2):
  for b in rotor:
   c=moved(b,angle=angle)
   for a in static:
    vol=intersect(a,c)
    if vol>0.001:
     row={'angle_deg':angle,'a':a.name,'b':b.name,'overlap_mm3':round(vol,4)}
     if group(a)=='switch' and b.name.startswith('04_'):contacts.append(row)
     else:sweep.append(row)
 clearance=[] # Unmeasured PCB component envelope is no longer a modeled body.
 report={'version':'0.3','neutral_collisions_mm3':hits,'x_sample_mm':list(range(-26,27,2)),
         'adjustment_collisions':adjustment,'angle_samples_deg':list(range(-30,31,2)),
         'rigid_sweep_collisions':sweep,'required_switch_displacement_against_static_reference':contacts,
         'board_keepout_collisions_mm3':None,
         'scope':'Rigid discrete geometric samples. Switch motion, facing compliance, strength, omitted hardware and real connector shapes are not simulated. Contact intersections are not clearance passes.',
         'all_bodies_solid':all(b.isSolid and b.lumps.count==1 for b in allbs),
         'body_count':len(allbs),'component_count':r.occurrences.count}
 with open(os.path.join(OUT,'validation','fusion_checks.json'),'w') as f:json.dump(report,f,indent=2)
 assert not hits and not adjustment and not sweep and not clearance, 'Interference found; see fusion_checks.json'
 # Internal overview from left side to expose the shaft and single contact insert.
 for b in allbs:
  b.isLightBulbOn=group(b) not in ('optional','keepout') and not b.name.startswith(('05_','06_','REF_Waveshare'))
 cam=app.activeViewport.camera;cam.viewOrientation=adsk.core.ViewOrientations.IsoTopLeftViewOrientation;app.activeViewport.camera=cam;app.activeViewport.refresh();adsk.doEvents();app.activeViewport.fit();app.activeViewport.refresh();adsk.doEvents()
 app.activeViewport.saveAsImageFile(os.path.join(OUT,'assets','fusion-mechanism.png'),1600,1200)
 # Closeup with non-essential structure hidden for explaining the direct drive.
 for b in allbs:
  b.isLightBulbOn=group(b) in ('rotor','switch') or b.name.startswith(('REF_STS','REF_servo_output'))
 app.activeViewport.refresh();adsk.doEvents();app.activeViewport.fit();app.activeViewport.refresh();adsk.doEvents();app.activeViewport.saveAsImageFile(os.path.join(OUT,'assets','fusion-direct-drive.png'),1400,1100)
 # Export neutral assembly, with optional pads and reference component keepout hidden.
 for b in allbs:b.isLightBulbOn=not b.name.startswith('06_')
 cam=app.activeViewport.camera
 cam.cameraType=adsk.core.CameraTypes.OrthographicCameraType
 cam.eye=adsk.core.Point3D.create(-18,-22,20)
 cam.target=adsk.core.Point3D.create(0.65,0,2.2)
 cam.upVector=adsk.core.Vector3D.create(0,1,0)
 cam.isSmoothTransition=False;cam.setExtents(20,15)
 app.activeViewport.camera=cam;app.activeViewport.refresh();adsk.doEvents()
 app.activeViewport.saveAsImageFile(os.path.join(OUT,'assets','fusion-assembly.png'),1600,1200)
 results={}
 results['f3d']=d.exportManager.execute(d.exportManager.createFusionArchiveExportOptions(os.path.join(OUT,'cad','Mechanical_Switch_v03.f3d')))
 results['step']=d.exportManager.execute(d.exportManager.createSTEPExportOptions(os.path.join(OUT,'cad','Mechanical_Switch_v03.step')))
 if not results['step'] and os.path.exists(os.path.join(OUT,'cad','Mechanical_Switch_v03.step')):os.remove(os.path.join(OUT,'cad','Mechanical_Switch_v03.step'))
 with open(os.path.join(OUT,'validation','exports.json'),'w') as f:json.dump(results,f,indent=2)
 assert results['f3d']
