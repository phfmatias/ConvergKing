from os import listdir
from MoleKing_util import Molecule
from sys import exit

class get_charge:

    def __init__(self,cMethod,monomer):
        self.cMethod = cMethod
        self.log = [x for x in listdir() if '.log' in x][0]
        if self.cMethod.lower() == 'aim':
            self.txt = [x for x in listdir() if '.txt' in x][0]
        self.calculosOk()
        self.monomer = monomer
        self.cargas = self.getCharge()

    def getCharge(self):
        if self.cMethod.lower() == 'chelp' or self.cMethod.lower() == 'chelpg' or self.cMethod.lower() == 'mk':
            arq = open(self.log,'r')
            rlines = arq.readlines()

            for i in range(len(rlines)):

                if 'ESP charges:' in rlines[i]:
                    start = i+2

                if 'Sum of ESP charges =' in rlines[i]:
                    end = i

        elif self.cMethod.lower() == 'cm5' or self.cMethod.lower() == 'hirshfeld':
            arq = open(self.log,'r')
            rlines = arq.readlines()

            for i in range(len(rlines)):
                
                if 'Hirshfeld charges, spin densities' in rlines[i]:
                    start = i+2
                
                if 'Hirshfeld charges with hydrogens' in rlines[i]:
                    end = i-1

        elif self.cMethod.lower() == 'nbo' or self.cMethod.lower() == 'npa':
            arq = open(self.log,'r')
            rlines = arq.readlines()

            for i in range(len(rlines)):

                if 'Summary of Natural Population' in rlines[i]:
                    start = i+6

                    end = i+len(self.monomer)+6

        elif self.cMethod.lower() == 'mulliken':
            arq = open(self.log,'r')
            rlines = arq.readlines()

            for i in range(len(rlines)):
                
                if 'Mulliken charges:' in rlines[i]:
                    start = i+2
                
                if 'Sum of Mulliken charges =' in rlines[i]:
                    end = i

        elif self.cMethod.lower() == 'aim':
            arq = open(self.txt,'r')
            rlines = arq.readlines()
            
            for i in range(len(rlines)):

                if 'The atomic charges after normalization and atomic volumes:' in rlines[i]:
                    start = i+1
    
                    end = i+len(self.monomer)+1

        #print(rlines[start:end])
        #return 0
        return rlines[start:end]

    def calculosOk(self):

        arq = open(self.log,'r')
        rlines = arq.readlines()

        for i in range(len(rlines)):
            if 'Error termination' in rlines[i]:
                print('Cálculo do {} deu errado!'.format(self.log))
                exit(0)

if __name__ == '__main__':
    y = Molecule()
    y.addAtom('C',-0.91782400,-0.35215350,-1.45464850)
    y.addAtom('C',-1.75330700,-1.60756650,-1.40140350)
    y.addAtom('O',-2.87534800,-1.65245250,-1.94042650)
    y.addAtom('N',-1.23885900,-2.63735550,-0.73874450)
    y.addAtom('H',-1.74681400,-3.38240250,-0.55206550)
    y.addAtom('H',-0.42521100,-2.62600950,-0.38446650)
    y.addAtom('H',-1.14347400,0.15074850,-0.668095500)
    y.addAtom('H',0.00000000,-0.59569250,-1.480303500)
    y.addAtom('H',-1.20093500,0.27017850,-2.171325500)

    get_charge('Hirshfeld',y)