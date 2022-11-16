![ConvergKing](https://user-images.githubusercontent.com/71854729/165822220-36ace15b-dc87-4266-aeb5-4ee5680e9fdc.png)

---
# ConvergKing


**ConvergKing** is a python script that automate the convergence of electrostatic environment convergence for crystals as described at supermolecular method, "Valverde, C.; Vaz, W. F.; Custodio, J. M. F.; Duarte, V. S.; Carvalho, P. S., Jr.; Figueredo, A. S.; de Aquino, G. L. B.; Baseia, B.; Napolitano, H. B. The Solid State Structure and Environmental Polarization Effect of a Novel Asymmetric Azine. New J. Chem. 2017, 41, 11361−11371".

---
# Input Files


ConvergKing make use of **three** input files: 
    <ul>
    <li>a info.in file that contains the quantum-mechanics and crystal simmetry parameters, a info.in example is available on APP folder;</li>
    <li>a assimetrical_unit.xyz file that contain the atomic positioning of the assimetric unit;</li>
    <li>a supercell.xyz file that contain the atomic positioning of the crystal lattice;</li>
    </ul>

---
# Output Files

ConvergKing output file are:
    <ul>
    <li>a dummy .gjf (Gaussian 16 input file) containing the converged charge field;</li>
    <li>the convergKing.out containing computational details of convergence process as well as the final converged ESP Charges;</li>
    <li>the dipole convergence graph.</li>
    </ul>

---
# Required Libraries
    <ul>
    <li>MoleKing_util -> https://github.com/lopesth/MoleKing_util, The authors would like to thank Lopes TH and Mateus RB for disponibilizing the MoleKing_util chemical package.</li>
    <li>Matplotlib;</li>
    <li>lmfit;</li>
    <li>numpy;</li>
    </ul>
    
---
        
# How to run:
    ```python
    python3 PATH/ConvergKing/ConvergKing.py
    ```

---
        
# Authors

The LEEDMol Research Group of the Universidade Federal de Goiás (UFG)

---
        
# Contact

email: phfmatias@discente.ufg.br
