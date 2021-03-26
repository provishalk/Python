# numpy array for images
import numpy as np
import matplotlib.pyplot as plt
from scipy import ndimage # Shift, roate and zoom it

from scipy import misc  # Load an image
face = misc.face(gray=True)

shifted_face = ndimage.shift(face, (50, 50))
shifted_face2 = ndimage.shift(face, (50, 50), mode='nearest')
rotated_face = ndimage.rotate(face, 30)
cropped_face = face[50:-50, 50:-50]
zoomed_face = ndimage.zoom(face, 2)
zoomed_face.shape

plt.subplot(151)
plt.imshow(shifted_face, cmap=plt.cm.gray)
plt.axis('off')