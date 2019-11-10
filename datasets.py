import os
import os.path as osp

import numpy as np
from torch.utils.data import Dataset


# ラベルから数値に変換する辞書
labels = ["bird", "cat", "deer", "dog", "frog", "horse", "airplane", "automobile", "ship", "truck"]
labels2int_dict = dict()
for i, label in enumerate(labels):
    labels2int_dict[label] = i


def label2int(label:str):
    """ [input] label (airplane, automobile, bird, cat, deer, dog, frog, horse, ship, truck)
        [output] int (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
    """
    return labels2int_dict[label]


class SiameseCifar(Dataset):
    """ ランダムにpairを作る
    """
    def __init__(self, cifar_dataset):
        """ [input]
                cifar_dataset = ["./dataset/cifar/train/airplane/13_airplane.png", .... ]
        """
        self.cifar_dataset = cifar_dataset # パスのリスト
        self.labels = [path.split("/")[4] for path in self.cifar_dataset] # 対応するラベルのリスト
        self.phase = self.cifar_dataset[0].split("/")[3] # train or test
        self.labels_set = set(self.labels) # set(0, 1, 2, 3, 4, 5, 6, 7, 8, 9)

        # trainであれば任意のペアを作る
        if self.phase == "train":
            self.label2indices = {label: np.where(np.array(self.labels) == label)[0] for label in self.labels_set}
        
    
    random_state = np.random.RandomState(29)
    positive_paris = [[i, random_state.choice(slef.)]]

            

        
        
