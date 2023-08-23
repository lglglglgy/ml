# -*- coding: utf-8 -*-


from __future__ import print_function
import torch.utils.data as data
import torch
import numpy as np
import scipy.io as sio
import h5py


class MyDataset(data.Dataset):
    def __init__(self, file_paths='load_test.mat',method = 'h',lens = 15):
        self.images = []
        self.labels = []
        print (file_paths)
        for path in file_paths:
            print(path)
            mat_data = sio.loadmat(path)

# 打印所有的键名
            print(mat_data.keys())
            mat_info = sio.whosmat(path)

# 打印文件结构信息
            for item in mat_info:
                name = item[0]
                data_type = item[1]
                data_shape = item[2]
               # print(f"Name: {name}, Data Type: {data_type}, Data Shape: {data_shape}")
            if method=='h':
                data = h5py.File(path)
                image,label = data['image'],data['label']
                image = np.transpose(image)
                label = np.transpose(label)
                image = torch.from_numpy(image)
                image = image[:,:,:,:,:]
                label = torch.from_numpy(label).float()
                self.images.append(image)
                self.labels.append(label)

            elif method=='nmnist_r':
                data = sio.loadmat(path)
                image = torch.from_numpy(data['image'])
                label = torch.from_numpy(data['label']).float()
                image = image.permute(0,3,1,2,4)
                self.images.append(image)
                self.labels.append(label)


            elif method=='nmnist_h':
                data = h5py.File(path)
                image, label = data['image'], data['label']
                image = np.transpose(image)
                label = np.transpose(label)
                image = torch.from_numpy(image)
                image = image[:, :, :, :, :]
                label = torch.from_numpy(label).float()
                image = image.permute(0, 3, 1, 2, 4)
                self.images.append(image)
                self.labels.append(label)

            else:
                data = sio.loadmat(path)
                image = torch.from_numpy(data['image'])
                label = torch.from_numpy(data['label']).float()
                self.images.append(image)
                self.labels.append(label)
                
            # self.num_sample = int((len(self.images)//100)*100)
            # print(self.images.size(),self.labels.size())
        self.images = torch.cat(self.images, dim=0)
        self.labels = torch.cat(self.labels, dim=0)
        self.num_sample = len(self.images)
        print(self.images.size(), self.labels.size())

    def __getitem__(self, index):#返回的是tensor
        img, target = self.images[index], self.labels[index]
        return img, target

    def __len__(self):
        return self.num_sample