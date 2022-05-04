import Image
import cv2
from PIL import Image
import numpy as np
OGcolor = (255,213,93,255)
healColor = (32,179,73,255)
defenceColor = (121,33,123,255)
attackColor = (63, 72, 204, 255)
def colorChange(input, target, destination, remove=False):
    img = Image.open(input)
    img = img.convert('RGBA')
    originalArr = np.array(img)
    for i in range(len(originalArr)):
        for j in range(len(originalArr[0])):
            if np.array_equiv(originalArr[i][j], target):
                if remove:
                    originalArr[i][j] = (0, 0, 0, 0)
                else:
                    originalArr[i][j] = destination
    imgNew = Image.fromarray(originalArr)
    w, h = imgNew.size
    top = 16
    right = w -32
    left = 32
    bottom = h
    #imgNew = imgNew.crop((left, top, right, bottom))
    #imgNew.show()
    imgNew.save(f'output/{input}')




def downSizer(input, n, invert= False, alpha= False,):
    img = Image.open(input)
    img = img.convert('RGBA')
    originalArr = np.array(img)
    print(originalArr[0][0])
    newArr = np.copy(originalArr)

    background = originalArr[0][0]
    start = int(n/2)
    k = 0
    if invert:
        for i in range(start, len(originalArr), n):
            m = len(originalArr)-1
            for j in range(start, len(originalArr[0]), n):
                newArr[k][m] = originalArr[i][j]
                if alpha and np.array_equiv(newArr[k][m], background):


                    newArr[k][m] = (0,0,0,0)
                m -= 1
            k += 1
    else:
        for i in range(start, len(originalArr), n):
            m = 0
            for j in range(start, len(originalArr[0]), n):
                newArr[k][m] = originalArr[i][j]
                if alpha and np.array_equiv(newArr[k][m], background):

                    newArr[k][m] = (0,0,0,0)
                # print(type(newArr[k][m]))
                # print(type(originalArr[i][j]))
                m += 1
            k += 1

    imgNew = Image.fromarray(newArr)
    imgNew.save(f'output/{input}')
    a = Image.open(f'output/{input}')
    w,h = a.size
    if invert:

        top = 0
        right = w
        left = w - w/n
        bottom = h/n
    else:
        top = 0
        right = w/n
        left = 0
        bottom = h / n


    # Cropped image of above dimension
    # (It will not change original image)
    #im1 = a.crop((left, top, right, bottom))

    # Shows the image in image viewer

    a.save(f'output/{input}')








for i in range(1,15):
    #colorChange(f'inputs/_ ({i}).png', healColor, attackColor, False)
    downSizer(f'inputs/_ ({i}).png', 1, True, False)
#downSizer('inputs/_ (4).png',3,False,True)
#colorChange('inputs/_ (17).png',OGcolor,healColor,True)
