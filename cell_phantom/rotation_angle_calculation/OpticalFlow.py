import numpy as np
import cv2
from matplotlib import pyplot as plt
import os

video = 'model'
folder_name = 'result'
if not os.path.exists(folder_name):
    os.makedirs(folder_name)

cap = cv2.VideoCapture(video + '.avi')
res = (1135, 800)
fourcc = cv2.VideoWriter_fourcc(*'MP4V')  #codec
video_path = os.path.join(folder_name, 'model_Tracked.mp4')
out = cv2.VideoWriter(video_path, fourcc, 10.0, res)
# create figure for ploting
fig, (ax2, ax3) = plt.subplots(2, 1)

# params for ShiTomasi corner detection
feature_params = dict(maxCorners=3,
                      qualityLevel=0.04,
                      minDistance=4,
                      blockSize=4)

# Parameters for lucas kanade optical flow
lk_params = dict(winSize=(10, 10),
                 maxLevel=1,
                 criteria=(cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 0.03))
# Empty array
value = []#coordinate values of 3 points
# Create some random colors
color = [[255, 229, 51], [0, 201, 182], [213, 158, 186]]

# Take first frame and find corners in it
ret, old_frame = cap.read()
old_gray = cv2.cvtColor(old_frame, cv2.COLOR_BGR2GRAY)

p0 = cv2.goodFeaturesToTrack(old_gray, mask=None, **feature_params)
print(p0)
# Create a mask image for drawing purposes
mask = np.zeros_like(old_frame)
z = 0
while (1):
    z += 1

    ret, frame = cap.read()
    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # calculate optical flow
    p1, st, err = cv2.calcOpticalFlowPyrLK(old_gray, frame_gray, p0, None, **lk_params)

    # Select good points
    good_new = p1[st == 1]
    good_old = p0[st == 1]
    value.append(good_old)
    # draw the tracks
    for i, (new, old) in enumerate(zip(good_new, good_old)):

        a, b = new.ravel()
        c, d = old.ravel()
        mask = cv2.line(mask, (int(a),int(b)),(int(c),int(d)), color[i], 8)
        frame = cv2.circle(frame, (int(a),int(b)), 10, color[i], -1)
    img =cv2.add(frame, mask)

    print(z) #to see how many frames

    out.write(img)

    # plotting
    # ax1.plot(good_old[0][0],good_old[0][1], 'ro')#X and Y point 1
    # ax1.plot(good_old[1][0],good_old[1][1], 'go')#X and Y point 2
    # ax1.plot(good_old[2][0],good_old[2][1], 'bo')#X and Y point 3
    # ax2.set_xlim(0, 150)
    # ax2.set_ylim(1, 140)
    # ax2.plot(z, good_old[0][0], 'bo')  # x with framerate point 1，第一个数字代表第几个点，第二个数字代表行，即x,y
    # ax2.plot(z, good_old[1][0], 'go')  # x with framerate point 2
    # ax2.plot(z, good_old[2][0], 'ro')  # x with framerate point 3
    # ax3.set_xlim(0, 150)
    # ax3.set_ylim(1, 140)
    # ax3.plot(z, good_old[0][1], 'bo')  # y with framerate point 1
    # ax3.plot(z, good_old[1][1], 'go')  # y with framerate point 2
    # ax3.plot(z, good_old[2][1], 'ro')  # y with framerate point 3

    # Now update the previous frame and previous points
    old_gray = frame_gray.copy()
    p0 = good_new.reshape(-1, 1, 2)
    if z == 179:
        break
out.release()
cv2.destroyAllWindows()



