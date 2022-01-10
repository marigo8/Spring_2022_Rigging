import maya.cmds as cmds

def locator():
    sels = cmds.ls(sl=True)
    
    bbox = cmds.xform(sels, q=True, boundingBox=True, ws=True)
    
    mid = [0,0,0]
    
    for i in range(3):
        mid[i] = (bbox[i] + bbox[i+3]) / 2
    
    loc = cmds.spaceLocator(position=[0,0,0], absolute=True)[0] 
    
    cmds.xform(loc,translation=mid, ws=True)

locator()