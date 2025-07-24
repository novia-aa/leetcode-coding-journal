class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        left, right = 0, m * n - 1

        while left <= right:
            mid = (left + right) // 2
            mid_value = matrix[mid // n][mid % n]  # 將 1D index 映射回 2D

            if mid_value == target:
                return True
            elif mid_value < target:
                left = mid + 1
            else:
                right = mid - 1

        return False


"""
2D matrix flatten 成 1D binary search
每列的第一個元素大於上一列的最後一個元素 → 可以視為「攤平成一維的有序陣列」


"""
