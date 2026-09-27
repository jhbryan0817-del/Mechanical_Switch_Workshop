"""Round-trip the local F3D, close only the verification copy, save original."""
import adsk.core,adsk.fusion,os,json
OUT=os.path.abspath(os.path.join(os.path.dirname(__file__),'..'))

def run(_context: str):
 app=adsk.core.Application.get()
 doc=next(x for x in app.documents if x.name=='Mechanical Switch');doc.activate()
 d=adsk.fusion.Design.cast(doc.products.itemByProductType('DesignProductType'))
 def snapshot(des):
  return {o.component.name:{b.name:b.volume*1000 for b in o.component.bRepBodies} for o in des.rootComponent.occurrences}
 original=snapshot(d)
 manager=app.importManager
 options=manager.createFusionArchiveImportOptions(os.path.join(OUT,'cad','Mechanical_Switch_v03.f3d'))
 copydoc=manager.importToNewDocument(options)
 assert copydoc and copydoc!=doc
 loaded=snapshot(adsk.fusion.Design.cast(copydoc.products.itemByProductType('DesignProductType')))
 assert original.keys()==loaded.keys()
 for name,bodymap in original.items():
  assert bodymap.keys()==loaded[name].keys()
  for body,volume in bodymap.items():assert abs(volume-loaded[name][body])<0.01
 report={'version':'0.3','components':len(loaded),'bodies':sum(len(v) for v in loaded.values()),'names_match':True,'volume_tolerance_mm3':0.01,'passed':True}
 copydoc.close(False);doc.activate()
 report['original_save_result']=doc.save('v0.3 simplified assembly and reinforced integral rocking shoe')
 with open(os.path.join(OUT,'validation','archive_reimport.json'),'w') as f:json.dump(report,f,indent=2)
