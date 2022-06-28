from os import listdir
from MoleKing_util import Molecule
from sys import exit

class get_charge:

    def __init__(self,cMethod,monomer):
        self.cMethod = cMethod
        self.log = [x for x in listdir() if '.log' in x][0]
        #if self.cMethod.lower() == 'aim':
        #    self.txt = [x for x in listdir() if '.txt' in x][0]
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

                    #end = i+len(self.monomer)+6
                if '* Total *' in rlines[i]:
                    end = i-1

        elif self.cMethod.lower() == 'mulliken':
            arq = open(self.log,'r')
            rlines = arq.readlines()

            for i in range(len(rlines)):
                
                if 'Mulliken charges:' in rlines[i]:
                    start = i+2
                
                if 'Sum of Mulliken charges =' in rlines[i]:
                    end = i

        elif self.cMethod.lower() == 'aim':
            arq = open(self.log,'r')
            rlines = arq.readlines()

            for i in range(len(rlines)):
                if 'III. PROPERTIES OF ATTRACTORS' in rlines[i]:
                    start = i+6
                    end = i+5+len(self.monomer)+1
            
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
    
    y.addAtom('C',-5.900792, 4.088448,19.211769)
    y.addAtom('H',-5.644930, 4.481152,20.015376)
    y.addAtom('C',-7.160418, 4.275648,18.757121)
    y.addAtom('H',-7.766678, 4.782336,19.246122)
    y.addAtom('C',-7.533496, 3.703232,17.556560)
    y.addAtom('H',-8.395515, 3.823040,17.227655)
    y.addAtom('C',-6.621609, 2.959424,16.856342)
    y.addAtom('H',-6.873560, 2.575872,16.047476)
    y.addAtom('C',-5.328005, 2.764320,17.327099)
    y.addAtom('C',-4.310879, 2.020346,16.611595)
    y.addAtom('H',-3.457829, 1.975168,16.981099)
    y.addAtom('C',-4.529586, 1.397760,15.455249)
    y.addAtom('H',-5.394488, 1.446848,15.118783)
    y.addAtom('C',-3.568493, 0.649792,14.658546)
    y.addAtom('C',-4.022239,-0.002080,13.504174)
    y.addAtom('H',-4.917179, 0.073216,13.263042)
    y.addAtom('C',-3.175385,-0.750298,12.719305)
    y.addAtom('C',-1.827914,-0.845312,13.063661)
    y.addAtom('C',-1.365586,-0.190528,14.193871)
    y.addAtom('H',-0.466609,-0.247104,14.423497)
    y.addAtom('C',-2.225980, 0.542464,14.981534)
    y.addAtom('H',-1.901153, 0.970944,15.740103)
    y.addAtom('C',-3.672783, 3.164928,19.122516)
    y.addAtom('H',-3.638527, 3.614208,19.970996)
    y.addAtom('H',-3.008008, 3.535168,18.537686)
    y.addAtom('H',-3.502511, 2.228928,19.249410)
    y.addAtom('C', 0.329653,-1.661504,12.486392)
    y.addAtom('H', 0.690401,-0.772928,12.523376)
    y.addAtom('H', 0.761657,-2.154048,11.785353)
    y.addAtom('H', 0.478277,-2.102464,13.325503)
    y.addAtom('N',-5.007286, 3.345472,18.524537)
    y.addAtom('O',-3.578142,-1.416563,11.604710)
    y.addAtom('O',-1.058063,-1.595027,12.228167)
    y.addAtom('H',-4.390670,-1.198080,11.407301)
    y.addAtom('C', 0.743614, 8.990842,17.115554)
    y.addAtom('C', 0.917200, 7.639757,17.043396)
    y.addAtom('H', 0.451709, 7.081152,17.623787)
    y.addAtom('C', 1.802044, 7.086144,16.090048)
    y.addAtom('C', 2.013247, 5.690880,15.969235)
    y.addAtom('H', 1.560937, 5.105152,16.532368)
    y.addAtom('C', 2.874153, 5.201664,15.035119)
    y.addAtom('H', 2.999823, 4.283136,14.962631)
    y.addAtom('C', 3.568780, 6.061952,14.185324)
    y.addAtom('H', 4.153427, 5.713344,13.550690)
    y.addAtom('C', 3.397387, 7.403968,14.277865)
    y.addAtom('H', 3.872276, 7.967232,13.711773)
    y.addAtom('C', 2.505976, 7.958080,15.223487)
    y.addAtom('C', 2.304052, 9.350016,15.334602)
    y.addAtom('H', 2.767075, 9.928256,14.771962)
    y.addAtom('C', 1.442762, 9.855872,16.253760)
    y.addAtom('H', 1.314292,10.775232,16.313756)
    y.addAtom('O',-1.468637, 8.797152,18.453693)
    y.addAtom('O', 0.422848, 9.820928,19.545605)
    y.addAtom('O',-0.750803,10.970586,17.788815)
    y.addAtom('S',-0.344999, 9.689805,18.326963)
    y.addAtom('O', 2.523148, 6.349824, 2.918231)
    y.addAtom('H', 2.061028, 6.306560, 3.598067)
    y.addAtom('H', 2.757953, 7.180160, 2.820595)
    y.addAtom('O',10.909254, 7.557056,10.980431)
    y.addAtom('H',10.788607, 8.186880,10.587093)
    y.addAtom('H',10.179979, 7.113600,11.062123)

    get_charge('chelpg',y)