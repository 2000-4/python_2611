#클로저(Closure)랑 데코레이터(Decorator)

# 클로저 : 내부 함수가 자신이 정의된 외부 함수의 변수들을 기억하고,
# 외부 함수의 실행이 끝난 후에도 해당 변수를 사용할 수 있는 구조

print('===== 1단계 : 함수 안에 함수 만들기 =====')

def outer() :
    print("outer 함수가 실행되었습니다.")
    
    def inner() :
        print('inner 함수가 실행되었습니다.')
    
    return inner # 함수 자체를 반환
    return inner() # 함수를 실행하고 그 결과를 반환 함수를 값으로 취급 가능


func = outer()
func()

print('\n ==== 2단계 : 클로저 ==== ')
# 클로저는 '외부 함수의 변수를 기억하는 내부 함수' 입니다.

def make_multiplier(x):
    # x는 make_multiplier 함수의 지역 변수
    
    def multiplier(n):
        # 내부 함수 multiplier는
        # 바깥 함수의 변수 x를 사용할 수 있다
        return x * n
    
    return multiplier # 함수 자체를 반환 multiplier()와 다르다. multiplier함수 실행값을 반환.

times3 = make_multiplier(3)
print(times3(10))
print(times3(5))

# 클로저 사용 X
'''
def times3(n) :
    return 3 * n


def times3(n) :
    return 5 * n
'''

print('\n===== 3단계 : 데코레이터 기본 구조 =====')

# 데코레이터는 '함수를 꾸며 주는 함수'
# 내부 구조는 클로저와 매우 유사

def decorator(func) : # 데코레이터 사용 시 필수 함수 네이밍 중요
    
    def wrapper() :
        print('함수 실행 전')
        func()
        print('함수 실행 후')
    
    return wrapper

@decorator # 데이코레이터를 사용하겠다는 것을 알림
def say_hello() :
    print('안녕하세요')
    
say_hello()


print('\n===== 4단계 : 매개변수가 있는 데코레이터  =====')

def decorator_width_args(func):
    def wrapper(name):
        print('실행 전')
        func(name)
        print('실행 후')
    return wrapper

@decorator_width_args
def say_name(name):
    print('이름 :', name)

say_name('홍길동')