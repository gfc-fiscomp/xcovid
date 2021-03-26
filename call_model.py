import torch
import torch.nn as nn
from torchvision import transforms
from torchvision import models
from PIL import Image

def load_model(model_path):
    # instantiate the model
    model = models.resnet50(pretrained=True)
    num_ftrs = model.fc.in_features
    model.fc = nn.Sequential(nn.Linear(num_ftrs, 2))

    model = model.to('cpu')

    # load the trained model weights
    model.load_state_dict(torch.load(model_path, map_location=torch.device('cpu')))
    model.eval()
    print('model loaded successfully!')

    return model

def predict(image_path, save_path):
    # load image
    img = Image.open(image_path).convert('RGB')

    # define transforms
    t = transforms.Compose([transforms.ToTensor(), transforms.Resize(224), transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])])

    # apply transforms and turn image into batch
    batch = torch.unsqueeze(t(img), 0)

    # load model
    model = load_model(save_path)

    # predict
    out = model(batch)
    _, preds = torch.max(out, 1) # gives us the final label

    with torch.no_grad(): # gives us a probability
        prob = nn.functional.softmax(out, dim=1)[0] * 100

    # define map
    m = {0: 'COVID-19 Negativo', 1: 'COVID-19 Positivo'}

    return (m[preds.item()], prob[preds.item()].item())
