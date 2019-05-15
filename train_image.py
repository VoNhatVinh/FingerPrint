from sklearn.neural_network import MLPClassifier

def train(X, y):
    clf = MLPClassifier(hidden_layer_sizes=1, activation='logistic', max_iter=5000)
    clf.fit(X, y)
    return clf

def predict(X, clf):
    return clf.predict(X)