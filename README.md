BUOY_DETECT
-----------
This repository contains the codes that uses ML (Machine Learning) techniques to detect the buoy. This is a combination of 3 parts - 


(1) `Pixel-trainer` : A ML-trainer module.


(2) `vw_detect` (`vw` = `vowpal wabbit`) : This module detects the buoy boundary with the help of ML, by taking the training data output of `Pixel-trainer`.


(3) `Region-blower` : This module blows / colors the region within the buoy boundary detected by `vw_detect`.

RUNNING THE SCRIPTS
-------------------

Without ROS

(1) `Pixel-trainer` :
                      
                      (1) Clone the repository : [Pixel-trainer-vw](https://github.com/pranaypratyush/Pixel-Trainer/tree/vw) 
                      
                      (2) `cd` into the directory
                      
                      (3) Run `cmake .`
                      
                      (4) Now run `./main path/to/the/imagefile`
                      
                      (5) Labelling involves pressing a key and left clicking and dragging the mouse
                      
                          For labelling Yellow press Crtl key
                          
                          For labelling Green press Shift key
                          
                          For labelling Red press Alt key
                          
                      (6) After labelling,click on the broom icon to save the hsv values to a `.txt` file
                      
                      (7) Click the `save` icon to save the image.



CONTRIBUTION
------------
The work flow is the same as that of any other repository. 


(1) Fork / clone the repository.


(2) Create a new branch , say `my-changes` and make your changes in this branch.


(3) Commit your changes and send a Pull request (PR) to this repository.

LICENSE
-------
[The MIT License](LICENSE.md) - [Team AUV , IIT Kharagpur](https://github.com/auviitkgp) - All Rights Reserved.
