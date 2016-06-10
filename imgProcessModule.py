import cv2 
import numpy as np

def find_edge(original):
    imgray = cv2.cvtColor(original, cv2.COLOR_BGR2GRAY)
    return cv2.Canny(imgray,120,150,apertureSize = 5)

def line_segments(original, imgray):
    minLineLength = 100
    maxLineGap = 10
    l,w,c = original.shape
    fLines = np.zeros((l,w,c),np.uint8)
    lines = cv2.HoughLinesP(imgray,1,np.pi/180,500,minLineLength,maxLineGap)
    for x1,y1,x2,y2 in lines[0]:
    	cv2.line(fLines,(x1,y1),(x2,y2),(255,255,255),2)
    return  fLines

def find_objects(original, lines,img_n):
    
    gLines = cv2.cvtColor(lines, cv2.COLOR_BGR2GRAY)
    contours, hierarchy = cv2.findContours(gLines, cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    for c in contours:
	approx = cv2.approxPolyDP(c, .01 * cv2.arcLength(c,True),True)
	if ( len(approx) >=4):
	    x,y,w,h = cv2.boundingRect(c)
	    if 400<h<900 and 400<w<1000:
		roi = original[y:y+h,x:x+w]
		cv2.imwrite("./forOCR/" + str(img_n) + ".png",roi)
		img_n=img_n+1;

    return img_n;



