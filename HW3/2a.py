import cv2
import numpy as np
import matplotlib.pyplot as plt
f_range = 15 # 低頻範圍
img = cv2.imread('DemoIMG_1.png', cv2.IMREAD_GRAYSCALE)
rows, cols = img.shape
cy, cx = int(rows / 2), int(cols/2)

# 傅立葉轉換後並位移低頻
shifted = np.fft.fftshift(np.fft.fft2(img))

magnitude_spectrum = 20 * np.log(np.abs(shifted))

im = plt.imshow(magnitude_spectrum, cmap='gist_rainbow')
plt.axis('off')

# 添加color bar
cb = plt.colorbar(im)
cb.set_label('Magnitude (dB)')

plt.show()


# 低頻範圍內設為 0
shifted[cy - f_range:cy + f_range, cx - f_range:cx + f_range] = 0

# 顯示一下頻域目前的樣子
magnitude_spectrum1 = 20 * np.log(np.abs(shifted))

im1 = plt.imshow(magnitude_spectrum1, cmap='gist_rainbow')
plt.axis('off')

# 添加color bar
cb = plt.colorbar(im1)
cb.set_label('Magnitude (dB)')

plt.show() 

# 逆轉換
inversed = np.fft.ifft2(np.fft.ifftshift(shifted))
inversed_img = np.abs(inversed).astype('uint8')
cv2.imshow('INVERSE FFT 2D', inversed_img)           

cv2.waitKey(0)
cv2.destroyAllWindows()







f_range = 15 # 低頻範圍
img = cv2.imread('DemoIMG_1.png', cv2.IMREAD_GRAYSCALE)
rows, cols = img.shape
cy, cx = int(rows / 2), int(cols/2)

x = np.arange(-cx, cx)
X, Y = np.meshgrid(np.arange(-cx, cx), np.arange(-cy, cy))

# 傅立葉轉換後並位移低頻
shifted = np.fft.fftshift(np.fft.fft2(img))

magnitude_spectrum = 20 * np.log(np.abs(shifted))

im = plt.imshow(magnitude_spectrum, cmap='gist_rainbow')
plt.axis('off')

# 添加color bar
cb = plt.colorbar(im)
cb.set_label('Magnitude (dB)')

plt.show()


# 低頻範圍內設為 0
shifted[X ** 2 + Y ** 2 > f_range ** 2] = 0
# 顯示一下頻域目前的樣子
magnitude_spectrum1 = 20 * np.log(np.abs(shifted))

im1 = plt.imshow(magnitude_spectrum1, cmap='gist_rainbow')
plt.axis('off')

# 添加color bar
cb = plt.colorbar(im1)
cb.set_label('Magnitude (dB)')

plt.show() 

# 逆轉換
inversed = np.fft.ifft2(np.fft.ifftshift(shifted))
inversed_img = np.abs(inversed).astype('uint8')
cv2.imshow('INVERSE FFT 2D', inversed_img)           

cv2.waitKey(0)
cv2.destroyAllWindows()




