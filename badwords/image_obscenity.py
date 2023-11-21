import warnings

# Ignore warninng torchvision 
warnings.filterwarnings("ignore", category=UserWarning, module="torchvision")

import torch
import torchvision.transforms as transforms
from torchvision.models import resnet50
from PIL import Image

class ImageClassifier:
    def __init__(self):
        # Load the pretrained ResNet model
        self.model = resnet50(pretrained=True)
        self.model.eval()

        # Define the image transformation pipeline
        self.transform = transforms.Compose([
            transforms.Resize(256),
            transforms.CenterCrop(224),
            transforms.ToTensor(),
            transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
        ])

    def classify_image(self, image_path):
        # Load the image
        image = Image.open(image_path)

        # Transform and normalize the image
        input_image = self.transform(image).unsqueeze(0)

        # Make a prediction
        with torch.no_grad():
            output = self.model(input_image)

        # Get probabilities for each class
        probabilities = torch.nn.functional.softmax(output[0], dim=0)

        # Determine the class with the highest probability
        if probabilities[1] > probabilities[0]:
            return True
        else:
            return False
