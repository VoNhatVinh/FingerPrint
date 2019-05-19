from mlpClassifier import train, predict
from preprocess import preprocess
import os
import numpy as np
import pickle


data_dir = os.getcwd() + '\\data\\train'
sub_dir = []
sub_file = []
for r, d, f in os.walk(data_dir):
    sub_dir.append(d)
    sub_file.append(f)
sub_dir = sub_dir[0]
sub_file = np.array(sub_file[1:])

count_file = 0; feature = []
for i in range(len(sub_file)):
    count_file += len(sub_file[i])
    for j in range(len(sub_file[i])):
        tmp = preprocess(data_dir+'/'+sub_dir[i]+'/'+sub_file[i, j])
        w, h = tmp.shape
        feature.append(np.reshape(tmp, w*h))

print(len(feature))

for i in range(len(sub_dir)):
    y = np.zeros(count_file)
    left = 0; right = 0; j = 0
    for j in range(i):
        left += len(sub_file[j])
        right += len(sub_file[j])
    right += len(sub_file[j])
    y[left:right] = 1
    model = train(feature, y)
    with open('model' + sub_dir[i] + '.pkl', 'wb') as fid:
        pickle.dump(model, fid)