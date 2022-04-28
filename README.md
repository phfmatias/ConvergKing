

ConvergKing is a python script that automate the convergence of electrostatic environment convergence for crystals as described at supermolecular method, "Valverde, C.; Vaz, W. F.; Custodio, J. M. F.; Duarte, V. S.; Carvalho, P. S., Jr.; Figueredo, A. S.; de Aquino, G. L. B.; Baseia, B.; Napolitano, H. B. The Solid State Structure and Environmental Polarization Effect of a Novel Asymmetric Azine. New J. Chem. 2017, 41, 11361−11371".

ConvergKing make use of three input files: 
    a info.in file that contains the quantum-mechanics and crystal simmetry parameters, a info.in example is available on APP folder;
    a assimetrical_unit.xyz file that contain the atomic positioning of the assimetric unit;
    a supercell.xyz file that contain the atomic positioning of the crystal lattice;

ConvergKing output file are:
    a dummy .gjf (Gaussian 16 input file) containing the converged charge field;
    the convergKing.out containing computational details of convergence process as well as the final converged ESP Charges;
    the dipole convergence graph.

Required libraries:
    MoleKing_util -> https://github.com/lopesth/MoleKing_util, The authors would like to thank Lopes TH and Mateus RB for disponibilizing the MoleKing_util chemical package. 
    Matplotlib;
    lmfit;
    numpy;

How to run:
    Just type python3 PATH/ConvergKing/ConvergKing.py

Authors: The LEEDMol Research Group of the Universidade Federal de Goiás (UFG)

More info:
    phfmatias.quimica@gmail.com
