from preprocess import preprocess
import pickle
import os
import numpy as np

data_dir = os.getcwd() + '\\data\\test\\'

all_file = os.listdir(data_dir)
for i in all_file:
    x = preprocess(data_dir + i)
    w, h = x.shape
    with open('test' + os.path.splitext(i)[0] + '.pkl', 'wb') as fid:
        pickle.dump(np.reshape(x, w*h), fid)