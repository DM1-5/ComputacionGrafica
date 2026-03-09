import numpy as np 
import matplotlib.pyplot as plt 

img = plt.imread('nasa.jpg')

h,w = img.shape[:2]

dx = 150 
dy = 150 

trasladada = np.zeros_like(img)

x1d = max(0, dx)
y1d = max(0, dy)
x2d = min(w, w + dx)
y2d = min(h, h + dy)

x1s = max(0, -dx)
y1s = max(0,-dy)
x2s = x1s + (x2d - x1d)
y2s = y1s + (y2d - y1d)

if x2d > x1d and y2d > y1d: 
  trasladada[y1d:y2d, x1d:x2d] = img[y1s:y2s, x1s:x2s]

plt.figure(figsize=(10,4))
plt.subplot(1,2,1)
plt.imshow(img)
plt.title('Original')


plt.subplot(1,2,2)
plt.imshow(trasladada)
plt.title('Trasladada')
plt.show()
