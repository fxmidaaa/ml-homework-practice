import numpy as np
import pandas as pd
def sigmoid(z):
    z = np.clip(z, -500, 500)
    return 1 / (1 + np.exp(-z))


def fit_logistic_regression(X, y, learning_rate=0.01, steps = 1_000):
    X = np.asarray(X, dtype=float)
    y = np.asarray(y, dtype=float)

    weights = np.zeros(X.shape[1])
    bias = 0.0

    for _ in range(steps):
        probabilities = sigmoid(X @ weights + bias)
        errors = probabilities - y
        weights -= learning_rate * (X.T @ errors) / X.shape[1]
        bias -= learning_rate * errors.mean()


    return weights, bias


def predict_logistic_regression(X, weights, bias):
    probabilities = sigmoid(np.asarray(X, dtype=float) @ weights + bias)
    return probabilities


# METRICS

y_val = []
y_pred = []
X = []
weights = np.ones(X.shape[1])
bias = 0.0
def f1_score(data=y_val, y_pred=y_pred):
    act_pos, act_neg = (data == 1), (data == 0)
    pred_pos, pred_neg = (y_pred >= 0.5), (y_pred < 0.5)

    tp, fp = (pred_pos & act_pos).sum(), (pred_pos & act_neg).sum()
    tn, fn = (pred_neg & act_neg).sum(), (pred_neg & act_pos).sum()

    precision = tp / (tp + fp) if (tp + fp) > 0 else 0
    recall = tp / (tp + fn) if (tp + fn) > 0 else 0

    return 2 * (precision * recall) / (precision + recall) # f1-score