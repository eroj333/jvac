import os
import imgProcessModule
import tOCR
import cv2

img_n=1
for x in os.listdir('./source/'):
    if x.endswith(".png"):
	print x
	original = cv2.imread('./source/'+x)
	img_n = imgProcessModule.find_objects(original,
	imgProcessModule.line_segments(original,
	imgProcessModule.find_edge(original)), img_n)

tOCR.begin_ocr()

