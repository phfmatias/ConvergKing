##   PYTHON FILE HEADER #
##
##   File:      [step0.py]
##
##   Author(s): ['Pedro H.F Matias','Mateus R. Barbosa']
##   Site(s):   ['https://github.com/phfmatias','https://github.com/Mateus-RB']
##   Email(s):  ['phfmatias@discente.ufg.br']
##   Credits:   ['Copyright © 2022 LEEDMOL. All rights reserved.']
##   Date:      ['22.10.2022']

from MoleKing import Molecule
from os import mkdir, listdir
from numpy import arange

class step0:
    def __init__(self,name,method,base,molecula,cpu,mem,radii,cMethod,vsns):
        """
        This class is responsible for creating the input file for the first step of the convergence process.

        Parameters
        ----------
        The parameters are described at getControls.py
        """

        self.method = method
        self.base = base
        self.name = name
        self.radii = radii
        self.cpu = cpu
        self.mem = mem
        self.molecula = molecula
        self.cMethod = cMethod
        self.vsns = vsns
        self.string = self.inputConstructor()
        if 'step0' in listdir():
            pass
        else:
            mkdir('step0')
        self.writeInput()
    
    def inputConstructor(self):
        """
        This method constructs the input file for the first step of the convergence process.

        Returns
        -------
        str
            The input file for the first step of the convergence process.        

        Description
        -------
        This method constructs the input file for the first step of the convergence process. It is responsible for writing the input file with the correct parameters for the calculation. The method is called by the __init__ method and returns the input file as a string.
        """

        write = '%nprocshared={}\n'.format(self.cpu)
        write += '%mem={}\n'.format(self.mem)

        if self.cMethod == 'aim':
            if self.vsns:
                write += '#p {0}/{1} AIM=CHARGES SCF=QC GFINPUT IOP(6/7=3) density=current NoSymm\n\n'.format(self.method,self.base)
            else:
                write += '#p {0}/{1} AIM=CHARGES SCF=TIGHT GFINPUT IOP(6/7=3) density=current NoSymm\n\n'.format(self.method,self.base)

        elif self.base == 'None':
            if len(self.radii) == 0:
                if self.cMethod == 'mulliken':
                    write += '#p {0} POP=Minimal density=current NoSymm\n\n'.format(self.method)
                else:
                    write += '#p {0} POP={1} density=current NoSymm\n\n'.format(self.method,self.cMethod)
            elif len(self.radii) > 0:
                if self.cMethod == 'mulliken':
                    write += '#p {0} POP=(Minimal,ReadRadii) density=current NoSymm\n\n'.format(self.method)
                else:
                    write += '#p {0} POP=({},ReadRadii) density=current NoSymm\n\n'.format(self.method,self.cMethod)    

        elif self.base != 'None':
            if len(self.radii) > 0:
                if self.cMethod == 'mulliken':
                    write += '#p {0}/{1} POP=(Minimal,ReadRadii) density=current NoSymm\n\n'.format(self.method,self.base)
                else:
                    write += '#p {0}/{1} POP=({2},ReadRadii) density=current NoSymm\n\n'.format(self.method,self.base,self.cMethod)
            else:
                if self.cMethod == 'mulliken':
                    write += '#p {0}/{1} POP=Minimal density=current NoSymm\n\n'.format(self.method,self.base)
                else:
                    write += '#p {0}/{1} POP={2} density=current NoSymm\n\n'.format(self.method,self.base,self.cMethod)

        # if self.vsns == True and self.cMethod == 'aim':
        #     write += '#p {0}/{1} AIM=CHARGES SCF=QC GFINPUT IOP(6/7=3) density=current NoSymm\n\n'.format(self.method,self.base)
        
        # if self.base == 'None' and len(self.radii) == 0:
        #     write += '#p {0} POP={1} density=current NoSymm\n\n'.format(self.method,self.cMethod)
        
        # elif self.base == 'None' and len(self.radii) >0:
        #     write += '#p {0} POP=({},ReadRadii) density=current NoSymm\n\n'.format(self.method,self.cMethod)
        
        # elif self.base != 'None' and len(self.radii) >0:
        #     write += '#p {0}/{1} POP=({2},ReadRadii) density=current NoSymm\n\n'.format(self.method,self.base,self.cMethod)
        
        # elif self.cMethod.lower() == 'aim':
        #     write += '#p {0}/{1} AIM=CHARGES SCF=TIGHT GFINPUT IOP(6/7=3) density=current NoSymm\n\n'.format(self.method,self.base)
        
        # elif self.cMethod.lower() == 'mulliken' and self.base == 'None' and len(self.radii) >0:
        #     write += '#p {0} POP=(Minimal,ReadRadii) density=current NoSymm\n\n'.format(self.method,self.base)
        
        # elif self.cMethod.lower() == 'mulliken' and self.base != 'None' and len(self.radii) >0:
        #     write += '#p {0}/{1} POP=(Minimal,ReadRadii) density=current NoSymm\n\n'.format(self.method,self.base)
        
        # elif self.cMethod.lower() == 'mulliken' and self.base != 'None' and len(self.radii) ==0:
        #     write += '#p {0}/{1} POP=Minimal density=current NoSymm\n\n'.format(self.method,self.base)
        
        # else:
        #     write += '#p {0}/{1} POP={2} density=current NoSymm\n\n'.format(self.method,self.base,self.cMethod)
        
        write += 'STEP 0 \n\n'
        write += '0 1\n'
        
        for atoms in self.molecula:
            write += '{} {:10.6f} {:10.6f} {:10.6f}\n'.format(atoms.getAtomicSymbol(),(atoms.getX()),float(atoms.getY()),float(atoms.getZ()))
        write+='\n'
        
        if len(self.radii) > 0:
            for i in arange(0, len(self.radii), 2):
                write += '{} {}'.format(self.radii[i], self.radii[i+1])
            write+='\n'

        return write
    
    def writeInput(self):
        """
        This method writes the input file for the first step of the convergence process.

        Description
        -------
        It writes the input file for the first step of the convergence process. The method is called by the __init__ method and writes the input file in the 'step0' directory.
        """
        
        arqv = open('step0/{}_step0.gjf'.format(self.name),'w')
        arqv.write(self.string)  


if __name__ == '__main__':
    y = Molecule()
    y.addAtom('C',4.730509,1.288533,0.463983)
    y.addAtom('C',3.895041,0.033141,0.517227)
    y.addAtom('O',2.773020,-0.011744,-0.021787)
    y.addAtom('N',4.409480,-0.996630,1.179876)
    y.addAtom('H',3.901534,-1.741664,1.366552)
    y.addAtom('H',5.223114,-0.985284,1.534148)
    y.addAtom('H',4.504864,1.791426,1.250524)
    y.addAtom('H',5.648318,1.044998,0.438328)
    y.addAtom('H',4.447404,1.910854,-0.252683)
    x = step0('teste', 'HF', '3-21g', y, 1, '10GB', False,'','Hirshfeld')