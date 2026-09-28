"""Run in Fusion with Mechanical Switch active. Exports current edited geometry; does not rebuild it."""
import adsk.core, adsk.fusion, json, math, os
OUTPUT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
def run(context):
    app=adsk.core.Application.get();d=adsk.fusion.Design.cast(app.activeProduct)
    assert d and 'Mechanical Switch' in app.activeDocument.name
    r=d.rootComponent;m=adsk.fusion.TemporaryBRepManager.get();em=d.exportManager
    for folder in ['cad','stl','assets','validation']:os.makedirs(os.path.join(OUTPUT_ROOT,folder),exist_ok=True)
    parts=[o for o in r.occurrences if o.name.startswith('PRINT')]
    assert len(parts)==4
    names=['01_integrated_chassis','02_servo_clamp','03_actuator_PLACEHOLDER','04_closed_branded_cover']
    report=[]
    for i,(o,name) in enumerate(zip(parts,names)):
        b=o.bRepBodies.item(0);assert b.isSolid and b.lumps.count==1
        t=m.copy(b);mat=adsk.core.Matrix3D.create()
        if i==2:mat.setToRotation(math.pi/2,adsk.core.Vector3D.create(0,1,0),adsk.core.Point3D.create(0,0,0))
        if i==3:mat.setToRotation(math.pi,adsk.core.Vector3D.create(1,0,0),adsk.core.Point3D.create(0,0,0))
        m.transform(t,mat);bb=t.boundingBox;shift=adsk.core.Matrix3D.create();shift.translation=adsk.core.Vector3D.create(-(bb.minPoint.x+bb.maxPoint.x)/2,-(bb.minPoint.y+bb.maxPoint.y)/2,-bb.minPoint.z);m.transform(t,shift)
        temp=r.occurrences.addNewComponent(adsk.core.Matrix3D.create());temp.component.name='Temporary print export';tb=temp.component.bRepBodies.add(t)
        path=os.path.join(OUTPUT_ROOT,'stl',name+'.stl');opt=em.createSTLExportOptions(tb,path);opt.meshRefinement=adsk.fusion.MeshRefinementSettings.MeshRefinementHigh;assert em.execute(opt)
        bb=tb.boundingBox
        report.append(dict(file=name+'.stl',source_component=o.name,units='mm',solid=True,lumps=1,volume_mm3=b.volume*1000,print_min_z_mm=bb.minPoint.z*10,print_size_mm=[round((getattr(bb.maxPoint,k)-getattr(bb.minPoint,k))*10,4) for k in ['x','y','z']]))
        temp.deleteMe()
    lid=parts[3];lid.isLightBulbOn=True
    cam=app.activeViewport.camera;cam.isPerspective=False;cam.target=adsk.core.Point3D.create(0,0,2.5);cam.eye=adsk.core.Point3D.create(10,-12,22);cam.upVector=adsk.core.Vector3D.create(0,1,0);app.activeViewport.camera=cam;app.activeViewport.fit();app.activeViewport.refresh()
    app.activeViewport.saveAsImageFile(os.path.join(OUTPUT_ROOT,'assets','fusion-assembly.png'),1400,1100)
    lid.isLightBulbOn=False;app.activeViewport.refresh();app.activeViewport.saveAsImageFile(os.path.join(OUTPUT_ROOT,'assets','fusion-internal.png'),1400,1100)
    lid.isLightBulbOn=True
    assert em.execute(em.createFusionArchiveExportOptions(os.path.join(OUTPUT_ROOT,'cad','Mechanical_Switch_v04.f3d')))
    assert em.execute(em.createSTEPExportOptions(os.path.join(OUTPUT_ROOT,'cad','Mechanical_Switch_v04.step')))
    with open(os.path.join(OUTPUT_ROOT,'validation','exports.json'),'w') as f:json.dump(report,f,indent=2)
    app.activeViewport.refresh()

