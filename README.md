![ConvergKing_Grad](https://user-images.githubusercontent.com/71854729/213286756-76a8e58b-c51c-45fb-a530-34a607cd753e.png)

---
# ConvergKing


**ConvergKing** is a python script that automate the convergence of electrostatic environment convergence for crystals as described at [supermolecular method](https://pubs.rsc.org/en/content/articlelanding/2017/nj/c7nj00618g).

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
   <li> MoleKing_util -> https://github.com/lopesth/MoleKing_util, The authors would like to thank Lopes TH and Mateus RB for disponibilizing the MoleKing_util chemical package.</li>
    <li>Matplotlib;</li>
    <li>lmfit;</li>
    <li>numpy;</li>
    </ul>
    
---
        
# How to run:
```bash
python3 PATH/ConvergKing/ConvergKing.py
 ```

---
        
# Authors

The LEEDMol Research Group of the Universidade Federal de Goiás (UFG)

---
        
# Contact

email: phfmatias@discente.ufg.br
