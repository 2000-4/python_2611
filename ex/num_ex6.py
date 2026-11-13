import numpy as np

np.random.seed(10)

# 1. 1부터 100까지의 정수 중에서 난수를 생성하여 (4, 5) 배열을 만들고 arr에 저장해주세요.
arr = np.random.randint(1, 101, (4, 5))


# 2. 생성된 배열의 차원, 형태, 원소 개수를 출력해주세요.
print(arr.ndim)
print(arr.shape)
print(arr.size)


# 3. 첫 번째 행과 세 번째 행만 선택해서 출력해주세요.
print(arr[[0, 2]])

# 4. 각 행의 평균을 구해주세요.
print(arr.mean(axis=1))

# 5. 각 열의 최댓값을 구해주세요.
print(arr.max(axis=0))

# 6. 50 이상인 값만 추출해주세요.
print(arr[arr >= 50])

# 7. 70 이상인 원소가 몇 개인지 출력해주세요.
print(np.count_nonzero(arr >= 70))

# ------------------------------
# count_nonzero()
# ㄴ> 배열에서 0이 아닌 값의 개수를 세는 함수
# ㄴ 조건식이 붙는다 True 1, False 0 > 직접 추출
# size = 추출 후에 개수를 추출
# ------------------------------

# 8. 60 이상이면 '합격', 60 미만이면 '불합격'인 새로운 배열을 만들어주세요.
avg = arr.mean(axis=1)
new_array = np.where(avg >= 60, '합격', '불합격')
print(new_array)

# 9. 전체 배열에서 최댓값의 위치를 (행, 열) 형태로 출력해주세요.
index = arr.argmax()
position = np.unravel_index(index, arr.shape)
print(position)

# 10. 배열의 모든 값에 10을 더한 뒤 100을 초과하는 값은 100으로 변경해주세요.
print(np.clip(arr + 10, 0, 100))