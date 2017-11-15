from PIL import Image as im
from PIL import ImageChops as ic
import random as rd
import numpy as np
import cPickle

#SET THESE VARIABLES
clothTypeToCat = "FILL IN NAME" #Should fill in list_category_cloth.txt for regular script
imagesAndLabels = "FILL IN NAME" #Should fill in list_category_
saveFile = "FILL IN NAME" # e.g. foobar.pkl
RESIZE_SIZE = 48 #Change depending on what input your CNN expects

#You can change these variables, but these are good defaults
SHADING_RANGE = range(15, 20)
ROTATION_RANGE = range (-15, 15)
OCCLUSION_SIZE = 6
OCCLUSION_BOX = im.fromarray(np.zeros((OCCLUSION_SIZE, OCCLUSION_SIZE, 3), dtype=np.uint8), "RGB")


def getConvertedCategories(filename):
    d = {}
    with open(filename) as f:
        numPairs = int(f.readline())
        colNames = f.readline().split()
        for i in range(numPairs):
           (key, val) = f.readline().split()
           d[i] = int(val)
    return d

def getImagesAndLabels(filename, categoryDict):
    images = []
    with open(filename) as f:
        numImages = int(f.readline())
        colNames = f.readline().split()
        for i in range(numImages):
            (img, label) = f.readline().split()
            images.append((img, categoryDict[int(label)]))
    return images

def add(a, b):
    return a+b

def subtract(a, b):
    return a - b


def genRandomOcclusion(image, label):
    image = image.copy()
    upper = rd.randint(2, RESIZE_SIZE - OCCLUSION_SIZE - 2)
    left = rd.randint(2, RESIZE_SIZE - OCCLUSION_SIZE - 2)
    lower = upper + OCCLUSION_SIZE
    right = left + OCCLUSION_SIZE
    image.paste(OCCLUSION_BOX, (left, upper, right, lower))
    return (np.asarray(image), label)

def genRandomShading(image, label):
    difference = rd.choice(SHADING_RANGE)
    operation = rd.choice([add ,subtract])
    shade = lambda x: min(max(operation(x, difference), 0), 256)
    image = im.eval(image, shade)
    return (np.asarray(image), label)

def genRandomRotation(image, label):
    image = image.rotate(rd.choice(ROTATION_RANGE))
    return (np.asarray(image), label)

#Call this function to open, transform, and resave images/labels in a list of tuples
def runScript():
    print("\n\nWARNING:\n")
    print("Make sure to set correct values for the variables at the top of the script (see comment above)\n\n")
    categoryDict = getConvertedCategories(clothTypeToCat)
    trainingData = getImagesAndLabels(imagesAndLabels, categoryDict)
    finalTrainingData = []
    for image, label in trainingData:
        image = im.open(image).convert("RGB")
        image = image.resize((RESIZE_SIZE, RESIZE_SIZE))
        imageMtx = np.asarray(image)
        finalTrainingData.append((imageMtx, label))
        finalTrainingData.append(genRandomOcclusion(image, label))
        finalTrainingData.append(genRandomShading(image, label))
        finalTrainingData.append(genRandomRotation(image, label))
    cPickle.dump(finalTrainingData, open(saveFile, "wb"))
    print("Saved file at " + saveFile)
    return None

#Function used for testing, don't call
def examine():
    pics = cPickle.load(open(saveFile, "rb"))
    print("Loaded Pics")
    for i in range(len(pics)):
        pic, label = pics[i]
        print(pic)
        image = im.fromarray(np.asarray(pic), "RGB")
        image.save(str(i) + ".png")
        print("Saved at " + str(i) + ".png")
