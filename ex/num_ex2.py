import numpy as np

arr = np.array([[1.5, 2.5, 3.5, 4.5],
                [5.5, 6.5, 7.5, 8.5]])


print(arr.dtype)
print(arr.itemsize)
print(arr.sum(axis=0))
print(arr.mean(axis=1))
print(arr.reshape(4,2))
arr_t = arr.T
print(arr_t.shape)
arr_f = arr.flatten()
print(arr_f.shape)

# 문제
# 1. arr의 dtype과 itemsize를 출력하시오.
# 2. axis=0 기준 합을 구하시오.
# 3. axis=1 기준 평균을 구하시오.
# 4. arr을 (4,2) 형태로 reshape 하시오.
# 5. reshape한 배열을 전치한 결과의 shape을 구하시오.
# 6. arr.flatten()으로 만든 배열의 shape은 무엇인가?
