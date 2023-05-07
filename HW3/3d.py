import numpy as np
import matplotlib.pyplot as plt
import cv2
# Load image
img = plt.imread('DemoIMG_1.png')
img2 = plt.imread('DemoIMG_6.png')


# Compute frequency domain coordinates
x, y = np.meshgrid(np.arange(-192, 192), np.arange(-192, 192))
dist = np.sqrt(x**2 + y**2)

# Design spectral filters
sigma_lpf = 32 / (2 * np.sqrt(2 * np.log(2)))
lpf_mask = np.exp(-dist**2 / (2 * sigma_lpf**2))
sigma_hpf = 128 / (2 * np.sqrt(2 * np.log(2)))
hpf_mask = 1 - np.exp(-dist**2 / (2 * sigma_hpf**2))

# Set cutoff threshold
lpf_threshold = 50
hpf_threshold = 25

# Apply filters in frequency domain
shifted = np.fft.fftshift(np.fft.fft2(img))
shifted2 = np.fft.fftshift(np.fft.fft2(img2))

shifted_lpf = shifted * lpf_mask
shifted_hpf = shifted2 * hpf_mask

# Apply thresholds
lpf_mask[lpf_mask < np.max(lpf_mask) * 10**(-lpf_threshold/20)] = 0
hpf_mask[hpf_mask < np.max(hpf_mask) * 10**(-hpf_threshold/20)] = 0

# Apply final filters in frequency domain
shifted_lpf_final = shifted * lpf_mask
shifted_hpf_final = shifted * hpf_mask

# Shift back to spatial domain
lpf = np.fft.ifft2(np.fft.ifftshift(shifted_lpf_final)).real
hpf = np.fft.ifft2(np.fft.ifftshift(shifted_hpf_final)).real

# Combine filtered images to create X-Y illusion
xy_illusion = np.zeros_like(img)
xy_illusion2 = np.zeros_like(img2)
xy_illusion[:, :192] = lpf[:, :192]
xy_illusion2[:, 192:] = hpf[:, 192:]
merged_img = cv2.add(img, img2)

# Display results
fig, axs = plt.subplots(2, 2, figsize=(8, 8))
axs[0, 0].imshow(img, cmap='gray')
axs[0, 0].set_title('Original Image')
axs[0, 0].axis('off')
axs[0, 1].imshow(np.log10(1 + np.abs(shifted)), cmap='gray')
axs[0, 1].set_title('Spectrum of Original Image')
axs[0, 1].axis('off')
axs[1, 0].imshow(lpf, cmap='gray')
axs[1, 0].set_title(f'Low-Pass Filtered Image\nThreshold: {lpf_threshold} dB')
axs[1, 0].axis('off')
axs[1, 1].imshow(hpf, cmap='gray')
axs[1, 1].set_title(f'High-Pass Filtered Image\nThreshold: {hpf_threshold} dB')
axs[1, 1].axis('off')
plt.show()

fig, ax = plt.subplots()
ax.imshow(merged_img, cmap='gray')
ax.set_title('X-Y Illusion')
ax.axis('off')
plt.show()