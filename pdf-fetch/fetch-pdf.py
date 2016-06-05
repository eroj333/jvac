'''
Download Today's newspaper from Kantipur.
'''

import urllib2
from datetime import date

url = 'http://epaper.ekantipur.com/epaper/the-kathmandu-post/'


def download_pdf(url):
    pdf_file = urllib2.urlopen(url).read()
    with open(output_name, 'wb') as file:
        file.write(pdf_file)

today = date.today()
year = today.year
month = today.month
day = today.day
if month < 10:
    month = '0' + str(month)
if day < 10:
    day = '0' + str(day)
current = "{}-{}-{}".format(year, month, day)
url += '{}/{}.pdf'.format(current, current)

output_name = 'Epaper-' + current + '.pdf'
download_pdf(url)
