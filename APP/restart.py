##   PYTHON FILE HEADER #
##
##   File:      [restart.py]
##
##   Author(s): ['Pedro H.F Matias','Mateus R. Barbosa]
##   Site(s):   ['https://github.com/phfmatias','https://github.com/Mateus-RB']
##   Email(s):  ['phfmatias@discente.ufg.br']
##   Credits:   ['Copyright © 2022 LEEDMOL. All rights reserved.']
##   Date:      ['22.10.2022']

from MoleKing_util import Molecule
from os import mkdir, listdir,getcwd,chdir
from numpy import arange

class restart:
    def __init__(self,nsteps):
        self.list_steps = [x for x in listdir() if 'step' in x] 
        if 'stepfinal' in self.list_steps:
            index = self.list_steps.index('stepfinal')
            self.list_steps.pop(index)
        
        if len(self.list_steps) == nsteps:
            self.norestart = True
        
        else:
            self.norestart = False

        self.nsteps = nsteps  
        self.checkSteps()

    def checkSteps(self):
        check = False
        for steps in self.list_steps:
            chdir(steps)
            rlines = open([x for x in listdir() if '.log' in x][0],'r').read()
            if 'Normal termination of Gaussian' not in rlines:
                self.problem = int(steps[-1])
                check = True
            chdir('..')     
        
        if check == False:
            self.problem = int(max(self.list_steps)[-1])

        #if len(self.list_steps)       

if __name__ == '__main__':
    x = restart(5)