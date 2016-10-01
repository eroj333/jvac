'''
Fetch the epaper for current day.
'''

import urllib2
from datetime import date


def download_file(url, location=''):
    file_name = url.split('/')[-1]
    location += file_name
    u = urllib2.urlopen(url)
    f = open(location, 'wb')
    meta = u.info()
    file_size = int(meta.getheaders("Content-Length")[0])
    print " Downloading: %s \n Size: %d MB" % (file_name, file_size / 1048576)

    file_size_dl = 0
    block_sz = 8192
    while True:
        buffer = u.read(block_sz)
        if not buffer:
            break

        file_size_dl += len(buffer)
        f.write(buffer)
        status = r"Completed: %3.2f%%" % (file_size_dl * 100. / file_size)
        status = status + chr(8)*(len(status)+1)
        print status,
    f.close()

if __name__ == '__main__':
    url = 'http://epaper.ekantipur.com/epaper/the-kathmandu-post/'
    today = date.today()
    year = today.year
    month = today.month
    day = today.day
    current = "{}-{:02}-{:02}".format(year, month, day)
    url += '{}/{}.pdf'.format(current, current)
    download_file(url, '/home/anon/Desktop/')
