# # # age = 20
# # # has_ticket = True

# # # if age >= 20 and has_ticket :
# # #     print("입장 가능합니다.")

# # # 문제시작
# # a = 10

# # # `==` => 같다.
# # if ( a == 10 ):
# #   print("참1")

# # # `!=` => 같지 않다.
# # if ( a != 10 ):
# #   print("거짓1")

# # if ( a > 10 ):
# #   print("거짓2")

# # if ( a >= 10 ):
# #   print("참2")

# # b = 10

# # if ( a == b ):
# #   print("참3")

# # # c 에는 true or false 이 담긴다.
# # c = a != b

# # if ( c ):
# #   print("거짓3")

# # if ( c == False ):
# #   print("참4")

# # # `not` => 반전
# # if ( not c ):
# #   print("참5")

# # if ( not(not c) ):
# #   print("거짓4")

# # d = True

# # if ( c != d ):
# #   print("참6")

# # if ( 10 > 5 and -6 > -10 and 10 != 10 ):
# #   print("거짓5")

# # if ( 10 < 5 and -6 < -10 and 10 != 10 or 10 > 5 ):
# #   print("참7")
# # # 문제끝

# # age = 35 # 25로 바꿔서 실행해보세요. 15로도 바꿔서 실행해보세요.

# # if age >= 30 :
# #     print("30대")
# # elif age >= 20 :
# #     print("20대")
# # else :
# #     print("10대")


# # age = 19

# # if age <= 19 or age >= 60 :
# #     print("할인 대상입니다.")
# # else :
# #     print("할인 대상이 아닙니다.")

# # print("== 정답 v2 ==")
# # print("할인 대상입니다.")
# # print("할인 대상이 아닙니다.")

# # i = 1
    
# # while i <= 3:
# #   print(i)
# #   i += 1 # 잊지 않기

# # print(i) # 4
# # i = 1

# # while i < 301 :
# #     print(i)
# #     i += i
    
# # i = 100

# # while i >= -25 :
# #     print(i)
# #     i = i - 1


# # i = 1
# # sum = 0
# # while i < 6 :
# #     sum = i + i
# #     i += 1
# #     print(sum)

# # while i < 101 :
# #     if i % 2 == 0:
# #         sum += i
# #     i += 1
# # print(sum)

# # while i < 1001 :
# #     i += 1
# #     if i % 3 == 0:
# #         print(i)
        

# # while i < 101 :
# #     i += 1
# #     if i % 2 == 0 :
# #         print(i)
# # i = 1
# # while i <= 10:
# #     j = 1
# #     while j <= 3:
# #         print(j)
# #         j += 1
# #     i += 1

# # for i in range(1, 5, 2):
# #     print(i)

# # i = 1
# # for i in range(1, 101) :
# #     print(i)


# # i = 100
# # for i in range(100, 0, -1) :
# #     print(i)

# # i = 1

# # while i < 10 :
# #     print(f"== {i}단 ==")
# #     i += 1
# #     j = 1
# #     while j < 10 :
# #         print(f"{j} * {i} = {j * i}")
# #         j += 1

# # for i in range(1, 10) :
# #     print(f"== {i}단 ==")
# #     for j in range(1, 10) :
# #         print(f"{j} * {i} = {j * i}")

# # def dan(x) : # x는 매개변수 / Parameter
# #     for i in range(1, 10) :
# #         print(f"== {i}단 ==")
# #         for j in range(1, 10) :
# #             print(f"{j} * {i} = {j * i}")
    
# # dan(7) # 7은 인자/인수 / Argument


# # def is_prime_number(num):
# #     if num < 2:
# #         return False
# #     for i in range(2, num):
# #         if num % i == 0:
# #             return False
# #     return True



# # print("3은 소수입니다 : {}".format(is_prime_number(3)))
# # print("4는 소수입니다 : {}".format(is_prime_number(4)))
# # print("5는 소수입니다 : {}".format(is_prime_number(5)))
# # print("6는 소수입니다 : {}".format(is_prime_number(6)))
# # print("7는 소수입니다 : {}".format(is_prime_number(7)))
# # print("1000은 소수입니다 : {}".format(is_prime_number(1000)))


# # ============ 2 일차 =====================


# List = [2, 1, 5, 6, 7]
# print(List)

# List1 = []
# List1.append(2)
# List1.append(1)
# List1.append(5)
# List1.append(6)
# List1.append(7)
# print(List1)

# List2 = ['월', '화', '수', '목', '금']
# List2 += ['토', '일']
# print(List2)
# print(List2[4])

# List3 = [2, 1, '오', 6, 7]
# # List3[2] = 5
# List3[List3.index('오')] = 5
# print(List3)

# List4 = ['월', '화', '수', '목', '금']
# if '화' in List4 :
#     print("화요일이 있습니다.")
# # i = List4.index('화')
# # print(i)

    
# List6 = ['월', '화', '수', '목', '금']
# del List6[4]
# print(List6)

# # if '금' in List6 :
# #     List6.pop(List6.index('금'))
# #     print(List6)


# # if '금' in List6 :
# #     List6.remove('금')
# #     print(List6)

# day ={
    # "1월" : 31,
    # "2월" : 28,
    # "3월" : 30
# }
# print(day)
# 

# month_end_days = {}

# for i in range(1, 12 + 1) : # 3까지 가기 위해 +1
#     month = str(i) + "월"
    
#     end_day = 31
    
#     if i == 2:
#         end_day = 28
#     elif i in [4, 6, 9, 11]:
#         end_day = 30

#     month_end_days[month] = end_day
    
# print(month_end_days)

# print('== 예제 1 ==')
# s = "안녕하세요."

# print('s의 길이 출력')
# print(len(s))

# # 문자열[시작:종료-1:간격[1]]
# print('s를 이루는 문장 중에서 옆에 거 2개 출력')

# print('s를 이루는 문장 중에서 문자 하나 건너뛰고 1개 출력')
# print(s[1:2])

# print(s[:4])

# print('s를 이루는 문장 중에서 앞에 문자 3개 건너뛰고, 나머지 전부 출력 len')
# print(s[3:len(s)])

# print('s를 이루는 문장 중에서 앞에 문자 3개를 건너뛰고, 나머지 뒤 인덱스 생략')
# print(s[3:])

# print('=== 예제 2 ===')
# s = '안녕하세요.'

# print('s를 이루는 문자를 하나씩 출력, while')
# print('s를 이루는 문자를 역순으로 출력, while')

# i = 0
# while i < len(s) :
#     print(s[i])
#     i += 1

# # 역순 출력
# i = len(s) - 1
# while i >= 0 :
#     print(s[i])
#     i -= 1
    
# for c in s:
#     print(c)
    
# print(" == 예제 3 ==")
# s = 'a안b녕c하d세e요f'

# print('s를 이루는 문장 중에서 한글만 출력')
# print(s[1] + s[3] + s[5] + s[7] + s[9])

# print('s를 이루는 문장 중에서 한글만 출력, for, if, or, continue ')
# for c in s:
#     if c == 'a' or c == 'b' or c == 'c' or c == 'd' or c == 'e' or c == 'f':
#         continue
#     print(c)
    
# for c in s :
#     if c != 'a' and c != 'b' and c != 'c' and c != 'd' and c != 'e' and c != 'f':
#         print(c)
        
# for c in s:
#     if c not in ['a', 'b', 'c', 'd', 'e', 'f']:
#         print(c)

# try :
#     num = int('abc')
#     print(num)
# except ValueError:
#     print('숫자로 변환할 수 없습니다')

# class Person:
#     def hello(self):
#         print("안녕하세요.")

# jin = Person() #jin은 Person의 인스턴스다.
# jin.hello()

# a = int(10)
# print(a)

# b = list(range(10)) # 클래스나 다름 없음 b는 list 클래스의 인스턴스다.
# b.append(20) # 메서드나 다름 없음
# print(type(b))

# class Person:
#     pass

# class Person:
#     def hello(self): # self는 인스턴스 메서드에서 본인을 참조하기 위함
#         print("안녕하세요.")
#     def hi(self):
#         self.hello() # self 리모컨을 거쳐서 hello를 하청한다.
        
# jin = Person()
# jin.hi()


# class Person:
#     def __init__(self) : # 생성자, 초기화 메서드 // 무조건 실행
#         self.hello = '안녕하세요.' # 클래스 안의 변수 = 속성 // 명사
        
#     def hi(self) :
#         print(self.hello) # self 리모컨을 거쳐서 hello를 하청한다.
        
# jin = Person() # 이 코드를 입력하자마자 init 메서드가 자동으로 실행이 된다. __init__()을 쓰지 않아도 바로 실행된다.
# jin.hi()

# # self는 함수 안에서 사용하는 것이고 그것을 밖으로 빼서 쓰고 싶으면 jin으로 쓰는 것이다.


# class Person:
    # def __init__(self, name, age, hobby) :
        # self.hello = '안녕하세요'
        # self.name = name
        # self.age = age
        # self.hobby = hobby
        # 
    # def introduce(self) :
        # print(f"{self.hello}, 저는{self.age}살 {self.name}입니다. {self.hobby}을 좋아합니다.") 
        # 
# jin = Person('진', 23, '운동')
# jin.introduce()


# class Person:
#     pass

# jin = Person()
# jin.name = '진' # 인스턴스를 생성한 뒤 속성 추가

# kim = Person()
# kim.name = '김'

# print(jin.name)
# print(kim.name) 
 
 
# 클래스 외부에서는 접근 불가, 클래스 내부에서만 사용 가능한 private attribute

# class Person:
#     def __init__(self, name, age, weight) :
#         self.name = name
#         self.age = age
#         self.__weight = weight
        
#     def diet(self, loss_weight):
#         self.__weight -= loss_weight
#         print(self.__weight)
        
# jin = Person('진' , 22, 80)
# jin.__weight -= 20

# print(jin.weight)



# class Person:
#     folder = [] #공용
    
# def add_files(self, file):
#         self.folder.append(file)
        
# jin = Person()
# jin.add_files('txt')
 
# kim = Person()
# kim.add_files('img')
 
# print(jin.folder)
# print(kim.folder)

print('추가 코드')