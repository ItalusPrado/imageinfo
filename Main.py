from PIL import Image
import numpy as np

def returnSampling( array ):
    media = [0,0,0]
    for value in array:
        media[0] += value[0]
        media[1] += value[1]
        media[2] += value[2]
    for index in range(0, len(media)):
        media[index] = media[index]/len(array)
        print media[index]
    return media

im = Image.open('maxresdefault.jpg', 'r')
data = list(im.getdata())
data2 = data
colsize, linesize = im.size
print linesize
array = []
for line in range(0,linesize):
    for col in range(0,colsize):
        array.append(data[col+line*colsize])



color = returnSampling(array)

for line in range(0,linesize):
    for col in range(0, colsize):
        data2[col+line*colsize] = color


for line in range(0,linesize):
    for col in range(0, colsize):
        data2[col+line*colsize] = (color[0],color[1],color[2])
# data2 = tuple(data2)
imgData = np.asarray(data2)
new_img = Image.new("RGB", (colsize, linesize), "white")
new_img.putdata(data2)
# img = Image.fromarray(imgData, 'RGB')

new_img.show()