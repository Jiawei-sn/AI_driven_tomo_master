function []=reconstruction_tomograph_show(Layer3,save_flag)
    if(~exist('save_flag','var'))
    save_flag = 0; 
    end
    for i = 1:400
            if save_flag==1
                file_save_path_tomograph ='C:\Users\yangb\OneDrive\Desktop\3d_reconstruction\model_build\tomograph_reconstruction\';
                prefix = 'cell'; 
                format = 'jpg'; 
                suffix = strcat('.',format); 
                img2=immultiply(Layer3(:,:,i),255);
                imwrite(uint8(img2),strcat(file_save_path_tomograph, prefix, num2str(i), suffix), format);
            end
        imagesc(Layer3(:,:,i));colormap("gray");caxis([0 1]);
        title(['tomography of reconstructed model,stack layer' num2str(i)]);colorbar;axis image off;
        pause(0.05);
    end
end