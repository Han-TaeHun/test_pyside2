#coding:utf8
import nuke
import nukescripts

class ImportFromTag( nukescripts.PythonPanel ):
    def __init__( self ):
        nukescripts.PythonPanel.__init__( self, "ImportFromTag" )
        self.projectKnob = nuke.String_Knob("{}".format(""), "Project")
        self.tagKnob = nuke.String_Knob("{}".format(""), "Tag")
        self.statusKnob = nuke.Enumeration_Knob("status", "Status", [ "All", "ASSIGN", "WIP", "CONFIRM", "DONE" ])
        self.plateKnob = nuke.Radio_Knob( "Type", "Type", [ "org", "output"] )
        for k in ( self.projectKnob, self.tagKnob, self.statusKnob, self.plateKnob ):
            self.addKnob( k )
        self.aaa()

    def aaa(self):
        print (self.projectKnob.value())
        print (self.tagKnob)
        

p = ImportFromTag()
p.showModalDialog()
print  (p.projectKnob.value())
print  (p.tagKnob.value())
print  (p.statusKnob.value())
print  (p.plateKnob.value())











class ShapePanel( nukescripts.PythonPanel ):
    def __init__( self, node ):
        '''List all roto paint nodes and the name of their respective shapes and strokes'''
        nukescripts.PythonPanel.__init__( self, 'RotoPaint Elements' )
        self.rpNode = node
        # CREATE KNOBS
        self.typeKnob = nuke.Enumeration_Knob( 'element', 'element / curve', ['Shapes', 'Strokes'] )
        self.elementKnob = nuke.Enumeration_Knob( 'curve', '', [] )
        self.elementKnob.clearFlag( nuke.STARTLINE )
        # ADD KNOBS
        for k in ( self.typeKnob, self.elementKnob ):
            self.addKnob( k )

        # STORE DICTIONARY OF ELEMENTS PER TYPE
        self.curveDict = {}
        # FILL DICTIONARY
        self.getData()

    def getData( self ):
        '''return a nested dictionary of all shapes and strokes per node'''
        self.curveDict={ 'Shapes':[], 'Strokes':[] }
        rootLayer = self.rpNode['curves'].rootLayer
        for e in rootLayer:
            if isinstance( e, nuke.rotopaint.Shape ):
                self.curveDict[ 'Shapes' ].append( e.name )
            elif isinstance( e, nuke.rotopaint.Stroke ):
                self.curveDict[ 'Strokes' ].append( e.name )


    def knobChanged( self, knob ):
        if knob is self.typeKnob or knob.name()=='showPanel':
            self.elementKnob.setValues( self.curveDict[ self.typeKnob.value() ] )




node = nuke.toNode('RotoPaint1')
p = ShapePanel(node)
if p.showModalDialog():
    print p.elementKnob.value()











p = nuke.Panel('my custom panel')

p.addButton('push here')


p.show()




































