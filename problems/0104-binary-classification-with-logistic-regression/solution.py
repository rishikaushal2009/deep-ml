import numpy as np

def predict_logistic(X: np.ndarray, weights: np.ndarray, bias: float) -> np.ndarray:
	return ((1/(1 + np.exp(-(X.dot(weights)+ bias)))) >= 0.5).astype(int)
	