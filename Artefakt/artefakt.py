import torch
import cv2
from PIL import Image
from albumentations.pytorch import ToTensorV2
import albumentations as A

def img_to_imgs(img_path, model_path):
    
    model = torch.load(model_path)

    imgs = []

    img = cv2.imread(img_path)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    transforms = get_transforms
    transformed = transforms(image=img)
    img = transformed['image']
    input_batch = [img.cuda()]

    if torch.cuda.is_available():

        device = torch.device("cuda") # use GPU to train
        model = model.to(device)
        model.eval()

        with torch.no_grad():
            prediction = model(input_batch)
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

def get_transforms(train=False):
    if train:
        transform = A.Compose([
            A.Resize(600, 600), # our input size can be 600px
            A.HorizontalFlip(p=0.3),
            A.VerticalFlip(p=0.3),
            A.RandomBrightnessContrast(p=0.1),
            A.ColorJitter(p=0.1),
            ToTensorV2()
        ], bbox_params=A.BboxParams(format='coco'))
    else:
        transform = A.Compose([
            A.Resize(600, 600), # our input size can be 600px
            ToTensorV2()
        ], bbox_params=A.BboxParams(format='coco'))
    return transform