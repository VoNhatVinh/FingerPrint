from mlpClassifier import train, predict
import numpy as np
import pickle
from main import main_predict

'''
Load data from a pickle file

Parameters:
----
filename: string
          a path to file need to load

Return:
----
A objet in a pickle file
'''
def load(filename):
    with open(filename, 'rb') as fid:
        return pickle.load(fid)


res = 0
X = []
X_test = []
X_test.append(load('test_pkl/test1_1.pkl'))
X_test.append(load('test_pkl/test2_2.pkl'))
X_test.append(load('test_pkl/test3_1.pkl'))
X_test.append(load('test_pkl/test4_1.pkl'))
X_test.append(load('test_pkl/test5_1.pkl'))
X.append(load('train_pkl/1_1.pkl'))
X.append(load('train_pkl/1_2.pkl'))
X.append(load('train_pkl/1_4.pkl'))
X.append(load('train_pkl/2_1.pkl'))
X.append(load('train_pkl/2_2.pkl'))
X.append(load('train_pkl/2_4.pkl'))
X.append(load('train_pkl/3_1.pkl'))
X.append(load('train_pkl/3_3.pkl'))
X.append(load('train_pkl/3_4.pkl'))
X.append(load('train_pkl/4_1.pkl'))
X.append(load('train_pkl/4_2.pkl'))
X.append(load('train_pkl/4_3.pkl'))
X.append(load('train_pkl/5_1.pkl'))
X.append(load('train_pkl/5_2.pkl'))
X.append(load('train_pkl/5_3.pkl'))

y_test = np.array(([1, 2, 3, 4, 5]))

for i in range(100):
    print("fit model 1...")
    y = np.zeros(15)
    y[0:3] = 1
    model1 = train(X, y)

    print("fit model 2...")
    y = np.zeros(15)
    y[3:6] = 1
    model2 = train(X, y)

    print("fit model 3...")
    y = np.zeros(15)
    y[6:9] = 1
    model3 = train(X, y)

    print("fit model 4...")
    y = np.zeros(15)
    y[9:12] = 1
    model4 = train(X, y)

    print("fit model 5...")
    y = np.zeros(15)
    y[12:15] = 1
    model5 = train(X, y)

    predictions = []
    tmp = predict(X_test, model1)
    predictions.append(tmp[:, 1])
    tmp = predict(X_test, model2)
    predictions.append(tmp[:, 1])
    tmp = predict(X_test, model3)
    predictions.append(tmp[:, 1])
    tmp = predict(X_test, model4)
    predictions.append(tmp[:, 1])
    tmp = predict(X_test, model5)
    predictions.append(tmp[:, 1])

    # Get index of max in row
    tmpRes = np.argmax(predictions, axis=0)
    for i in range(len(tmpRes)):
        tmpRes[i] += 1
    print(tmpRes)

    # Compare and compute sum
    res += sum(tmpRes == y_test)

print(res)
print(res/500)
