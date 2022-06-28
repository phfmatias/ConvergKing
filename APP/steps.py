from MoleKing_util import Molecule
from os import mkdir, listdir
from numpy import arange

class step:

    def __init__(self, step,metodo, base, molecula, name, cargas,nx,ny,nz,cpu,mem,sheril,radii,cMethod,vsns):
        self.metodo = metodo
        self.base = base
        self.name = name
        self.molecula = molecula
        self.radii = radii
        self.step = step
        self.cargas = cargas
        #self.ncela = ncela
        self.sheril = sheril
        self.vsns = vsns
        self.nx = nx
        self.ny = ny
        self.nz = nz
        self.cpu = cpu
        self.mem = mem
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
                    Monomero.addAtom(M[i].getAtomicSymbol(),M[i].getX(), M[i].getY(),M[i].getZ(),float(cel[i].split()[3]))

            for atom in Monomero:
                for x in arange(self.nx):
                    for y in arange(self.ny):
                        for z in arange(self.nz):
                            cargasSherril.append(atom.getCharge())

            rlines = celaT.readlines() 
            ncela = int(int(rlines[0])/(self.nx*self.nz*self.ny*len(Monomero)))

            for atom in Monomero:
                for x in arange(self.nx):
                    for y in arange(self.ny):
                        for z in arange(self.nz):
                            for i in arange(ncela-1):
                                cargasSherril.append(atom.getCharge())                    
           
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

        if self.sheril == False and self.vsns == True:
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
            ngeo = len(pos_envolvida[2:])
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
                    cargas.append(linhas.split()[3])

            for lines in pos_envolvida[2:]:
                lines = '{},{},{}'.format(lines.split()[1],lines.split()[2],lines.split()[3])
                #if lines in xyz:
                #    pass
                #else:
                x.append(lines.split(',')[0])
                y.append(lines.split(',')[1])
                z.append(lines.split(',')[2])

            Cela =  Molecule()

            nmoleculas = 8788            

            cont_carga = 0

            for i in range(0,(nmoleculas*34)+1):
                if cont_carga != 34 and i != nmoleculas:    
                    Cela.addChargePoints(float(x[i]),float(y[i]),float(z[i]),float(cargas[cont_carga]))
                    cont_carga +=1
                if cont_carga == 34 and i != nmoleculas:
                    cont_carga = 0

            cont_carga = 34

            for i in range((nmoleculas*34)+1,(nmoleculas*55)+1):
                if cont_carga != 55 and i != nmoleculas:    
                    Cela.addChargePoints(float(x[i]),float(y[i]),float(z[i]),float(cargas[cont_carga]))
                    cont_carga +=1
                if cont_carga == 55 and i != nmoleculas:
                    cont_carga = 34

            cont_carga = 55

            for i in range((nmoleculas*55)+1,(nmoleculas*58)+1):
                if cont_carga != 58 and i != nmoleculas:    
                    Cela.addChargePoints(float(x[i]),float(y[i]),float(z[i]),float(cargas[cont_carga]))
                    cont_carga +=1
                if cont_carga == 58 and i != nmoleculas:
                    cont_carga = 55

            cont_carga = 58

            for i in range((nmoleculas*57)+1,(nmoleculas*60)+1):
                if cont_carga != 61 and i != nmoleculas:    
                    Cela.addChargePoints(float(x[i]),float(y[i]),float(z[i]),float(cargas[cont_carga]))
                    cont_carga +=1
                if cont_carga == 61 and i != nmoleculas:
                    cont_carga = 58

            CelaTrue = Molecule()
        
            for atom in Monomero:
                CelaTrue.addAtom(atom)

            c = 0

            for cp in Cela.getChargePoints():
                if '{},{},{}'.format(cp[0],cp[1],cp[2]) in xyz:
                    pass
                else:
                    CelaTrue.addChargePoints(float(cp[0]),float(cp[1]),float(cp[2]),float(cp[3]))

            Cela = CelaTrue

            return Cela

        if self.sheril == False and self.vsns == False:
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
                    cargas.append(linhas.split()[3])

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

        if self.vsns == True:
            write += '#p {0}/{1} POP={2} SCF=QC density=current NoSymm Charge\n\n'.format(self.metodo,self.base,self.cMethod)        
        elif self.vsns == True and self.cMethod == 'aim':
            write += '#p {0}/{1} AIM=CHARGES SCF=QC GFINPUT IOP(6/7=3) density=current NoSymm Charge\n\n'.format(self.metodo,self.base)
            
        if self.vsns == False:

            if self.base == 'None' and len(self.radii) == 0:
                write += '#p {0} POP={1} density=current NoSymm Charge\n\n'.format(self.metodo,self.cMethod)
            elif self.base == 'None' and len(self.radii) >0:
                write += '#p {0} POP=({1},ReadRadii) density=current NoSymm Charge\n\n'.format(self.metodo,self.cMethod)
            elif self.base != 'None' and len(self.radii) >0:
                write += '#p {0}/{1} POP=({2},ReadRadii) density=current NoSymm Charge\n\n'.format(self.metodo,self.base,self.cMethod)

            elif self.cMethod.lower() == 'aim' and self.vsns == False:
                write += '#p {0}/{1} AIM=CHARGES SCF=TIGHT GFINPUT IOP(6/7=3) density=current NoSymm Charge\n\n'.format(self.metodo,self.base)
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

        #if self.cMethod == 'AIM':
        #    write+= '{}_wfn.wfn'.format(self.name)
        #    write+='\n'

        return write

    def writeInput(self):
        arqv = open('step{0}/{1}_step{0}.gjf'.format(self.step,self.name),'w')
        arqv.write(self.string)  

if __name__ == '__main__':
    y = Molecule()
    
    cargas = ['     1  C    0.058959\n', '     2  H    0.164720\n', '     3  C   -0.212604\n', '     4  H    0.173666\n', '     5  C    0.112217\n', '     6  H    0.122024\n', '     7  C   -0.326464\n', '     8  H    0.191955\n', '     9  C    0.415547\n', '    10  C   -0.397518\n', '    11  H    0.190690\n', '    12  C   -0.030304\n', '    13  H    0.136557\n', '    14  C    0.157883\n', '    15  C   -0.405756\n', '    16  H    0.183219\n', '    17  C    0.323992\n', '    18  C    0.291090\n', '    19  C   -0.241793\n', '    20  H    0.181511\n', '    21  C   -0.236885\n', '    22  H    0.180323\n', '    23  C   -0.081754\n', '    24  H    0.124701\n', '    25  H    0.132542\n', '    26  H    0.068868\n', '    27  C    0.188826\n', '    28  H    0.012759\n', '    29  H    0.060542\n', '    30  H    0.010356\n', '    31  N   -0.067649\n', '    32  O   -0.656348\n', '    33  O   -0.325397\n', '    34  H    0.502737\n', '    35  C   -0.170774\n', '    36  C   -0.165602\n', '    37  H    0.111081\n', '    38  C    0.143189\n', '    39  C   -0.278699\n', '    40  H    0.154666\n', '    41  C   -0.134119\n', '    42  H    0.107945\n', '    43  C   -0.094901\n', '    44  H    0.104039\n', '    45  C   -0.277141\n', '    46  H    0.151727\n', '    47  C    0.206510\n', '    48  C   -0.345998\n', '    49  H    0.165071\n', '    50  C    0.045610\n', '    51  H    0.092306\n', '    52  O   -0.778291\n', '    53  O   -0.749955\n', '    54  O   -0.750949\n', '    55  S    1.471975\n', '    56  O   -0.948543\n', '    57  H    0.478658\n', '    58  H    0.463607\n', '    59  O   -1.007709\n', '    60  H    0.519602\n', '    61  H    0.483484\n']
    
    y.addAtom('C',-5.900792,4.088448,19.211769)
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

    x = step(1, 'HF', '3-21g', y, 'teste', cargas, 13, 13, 13, 13, '10GB', False, '', 'chelpg',True)