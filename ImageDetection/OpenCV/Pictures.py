"""
Script to find average color of pictures
"""

# Necessary imports
import cv2
import numpy as np
from skimage import io
import matplotlib.pyplot as plt

# read in image
img = io.imread('SP_Logo.png')   # [:, :, :-1]
img1 = io.imread('GreyImage.png')

imgs = [img, img1]

# average color of image
average = img.mean(axis=0).mean(axis=0)
avg_patch = np.ones(shape=img.shape, dtype=np.uint8)*np.uint8(average)


# dominant colors, needs number of colors, and clustering method
pixels = np.float32(img.reshape(-1, 3))
n_colors = 3
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 200, .1)
flags = cv2.KMEANS_RANDOM_CENTERS

_, labels, palette = cv2.kmeans(pixels, n_colors, None, criteria, 10, flags)
_, counts = np.unique(labels, return_counts=True)

dominant = palette[np.argmax(counts)]
indices = np.argsort(counts)[::-1]
freqs = np.cumsum(np.hstack([[0], counts[indices]/float(counts.sum())]))
rows = np.int_(img.shape[0]*freqs)

dom_patch = np.zeros(shape=img.shape, dtype=np.uint8)
for i in range(len(rows) - 1):
    dom_patch[rows[i]:rows[i + 1], :, :] += np.uint8(palette[indices[i]])

fig, (ax0, ax1, ax2) = plt.subplots(1, 3, figsize=(12, 6))
ax0.imshow(avg_patch)
ax0.set_title('Average color')
ax0.axis('off')
ax1.imshow(dom_patch)
ax1.set_title('Dominant colors')
ax2.axis('off')
ax2.imshow(img)
ax2.set_title('OG')
ax2.axis('off')
plt.show()

# end
