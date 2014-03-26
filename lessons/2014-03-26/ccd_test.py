￼from Bio.PDB import *

def myprint (string):
    print "\n" + string + " ->", eval(string)

parser=PDBParser()
structure=parser.get_structure('cysteine', 'BTC.pdb')
myprint("structure")
model = structure[0]
myprint("model")
chain = model[' ']
myprint("chain")
residue = chain[0] 
myprint("residue")

for atom in residue:
	print atom.get_serial_number(), atom.get_coord()

myprint("[atom.get_name() for atom in residue]")

myprint("[atom.get_name() for atom in structure[0][' '][0]]")


def getPdbConnect (filename):
    myfile = open(filename,'r')
    for record in myfile:
        terms = record.split()
        if terms[0] == "CONECT": print terms
    myfile.close()

## units = Angstrom: 1 x 10^(-10)
    

myprint("getPdbConnect('BTC.pdb')")


from pyplasm import *
def getPdbConnect (filename):
    myfile = open(filename,'r')
    for record in myfile:
        terms = record.split()
        if terms[0] == "CONECT":
            terms = AA(eval)(terms[1:])
            print terms
    myfile.close()

myprint("getPdbConnect('BTC.pdb')")


from pyplasm import *
def getPdbConnect (filename):
    myfile = open(filename,'r')
    for record in myfile:
        terms = record.split()
        if terms[0] == "CONECT":
            node,terms = eval(terms[1]),AA(eval)(terms[2:])
            print node,terms
    myfile.close()

myprint("getPdbConnect('BTC.pdb')")


from pyplasm import *
def getPdbConnect (filename):
    myfile = open(filename,'r')
    for record in myfile:
        terms = record.split()
        if terms[0] == "CONECT":
            arcs = DISTL([ eval(terms[1]),AA(eval)(terms[2:]) ])
            print arcs
    myfile.close()

myprint("getPdbConnect('BTC.pdb')")


from pyplasm import *
def getPdbConnect (filename):
    myfile = open(filename,'r')
    for record in myfile:
        terms = record.split()
        if terms[0] == "CONECT":
            arcs = DISTL([ eval(terms[1]),AA(eval)(terms[2:]) ])
            arcs = [arc for arc in arcs if arc[0] < arc[1]]
            print arcs
    myfile.close()

myprint("getPdbConnect('BTC.pdb')")


from pyplasm import *
def getPDBconnect (filename):
    myfile = open(filename,'r')
    arcs = []
    for record in myfile:
        terms = record.split()
        if terms[0] == "CONECT":
            pairs = DISTL([ eval(terms[1]), AA(eval)(terms[2:]) ])
            arcs += [arc for arc in pairs if arc[0] < arc[1]]
    myfile.close()
    return arcs

myprint("getPDBconnect('BTC.pdb')")


myprint("[atom.get_coord() for atom in residue]")




myprint("[atom.get_coord().tolist() for atom in residue]")



def graph (filename):
    parser=PDBParser()
    structure=parser.get_structure('molecule', filename)
    model = structure[0]
    chain = model[' ']
    residue = chain[0]
    
    nodes = [atom.get_coord().tolist() for atom in residue]
    edges = getPDBconnect('BTC.pdb')
    return nodes,edges

myprint("graph('BTC.pdb')")




def graph (filename):
    parser=PDBParser()
    structure=parser.get_structure('molecule', filename)
    model = structure[0]
    chain = model[' ']
    residue = chain[0]
    
    nodes = [atom.get_coord().tolist() for atom in residue]
    edges = getPDBconnect('BTC.pdb')
    return MKPOL([nodes,edges,None])

myprint("graph('BTC.pdb')")




VIEW(graph('BTC.pdb'))


#--------------------------------------------------
#--Insert atom spheres-----------------------------
#--------------------------------------------------

from atomic_radius import *


myprint("atomic_radius['Mg']")
myprint("atomic_radius['O'][0:2]")



myprint("[atom.get_id() for atom in residue]")
myprint("[atom.get_id()[0] for atom in residue]")
myprint("set([atom.get_id()[0] for atom in residue])")
myprint("list(set([atom.get_id()[0] for atom in residue]))")


atom_color = {
    'H': Color4f([0.8, 0.8, 0.8, 1.0]), # ligth gray
    'C': Color4f([0.3, 0.3, 0.3, 1.0]), # dark gray (quite black)
    'N': BLUE,
    'O': RED,
    'F': Color4f([0.0, 0.75, 1.0, 1.0]), # ligth blue
    'P': ORANGE,
    'S': YELLOW,
    'Cl': GREEN,
    'K': Color4f([200./255, 162./255, 200./255, 1.0]) # lilac
}

myprint("VIEW(COLOR(atom_color['H'])(CUBOID([1,1])))")
myprint("VIEW(COLOR(atom_color['K'])(CUBOID([1,1])))")



def sphere(atom_code):
    return COLOR(atom_color[atom_code])(
        SPHERE(atomic_radius[atom_code][RADIUS_TYPE]/100.)([8,16]))

myprint("VIEW(sphere('F'))")


VIEW(STRUCT([ sphere('F'), T([1,2,3])([0.,.3,.5]), sphere('H') ]))
 





def graph2 (filename):
    parser=PDBParser()
    structure=parser.get_structure('molecule', filename)
    model = structure[0]
    chain = model[' ']
    residue = chain[0]
    
    nodes = [atom.get_coord().tolist() for atom in residue]
    transls = AA(T([1,2,3]))(nodes)
    return STRUCT(CONS(transls)(sphere('H')))

myprint("graph2('BTC.pdb')")

VIEW(STRUCT([ graph('BTC.pdb'), graph2('BTC.pdb') ]))





atom_types = [atom.get_id()[0] for atom in residue]
myprint("atom_types")

AA(sphere)(atom_types)







def graph3 (filename):
    parser = PDBParser()
    structure = parser.get_structure('molecule', filename)
    residue = structure[0][' '][0]    
    nodes = [atom.get_coord().tolist() for atom in residue]
    transls = AA(T([1,2,3]))(nodes)
    atom_types = [atom.get_id()[0] for atom in residue]
    atoms = AA(sphere)(atom_types)    
    return STRUCT(AA(STRUCT)(TRANS([transls,atoms])))

VIEW(graph3('BTC.pdb'))

VIEW(graph3('OTY.pdb'))

VIEW(graph3('GAL.pdb'))

VIEW(graph3('ATP.pdb'))
    
