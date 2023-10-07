function []=tomograph_original_show(original_model,save_flag)%slice_original_show(original_model,0)
if(~exist('save_flag','var'))
    save_flag = 0;  % 如果未出现该变量，则对其进行赋值
end
for i = 1:400
    if save_flag==1
        %             file_save_path_tomograph ='C:\Users\yangb\OneDrive\Desktop\3d_reconstruction\model_build\tomograph_original\';
        %             prefix = 'tomograph'; % 文件名前缀
        %             format = 'png'; % （图片）文件格式
        %             suffix = strcat('.',format); % 文件后缀
        img2=original_model(:,:,i);
        img2=immultiply(img2/1.3,255);%%%%%%%%%%%%%%%img2/1.3,1.3为像素最大值
        %             imwrite(uint8(img2),strcat(file_save_path_tomograph, prefix, num2str(i), suffix), format);%保存图像到目标位置
    end
    img2=original_model(:,:,i);
    imagesc(img2);colormap("gray");caxis([0 1]);%slice of original moddel,原模型切片
    title(['tomography of original model,stack layer' num2str(i)]);colorbar;axis image off;
    pause(0.05);
end
%figure;
end