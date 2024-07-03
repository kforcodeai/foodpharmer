import cv2
from matplotlib import pyplot as plt
import easyocr


class get_ocr():
    def __int__(self):
        # easyocr.__init__()
        self.reader = easyocr.Reader(['en'], gpu=False)
        self.threshold = 0.25

    def draw_bounding_boxes(self,image, detections, threshold=0.25):
        for bbox, text, score in detections:
            if score > threshold:
                cv2.rectangle(image, tuple(map(int, bbox[0])), tuple(map(int, bbox[2])), (0, 255, 0), 5)
                cv2.putText(image, text, tuple(map(int, bbox[0])), cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.65, (255, 0, 0), 2)

    def ocr_from_image(self,img_format, debug=False):
        '''This function checks if image is path or image numpy file'''
        #check im path, numpy array
        self.img = img_format
        # reader = easyocr.Reader(['en'], gpu=False)
        self.reader = easyocr.Reader(['en'], gpu=False)
        self.text_detections = self.reader.readtext(self.img)
        if debug:
            self.display_text()

        return self.text_detections

    def display_text(self):
        self.threshold=0.25
        self.draw_bounding_boxes(self.img, self.text_detections, self.threshold)
        print(self.text_detections)
        plt.imshow(cv2.cvtColor(self.img, cv2.COLOR_BGR2RGBA))
        plt.show()











