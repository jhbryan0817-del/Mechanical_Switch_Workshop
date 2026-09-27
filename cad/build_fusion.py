import adsk.core, adsk.fusion, os, json, math, struct
OUT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..')) # Or set your output folder explicitly for MCP.
# All engineering dimensions are mm; Fusion internal geometry uses cm.
PILOT=2.7

def run(_context: str):
 app=adsk.core.Application.get(); d=adsk.fusion.Design.cast(app.activeProduct)
 assert app.activeDocument.name.startswith('Mechanical Switch'), 'Activate Mechanical Switch first'
 root=d.rootComponent
 assert root.occurrences.count==0 and root.bRepBodies.count==0, 'Run in an empty design only'
 d.designType=adsk.fusion.DesignTypes.DirectDesignType
 tm=adsk.fusion.TemporaryBRepManager.get()
 P=lambda x,y,z:adsk.core.Point3D.create(x/10,y/10,(z+9)/10)
 V=lambda x,y,z:adsk.core.Vector3D.create(x,y,z)
 def box(x0,y0,z0,x1,y1,z1):
  return tm.createBox(adsk.core.OrientedBoundingBox3D.create(P((x0+x1)/2,(y0+y1)/2,(z0+z1)/2),V(1,0,0),V(0,1,0),(x1-x0)/10,(y1-y0)/10,(z1-z0)/10))
 def cyl(x,y,z0,z1,r):
  return tm.createCylinderOrCone(P(x,y,z0),r/10,P(x,y,z1),r/10)
 def op(a,b,cut=False):
  assert tm.booleanOperation(a,b,adsk.fusion.BooleanTypes.DifferenceBooleanType if cut else adsk.fusion.BooleanTypes.UnionBooleanType)
  return a
 def hole(a,x,y,z0,z1,diam):return op(a,cyl(x,y,z0,z1,diam/2),True)
 def slot(a,x0,y0,x1,y1,z0,z1,diam):
  r=diam/2
  if y0==y1:s=box(x0,y0-r,z0,x1,y0+r,z1)
  else:s=box(x0-r,y0,z0,x0+r,y1,z1)
  op(s,cyl(x0,y0,z0,z1,r));op(s,cyl(x1,y1,z0,z1,r))
  return op(a,s,True)
 def meshout(b,name):
  calc=b.meshManager.createMeshCalculator();calc.surfaceTolerance=0.001
  mesh=calc.calculate();pts=mesh.nodeCoordinates;ids=mesh.nodeIndices
  # Translate each export to a convenient origin; mm units, no scale guessing.
  bb=b.boundingBox;ox=bb.minPoint.x;oy=bb.minPoint.y;oz=bb.minPoint.z
  with open(os.path.join(OUT,'stl',name+'.stl'),'wb') as f:
   f.write(b'Mechanical Switch Workshop; millimetres'.ljust(80,b' '));f.write(struct.pack('<I',mesh.triangleCount))
   for i in range(0,len(ids),3):
    p=[pts[ids[i+j]] for j in range(3)];u=p[0].vectorTo(p[1]);v=p[0].vectorTo(p[2]);n=u.crossProduct(v);n.normalize()
    vals=[n.x,n.y,n.z]+[q for pp in p for q in [(pp.x-ox)*10,(pp.y-oy)*10,(pp.z-oz)*10]]
    f.write(struct.pack('<12fH',*vals,0))
 manifest=[]
 def part(name,body,printable=True):
  c=root
  b=c.bRepBodies.add(body);b.name=name
  color='White' if name.startswith('REF_87') else ('Black' if name.startswith('REF_STS') or name.startswith('08') else ('Green' if name.startswith('REF_Waveshare') else ('Yellow' if name.startswith(('06','07','11','REF_tape')) else ('Blue' if name.startswith(('01','09','10','12')) else 'Gray'))))
  b.appearance=app.materialLibraries.itemByName('Fusion Appearance Library').appearances.itemByName('Plastic - Matte ('+color+')')
  bb=b.boundingBox
  manifest.append({'name':name,'printable':printable,'volume_mm3':b.volume*1000,'bounds_mm':[[p.x*10,p.y*10,p.z*10] for p in [bb.minPoint,bb.maxPoint]],'solid':b.isSolid})
  if printable: meshout(b,name)
  return c,b
 # Faceplate-bonding bezel. Wall z=0, nominal plate front z=10; rear lands z=11.
 a=box(-49,-49,2,49,49,6);op(a,box(-34.5,-31.5,1,34.5,31.5,7),True)
 # Screw-cap reliefs open into the main window.
 for x in [-39,39]:op(a,box(x-6,-13,1,x+6,13,7),True)
 for y in [-40,40]:
  for x in [-44,44]:op(a,box(x-5,y-5,6,x+5,y+5,11))
  op(a,box(-49,y-5,11,49,y+5,15))
  slot(a,-28.5,y,28.5,y,10.9,15.1,3.4)
 # Sidecar pilots are blind from front; wall-side tape plane stays closed.
 for x in [-45,45]:
  for y in [-16,16]:
   op(a,cyl(x,y,6,11,4));hole(a,x,y,2.5,11.2,PILOT)
 part('01_faceplate_tape_frame',a)
 # Bridge uses two M3 bolts and sliding M3 nuts under raised rails.
 a=box(-32,-45,15.3,32,45,19.3);op(a,box(-20,-35,15,20,35,20),True)
 for y in [-40,40]:hole(a,0,y,15,20,3.4)
 for x in [-26,26]:
  for y in [-20,20]:slot(a,x,y-12,x,y+12,15,20,3.4)
 part('02_xy_bridge',a)
 # Cassette lower guide; four M3 bolt positions match the bridge's Y slots.
 a=box(-32,-37,19.6,32,37,23.6)
 for x in [-26,26]:
  for y in [-20,20]:hole(a,x,y,19,24,3.4)
 for y in [-11,11]:hole(a,0,y,19,24,5.3)
 # Four load-bearing pillars, clear of all adjustment screw heads.
 for x in [-24,24]:
  for y in [-31,31]:
   op(a,box(x-4,y-4,23.6,x+4,y+4,49.0));hole(a,x,y,38,49.2,PILOT)
 part('03_lower_guide_and_pillars',a)
 # Upper cup guide attaches halfway up pillars using a drop-in fit and M3 side-free vertical screws.
 # A removable plate seats on four dedicated spacer sleeves around the pillars.
 a=box(-28,-35,29,28,35,32)
 for x in [-24,24]:
  for y in [-31,31]:op(a,box(x-4.3,y-4.3,28,x+4.3,y+4.3,33),True)
 for y in [-11,11]:hole(a,0,y,28,33,13.5)
 # Open sides relieve guide drag and allow spring inspection.
 op(a,box(-17,-6,28,17,6,33),True)
 part('04_follower_guide',a)
 # Four separate sleeves support guide at z29; top cradle retains it through pillars.
 for idx,(x,y) in enumerate([(-24,-31),(24,-31),(-24,31),(24,31)]):
  a=box(x-6,y-6,23.6,x+6,y+6,29);op(a,box(x-4.2,y-4.2,23,x+4.2,y+4.2,30),True)
  part('05_guide_spacer_'+str(idx+1),a)
  a=box(x-6,y-6,32,x+6,y+6,49.3);op(a,box(x-4.2,y-4.2,31,x+4.2,y+4.2,50),True)
  part('05b_guide_retainer_'+str(idx+1),a)
 for idx,y in enumerate([-11,11]):
  # Stem flange is inside the cup. A spring above it transmits cam load.
  a=cyl(0,y,6.8,27.6,2.4);op(a,cyl(0,y,27.6,29.6,4.8));hole(a,0,y,6.7,22.0,2.7)
  groove=cyl(0,y,18.5,19.4,2.5);op(groove,cyl(0,y,18.4,19.5,1.9),True);op(a,groove,True)
  part('06_contact_stem_'+str(idx+1),a)
  clip=cyl(0,y,18.5,19.3,4.5);hole(clip,0,y,18.4,19.4,3.9);op(clip,box(-1.65,y,18.4,1.65,y+5,19.4),True)
  part('06b_stem_retaining_clip_'+str(idx+1),clip)
  # Cup roof z36.6 gives 7mm installed length for primary spring.
  a=cyl(0,y,28.6,38.6,6.5);hole(a,0,y,28.5,36.6,10.2)
  op(a,cyl(0,y,38.6,44,1.5))
  part('07_spring_cup_'+str(idx+1),a)
  # TPU flat pad has a blind M3 head pocket; bond onto screw head after adjustment.
  a=box(-5,y-3.5,2.8,5,y+3.5,6.3);hole(a,0,y,4.3,6.4,5.8)
  part('08_tpu_shoe_'+str(idx+1),a)
 # Servo cradle: measured envelope only, output-axis offset is a configurable assumption.
 a=box(-32,-37,49.3,32,37,52.3);hole(a,0,0,49,53,23)
 for x in [-24,24]:
  for y in [-31,31]:hole(a,x,y,49,53,3.4)
 # Open cradle, no unverified manufacturer mounting-ear holes.
 for x in [-15.8,15.8]:op(a,box(x-2,-14,52.3,x+2,34,87.6))
 op(a,box(-17.8,34,52.3,17.8,37,87.6))
 for x in [-15.8,15.8]:
  for y in [-9,29]:hole(a,x,y,77,88,PILOT)
 for deg in [-55,55]:
  t=math.radians(deg);op(a,cyl(23*math.cos(t),23*math.sin(t),44,49.3,2))
 part('09_servo_cradle',a)
 a=box(-20,-14,87.9,20,37,91.9)
 op(a,box(-10,-4,87,10,24,93),True)
 for x in [-15.8,15.8]:
  for y in [-9,29]:hole(a,x,y,87,93,3.4)
 part('10_servo_retaining_cap',a)
 # Cam uses four holes on an assumed 14mm bolt circle: verify physical disc first.
 a=cyl(0,0,44,47,19);op(a,box(18,-1.5,44,24,1.5,47));hole(a,0,0,43,48,7)
 for deg in [0,90,180,270]:
  t=math.radians(deg);x,y=7*math.cos(t),7*math.sin(t)
  hole(a,x,y,43,48,3.4)
 # Smooth sampled lobe profile generated as lofted radial rectangular stations in a separate component.
 camc,camb=part('11_face_cam_blank',a,False)
 # Build each raised lobe as loft through radial plane sketches; flat top plus cosine ramps.
 for center in [-50,50]:
  profiles=adsk.core.ObjectCollection.create()
  for deg in range(center-28,center+29,2):
   rel=abs(deg-center)
   h=4 if rel<=6 else (0.05+3.95*(1+math.cos(math.pi*(rel-6)/22))/2)
   t=math.radians(deg)
   # vertical radial plane through cam axis, local sketch coords found with modelToSketchSpace.
   planein=camc.constructionPlanes.createInput()
   planein.setByPlane(adsk.core.Plane.create(P(0,0,44),V(-math.sin(t),math.cos(t),0)))
   plane=camc.constructionPlanes.add(planein)
   sk=camc.sketches.add(plane)
   pts=[P(8*math.cos(t),8*math.sin(t),44.05),P(14*math.cos(t),14*math.sin(t),44.05),P(14*math.cos(t),14*math.sin(t),44-h),P(8*math.cos(t),8*math.sin(t),44-h)]
   sp=[sk.modelToSketchSpace(p) for p in pts]
   for j in range(4):sk.sketchCurves.sketchLines.addByTwoPoints(sp[j],sp[(j+1)%4])
   profiles.add(sk.profiles.item(0));sk.isVisible=False;plane.isLightBulbOn=False
  li=camc.features.loftFeatures.createInput(adsk.fusion.FeatureOperations.JoinFeatureOperation)
  for p in profiles:li.loftSections.add(p)
  li.isSolid=True;camc.features.loftFeatures.add(li)
 camb.name='11_face_cam_4mm'
 meshout(camb,camb.name)
 # Open sidecar: accessible connectors and antenna, avoids guessed connector apertures.
 a=box(56,-39,2,97,39,5)
 for x in [65,88]:
  for y in [-29,29]:op(a,cyl(x,y,4,7,3.2));op(a,cyl(x,y,7,9,1.25))
 # Reversible mounting strap integrated into tray; two front-access bolts to frame.
 for y in [-16,16]:
  op(a,box(40,y-4,11.3,60,y+4,14.3));op(a,box(56,y-4,5,60,y+4,14.3));hole(a,45,y,11,15,3.4)
 # Zip-tie slots for PCB retention and cable strain relief, clear of PCB underside.
 for y in [-34,34]:
  for x in [60,93]:op(a,box(x-1.5,y-2,0,x+1.5,y+2,5),True)
 part('12_open_controller_sidecar',a)
 a=box(-24,-10,0,24,10,10)
 for x,diam in [(-18,2.5),(-6,2.6),(6,2.7),(18,2.8)]:hole(a,x,0,1,11,diam)
 c,b=part('13_m3_pilot_coupon',a);b.isLightBulbOn=False
 # Clearly named reference envelopes, not printable parts.
 c,b=part('REF_87mm_faceplate_assumed_10mm_projection',box(-43.5,-43.5,-9,43.5,43.5,1),False)
 c,b=part('REF_STS3215_envelope_axis_offset_unverified',box(-12.35,-12.35,52.3,12.35,32.85,87.3),False)
 c,b=part('REF_Waveshare_PCB_envelope',box(61.5,-32.5,7,91.5,32.5,8.6),False)
 for i,(x0,y0,x1,y1) in enumerate([(-35,-42.5,35,-32.5),(-35,32.5,35,42.5),(-42.5,-30,-34.5,-16),(-42.5,16,-34.5,30),(34.5,-30,42.5,-16),(34.5,16,42.5,30)]):
  part('REF_tape_land_'+str(i+1),box(x0,y0,1,x1,y1,2),False)
 # Save machine-readable inventory and native exchange artifacts.
 app.activeViewport.fit();cam=app.activeViewport.camera;cam.viewOrientation=adsk.core.ViewOrientations.IsoTopRightViewOrientation;app.activeViewport.camera=cam;app.activeViewport.fit()
 app.activeViewport.saveAsImageFile(os.path.join(OUT,'assets','fusion-assembly.png'),1600,1200)









