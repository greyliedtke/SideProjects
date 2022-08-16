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


imgs = [img, img] #, img1]


class ImgToColors:
    def __init__(self, image):
        self.image = image
        self.average_patch = []         # array for avg color
        self.dominant_patch = []    # array for dominant patch of colors
        self.average_color()
        self.dominant_color(4)

    # function to get average color from image
    def average_color(self):
        image_mean = self.image.mean(axis=0).mean(axis=0)
        self.average_patch = np.ones(shape=self.image.shape, dtype=np.uint8)*np.uint8(image_mean)

    # function to get dominant color from image
    def dominant_color(self, n_colors):
        dim = 3
        print(len(self.image))
        print(self.image.shape)
        pixels = np.float32(self.image.reshape(-1, dim))
        criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 200, .1)
        flags = cv2.KMEANS_RANDOM_CENTERS
        _, labels, palette = cv2.kmeans(pixels, n_colors, None, criteria, 10, flags)
        _, counts = np.unique(labels, return_counts=True)
        dominant = palette[np.argmax(counts)]
        indices = np.argsort(counts)[::-1]
        freqs = np.cumsum(np.hstack([[0], counts[indices] / float(counts.sum())]))
        rows = np.int_(self.image.shape[0] * freqs)
        dom_patch = np.zeros(shape=self.image.shape, dtype=np.uint8)
        for i in range(len(rows) - 1):
            dom_patch[rows[i]:rows[i + 1], :, :] += np.uint8(palette[indices[i]])
        self.dominant_patch = dom_patch


im2cs = []
for im in imgs:
    im2c = ImgToColors(im)
    im2cs.append(im2c)


# function to plot figs according to blah
def plotting_figs(color_figs):
    fig, ax_figs = plt.subplots(len(color_figs), 3, figsize=(12, 6))

    for f in range(len(color_figs)):
        ax_figs[f][0].imshow(color_figs[f].image)
        # ax_figs[f][1].imshow(color_figs[f].avg_patch)
        ax_figs[f][2].imshow(color_figs[f].dominant_patch)
        # ax_figs[f].set_title('Average color')
        # ax_figs[f].axis('off')

    plt.show()


plotting_figs(im2cs)

# fig, (ax0, ax1, ax2) = plt.subplots(1, 3, figsize=(12, 6))
# ax0.imshow(avg_patch)
# ax0.set_title('Average color')
# ax0.axis('off')
# ax1.imshow(dom_patch)
# ax1.set_title('Dominant colors')
# ax2.axis('off')
# ax2.imshow(img)
# ax2.set_title('OG')
# ax2.axis('off')
# plt.show()

# end
