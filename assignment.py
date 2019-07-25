#!/usr/bin/python
# -*- coding: utf-8 -*-

# Author: Venugopal Reddy
# Created: 19 Jul 2019

# Usage: python3 assignment.py <input file>

# Program Starts here
import os
import requests
import sys
import random
import logging
import string
from urllib.parse import urlparse
#from urlparse import urlparse

outDir = os.path.join('.', 'images')
handler = logging.StreamHandler()
logger = logging.getLogger()
formatter = logging.Formatter(
    '%(asctime)s %(name)-12s %(levelname)-8s %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel(logging.DEBUG)



def randomString(stringLength):
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for i in range(stringLength))


def getFilenameFromUrl(url):
    try:
        url = urlparse(url)
        return url.path.split('/').pop()
    except:
        return randomString(8)


def usage():
    print(
        'Usage:\nMissing <Image URL List Text File>\npython3 assignment.py <Path to Image URLs Text File>')


def writeFile(response, filename, image):
    try:
        with open(filename, 'wb') as file:
            for chunk in response.iter_content(4096):
                file.write(chunk)
    except:
        print('unable to write image {image}')


def downloadImages(image):
    try:
        response = requests.get(image, stream=True)
        filename = os.path.join(outDir, getFilenameFromUrl(image))

        if response.status_code == 200:
            writeFile(response, filename, image)
            return True
        else:
            logger.error("Unable to download image " + image)
            return False
    except:
        logger.error("Unable to download image " + image) 
        return False


def readFromFile(filename):
    try:
        with open(filename, 'r') as file:
            return file.readlines()

    except IOError:
        return ''


def verifyFile(filename):
    if(os.path.exists(filename) and os.path.isfile(filename)):
        return True

    return False


def getFilename():
    if(len(sys.argv) != 2):
        usage()
        #sys.exit()
        os._exit(1)
    return sys.argv.pop()


if __name__ == "__main__":
    filename = getFilename()
    images = list()

    if(verifyFile(filename)):
        images = readFromFile(filename)

    logger.info('Image URL List: ' + ", ".join(images))

    if(len(images) == 0):
        print("Error: Error reading file {filename}")
        sys.exit()

    for image in images:
        image = image.strip()
        downloadImages(image)
