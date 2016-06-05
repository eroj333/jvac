import os

pdf_file = 'my.pdf'

command = 'convert -density 150 {} -quality 90 page.png | ls'.format(pdf_file)
print "Starting conversion."
os.system(command)
os.system('mv *png images/')
print "Converted all."
