import cv2 as cv
from skimage import feature


def compute_hog_from_path(filepath: str):
    img = cv.imread(filepath, 0)
    resized_img = cv.resize(img, (128, 128))
    hog, hog_img = feature.hog(resized_img, orientations=9, pixels_per_cell=(8, 8),
                         cells_per_block=(2, 2), block_norm='L2-Hys',
                         visualize=True, transform_sqrt=True)
    return (hog, hog_img)