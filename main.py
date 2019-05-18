from mlpClassifier import predict
from preprocess import preprocess
import numpy as np
import os
import pickle

data_path = os.getcwd() + '\\data\\test\\'

def main_predict():
    '''input'''
    so_luong_anh = int(input("Nhap so luong anh can test(0 < x <= 5): "))
    path_image = []
    if so_luong_anh > 0 and so_luong_anh <= 5:
        for i in range(1, so_luong_anh + 1):
            path = input("Nhap ten cua anh thu " + str(i) + ": ")
            path_image.append(data_path + path)

    X = []
    #Create test set X
    for i in range(len(path_image)):
        tmp = preprocess(path_image[i])
        w, h = tmp.shape
        X.append(np.reshape(tmp, w*h))
    
	#Predict  X with model
    predictions = []
    for i in range(1, 6):
        print('Predict with mode' + str(i) + '.pkl:')
        with open('model' + str(i) + '.pkl', 'rb') as fid:
            model = pickle.load(fid)
        tmp = predict(X, model)
        predictions.append(tmp[:, 1])
    res = np.argmax(predictions, axis=0)
    for i in range(len(res)):
        res[i] += 1
    return res

	
if __name__ == "__main__":
    print(main_predict())
