#!/bin/bash
# Installs the requirements for the project

# Install ImageMagick
apt-get -y install imagemagick

# Install OpenCV2
apt-get -y install 

# Install the python binding for opencv
apt-get -y install libopencv-dev python-opencv

# Install Tesseract
apt-get -y install tesseract-ocr

# Install PIP
apt-get -y install python-pip

# Install Virtualenv
pip install virtualenv

# Install RVM
\curl -sSL https://get.rvm.io | bash -s stable

# Install Ruby
rvm install 2.3.1
rvm --default use 2.1.1

# Install Rails
gem install -V rails -v 3.2.16