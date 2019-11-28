import cv2

def check(color, testColor):

    if (color[0] == testColor[0]):
            if(color[1] == testColor[1]):
                if(color[2] == testColor[2]):
                    return 1
    else:
        return 0


def fillShapes(imageIn):
    width, height = imageIn.shape[:2]
    white = [255,255,255]
    for i in range(0, height):
        # print(i)
        for j in range(0, width):
            color = imageIn[j, i]

            if check(color, white) == 0:
                for k in range(j, width):
                    if check(color, imageIn[j, i]) == 1:
                        for l in range(j,k):
                            imageIn[l, i] = color

    return imageIn





#images = ['image1','image2','image3']
images = ['mono']

for s in images:
    image = cv2.imread('mono.png')
    cv2.imshow('image',image)
    image2 = fillShapes(image.copy())
    cv2.imshow('image2',image2)
    cv2.imwrite(s+'Filled.jpg', image2)

cv2.waitKey(0)
cv2.destroyAllWindows()
