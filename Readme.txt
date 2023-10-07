Cell Phantom reconstruction

1. Main Module: main.m provides an overview of the process of cell model building, projection, and reconstruction.
2. Rotation Angle Calculation: The folder rotation_angle_calculation includes OpticalFlow.py and PhiTheta_model.py scripts. These scripts are written in Python.
  • OpticalFlow.py script demonstrates how to detect and track the feature points within the simulated cell model.
  • PhiTheta_model.py script presents the calculation process of rotation angle, which is based on the coordinate values of feature points.
After running the Python scripts, the tracked results and calculated rotation angles are stored in the folder rotation_angle_calculation/result.

HL60 Cell Reconstruction
example_data can be download: https://cloudstore.zih.tu-dresden.de/index.php/apps/files/?dir=/mcfocr_tomo_data/Cell_example_data&fileid=595759307

The HL60 cell reconstruction part includes the following modules:
3D Reconstruction: main.m is used to perform the 3D tomographic reconstruction of the cell from pre-processed projections. 

The angle.mat file contains the calculated rotation angles. The pre-processed projections of the cell are stored in the \example_data\preprocessed_projections folder. The final output includes the sinogram and tomography of the reconstructed cell.
ImageJ/FIJI is used to visualize the 3D tomographic reconstruction.

Preprocessing:
1. Cell Detection: The cell_detection module is built upon the YOLOv5 architecture to detect cells from a complex environment.
   Hardware and software used here:Python-3.7.6 torch-1.12.1+cu116 CUDA:0 (NVIDIA GeForce RTX 3050 Laptop GPU, 4096MiB)
   The original sample data 'cell.mp4' and pre-trained network weights 'best.pt' can be downloaded: https://cloudstore.zih.tu-dresden.de/index.php/s/CxMp6P2K5mdjrZt
 	
 • train.py is used to train the YOLOv5 network. The pre-trained network weights are stored in 'best.pt'.
  • detect.py is designed to detect the cell from the large environment.
2. Segmentation: Segmentation is used to isolate the detected cell frames from the background. The method used is the 'Trainable Weka Segmentation' plugin from ImageJ software.
3. Calibration: CalibrationOnOrginal3.py script is used to calibrate each frame to a consistent center point. This calibration is done by finding the minimal enclosed circle of each frame.
     The sample data can be download: https://cloudstore.zih.tu-dresden.de/index.php/apps/files/?dir=/mcfocr_tomo_data/Cell_calibration_segment_image_data&fileid=595761728
4. Angle Calculation:
    The sample data can be download: https://cloudstore.zih.tu-dresden.de/index.php/apps/files/?dir=/mcfocr_tomo_data/Cell_angle_calculation_data&fileid=595761249
  • OpticalFlow_cell.py detects and tracks the features of the cell rotation process.
  • PhiTheta_cell.py calculates the rotation angle based on the detected features.

Note
Please note that this software is currently in a prototype stage, and it is undergoing continuous development and enhancement. We encourage feedback and suggestions to improve this prototype further. Please feel free to open issues or send us your comments.
