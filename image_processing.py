import cv2
import numpy as np

def unsharp_mask(image, sigma=1.0, amount=1.5, threshold=0):
    """
    image: np.ndarray (BGR или grayscale)
    sigma: радиус размытия (гаусс)
    amount: сила эффекта (0 = без изменений, 1..3 типично)
    threshold: минимальная разница, ниже которой не усиливаем (шумоподавление)
    """
    # Размытие по Гауссу
    blurred = cv2.GaussianBlur(image, (0, 0), sigma)

    # Маска высоких частот
    sharpened = cv2.addWeighted(image, 1.0 + amount, blurred, -amount, 0)
    return sharpened


def gray_world_fast(image):
    img = image.astype(np.float32)
    means = img.mean(axis=(0, 1))  # shape (3,) в порядке B,G,R
    means = np.maximum(means, 1e-6)
    target = means.mean()
    gains = target / means  # shape (3,)
    out = img * gains  # broadcasting по каналам
    return np.clip(out, 0, 255).astype(np.uint8)



