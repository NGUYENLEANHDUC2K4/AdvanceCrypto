import cv2
import numpy as np

def xor_images(img1, img2):
  img_a = cv2.imread(img1)
  img_b = cv2.imread(img2)
  xor_result = cv2.bitwise_xor(img_a, img_b)
  cv2.imshow('XOR Result', xor_result)
  cv2.waitKey(0)
  cv2.destroyAllWindows()

img1_path = '../flag.png'
img2_path = '../lemur.png'
xor_images(img1_path, img2_path)