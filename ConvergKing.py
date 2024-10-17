##   PYTHON FILE HEADER #
##
##   File:      [ConvergKing.py]
##
##   Author(s): ['Pedro H.F Matias','Mateus R. Barbosa']
##   Site(s):   ['https://github.com/phfmatias','https://github.com/Mateus-RB']
##   Email(s):  ['phfmatias@discente.ufg.br']
##   Credits:   ['Copyright © 2022 LEEDMOL. All rights reserved.']
##   Date:      ['22.10.2022']



from MoleKing import Molecule
from time import time
from os import chdir,getcwd
from sys import argv
from subprocess import call
from APP.runqm import run_g16
from APP.step0 import step0
from APP.header import header
from APP.getcharge import get_charge
from APP.steps import step
from APP.getDipole import getdipole
from APP.getControls import getinfo
from APP.restart import restart

if __name__ == '__main__':

    start = time()
    
    conv = getinfo()
    h = header()
    header = h.headerfile
    

    header.write('\nStarting Convergence.....\n')

    if conv.restart == True:
        rStep = restart(conv.nsteps).problem
        checkRestart = restart(conv.nsteps).norestart
        stepsDone = restart(conv.nsteps).list_steps

        if rStep == 0 or rStep == 1 or checkRestart == True :
            conv.restart = False

        header.write('\nRestart option is just allowed if restart step is bigger than 2. in this case, we will run the simulation from beginning.\n')

    home = getcwd()
    
    arq = open('assimetrical_unit.xyz','r')
    monomer = Molecule()
    rlines = arq.readlines()
    for lines in rlines[2:]:
        monomer.addAtom(str(lines.split()[0]),float(lines.split()[1]),float(lines.split()[2]),float(lines.split()[3]))

    if conv.restart == False:
        header.write('\nRUNNING -> STEP0 -> ')
        step0(conv.name, conv.method, conv.base, monomer,conv.cpu,conv.mem,conv.radii,conv.cMethod,conv.vsns)
        chdir('step0')
        run_g16()
        header.write('DIPOLE MOMENT = {:.4f} -> Runtime: {:.2f}s\n'.format(h.getDipole(conv.cMethod),(abs(start - time()))))
        cargas = get_charge(conv.cMethod,monomer).cargas
        chdir(home)

        for x in range(1,conv.nsteps):
            header.write('RUNNING -> STEP{} -> '.format(x))
            step(x, conv.method, conv.base, monomer, conv.name, cargas, conv.nx, conv.ny, conv.nz, conv.cpu, conv.mem, conv.radii,conv.cMethod,conv.vsns)
            chdir('step{}'.format(x))
            run_g16()  
            header.write('DIPOLE MOMENT = {:.4f} -> Runtime: {:.2f}s\n'.format(h.getDipole(conv.cMethod),(abs(start - time()))))
            cargas = get_charge(conv.cMethod,monomer).cargas
            chdir(home)
        getdipole(conv.name,x,conv.cMethod)
        step('final', conv.method, conv.base, monomer, conv.name, cargas, conv.nx, conv.ny, conv.nz, conv.cpu, conv.mem, conv.radii,conv.cMethod,conv.vsns)
    
    if conv.restart == True:    
        chdir('step'+str(rStep))
        cargas = get_charge(conv.cMethod,monomer).cargas
        chdir('..')

        for sDone in stepsDone:
            chdir(sDone)
            header.write('RUNNING -> STEP{} -> '.format(sDone[-1]))            
            header.write('DIPOLE MOMENT = {:.4f} -> Runtime: {:.2f}s\n'.format(h.getDipole(conv.cMethod),(abs(start - time())))) 
            chdir('..')

        for x in range(rStep+1,conv.nsteps):
            header.write('RUNNING -> STEP{} -> '.format(x))
            step(x, conv.method, conv.base, monomer, conv.name, cargas, conv.nx, conv.ny, conv.nz, conv.cpu, conv.mem,conv.radii,conv.cMethod,conv.vsns)
            chdir('step{}'.format(x))
            run_g16()
            header.write('DIPOLE MOMENT = {:.4f} -> Runtime: {:.2f}s (RESTARTED)\n'.format(h.getDipole(conv.cMethod),(abs(start - time()))))
            cargas = get_charge(conv.cMethod,monomer).cargas
            chdir(home)
        getdipole(conv.name,x,conv.cMethod)
        step('final', conv.method, conv.base, monomer, conv.name, cargas,  conv.nx, conv.ny, conv.nz, conv.cpu, conv.mem, conv.radii,conv.cMethod,conv.vsns)

    if conv.cMethod.lower() == 'chelp' or conv.cMethod.lower() == 'chelpg':
        header.write('\nThe converged ESP Charge using {} scheme are:\n\n'.format(conv.cMethod))
        for x in cargas:
            header.write(x)
    
    elif conv.cMethod.lower() == 'mk':
        header.write('\nThe converged ESP Charge using MK scheme are:\n\n')
        for x in cargas:
            header.write(x)

    elif conv.cMethod.lower() == 'mulliken':
        header.write('\nThe converged Mulliken Charge are:\n\n')
        for x in cargas:
            header.write(x)

    elif conv.cMethod.lower() == 'cm5':
        header.write('\nThe converged CM5 Charge are:\n\n')
        for x in cargas:
            header.write('{}  {}   {}\n'.format(x.split()[0],x.split()[1],x.split()[7]))

    elif conv.cMethod.lower() == 'hirshfeld':
        header.write('\nThe converged Hirshfeld Charge are:\n\n')
        for x in cargas:
            header.write('{}  {}   {}\n'.format(x.split()[0],x.split()[1],x.split()[2]))

    elif conv.cMethod.lower() == 'nbo' or conv.cMethod.lower() == 'npa':
        header.write('\nThe converged Natural Charge ({}) are:\n\n'.format(conv.cMethod))
        for x in cargas:
            header.write('{}  {}   {}\n'.format(x.split()[0],x.split()[1],x.split()[2]))

    header.write('\nRuntime: {:.2f}s'.format(abs(start - time())))
