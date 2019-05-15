from preprocess import preprocess
from train_image import train, predict
import numpy as np
import pickle

train1 = preprocess('1_1.bmp')
train2 = preprocess('1_2.bmp')
train3 = preprocess('1_3.bmp')
train4 = preprocess('2_1.bmp')
train5 = preprocess('2_2.bmp')
train6 = preprocess('2_3.bmp')

test1 = preprocess('1_4.bmp')
test2 = preprocess('2_4.bmp')

w, h = train1.shape
train1 = np.reshape(train1, (1, w*h))
train2 = np.reshape(train2, (1, w*h))
train3 = np.reshape(train3, (1, w*h))
train4 = np.reshape(train4, (1, w*h))
train5 = np.reshape(train5, (1, w*h))
train6 = np.reshape(train6, (1, w*h))

test1 = np.reshape(test1, (1, w*h))
test2 = np.reshape(test2, (1, w*h))

X = train1
X = np.vstack((X, train2[0]))
X = np.vstack((X, train3[0]))
X = np.vstack((X, train4[0]))
X = np.vstack((X, train5[0]))
X = np.vstack((X, train6[0]))

y = [1, 1, 1, 0, 0, 0]

model = train(X, y)
# with open('model.pkl', 'wb') as fid:
#    pickle.dump(model, fid)
test = test1
test = np.vstack((test, test2[0]))

print(predict(test, model))
