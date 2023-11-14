# AI-driven Projection Tomography Reconstruction

## Cell Phantom Reconstruction

## Overview
- **Main Module**: `main.m` provides a step-by-step illustration of the cell model building, projection, and reconstruction processes.

## Rotation Angle Calculation
The `rotation_angle_calculation` folder contains Python scripts:
- `OpticalFlow.py`: Demonstrates feature point detection and tracking within the simulated cell model.
- `PhiTheta_model.py`: Outlines the rotation angle calculation based on the feature points' coordinates.

After executing these Python scripts, results, along with the computed rotation angles, can be found in `rotation_angle_calculation/result`.

## HL60 Cell Reconstruction

**Test Data**: [Download here](https://doi.org/10.6084/m9.figshare.24523618).

Modules:
- **3D Reconstruction**: `main.m` facilitates the 3D tomographic reconstruction using pre-processed projections.
  - `angle.mat` includes the determined rotation angles.
  - Pre-processed cell projections are saved in `\example_data\preprocessed_projections`.
  - The final results comprise both the sinogram and tomographic reconstructions of the cell.
  
Visualization of the 3D tomographic reconstruction can be achieved using ImageJ/FIJI.

## Preprocessing

1. **Cell Detection**:
   - Based on the YOLOv5 architecture, the `cell_detection` module detects cells within intricate environments.
   - **Environment**:
     - Python-3.7.6
     - torch-1.12.1+cu116
     - CUDA:0 (NVIDIA GeForce RTX 3050 Laptop GPU, 4096MiB)
   - **Resources**: 
     - `train.py`: Trains the YOLOv5 network. Pre-trained weights are saved in 'best.pt'.
     - `detect.py`: Cell detection in extensive environments.
     
2. **Segmentation**: 
   - The 'Trainable Weka Segmentation' plugin from ImageJ helps isolate detected cell frames from the background.

3. **Calibration**: 
   - `CalibrationOnOrginal3.py`: Calibrates each frame to a consistent central point by identifying the minimal enclosing circle.

4. **Angle Calculation**:
     - `OpticalFlow_cell.py`: Detects and tracks the cell rotation features.
     - `PhiTheta_cell.py`: Determines the rotation angle using the tracked features.

## Note
This software is still in its prototype phase, undergoing regular enhancements. Feedback and suggestions are highly encouraged to refine the prototype. For any queries or suggestions, raise an issue or contact us directly.
