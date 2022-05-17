import torch
import torch.utils.data
import torchvision
from torchvision.models.detection.faster_rcnn import FastRCNNPredictor
import os
import sys

from engine import evaluate

from dataset import custom_dataset


def get_model_instance_segmentation(num_classes):
    # load an instance segmentation model pre-trained pre-trained on COCO
    model = torchvision.models.detection.fasterrcnn_resnet50_fpn(pretrained=True)
    # # get number of input features for the classifier
    in_features = model.roi_heads.box_predictor.cls_score.in_features
    # # replace the pre-trained head with a new one
    model.roi_heads.box_predictor = FastRCNNPredictor(in_features, num_classes)

    return model

def get_transform():
    custom_transforms = []
    custom_transforms.append(torchvision.transforms.ToTensor())
    return torchvision.transforms.Compose(custom_transforms)

# collate_fn needs for batch
def collate_fn(batch):
    return tuple(zip(*batch))

def main():
    version = '9.3'
    save_path = os.path.dirname(os.path.realpath(sys.argv[0]))
    #save_path = f'D:/User Data/Documents/Research Ref/Main_research/ML/v{version}'
    os.makedirs(save_path, exist_ok=True)
    test_image = os.path.join(save_path, "testing_data")
    test_coco = os.path.join(save_path,"testing_data.json")
    model_path = os.path.join(save_path,"model_final.pth")
    num_classes = 7

    test_dataset = custom_dataset(root=test_image, 
                        annotation=test_coco,
                        transforms=get_transform())
    
    train_batch_size = 1
    
    test_data_loader = torch.utils.data.DataLoader(test_dataset,
                                          batch_size=train_batch_size,
                                          shuffle=True,
                                          num_workers=4,
                                          collate_fn=collate_fn)

    device = torch.device('cuda') if torch.cuda.is_available() else torch.device('cpu')

    model = get_model_instance_segmentation(num_classes)  
    model.to(device)

    params = [p for p in model.parameters() if p.requires_grad]
    optimizer = torch.optim.SGD(params, lr=0.005, momentum=0.9, weight_decay=0.0005)    

    checkpoint = torch.load(model_path,'cpu')
    
    model.load_state_dict(checkpoint['model_state_dict'])
    optimizer.load_state_dict(checkpoint['optimizer_state_dict'])
    #model.eval()
    evaluate(model, test_data_loader, device=device)

    print("That's it!")
    
if __name__ == "__main__":
    main()