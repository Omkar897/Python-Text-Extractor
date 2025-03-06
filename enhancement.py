import cv2

# Function to perform image enhancement
def enhance_image(image_path):
    image = cv2.imread(image_path)

    scaled_image = cv2.resize(image, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)

    alpha = 1.0
    beta = 30
    enhanced_image = cv2.convertScaleAbs(scaled_image, alpha=alpha, beta=beta)

    gray_image = cv2.cvtColor(enhanced_image, cv2.COLOR_BGR2GRAY)
    _, binarized_image = cv2.threshold(gray_image, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

    denoised_image = cv2.fastNlMeansDenoising(binarized_image, h=10, templateWindowSize=7, searchWindowSize=21)

    return denoised_image
