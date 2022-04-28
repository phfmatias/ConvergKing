from MoleKing_util import Molecule
from os import mkdir, listdir
from numpy import arange

class step:

    def __init__(self, step,metodo, base, molecula, name, cargas,ncela,nx,ny,nz,cpu,mem,sheril,radii,cMethod):
        self.metodo = metodo
        self.base = base
        self.name = name
        self.molecula = molecula
        self.radii = radii
        self.step = step
        self.cargas = cargas
        self.ncela = ncela
        self.sheril = sheril
        self.nx = nx
        self.ny = ny
        self.cpu = cpu
        self.mem = mem
        self.nz = nz
        self.cMethod = cMethod
        self.cela = self.constructSM()
        self.string = self.inputConstructor()
        if 'step{}'.format(self.step) in listdir():
            pass
        else:
            mkdir('step{}'.format(self.step))
        self.writeInput()

    def constructSM(self):
        if self.sheril == True:
            cel = self.cargas   #pegar as cargas do step anterior
            celaT = open('supercell.xyz','r') #pegar as posições gerados no  cristalatte            
            M = self.molecula
            Monomero = Molecule()
            Cela = Molecule()
            cargasSherril = []

            if self.cMethod.lower() == 'chelpg' or self.cMethod.lower() == 'chelp' or self.cMethod.lower() == 'mk' or self.cMethod.lower() == 'mulliken':
                for i in range(len(M)):
                    Monomero.addAtom(M[i].getAtomicSymbol(),M[i].getX(), M[i].getY(),M[i].getZ(),float(cel[i].split()[2]))
            
            elif self.cMethod.lower() == 'cm5':
                for i in range(len(M)):
                    Monomero.addAtom(M[i].getAtomicSymbol(),M[i].getX(), M[i].getY(),M[i].getZ(),float(cel[i].split()[7]))
            
            elif self.cMethod.lower() == 'hirshfeld':
                for i in range(len(M)):
                    Monomero.addAtom(M[i].getAtomicSymbol(),M[i].getX(), M[i].getY(),M[i].getZ(),float(cel[i].split()[2]))

            elif self.cMethod.lower() == 'nbo' or self.cMethod.lower() == 'npa':
                for i in range(len(M)):
                    Monomero.addAtom(M[i].getAtomicSymbol(),M[i].getX(), M[i].getY(),M[i].getZ(),float(cel[i].split()[2]))

            elif self.cMethod.lower() == 'aim':
                for i in range(len(M)):
                    Monomero.addAtom(M[i].getAtomicSymbol(),M[i].getX(), M[i].getY(),M[i].getZ(),float(cel[i].split()[4]))

            for atom in Monomero:
                for x in arange(self.nx):
                    for y in arange(self.ny):
                        for z in arange(self.nz):
                            cargasSherril.append(atom.getCharge())

            for atom in Monomero:
                for x in arange(self.nx):
                    for y in arange(self.ny):
                        for z in arange(self.nz):
                            for i in arange(self.ncela-1):
                                cargasSherril.append(atom.getCharge())

            rlines = celaT.readlines()
            xyz = []
            for atom in Monomero:
                xyz.append('{},{:.8f},{:.8f},{:.8f}\n'.format(atom.getAtomicSymbol(), atom.getX(), atom.getY(), atom.getZ()))                
            
            #cargas_conv = (open('cargas_convergidas.data','w')) #ESCREVE A CARGA CONVERGIDA
            
            for i in arange(len(cargasSherril)):
                line = '{},{:.8f},{:.8f},{:.8f}\n'.format(rlines[i+2].split()[0],float(rlines[i+2].split()[1]),float(rlines[i+2].split()[2]),float(rlines[i+2].split()[3]))                
                #cargas_conv.write('{},{},{},{},{}\n'.format(line.split(',')[0],line.split(',')[1],line.split(',')[2],line.split(',')   [3],cargasSherril[i]))

                if line in xyz:
                    pass

                else:
                    #conferir.addAtom(str(line.split(',')[0]),float(line.split(',')[1]), float(line.split(',')[2]), float(line.split    (',')[3]), float#cargasSherril[i]))

                    #print(line.split()[1],line.split()[2],line.split()[3],cargasSherril[i])

                    Cela.addChargePoints(float(line.split(',')[1]), float(line.split(',')[2]), float(line.split(',')[3]),   cargasSherril[i])

            #for atom in conferir:
                #print(atom)

            for atom in Monomero:
                Cela.addAtom(atom)

            return Cela

        if self.sheril == False:
            M = self.molecula
            Monomero = Molecule()
            cont_pos = 0
            cont_carga = 0
            contador = []
            x = []
            y = []
            z = []
            cargas = []
            xyz = []

            for i in range(len(M)):
                Monomero.addAtom(M[i].getAtomicSymbol(),M[i].getX(), M[i].getY(),M[i].getZ())

            for atom in Monomero:
                xyz.append('{:.6f},{:.6f},{:.6f}'.format(atom.getX(), atom.getY(), atom.getZ()))

            natomos = len(M)
            pos = open('supercell.xyz','r')
            pos_envolvida = pos.readlines()
            nlinhas = len(pos_envolvida)-2-len(M)

            if self.cMethod.lower() == 'chelpg' or self.cMethod.lower() == 'chelp' or self.cMethod.lower() == 'mk' or self.cMethod.lower() == 'mulliken':
                for linhas in self.cargas:
                    cargas.append(linhas.split()[2])

            elif self.cMethod.lower() == 'cm5':
                for linhas in self.cargas:
                    cargas.append(linhas.split()[7])

            elif self.cMethod.lower() == 'hirshfeld':
                for linhas in self.cargas:
                    cargas.append(linhas.split()[2])

            elif self.cMethod.lower() == 'nbo' or self.cMethod.lower() == 'npa':
                for linhas in self.cargas:
                    cargas.append(linhas.split()[2])

            elif self.cMethod.lower() == 'aim':
                for linhas in self.cargas:
                    cargas.append(linhas.split()[4])

            for lines in pos_envolvida[2:]:
                lines = '{},{},{}'.format(lines.split()[1],lines.split()[2],lines.split()[3])
                if lines in xyz:
                    pass
                else:
                    x.append(lines.split(',')[0])
                    y.append(lines.split(',')[1])
                    z.append(lines.split(',')[2])    

            Cela =  Molecule()
            
            while cont_pos != nlinhas:
                Cela.addChargePoints(float(x[cont_pos]),float(y[cont_pos]),float(z[cont_pos]),float(cargas[cont_carga]))
                cont_pos+=1
                cont_carga+=1
                if cont_carga == natomos and cont_pos != nlinhas:
                    contador.append(cont_carga)
                    cont_carga = 0
            
            for atom in Monomero:
                Cela.addAtom(atom)
 
            return Cela

    def inputConstructor(self):        
        ipt = '%chk={}_step{}.chk'.format(self.name,self.step)
        write = '%nprocshared={}\n'.format(self.cpu)
        write += '%mem={}\n'.format(self.mem)
        if self.base == 'None' and len(self.radii) == 0:
            write += '#p {0} POP={1} density=current NoSymm Charge\n\n'.format(self.metodo,self.cMethod)
        elif self.base == 'None' and len(self.radii) >0:
            write += '#p {0} POP=({1},ReadRadii) density=current NoSymm Charge\n\n'.format(self.metodo,self.cMethod)
        elif self.base != 'None' and len(self.radii) >0:
            write += '#p {0}/{1} POP=({2},ReadRadii) density=current NoSymm Charge\n\n'.format(self.metodo,self.base,self.cMethod)

        elif self.cMethod.lower() == 'aim':
            write += '#p {0}/{1} out=wfn density=current NoSymm Charge\n\n'.format(self.metodo,self.base)

        elif self.cMethod.lower() == 'mulliken' and self.base == 'None' and len(self.radii) >0:
            write += '#p {0} POP=(Minimal,ReadRadii) density=current NoSymm Charge\n\n'.format(self.metodo,self.base)
        elif self.cMethod.lower() == 'mulliken' and self.base != 'None' and len(self.radii) >0:
            write += '#p {0}/{1} POP=(Minimal,ReadRadii) density=current NoSymm Charge\n\n'.format(self.metodo,self.base)
        elif self.cMethod.lower() == 'mulliken' and self.base != 'None' and len(self.radii) ==0:
            write += '#p {0}/{1} POP=Minimal density=current NoSymm Charge\n\n'.format(self.metodo,self.base)

        else:
            write += '#p {0}/{1} POP={2} density=current NoSymm Charge\n\n'.format(self.metodo,self.base,self.cMethod)
        write += 'STEP {} \n\n'.format(self.step)
        write += '0 1\n'

        for atom in self.cela:
            write+='{}    {:.8f}   {:.8f}   {:.8f}\n'.format(atom.getAtomicSymbol(), atom.getX(), atom.getY(), atom.getZ())
        write+='\n'
        for cp in self.cela.getChargePoints():
            write+='  {}   {}   {}   {}\n'.format(cp[0], cp[1], cp[2], cp[3])

        write+='\n'

        if len(self.radii) > 0:
            for i in arange(0, len(self.radii), 2):
                write += '{} {}'.format(self.radii[i], self.radii[i+1])        
            write+='\n'

        if self.cMethod == 'AIM':
            write+= '{}_wfn.wfn'.format(self.name)
            write+='\n'

        return write

    def writeInput(self):
        arqv = open('step{0}/{1}_step{0}.gjf'.format(self.step,self.name),'w')
        arqv.write(self.string)  

if __name__ == '__main__':
    y = Molecule()
    
    #cargas = ['1  C   -0.408347','2  C    0.850242','3  O   -0.622226','4  N   -0.997305','5  H    0.427780','6  H    0.408574','7  H    0.108310','8  H    0.111375','9  H    0.121598']

    #cargas = ['     1  C   -0.069071   0.000000  -0.004429   0.001631   0.001796  -0.257900\n', '     2  C    0.252555   0.000000   0.057086   0.000544   0.035867   0.338368\n', '     3  O   -0.378188   0.000000   0.215417   0.005165   0.106119  -0.420389\n', '     4  N   -0.160250   0.000000  -0.000697   0.007556   0.030908  -0.731140\n', '     5  H    0.126925   0.000000  -0.102894  -0.178824   0.056036   0.365256\n', '     6  H    0.114270   0.000000   0.185122  -0.016905   0.091487   0.370562\n', '     7  H    0.037115   0.000000  -0.038276   0.092093   0.115553   0.111946\n', '     8  H    0.028665   0.000000   0.145320  -0.035485  -0.001485   0.106383\n', '     9  H    0.047980   0.000000  -0.042070   0.117884  -0.101003   0.116913\n']

    #cargas = ['      C    1   -0.68329      1.99838     4.68088    0.00403     6.68329\n', '      C    2    0.76766      1.99925     3.19323    0.03986     5.23234\n', '      O    3   -0.66883      1.99965     6.66735    0.00183     8.66883\n', '      N    4   -0.86869      1.99894     5.86334    0.00641     7.86869\n', '      H    5    0.40088      0.00000     0.59697    0.00214     0.59912\n', '      H    6    0.37705      0.00000     0.62184    0.00111     0.62295\n', '      H    7    0.22873      0.00000     0.76959    0.00168     0.77127\n', '      H    8    0.20315      0.00000     0.79493    0.00192     0.79685\n', '      H    9    0.24333      0.00000     0.75474    0.00193     0.75667\n']

    #cargas = ['     1  C   -0.727292\n', '     2  C    0.801969\n', '     3  O   -0.639957\n', '     4  N   -0.924040\n', '     5  H    0.364184\n', '     6  H    0.344818\n', '     7  H    0.272084\n', '     8  H    0.230675\n', '     9  H    0.277560\n']

    #cargas = ['      1 (C )    Charge:    0.291104     Volume:    63.649 Bohr^3\n', '      2 (C )    Charge:    1.265493     Volume:    42.383 Bohr^3\n', '      3 (O )    Charge:   -1.012863     Volume:   108.150 Bohr^3\n', '      4 (N )    Charge:   -1.185355     Volume:   101.364 Bohr^3\n', '      5 (H )    Charge:    0.422926     Volume:    22.015 Bohr^3\n', '      6 (H )    Charge:    0.387384     Volume:    22.095 Bohr^3\n', '      7 (H )    Charge:   -0.072782     Volume:    42.841 Bohr^3\n', '      8 (H )    Charge:   -0.097471     Volume:    43.206 Bohr^3\n', '      9 (H )    Charge:    0.001563     Volume:    41.561 Bohr^3\n']

    #cargas = ['     1  C   -0.566093\n', '     2  C    0.987178\n', '     3  O   -0.682453\n', '     4  N   -1.112693\n', '     5  H    0.460430\n', '     6  H    0.442831\n', '     7  H    0.164643\n', '     8  H    0.149555\n', '     9  H    0.156603\n']


    y.addAtom('C',4.730509,1.288533,0.463983)
    y.addAtom('C',3.895041,0.033141,0.517227)
    y.addAtom('O',2.773020,-0.011744,-0.021787)
    y.addAtom('N',4.409480,-0.996630,1.179876)
    y.addAtom('H',3.901534,-1.741664,1.366552)
    y.addAtom('H',5.223114,-0.985284,1.534148)
    y.addAtom('H',4.504864,1.791426,1.250524)
    y.addAtom('H',5.648318,1.044998,0.438328)
    y.addAtom('H',4.447404,1.910854,-0.252683)

    x = step(1, 'HF', '3-21g', y, 'teste', cargas, 18, 7, 7, 7, 1, '10GB', False, '', 'Hirshfeld')
    #x = step0('teste', 'HF', '6-31g', y, 1, '2GB', False,'','ChelpG')