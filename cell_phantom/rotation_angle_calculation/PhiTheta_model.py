import numpy as np
import matplotlib.pyplot as plt
import math
import scipy.io as io
import matplotlib.animation as animation
import h5py
import os

value = np.load('model.npy')
sum_x = [0] * 180
sum_x2 = [0] * 180
sum_x3 = [0] * 180

sum_z = [0] * 466
sum_z2 = [0] * 466
sum_z3 = [0] * 466

diff_x = [0] * 466
diff_x2 = [0] * 466
diff_x3 = [0] * 466

diff_z = [0] * 466
diff_z2 = [0] * 466
diff_z3 = [0] * 466

angle_x_save = [0] * 466
angle_x2_save = [0] * 466
angle_x3_save = [0] * 466

angle_z_save = [0] * 466
angle_z2_save = [0] * 466
angle_z3_save = [0] * 466


def set_equirectangluar_plot():
    # plt.xlim(-180, 180)
    plt.ylim(-180, 180)
    # plt.xticks(np.arange(-180.0, 181.0, step=45.0))
    plt.yticks(np.arange(-180.0, 181.0, step=30.0))
    # plt.xlabel('Longitude [degree]')
    # plt.ylabel('Lattitude [degree]')
    plt.grid()

def plotting_point(x, y):
    ###############
    ##Potato Cell
    # r= 62
    # x_center=88
    # y_center=68

    r = 314 # radius of the object
    x_center = 567.5  # the x coordinate of the centre point xm
    y_center = 401  # the y coordinate of the cntre point ym
    ############

    z_center = np.sqrt(
        abs(r * r - x_center * x_center - y_center * y_center))

    z = np.sqrt(r * r - (x_center - x) * (x_center - x) - (y_center - y) * (y_center - y)) + z_center
    # 或者z=z_center-np.sqrt(r * r - (x_center - x) * (x_center - x) - (y_center - y )* (y_center - y))

    # if flag2>0:
    #     z = np.sqrt(r * r - (x_center - x) * (x_center - x) - (y_center - y )* (y_center - y))
    # else:
    #     z=-np.sqrt(-(r * r - (x_center - x) * (x_center - x) - (y_center - y )* (y_center - y)))

    dx = x - x_center
    dy = y - y_center
    dz = z - z_center

    r_new=math.sqrt(r*r-dy*dy)

    angle_x = math.acos(dy/r_new)  # np.arctan(dz/dy),math.acos(dy/r)
    #if abs(r_new)<abs(dx): r_new=dx
    angle_y = math.acos(dx/r_new)  # np.arctan(dz/dx),math.acos(dx/r_new)
    angle_z = np.arctan(dy / dx)

    return  angle_y * 180 / np.pi, r_new, angle_z * 180 / np.pi#dx, dy,dz#


for i in range(0, len(value) - 1):  # i<466 range(0, len(value) - 1)
    angle_x, angle_y, angle_z = plotting_point(value[i][0][0], value[i][0][1])
    angle_x2, angle_y2, angle_z2 = plotting_point(value[i][1][0], value[i][1][1])
    angle_x3, angle_y3, angle_z3 = plotting_point(value[i][2][0], value[i][2][1])

    angle_x_save[i] = angle_x
    angle_x2_save[i] = angle_x2
    angle_x3_save[i] = angle_x3


    angle_z_save[i] = angle_z
    angle_z2_save[i] = angle_z2
    angle_z3_save[i] = angle_z3



# np.save('angle_original_x0', angle_x_save)  # 保存直线的数据
# np.save('angle_original_x1', angle_x2_save)
# np.save('angle_original_x2', angle_x3_save)
def angle_x_save_plot():
    #plt.figure(figsize=(2, 4))
    #plt.figure(dpi=50)
    for i in range(0, 180):  # 对angle_x进行累加 range(0, 466)
        if i > 0:

            diff_x[i] = angle_x_save[i] - angle_x_save[i - 1]
            if abs(diff_x[i])>2:
                diff_x[i]=2
            sum_x[i] = sum_x[i - 1] + abs(diff_x[i])
            #if i==126:sum_x[i]=sum_x[i]+63

            diff_x2[i] = angle_x2_save[i] - angle_x2_save[i - 1]  # 第二个点
            if abs(diff_x2[i])>2:
                diff_x2[i]=2

            sum_x2[i] = sum_x2[i - 1] + abs(diff_x2[i])
            #if i == 125: sum_x2[i] = sum_x2[i] + 40.75

            diff_x3[i] = angle_x3_save[i] - angle_x3_save[i - 1]  # 第三个点
            if abs(diff_x3[i])>2:
                diff_x3[i]=2
            sum_x3[i] = sum_x3[i - 1] + abs(diff_x3[i])

            # if sum_x3[i]>112:
            #     sum_x3[i]=sum_x3[i]-10
            plt.plot(i, sum_x[i], 'bo', linewidth=1, markersize=1)
            plt.plot(i, sum_x2[i], 'go', linewidth=1, markersize=1)
            # plt.xlim((0, 25))
            # plt.ylim((0, 200))
            #plt.axis([0,27,0,200])
            plt.plot(i, sum_x3[i], 'ro', linewidth=1, markersize=1)
            plt.xlabel('Time [s]')  #
            plt.ylabel('Cell orientation [°]')

            plt.grid()

angle_x_save_plot()

# np.save('sum_x0',sum_x)
# np.save('sum_x1',sum_x2)
# np.save('sum_x2',sum_x3)
#print(sum_x3)



#angle_z_save_plot()
#plt.savefig("Angle_x-axis.png", dpi=300, quality=80, optimize=True, progressive=True)
#io.savemat('model4.mat',{'model4':sum_x})
x_new=np.linspace(0,180,180)
p3 = plt.plot(x_new,  x_new , 'k-')
folder_name = 'result'

if not os.path.exists(folder_name):
    os.makedirs(folder_name)

save_path = "result/rotation_angle_calculation.png"
plt.savefig(save_path, dpi=300)
# plt.savefig("rotation_angle_calculation.png", dpi=300)
plt.show()
