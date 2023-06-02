fruits = ("사과", "배", "딸기", "포도")
print(fruits)
print(type(fruits[0]))
print(type(fruits[1]))
print(type(fruits[0:3]))
print(type(fruits[::-1]))

# fruits[0] = "망고" # 에러 남. 즉, 값 변경 불가
# fruits.append('망고') # 에러 남. 

name = "홍길동"
age = 12
phone = "010-0000-0000"
kor = 90

# str: 클래스, 파이썬에서 제공하는 데이터 타입
# %s: 문자열, %d: 정수, %f: 실수
s1 = str.format("이름: %s, 나이: %d, 전화번호: %s" 
                % (name, age, phone)) # (name, ~) 튜플 형태로 ㅣ반환
print(s1, type(s1))

s2 = str.format("이름: %s, 국어: %d, 영어: %d, 수학: %d" 
                % ("임꺽정", 90, 70, 80))
print(s2, type(s2))


# 두 변수 값을 바꿀 때
a=5
b=3
# temp = a
# a = b
# b = a
# print(f"a = {a}, b = {b}") # 기존 방법
a, b = b, a
print(f"a = {a}, b = {b}") # 튜플을 이용한 값 바꿈


# 
