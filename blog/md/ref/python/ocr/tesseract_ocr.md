# Tesseract Tutorial

OCR technology offers capabilities to perform two primary tasks:

1. Convert Image to Text
2. Convert PDF to Image

These capabilities significantly enhance development and research efficiency. There are two approaches to achieve this: using Pytesseract and employing OpenCV.

## OCR Code

### Pytesseract Approach

```python
# Importing necessary modules
import os  
import pytesseract as tess  
from PIL import Image  
from pdf2image import convert_from_path  

# Function to extract text from a PDF file
def read_pdf(file_name):   
    pages = []

    try:
        # Convert the PDF file to a list of PIL images
        images = convert_from_path(file_name)  

        # Extract text from each image
        for i, image in enumerate(images):
            filename = f"page_{i}_{os.path.basename(file_name)}.jpeg"  
            image.save(filename, "JPEG")  
            text = tess.image_to_string(Image.open(filename))  
            pages.append(text)  

    except Exception as e:
        print(str(e))

    # Write the extracted text to a file
    output_file_name = os.path.splitext(file_name)[0] + ".txt"  
    with open(output_file_name, "w") as f:
        f.write("\n".join(pages))  

    return output_file_name

# Example usage
pdf_file = "sample.pdf"
print(read_pdf(pdf_file))

 ![OCR Project](https://kevinli-webbertech.github.io/blog/images/ocr/download.png)

## OpenCV Approach

# Importing necessary modules
import cv2
import os
import argparse
import pytesseract
from PIL import Image

# Argument Parser
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image folder")
ap.add_argument("-p", "--pre_processor", default="thresh", help="the preprocessor usage")
args = vars(ap.parse_args())

# Reading the image
images = cv2.imread(args["image"])
gray = cv2.cvtColor(images, cv2.COLOR_BGR2GRAY)

# Preprocessing based on user input
if args["pre_processor"] == "thresh":
    cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
if args["pre_processor"] == "blur":
    cv2.medianBlur(gray, 3)

# Saving the processed image
filename = f"{os.getpid()}.jpg"
cv2.imwrite(filename, gray)

# Extracting text using Tesseract
text = pytesseract.image_to_string(Image.open(filename))
os.remove(filename)
print(text)

# Displaying the output images
cv2.imshow("Image Input", images)
cv2.imshow("Output In Grayscale", gray)
cv2.waitKey(0)

![OCR Project](https://kevinli-webbertech.github.io/blog/images/ocr/downloadocr.png)

## Conclusion

### Which Approach is Better?

Choosing between Pytesseract and OpenCV depends on specific requirements:

- **Pytesseract for PDFs:** Efficient for handling multi-page PDF documents, especially scanned ones. Processes each page individually and extracts text.

- **OpenCV for Images:** Ideal for improving OCR accuracy on individual images through customizable preprocessing steps such as thresholding and blurring.

Both methods leverage Tesseract's robust OCR capabilities, catering to different use cases. Understanding their strengths and limitations helps in selecting the best approach for your project.
