function []=reconstruction_sinogram_show(R_reshape,save_flag)
    if(~exist('save_flag','var'))
    save_flag = 0;  
    end
    for i = 1:400
        if save_flag==1
                file_save_path_sinogram ='C:\Users\yangb\OneDrive\Desktop\3d_reconstruction\model_build\sinogram_reconstruction\';
                prefix = 'cell'; 
                format = 'jpg'; 
                suffix = strcat('.',format); 
                %img2=immultiply(Layer3(:,:,i),255)
                img2=squeeze(R_reshape(i,:,:));
                imwrite(uint8(img2),strcat(file_save_path_sinogram, prefix, num2str(i), suffix), format);
        end

        %img2=squeeze(R_reshape(i,:,:));
        imagesc(squeeze(R_reshape(i,:,:)));colormap("gray");
        pause(0.1)
    end
end