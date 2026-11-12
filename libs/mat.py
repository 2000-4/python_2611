# Matplotlib = 데이터를 표현할 수 있게 해 주는 파이썬 라이브러리
# ㄴ> 시각화 도구
# figure => 큰 도화지
# subplots => 도화지 원에 나눠진 작은 칸들

import matplotlib.pyplot as plt

# 기본 스타일 적용
plt.style.use('default')

# # y값만 전달, x는 자동으로 0, 1, 2, 3이 설정
# plt.plot([2, 4, 6, 8])

# x = [2, 4, 6, 8]
# y = [1, 3, 5, 7]
# plt.plot(x, y)

# plt.show()

# fig = plt.figure()

# # (행 개수)
# fig.add_subplot(1, 2, 1)
# fig.add_subplot(1, 2, 2)
# plt.show()


# fig = plt.figure()

# # (행 개수, 열 개수, 위치값)
# fig.add_subplot(1, 3, 1)
# fig.add_subplot(1, 3, 3)
# plt.show()

# fig = plt.figure()


# fig.add_subplot(1, 2, 1)
# fig.add_subplot(2, 2, 2) # 열 개수는 모두 동일해야 하고, 열 개수보다 위치값이 클 수 없다.
# plt.show()

# # ========== 
# # 이전 figure 모두 닫기


# fig = plt.figure()

# a1 = fig.add_subplot(1, 2, 1)
# a2 = fig.add_subplot(1, 2, 2)

# x = range(0, 10)
# y = range(5, 15)
# a1.plot(x, y, 'yD')

# x = range(0, 50)
# y = range(0, 50)
# a2.plot(x, y, 'm*') # 스타일 변경

# plt.show()

plt.close('all')

# ggplot 특징
# - 배경에 격자(grid)가 있음
# - 데이터 비교가 쉬움

fig = plt.figure()


plt.style.use('ggplot')
# 1 행 1열짜리 영역에서 1번째 위치에 그래프 생성

a = fig.add_subplot(111)
x = [3, 4] #막대의 위치(좌표 기준)
y = [1, 2] #막대의 높이(값 기준)

labels = ['english', 'math']
colors = ['red', 'blue']
a.bar(x, y, tick_label=labels, color=colors) # 새로 막대
a.barh(x, y, tick_label=labels, color=colors) # 가로 막대

plt.show()

