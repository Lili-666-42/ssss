from time import sleep
import torch
import torch.nn as nn
import numpy as np



class Generator(nn.Module):
    def __init__(self):
        super(Generator, self).__init__()

        # Сверточные слои для извлечения признаков из входного изображения
        self.conv1 = nn.Conv2d(3, 64, kernel_size=9, stride=1, padding=4)
        self.relu1 = nn.PReLU()

        # Блоки остатков (Residual Blocks)
        self.residual_blocks = self.make_residual_blocks(64, num_blocks=16)

        # Де-сверточные слои для увеличения разрешения
        self.deconv1 = nn.ConvTranspose2d(64, 64, kernel_size=4, stride=2, padding=1)
        self.relu2 = nn.PReLU()
        self.deconv2 = nn.ConvTranspose2d(64, 3, kernel_size=9, stride=1, padding=4)

    def make_residual_blocks(self, num_features, num_blocks):
        blocks = []
        for _ in range(num_blocks):
            blocks.append(ResidualBlock(num_features))
        return nn.Sequential(*blocks)

    def forward(self, x):
        # Прямой проход генератора
        out1 = self.relu1(self.conv1(x))
        out = self.residual_blocks(out1)
        out = self.relu2(self.deconv1(out + out1))
        out = self.deconv2(out)
        return out

class ResidualBlock(nn.Module):
    def __init__(self, num_features):
        super(ResidualBlock, self).__init__()
        self.conv1 = nn.Conv2d(num_features, num_features, kernel_size=3, stride=1, padding=1)
        self.bn1 = nn.BatchNorm2d(num_features)
        self.conv2 = nn.Conv2d(num_features, num_features, kernel_size=3, stride=1, padding=1)
        self.bn2 = nn.BatchNorm2d(num_features)
        self.relu = nn.PReLU()

    def forward(self, x):
        residual = x
        out = self.relu(self.bn1(self.conv1(x)))
        out = self.bn2(self.conv2(out))
        out = out + residual
        return out

class Discriminator(nn.Module):
    def __init__(self):
        super(Discriminator, self).__init__()
        self.model = nn.Sequential(
            nn.Conv2d(3, 64, kernel_size=3, padding=1),
            nn.LeakyReLU(0.2),
            nn.Conv2d(64, 64, kernel_size=3, padding=1, stride=2),
            #nn.BatchNorm2d(64),
            nn.LeakyReLU(0.2),
            nn.Conv2d(64, 128, kernel_size=3, padding=1),
            #nn.BatchNorm2d(128),
            nn.LeakyReLU(0.2),
            nn.Conv2d(128, 128, kernel_size=3, padding=1, stride=2),
            #nn.BatchNorm2d(128),
            nn.LeakyReLU(0.2),
            nn.AdaptiveAvgPool2d(1),
            nn.Conv2d(128, 1024, kernel_size=1),
            nn.LeakyReLU(0.2),
            nn.Conv2d(1024, 1, kernel_size=1)
        )

    def forward(self, x):
        return torch.sigmoid(self.model(x))
    

generator = Generator()
generator.load_state_dict(torch.load('frontend/ist/generator1.pth'))


def obr(im, brigh, contr ):
    if brigh:brigh =3
    else : brigh =1
    if contr:contr =6
    else :contr =1
    im = (im * brigh / contr)
    im = im.astype(np.uint8)
    sleep(2)
    return im

'''
def obr(img, brigh, contr ):
    img = torch.Tensor(img).permute(2, 1, 0).unsqueeze(0)
    img = generator(img)
    img = img[0]
    img = img.permute(2, 1, 0).detach().numpy()
    img = img.astype(np.uint8)
    return img
'''