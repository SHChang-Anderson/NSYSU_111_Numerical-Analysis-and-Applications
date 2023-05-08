import numpy as np
import cv2
import matplotlib.pyplot as plt

# Load image
img = cv2.imread('DemoIMG_1.png', 0)

shifted = np.fft.fftshift(np.fft.fft2(img))






# Compute frequency domain coordinates
x, y = np.meshgrid(np.arange(-192, 192), np.arange(-192, 192))
dist = np.sqrt(x**2 + y**2)

# Compute low-pass filter mask
sigma = 64 / (2 * np.sqrt(2 * np.log(2)))
lpf_mask = np.exp(-dist**2 / (2 * sigma**2))
im = plt.imshow(lpf_mask, cmap='gray')
cb = plt.colorbar(im)
cb.set_label('Magnitude (dB)')
plt.imshow(lpf_mask, cmap='gray')
plt.title('low-pass filter mask')
plt.axis('off')
plt.show()



# Shift and apply filter in frequency domain
shifted = np.fft.fftshift(np.fft.fft2(img))
shifted_lpf = shifted * lpf_mask

# Shift back to spatial domain
lpf = np.fft.ifft2(np.fft.ifftshift(shifted_lpf)).real

# Display original and filtered images
fig, axs = plt.subplots(1, 2)
axs[0].imshow(img, cmap='gray')
axs[0].set_title('Original Image')
axs[0].axis('off')
axs[1].imshow(lpf, cmap='gray')
axs[1].set_title('Low-Pass Filtered Image')
axs[1].axis('off')
plt.show()