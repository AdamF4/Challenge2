import cv2


def convertToMono(imageIn, threshold):
    width, height = imageIn.shape[:2]

    for i in range(0, height):
        for j in range(0, width):
            color = imageIn[j, i]
            total = 0
            for k in range(0, 2):
                total += color[k]
            average = total/3
            # imageIn[j, i] = [average, average, average]
            if average > threshold:
                imageIn[j, i] = [255, 255, 255]
            else:
                imageIn[j, i] = [0, 0, 0]
    return imageIn

def improvedQuality(imageIQ):
    width, height = imageIQ.shape[:2]
    average = 0
    count = 0
    for i in range(0, height):
        for j in range(0, width):
            color = imageIQ[j, i]
            total = 0
            for k in range(0, 3):
                total += color[k]
            average += total/3
            count += 1
    print((average/count)*0.8)
    return convertToMono(imageIQ, (average/count)*0.8)

images = ['1.jpg','2.png','3.jpg','4.jpg']
for s in images:
    image = cv2.imread(s)
    image2 = convertToMono(image.copy(), 128)
    cv2.imwrite('mono'+s, image2)
    image3 = improvedQuality(image.copy())
    cv2.imwrite('improved'+s, image3)

cv2.waitKey(0)
cv2.destroyAllWindows()
