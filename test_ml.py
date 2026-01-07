from sklearn.ensemble import RandomForestClassifier
import pytest
import numpy as np
# TODO: add necessary import
from ml.model import train_model, compute_model_metrics, inference

# TODO: implement the first test. Change the function name and input as needed
def test_model():
    """
    
    Tests that train_model returns a RandomForestClassifier model

    """
    model = train_model([[0, 0], [1, 1]], [0, 1])
    assert isinstance(model, RandomForestClassifier), "train_model did not return a RandomForestClassifier"

# TODO: implement the second test. Change the function name and input as needed
def test_training_data_type():
    """
    Tests that the training data types are correct
    
    """
    X = np.array([[0, 0], [1, 1], [2, 2]])
    y = np.array([0, 1, 2])

    assert isinstance(X, np.ndarray)
    assert isinstance(y, np.ndarray)



# TODO: implement the third test. Change the function name and input as needed
def test_compute_metrics():
    """
    Tests that compute_model_metrics returns precision, recall, and fbeta as floats
    """
    y_true = np.array([0, 1, 1, 0, 1])
    y_pred = np.array([0, 1, 0, 0, 1])
    precision, recall, fbeta = compute_model_metrics(y_true, y_pred)
    assert isinstance(precision, float), "Precision is not a float"
    assert isinstance(recall, float), "Recall is not a float"
    assert isinstance(fbeta, float), "Fbeta is not a float"
 
