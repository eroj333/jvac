from PIL import Image 
from pytesseract import image_to_string 

image_file = "tt.png";
img = Image.open(image_file);
text = image_to_string(img);
with open('output.txt','w') as file:
	file.write(text)
