"""
Definition of ImageFolderDataset dataset class
"""

# pylint: disable=too-few-public-methods

import os

import numpy as np
from PIL import Image

from .base_dataset import Dataset


class ImageFolderDataset(Dataset):
    """CIFAR-10 dataset class"""
    def __init__(self, *args,
                 transform=None,
                 download_url="https://cdn3.vision.in.tum.de/~dl4cv/cifar10.zip",
                 **kwargs):
        super().__init__(*args, 
                         download_url=download_url,
                         **kwargs)
        
        self.classes, self.class_to_idx = self._find_classes(self.root_path)
        self.images, self.labels = self.make_dataset(
            directory=self.root_path,
            class_to_idx=self.class_to_idx
        )
        # transform function that we will apply later for data preprocessing
        self.transform = transform

    @staticmethod
    def _find_classes(directory):
        """
        Finds the class folders in a dataset
        :param directory: root directory of the dataset
        :returns: (classes, class_to_idx), where
          - classes is the list of all classes found
          - class_to_idx is a dict that maps class to label
        """
        classes = [d.name for d in os.scandir(directory) if d.is_dir()]
        classes.sort()
        class_to_idx = {classes[i]: i for i in range(len(classes))}
        return classes, class_to_idx

    @staticmethod
    def make_dataset(directory, class_to_idx):
        """
        Create the image dataset by preparaing a list of samples
        Images are sorted in an ascending order by class and file name
        :param directory: root directory of the dataset
        :param class_to_idx: A dict that maps classes to labels
        :returns: (images, labels) where:
            - images is a list containing paths to all images in the dataset, NOT the actual images
            - labels is a list containing one label per image
        """
        images, labels = [], []

        for target_class in sorted(class_to_idx.keys()):
            label = class_to_idx[target_class]
            target_dir = os.path.join(directory, target_class)
            for root, _, fnames in sorted(os.walk(target_dir)):
                for fname in sorted(fnames):
                    path = os.path.join(root, fname)
                    images.append(path)
                    labels.append(label)

        assert len(images) == len(labels)
        return images, labels

    def __len__(self):
        length = None
        ########################################################################
        # TODO:                                                                #
        # Return the length of the dataset (number of images)                  #
        ########################################################################

        #all_file=os.listdir(self.root_path)
        #leng=0
        #for i in range(0,len(all_file)):
        #    target_file= os.path.join(self.root_path, all_file[i])
        #    file=os.listdir(target_file)
        #    leng+=len(file)
        #length=leng
        length=len(self.images)

        ########################################################################
        #                           END OF YOUR CODE                           #
        ########################################################################
        return length

    @staticmethod
    def load_image_as_numpy(image_path):
        """Load image from image_path as numpy array"""
        return np.asarray(Image.open(image_path), dtype=float)

    def __getitem__(self, index):
        data_dict = None
        ########################################################################
        # TODO:                                                                #
        # create a dict of the data at the given index in your dataset         #
        # The dict should be of the following format:                          #
        # {"image": <i-th image>,                                              #
        # "label": <label of i-th image>}                                      #
        # Hints:                                                               #
        #   - use load_image_as_numpy() to load an image from a file path      #
        #   - If applicable (Task 4: 'Transforms and Image Preprocessing'),    #
        #     make sure to apply self.transform to the image:                  #                           
        #     image_transformed = self.transform(image)                        #
        ########################################################################
        d={'image': '2341', 'label': 1}
       # classes = ['plane', 'car', 'bird', 'cat', 'deer','dog', 'frog', 'horse', 'ship', 'truck',]
       # index_sum=0
       # cls=0
       # num=0
       # for i in range(0,9):
       #     class_path=os.path.join(self.root_path, classes[i])
       #     class_file=os.listdir(class_path)
       #     sum_last_loop=index_sum
       #     index_sum+=len(class_file)
       #     if index<index_sum:
       #         cls=i
       #         num=index-sum_last_loop
       #         break
       # class_path=os.path.join(self.root_path, classes[cls])
       # all_file=os.listdir(class_path)
       # img_path=os.path.join(class_path, all_file[num])
        img_path=self.images[index]
        image=ImageFolderDataset.load_image_as_numpy(img_path)
        image_transformed = self.transform(image)
        #d['image']=image
        d['image']=image_transformed
        d['label']=self.labels[index]
        data_dict=d
        pass

        ########################################################################
        #                           END OF YOUR CODE                           #
        ########################################################################
        return data_dict
