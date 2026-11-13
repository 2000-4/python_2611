import numpy as np

arr = np.array([[3, 6, 9],
                [2, 4, 8],
                [5, 7, 1]])

print(arr.shape)
print(arr.ndim)
print(arr.mean(axis=0))
print(arr.max(axis=1))
print((arr.T).shape)
print((arr.flatten()).min())
print(arr.reshape(1, 9))

# 문제
# 1. arr의 shape과 ndim을 출력하시오.
# 2. 열 방향 평균을 구하시오.
# 3. 행 방향 최댓값을 구하시오.
# 4. arr을 전치행렬로 만든 후 shape을 출력하시오.
# 5. arr을 1차원으로 펼친 뒤 최솟값을 구하시오.
# 6. arr을 (1, 9) 형태로 reshape 하시오.