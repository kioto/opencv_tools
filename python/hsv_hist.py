# -*- coding: utf-8 -*-

import cv2
import pylab
import sys
import os
import glob

def hsv_hist(filename, pshow):
    image_rgb = cv2.imread(filename)
    if image_rgb is None:
        print "%s: No such file or directory" % filename
        quit()
    # HSVに変換
    image_hsv = cv2.cvtColor(image_rgb, cv2.COLOR_BGR2HSV)

    # HSVのヒストグラム
    graph = pylab.figure('HSV histgram')
    ## Hule
    graph.add_subplot(311)
    pylab.hist(image_hsv[:,:,0].ravel(), 180, range=(0,179), fc='r')
    pylab.ylabel('Hule')
    pylab.xlim(0,180)
    ## Saturation
    graph.add_subplot(312)
    pylab.hist(image_hsv[:,:,1].ravel(), 255, range=(0,255), fc='g')
    pylab.ylabel('Satuation')
    pylab.xlim(0,255)
    ## Value
    graph.add_subplot(313)
    pylab.hist(image_hsv[:,:,2].ravel(), 255, range=(0,255), fc='b')
    pylab.ylabel('Value')
    pylab.xlim(0,255)

    if pshow:
        pylab.show()
    else:
        # write file
        basename = os.path.basename(filename)
        (fname, ext) = os.path.splitext(basename)
        out_fname = 'hsv_'+fname+ext
        pylab.savefig(out_fname)
        print out_fname

if __name__ == '__main__':
    # イメージファイル読み込み
    if len(sys.argv) < 2:
        print "usage : python hsv_hist.py [-p] <imagefile> [<imagefiles>...]"
        quit()
    pshow = False
    if '-p' in sys.argv:
        pshow = True
        sys.argv.pop(sys.argv.index('-p'))

    for filename in sys.argv[1:]:
        hsv_hist(filename, pshow)

# end of file
