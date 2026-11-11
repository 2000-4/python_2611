# 기본 변수 
age = 30

# 어노테이션 추가
# 변수이름: 자료형 = 값
age: int = 30

print(age)


# 주로 코드 설명용으로 사용한다 // 코드 가독성
print('\n==== 함수 어노테이션 ====')
def add(a: int, b: int) -> int : # 반환값도 int다
    return a + b

print(add(3, 5))
print(add('3', '5')) # 또한 int로 취급되기 때문에 신중해야 한다

print('\n ==== 리스트, 딕셔너리 어노테이션 ====')



nums: list[int] = [1, 2, 3]


person : dict[str, int] = { # 스트링과 int로 이루어진 딕셔너리를 사용하겠다
    'age' : 30,
    'height' : 170
}

print(nums)