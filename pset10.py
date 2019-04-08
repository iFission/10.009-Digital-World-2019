#%%
'hw1'
import numpy as np
from sklearn.metrics import confusion_matrix, classification_report


def get_metrics(actual_targets, predicted_targets, labels):

    c_matrix = confusion_matrix(
        actual_targets, predicted_targets,
        labels)  # returns a ndarray of tn, fp, fn, tp. to assign, add .ravel()

    tn, fp, fn, tp = c_matrix.ravel()

    output = {
        'confusion matrix': c_matrix,
        'total records': len(actual_targets),
        'accuracy': round((tp + tn) / len(actual_targets), 3),
        'sensitivity': round(tp / (tp + fn), 3),
        'false positive rate': round(fp / (fp + tn), 3)
    }

    return output


#%%
'hw2'


def five_number_summary(x):
    if x.ndim != 2:
        return None

    ls = []

    for i in range(x.shape[1]):
        column = x[:, i]
        # print(column)

        stats = {
            'minimum': np.min(column),
            'first quartile': np.percentile(column, 25),
            'median': np.percentile(column, 50),
            'third quartile': np.percentile(column, 75),
            'maximum': np.max(column)
        }
        ls.append(stats)
    return ls


#%%
'hw3'

import numpy as np


def normalize_minmax(data):
    if data.ndim != 2:
        return None

    ls = []

    for i in range(data.shape[1]):
        column = data[:, i]

        # using feature scaling
        column = (column - np.min(column)) / (np.max(column) - np.min(column))
        ls.append(column)

    # convert to np array, transpose to original shape, as originally, lists are added row by row
    return np.array(ls).T


#%%
'hw4'

from sklearn.model_selection import train_test_split
from sklearn import neighbors, datasets
from sklearn.metrics import confusion_matrix
import numpy as np


def knn_classifier(b, feature_list, size, seed, k):
    features = b.data[:, feature_list]
    labels = b.target
    features = normalize_minmax(features)

    train_features, test_features, train_labels, test_labels = train_test_split(
        features, labels, test_size=size, random_state=seed)

    model = neighbors.KNeighborsClassifier(n_neighbors=k)
    model.fit(train_features, train_labels)

    predicted_labels = model.predict(test_features)

    results = get_metrics(test_labels, predicted_labels, [1, 0])
    # requires label = [1,0] to pass vocareum's test case, but pset's pdf  arranges confusion matrix otherwise (normal, expected)

    return results


# b = datasets.load_breast_cancer()
# feature_list = range(20)

# knn_classifier(b, feature_list, .4, 2752, 3)

#%%
'hw5'

from sklearn import linear_model
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
import numpy as np


def linear_regression(b, x_index, y_index, size, seed):
    x = b.data[:, [x_index]]
    y = b.data[:, [y_index]]

    x_train, x_test, y_train, y_test = train_test_split(
        x, y, test_size=size, random_state=seed)

    model = linear_model.LinearRegression()
    model.fit(x_train, y_train)

    y_predict = model.predict(x_test)

    mse = mean_squared_error(y_test, y_predict)
    r2 = r2_score(y_test, y_predict)

    results = {
        'coefficients': model.coef_,
        'intercept': model.intercept_,
        'mean squared error': mse,
        'r2 score': r2
    }

    return x_train, y_train, x_test, y_predict, results


#%%
'hw6'
import numpy as np
from sklearn import linear_model
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import PolynomialFeatures


def multiple_linear_regression(b, x_index, y_index, order, size, seed):
    x = b.data[:, [x_index]]
    y = b.data[:, [y_index]]

    poly = PolynomialFeatures(order, include_bias=False)
    x = poly.fit_transform(x)
    print(x.shape)

    x_train, x_test, y_train, y_test = train_test_split(
        x, y, test_size=size, random_state=seed)

    model = linear_model.LinearRegression()
    model.fit(x_train, y_train)

    y_predict = model.predict(x_test)

    mse = mean_squared_error(y_test, y_predict)
    r2 = r2_score(y_test, y_predict)

    results = {
        'coefficients': model.coef_,
        'intercept': model.intercept_,
        'mean squared error': mse,
        'r2 score': r2
    }

    return x_train[:, [x_index]], y_train, x_test[:, [x_index
                                                      ]], y_predict, results


multiple_linear_regression(b, 0, 3, 4, .4, 2752)
#%%
'hw7'
from sklearn.model_selection import train_test_split
from sklearn import neighbors, datasets
from sklearn.metrics import confusion_matrix, accuracy_score
import numpy as np


def knn_classifier_full(b, feature_list, size, seed):
    features = b.data[:, feature_list]
    labels = b.target
    features = normalize_minmax(features)

    train_features, other_features, train_labels, other_labels = train_test_split(
        features, labels, test_size=size, random_state=seed)
    val_features, test_features, val_labels, test_labels = train_test_split(
        other_features, other_labels, test_size=.5, random_state=seed)

    acc_ls = []
    metrics_ls = []

    for k in range(1, 20 + 1):
        model = neighbors.KNeighborsClassifier(n_neighbors=k)
        model.fit(train_features, train_labels)
        predicted_labels = model.predict(val_features)
        acc_ls.append(accuracy_score(val_labels, predicted_labels))

        metrics = get_metrics(val_labels, predicted_labels, [1, 0])
        metrics_ls.append(metrics)

    acc_max = max(acc_ls)
    k_best = acc_ls.index(acc_max) + 1
    val_set = metrics_ls[k_best - 1]

    model = neighbors.KNeighborsClassifier(n_neighbors=k_best)
    model.fit(train_features, train_labels)
    predicted_labels = model.predict(test_features)
    test_set = get_metrics(test_labels, predicted_labels, [1, 0])

    results = {
        'best k': k_best,
        'validation set': val_set,
        'test set': test_set
    }

    return results


# b = datasets.load_breast_cancer()
# knn_classifier_full(b, feature_list, .4, 2752)