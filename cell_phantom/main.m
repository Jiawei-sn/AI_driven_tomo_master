%% 
clc;
clear all;
addpath("functions\");
%% model building
% parameter of original model

e =    [  
          0.3   .80   .80   .80      0       0        0      0      0      0    
          -.7   .50   .30   .40      0  -.0184      0.2      0      0     10    
          1.5   .15   .15   .15      0  -.0184      0.2      0      0      0    
            6  .025  .025  .025      0    -0.6     -0.5      0      0      0    
            6  .025  .025  .025   0.67     0.3    -0.25      0      0      0    
         ];

original_model = phantom3d(e,400);


%% projection
theta = 0:180;% projection angle

for i = 1:400
    R(:,:,i) = radon(squeeze(original_model(:,:,i)),theta);%sinogram of model,(sinogram纵坐标（图像宽度？）,angle角度,i层数)
end

R_reshape = permute(R,[3,1,2]);

%% display the projection and sinogram of original model

projection_show(R_reshape);% display the projection of original model
sinogram_original_show(R);% display the sinogram of original model
tomograph_original_show(original_model);% display the tomography of original model

%% reconstruction
x = 0:180;
%The calculated rotation angle theta0 is a linear function,
%the parameters are obtained based on optical flow feature point tracking and angle calculation.
theta0=0.9768*x+20; 

for i = 1:400
    Layer3(:,:,i)=iradon(squeeze(R_reshape(i,:,:)),theta,'spline','Shepp-Logan');%(each layer,i)
    disp(i);
end

%% reconstruction display

reconstruction_tomograph_show(Layer3); 


