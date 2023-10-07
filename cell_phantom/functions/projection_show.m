function []=projection_show(R_reshape,save_flag)% projection_show(R_reshape,0)
    if(~exist('save_flag','var'))
    save_flag = 0;  
    end
    for i = 1:180
        if save_flag==1
                file_save_path_tomograph ='\image_projection';
                prefix = 'projection'; 
                format = 'png'; 
                suffix = strcat('.',format); 
                img2=R_reshape(:,:,i);
                %img2=immultiply(Layer3(:,:,i),255)
                imwrite(uint8(img2),strcat(file_save_path_tomograph, prefix, num2str(i), suffix), format);
        end
        imagesc(R_reshape(:,:,i));colormap("gray");colorbar;%caxis([0 255]);%projection of model after calculation，原模型不同角度投影，可用来追踪
        title('projection of original model');
        axis image off;
        pause(0.1)
    end
end