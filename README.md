# tensorflow-calculate-SVF
Using [PSPNet-Keras-tensorflow](https://github.com/Vladkryvoruchko/PSPNet-Keras-tensorflow) to calculate SVF(sky view factor) and TVF(tree view factor).

## Usage:
1. Install dependencies: `pip install -r requirements.txt --upgrade`

2. download [pspnet50_ade20k.h5](https://www.dropbox.com/s/0uxn14y26jcui4v/pspnet50_ade20k.h5?dl=1), [pspnet50_ade20k.json](https://www.dropbox.com/s/v41lvku2lx7lh6m/pspnet50_ade20k.json?dl=1), this is the weight I used in this project. (for more information please refer to [this link](https://github.com/Vladkryvoruchko/PSPNet-Keras-tensorflow).)

3. Go to the project directory, create a folder `'imgs'`(or whatever you like) and put your panorama pictures in it.

4. Run `python autoCallpspnet.py imgs`, the program identifies sky/tree/building elements in the pictures and colors them differently. The recognized pictures are automaticlly saved in imgs-recognized.  

![origin](https://github.com/cynthiaCC/tensorflow-calculate-SVF/blob/master/imgs/01-108.971906%2C34.245881.jpg)  
![recognized](https://github.com/cynthiaCC/tensorflow-calculate-SVF/blob/master/imgs-recognized/01-108.971906%2C34.245881_seg.jpg)  

5. Run `python PanoramicToFisheye.py imgs-recognized`. This will transfer the panorama pictures to fisheye pictures in order to calculate SVF and TVF. The fisheye pictures are automaticlly saved in imgs-fisheye.  

![recognized](https://github.com/cynthiaCC/tensorflow-calculate-SVF/blob/master/imgs-recognized/01-108.971906%2C34.245881_seg.jpg)  
![fisheye](https://github.com/cynthiaCC/tensorflow-calculate-SVF/blob/master/imgs-fisheye/01-108.971906%2C34.245881_seg.jpg)  

6. Run `python calculateResult.py imgs-fisheye`. This will calculate SVF and TVF results.
