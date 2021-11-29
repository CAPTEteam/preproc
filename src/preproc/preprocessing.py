import os
import cv2
import matplotlib.pyplot as plt
import tqdm
import json
import logging
import pathlib

_LOGGER = logging.getLogger(__name__)

def princ(config):

    with open(config) as json_file:
            config = json.load(json_file)

    def automatic_brightness_and_contrast(image, clip_hist_percent=0.01):
        
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        hist = cv2.calcHist([gray],[0],None,[256],[0,256])
        hist_size = len(hist)

        accumulator = []
        accumulator.append(float(hist[0]))
        for index in range(1, hist_size):
            accumulator.append(accumulator[index -1] + float(hist[index]))

        maximum = accumulator[-1]
        clip_hist_percent *= (maximum/100.0)
        clip_hist_percent /= 2.0

        minimum_gray = 0
        while accumulator[minimum_gray] < clip_hist_percent:
            minimum_gray += 1

        maximum_gray = hist_size -1
        while accumulator[maximum_gray] >= (maximum - clip_hist_percent):
            maximum_gray -= 1

        alpha = 255 / (maximum_gray - minimum_gray)
        beta = -minimum_gray * alpha

        new_hist = cv2.calcHist([gray],[0],None,[256],[minimum_gray,maximum_gray])
        plt.plot(hist)
        plt.plot(new_hist)
        plt.xlim([0,256])
        plt.show()


        auto_result = cv2.convertScaleAbs(image, alpha = alpha+0.4, beta = beta*2)
        return (auto_result, alpha, beta)



    image_dir = config['relative_paths']['input']

    filelist = os.listdir(image_dir + config['relative_paths']['ext'] ) # Path images

    for file in tqdm(filelist):
        
        if file.endswith('.jpg') or pic.endswith('.png') or pic.endswith('.JPG')

            image = cv2.imread(image_dir + config['relative_paths']['input'] + file)
            auto_result, alpha, beta = automatic_brightness_and_contrast(image)
            cv2.imwrite(image_dir + config['relative_paths']['out'] + file, auto_result)

        else :

            continue
