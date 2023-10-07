function []=sinogram_original_show(R,save_flag)%sinogram_original_show(R,0)
    if(~exist('save_flag','var'))
    save_flag = 0;  
    end
    %figure;
    for i = 1:400
        if save_flag==1
            file_save_path_tomograph ='C:\Users\yangb\OneDrive\Desktop\3d_reconstruction\model_build\sinogram_original\';
            prefix = 'sinogram';
            format = 'png'; 
            suffix = strcat('.',format); 
            img2=R(:,:,i);
            %img2=immultiply(Layer3(:,:,i),255)
            imwrite(uint8(img2),strcat(file_save_path_tomograph, prefix, num2str(i), suffix), format);
        end
    imagesc(R(:,:,i));colormap("gray");%colorbar;caxis([0 100]);
    title('sinogram of original model');
    pause(0.05);
    end
end