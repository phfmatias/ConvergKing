##   PYTHON FILE HEADER #
##
##   File:      [getDipole.py]
##
##   Author(s): ['Pedro H.F Matias','Mateus R. Barbosa]
##   Site(s):   ['https://github.com/phfmatias','https://github.com/Mateus-RB']
##   Email(s):  ['phfmatias@discente.ufg.br']
##   Credits:   ['Copyright © 2022 LEEDMOL. All rights reserved.']
##   Date:      ['22.10.2022']

from os import mkdir, listdir
import matplotlib.pyplot as pyplot
from lmfit import Model
from numpy import arange,exp,array

def E(x, a, b, c):
    return a+b*exp(-c*x)

class getdipole:

    def __init__(self,name,steps,cMethod):
        self.name = name
        self.cMethod = cMethod
        self.dip = []
        folders = ['step{}'.format(i) for i in range(steps+1)]
        for arqs in folders:
            self.dip.append(self.getDipole(arqs+'/'+name+'_'+arqs+'.log'))
        self.plotGraph()

    def getDipole(self,name):
        x = open(name,'r')
        rlines = x.readlines()
        tot = []
        for i in range(len(rlines)):
            if 'Tot=' in rlines[i] and 'NPt' not in rlines[i]:
                tot.append(rlines[i])
        dipole = float(tot[-1].split()[7])
        return dipole

    def plotGraph(self):

        dadosy = array(self.dip)
        dadosx = arange(len(self.dip))        
        Modelo_ajuste = Model(E) # definimos o modelo de ajuste com Model
        ajusteMarcos = Modelo_ajuste.fit(dadosy, x=dadosx, a=1, b=1, c=2)
        # print(ajusteMarcos.fit_report())

        YY=E(arange(0,10,0.01), ajusteMarcos.params['a'].value, ajusteMarcos.params['b'].value, ajusteMarcos.params['c'].value)

        pyplot.title('Convergência de Dipolo do {0} - {1}'.format(self.name,self.cMethod))
        pyplot.plot(arange(0,10,0.01), YY, '--', color='#000000')
        pyplot.plot(dadosx, dadosy, 'o', markersize=9, color='#0000cc')
        pyplot.ylabel('Dipole (D)', fontsize=15)
        pyplot.xlabel('Interation Step', fontsize=15)
        pyplot.xlim(-0.2, max(dadosx)+0.2)
        pyplot.xticks(range(len(dadosy)), range(len(dadosy)))
        pyplot.savefig('{0}_{1}.png'.format(self.name,self.cMethod), dpi=500, transparent=True) ##Aqui troca o nome##

if __name__ == '__main__':

    getdipole('teste', 1, 'mulliken')