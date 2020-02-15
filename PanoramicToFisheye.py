# _*_ coding: utf-8 _*_

import cv2
import numpy as np
import math
import os
import time
import sys

time_start=time.time()


# 生成鱼眼图
if len(sys.argv) == 2:
    filepath = sys.argv[1]
    files = os.listdir(filepath)

    outputpath = filepath[:-10] + 'fisheye'
    isExists = os.path.exists(outputpath)
    if not isExists:
        os.mkdir(outputpath)
    cx = 1024 / (2 * math.pi)
    cy = 1024 / (2 * math.pi)
    r0 = 1024 / (2 * math.pi)

    def create_img(img_name):
        #png_name = "108.952271_34.270684.png"
        img = cv2.imread(filepath+'\\'+ img_name)
        fisheyeimg = np.zeros([250, 250, 3], np.uint8)
        for xf in range(250):
            for yf in range(250):
                r = math.sqrt((xf - cx) ** 2 + (yf - cy) ** 2)
                if yf < cx:
                    theta = 3 * math.pi / 2 - math.atan((xf - cy) / (yf - cx))
                else:
                    theta = math.pi / 2 - math.atan((xf - cy) / (yf - cx))
                yc = int(theta * 1024 / (2 * math.pi))
                xc = int(r * 512 / r0)
                if (xc <= 256 and yc < 1024):
                    # png格式
                    # fisheyeimg[xf, yf] = np.append(img[xc, yc],-1)

                    # jpg格式
                    fisheyeimg[xf, yf] = img[xc, yc]
        # cv2.imshow("Display window", fisheyeimg)
        # cv2.waitKey(0)

        # 将图片裁剪一下，提高计算效率
        cropped_fisheye = fisheyeimg[77:250, 77:250]
        # circle center[163,163], radius = 81 保存为jpj格式
        fliped_img = cv2.flip(cropped_fisheye, 1, dst=None)  # 水平镜像 isExists=os.path.exists(path)
        cv2.imwrite(outputpath+'/' + img_name, fliped_img, [int(cv2.IMWRITE_JPEG_QUALITY), 100])
        # circle center[163,163], radius = 81 保存为png格式
        # cv2.imwrite(png_name, cropped_fisheye, [int(cv2.IMWRITE_PNG_COMPRESSION), 0])

    for img_name in files:
        print('开始生成'+img_name+'的鱼眼图.....')
        create_img(img_name)
        print('生成完毕！')

time_end=time.time()
print('totally cost',time_end-time_start)