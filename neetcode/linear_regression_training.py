import numpy as np
from numpy.typing import NDArray


class Solution:
    def get_derivative(self, model_prediction: NDArray[np.float64], ground_truth: NDArray[np.float64], N: int, X: NDArray[np.float64], desired_weight: int) -> float:
        # note that N is just len(X)
        return np.squeeze(-2 * ((ground_truth[None,:] - model_prediction[None,:]) @ X) / N)

    def get_model_prediction(self, X: NDArray[np.float64], weights: NDArray[np.float64]) -> NDArray[np.float64]:
        return np.squeeze(np.matmul(X, weights))

    learning_rate = 0.01

    def train_model(
        self, 
        X: NDArray[np.float64], 
        Y: NDArray[np.float64], 
        num_iterations: int, 
        initial_weights: NDArray[np.float64]
    ) -> NDArray[np.float64]:

        weights = initial_weights
        for i in range(num_iterations):
            model_prediction = self.get_model_prediction(X, weights)
            deriv = self.get_derivative(model_prediction, Y, len(X), X, len(X[0]))
            weights -= self.learning_rate*deriv
        return np.round(weights, 5)

solution = Solution()

X = [[1, 2, 3], [1, 1, 1]]
Y = [6, 3]
num_iterations = 10
initial_weights = [0.2, 0.1, 0.6]

np.testing.assert_equal(solution.train_model(np.array(X), np.array(Y), num_iterations, np.array(initial_weights)), np.array([0.50678, 0.59057, 1.27435]))
