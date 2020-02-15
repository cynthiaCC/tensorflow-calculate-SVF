# _*_ coding: utf-8 _*_
import os
import sys
import time

time_start=time.time()

# 识别天空植物建筑
#全景图存储路径
if len(sys.argv) == 2:
    imgfilepath = sys.argv[1]
    #调用pspnet tensorflow
    imgfiles = os.listdir(imgfilepath)

    resultpath = imgfilepath + '-recognized'
    isExists = os.path.exists(resultpath)
    if not isExists:
        os.mkdir(resultpath)
    resultfiles = os.listdir(resultpath)
    for imgfile in imgfiles:
        if imgfile[:-4]+'_seg'+'.jpg' not in resultfiles:
            print(imgfile)
            os.system('python pspnet.py -m pspnet50_ade20k -i '+imgfilepath+'/'+imgfile+' -o '+resultpath+'/'+imgfile)

        else:
            print('已分析过该图片' + imgfile+', 跳过')
time_end=time.time()
print('totally cost',time_end-time_start)