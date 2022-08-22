import torch
import cv2
from PIL import Image

def img_to_imgs(img):
    model = torch.load("path/to/saved_model")

    imgs = []

    if torch.cuda.is_available():

        device = torch.device("cuda") # use GPU to train
        model = model.to(device)
        model.eval()

        with torch.no_grad():
            prediction = model([img.to(device)])
            pred = prediction[0]

            for index, det in enumerate(pred['boxes']):
                if pred['scores'][index] > 0.8:
                    x0 = int(det[1]*img.shape[1])
                    y0 = int(det[0]*img.shape[0])
                    x1 = int(det[3]*img.shape[1])
                    y2 = int(det[2]*img.shape[0])
                    img_cropped = img.crop((x0, y0, x1, y2))
                    imgs.append(img_cropped)

    return imgs

