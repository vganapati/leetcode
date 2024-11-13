class Solution:
    def get_minimizer(self, iterations: int, learning_rate: float, init: int) -> float:
        val = init

        for i in range(iterations):
            gradient = -2*val
            val += learning_rate*gradient
        
        return round(val, 5)

if __name__ == "__main__":
    solution = Solution()
    iterations = 0; learning_rate = 0.01; init = 5
    assert solution.get_minimizer(iterations, learning_rate, init) == 5

    iterations = 10; learning_rate = 0.01; init = 5
    assert solution.get_minimizer(iterations, learning_rate, init) == 4.08536

