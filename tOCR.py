from PIL import Image 
from pytesseract import image_to_string 
from multiprocessing import Pool
import os

files = os.listdir('./forOCR/')

def processed(i):
    if files[i].endswith(".png"):
	    os.system('convert -resize 500% ./forOCR/{} ./forOCR/{}'.format(files[i],'x'+files[i]))
	    print files[i]
	    image_file = "./forOCR/x" + files[i];
	    img = Image.open(image_file);
	    text = image_to_string(img);
	    op_file = './textOP/' + files[i] + '.txt'
	    with open(op_file,'w') as file:
		    file.write(text)
	    os.system('rm {}'.format(image_file))

	    
    else:
        print "Condition not matched"

def begin_ocr():
	pool = Pool(3)
	pool.map(processed,range(len(files)))
	

