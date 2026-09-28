"""v0.3 direct rocker actuator. Dimensions mm; Z=0 faceplate front; X horizontal.
Run in an empty Mechanical Switch design. Export in a second transaction.
Named direct solids are editable; these constants/source drive dimensional edits.
"""
import adsk.core, adsk.fusion, os, json, math, struct
OUT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
REPLACE_EXISTING = False
PILOT=2.7
X_TRAVEL=52.0
AXIS_Z=16.0
PAD_CONTACT_Z=7.3 # rigid land; optional 0.5 mm soft facing gives 6.8 mm contact

def run(_context: str):
 app=adsk.core.Application.get()
 doc=next(doc for doc in app.documents if doc.name=='Mechanical Switch')
 doc.activate();d=adsk.fusion.Design.cast(doc.products.itemByProductType('DesignProductType'));root=d.rootComponent
 assert doc.name=='Mechanical Switch'
 assert REPLACE_EXISTING or root.occurrences.count==0
 if not REPLACE_EXISTING: assert root.bRepBodies.count==0, 'Archive existing design before replacement'
 d.designIntent=adsk.fusion.DesignIntentTypes.HybridDesignIntentType
 d.designType=adsk.fusion.DesignTypes.DirectDesignType
 if REPLACE_EXISTING:
  for o in list(root.occurrences): o.deleteMe()
  for b in list(root.bRepBodies): b.deleteMe()
  for sk in list(root.sketches): sk.deleteMe()
  for pl in list(root.constructionPlanes): pl.deleteMe()
 for sub in ('cad','stl','assets','validation'): os.makedirs(os.path.join(OUT,sub),exist_ok=True)
 tm=adsk.fusion.TemporaryBRepManager.get()
 P=lambda x,y,z:adsk.core.Point3D.create(x/10,y/10,z/10)
 V=lambda x,y,z:adsk.core.Vector3D.create(x,y,z)
 def box(x0,y0,z0,x1,y1,z1):
  assert x1>x0 and y1>y0 and z1>z0
  return tm.createBox(adsk.core.OrientedBoundingBox3D.create(P((x0+x1)/2,(y0+y1)/2,(z0+z1)/2),V(1,0,0),V(0,1,0),(x1-x0)/10,(y1-y0)/10,(z1-z0)/10))
 def cyl(x,y,z0,z1,r): return tm.createCylinderOrCone(P(x,y,z0),r/10,P(x,y,z1),r/10)
 def xcyl(x0,x1,y,z,r): return tm.createCylinderOrCone(P(x0,y,z),r/10,P(x1,y,z),r/10)
 def op(a,b,cut=False):
  assert tm.booleanOperation(a,b,adsk.fusion.BooleanTypes.DifferenceBooleanType if cut else adsk.fusion.BooleanTypes.UnionBooleanType)
  return a
 def rr(x0,y0,z0,x1,y1,z1,r):
  a=box(x0+r,y0,z0,x1-r,y1,z1);op(a,box(x0,y0+r,z0,x1,y1-r,z1))
  for x in (x0+r,x1-r):
   for y in (y0+r,y1-r): op(a,cyl(x,y,z0,z1,r))
  return a
 def hole(a,x,y,z0,z1,diam):return op(a,cyl(x,y,z0,z1,diam/2),True)
 def slot(a,x0,x1,y,z0,z1,diam):
  s=box(x0,y-diam/2,z0,x1,y+diam/2,z1)
  op(s,cyl(x0,y,z0,z1,diam/2));op(s,cyl(x1,y,z0,z1,diam/2));return op(a,s,True)
 def xslot(a,x0,x1,y0,y1,z,diam):
  s=box(x0,y0,z-diam/2,x1,y1,z+diam/2)
  op(s,xcyl(x0,x1,y0,z,diam/2));op(s,xcyl(x0,x1,y1,z,diam/2));return op(a,s,True)
 manifest=[]; components={}
 def target(name):
  if name.startswith("REF_STS") or name.startswith("REF_servo") or name.startswith("REF_metal"): return "07 Servo and stock metal horn"
  if name.startswith("REF_Waveshare"): return "08 ESP32 servo driver"
  if name.startswith("REF_"): return "09 Reference switch board"
  return name
 def meshout(b,name):
  calc=b.meshManager.createMeshCalculator();calc.surfaceTolerance=0.001
  mesh=calc.calculate();pts=mesh.nodeCoordinates;ids=mesh.nodeIndices;bb=b.boundingBox
  ox=bb.minPoint.x;oy=bb.minPoint.y;oz=bb.minPoint.z
  with open(os.path.join(OUT,'stl',name+'.stl'),'wb') as f:
   f.write(b'Mechanical Switch v0.3; units mm'.ljust(80,b' '));f.write(struct.pack('<I',mesh.triangleCount))
   for i in range(0,len(ids),3):
    p=[pts[ids[i+j]] for j in range(3)];n=p[0].vectorTo(p[1]).crossProduct(p[0].vectorTo(p[2]));n.normalize()
    vals=[n.x,n.y,n.z]+[v for pp in p for v in ((pp.x-ox)*10,(pp.y-oy)*10,(pp.z-oz)*10)]
    f.write(struct.pack('<12fH',*vals,0))
 def part(name,body,color='Gray',printable=True,visible=True,group='carriage'):
  key=target(name)
  if key not in components:
   occ=root.occurrences.addNewComponent(adsk.core.Matrix3D.create());occ.component.name=key;components[key]=occ.component
  b=components[key].bRepBodies.add(body);b.name=name
  assert b.isSolid and b.lumps.count==1, name+' must be one connected solid'
  appearance=app.materialLibraries.itemByName('Fusion Appearance Library').appearances.itemByName('Plastic - Matte ('+color+')')
  if appearance:b.appearance=appearance
  b.isLightBulbOn=visible;b.attributes.add('MechanicalSwitch','group',group);bb=b.boundingBox
  manifest.append({'name':name,'printable':printable,'group':group,'visible':visible,'volume_mm3':b.volume*1000,'bounds_mm':[[p.x*10,p.y*10,p.z*10] for p in (bb.minPoint,bb.maxPoint)]})
  if printable:meshout(b,name)
  return b
 # Fixed base. Only the six tape lands bond to faceplate plastic.
 a=rr(-43,-43,1,43,43,2,4);op(a,rr(-37,-29,0.9,37,29,2.1,3),True)
 for x in (-31,31):hole(a,x,0,0.9,2.1,12)
 for y in (-39,39):
  op(a,rr(-38,y-3,1,38,y+3,11,2));hole(a,0,y,3,11.1,PILOT)
 part('01_mounting_frame',a,'White',group='fixed')
 # Internal carriage, sliding over the base on two front-access slot screws.
 a=box(-30,-43,11.3,48,-35,14.3);op(a,box(-30,35,11.3,48,43,14.3))
 for x in (-30,47.4):op(a,box(x,-42,11.3,x+2,42,14.3))
 for y in (-39,39):slot(a,-X_TRAVEL/2,X_TRAVEL/2,y,11.2,14.4,3.4)
 op(a,box(10,-15,2.3,49,34,3.3))
 op(a,box(47.4,-15,3.3,49,42,28.7))
 op(a,box(10,-15,3.3,49,-13,28.7))
 op(a,box(10,33.4,3.3,49,34.8,28.7))
 for x,y in ((16,-18),(43,37)):
  op(a,cyl(x,y,11.3,28.7,3.6))
  if y<0:op(a,box(12,-18,11.3,20,-14,15.3))
  hole(a,x,y,20.7,28.8,PILOT)
 for x,y in ((-25,-25),(-25,25),(44,-25),(50,25)):
  if x==50:
   post=cyl(x,y,11.3,33,3.1);op(post,box(40,y-4,11.2,47.4,y+4,28.7),True);op(a,post)
  elif x<0:op(a,box(-30,y-4,11.3,-21,y+4,33))
  else:op(a,box(41,y-3,11.3,48,y+3,33))
  hole(a,x,y,25,33.1,PILOT)
 for y0,y1 in ((-42.4,-35.6),(35.6,42.4)):op(a,box(-31,y0,2.2,50,y1,11.2),True)
 part('02_sliding_servo_chassis',a)
 # Servo retention cap: foam shims take up the body clearance.
 a=box(12,-21.5,29,47,40.5,31);op(a,box(17,-10,28.9,42,29,31.1),True)
 for x,y in ((16,-18),(43,37)):hole(a,x,y,28.9,31.1,3.4)
 op(a,box(46.5,21.5,28.9,54,28.5,31.1),True)
 part('03_servo_clamp',a)
 # One rigid shoe: 6.2 mm horn web, broad 5 mm bridge, two integral contact lands.
 # Slots and stock metal spline are retained; no TPU leaf, stem or central screw.
 a=box(0.5,-12,12,6.7,12,26)
 op(a,rr(-5,-9,11,5,9,16,1.5))
 for y in (-6.5,6.5):op(a,rr(-5,y-2,PAD_CONTACT_Z,3,y+2,12,1))
 for y in (-7,7):op(a,xcyl(-5,6.7,y,AXIS_Z,4.2))
 op(a,xcyl(-5.1,6.8,0,AXIS_Z,3.5),True)
 for sign in (-1,1):
  ys=sorted((sign*6,sign*8));xslot(a,-5.1,6.8,ys[0],ys[1],AXIS_Z,3.4)
 part('04_integral_rocking_shoe',a,'Yellow',group='rotor')
 # Removable controller shelf above the servo. Pins fit board holes, ties retain.
 a=rr(-29,-29,33.3,54,29,35.3,3);op(a,rr(-14,-7,33.2,35,7,35.4,2),True)
 op(a,rr(-19,17,33.2,34,23,35.4,2),True)
 for x,y in ((-25,-25),(-25,25),(44,-25),(50,25)):hole(a,x,y,33.2,35.4,3.4)
 for x in (-16.5,41.5):
  for y in (-11.5,11.5):
   op(a,cyl(x,y,35.3,37.3,2.7));op(a,cyl(x,y,37.3,39.3,1.2))
   slot(a,x-2,x+2,y+(4.5 if y>0 else -4.5),33.2,35.4,1.8)
 part('05_controller_shelf',a)
 # Rounded enclosure, two millimetre walls, broad side connector access.
 a=rr(-33,-46,2.3,56,46,53,5);op(a,rr(-31,-44,2.2,54,44,51,3),True)
 for y0,y1 in ((-42.4,-35.6),(35.6,42.4)):op(a,box(-34,y0,2.2,57,y1,11.6),True)
 for x0,x1 in ((-34,-30),(53,57)):op(a,box(x0,-18,36,x1,18,49),True)
 for x,y in ((-25,-25),(-25,25),(44,-25),(50,25)):
  op(a,cyl(x,y,35.6,51.2,3.5));hole(a,x,y,35.5,53.1,3.4);hole(a,x,y,50.5,53.1,6.2)
 for y in (-7.5,-2.5,2.5,7.5):slot(a,-12,29,y,50.9,53.1,1.8)
 part('06_rounded_enclosure',a,'White',visible=False)
 # Simplified references, never print. Small rocker size comes from photo ratio.
 part('REF_faceplate_86mm',rr(-43,-43,-9,43,43,0,3),'White',False,group='fixed')
 part('REF_short_rounded_rocker_17mm_assumption',rr(-8.5,-8.5,0,8.5,8.5,6,4),'White',False,group='switch')
 part('REF_STS3215_body_45p2x24p7x35',box(12,-12.35,3.65,47,32.85,28.35),'Black',False)
 part('REF_servo_output_axis',xcyl(8.9,12,0,AXIS_Z,3),'Gray',False)
 a=xcyl(6.7,8.7,0,AXIS_Z,9);op(a,xcyl(6.6,8.8,0,AXIS_Z,1.6),True)
 for y in (-7,7):op(a,xcyl(6.6,8.8,y,AXIS_Z,1.5),True)
 part('REF_metal_horn_verify_hardware',a,'Gray',False,group='rotor')
 a=box(-20,-15,37.3,45,15,38.9)
 for x in (-16.5,41.5):
  for y in (-11.5,11.5):hole(a,x,y,37.2,39,2.75)
 part('REF_Waveshare_PCB_65x30',a,'Green',False)
 data={'version':'0.3','units':'mm','axis':[1,0,0],'axis_origin_mm':[0,0,AXIS_Z],'horizontal_travel_mm':X_TRAVEL,'nominal_tape_area_mm2':1500,'component_count':len(components),'contact_land_z_mm':PAD_CONTACT_Z,'assumptions':{'rocker_mm':[17,17,6],'servo_shaft_offset_mm':12.35,'pcb_component_height_mm':10.1},'parts':manifest}
 with open(os.path.join(OUT,'validation','build_manifest.json'),'w') as f:json.dump(data,f,indent=2)
 cam=app.activeViewport.camera
 cam.cameraType=adsk.core.CameraTypes.OrthographicCameraType
 cam.eye=adsk.core.Point3D.create(-18,-22,20)
 cam.target=adsk.core.Point3D.create(0.65,0,2.2)
 cam.upVector=adsk.core.Vector3D.create(0,1,0)
 cam.isSmoothTransition=False;cam.setExtents(20,15)
 app.activeViewport.camera=cam;app.activeViewport.refresh();adsk.doEvents()
 app.activeViewport.saveAsImageFile(os.path.join(OUT,'assets','fusion-assembly.png'),1600,1200)







 # Explicit completion marker: some Fusion MCP versions suppress print output.
 with open(os.path.join(OUT,'validation','build_complete.json'),'w') as f:json.dump({'version':'0.3','components':len(components),'bodies':len(manifest)},f)


