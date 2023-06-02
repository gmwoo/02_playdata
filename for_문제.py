# 문제 1. 3의 배수를 10개만 한줄로 출력
for i in range(1, 11):
    print(i*3, end = ' ')
print()
# print([i for i in range(3, 31, 3)], end = ' ')  # 한 줄
print()

# 문제 2. 100, 90, 80, 70, ..., 10 까지 한줄로 출력
lst_2 = [i for i in range(10, 101, 10)]
print(lst_2[::-1], end = ' ')
print()

# 문제 3. 다음 리스트에서 홀수번째 방 데이터만 출력. 1, 3, 5, 7, 9, ...
colors = ["red", "green", "blue", "cyan", "magenta", "black", "brown", "yellow", "green"]
print(colors[1::2])

# 문제 4. 구구단 4단 출력
print([i for i in range(4, 40, 4)], end = ' ')
print()

# 문제 5. 정수를 1~100까지 출력하는데, 10개 마다 줄바꿈 할 것. 힌트) if문 사용
lst_5 = [i for i in range(1, 101)]
for i in lst_5:
    if i % 10 == 0:
        print(i, end = ' ')
        print()
    else: print(i, end = ' ')
    
# 문제 6. 1~100까지 중에 홀수 합계
sum = 0
for i in range(1, 101, 2):
    sum = sum + i
print(sum)

# 문제 7. 1~100까지 중에 7의 배수의 개수
lst_7 = []
for i in range(1,101):
    if i%7==0:
        lst_7.append(i)
print(len(lst_7))
# print(len([i for i in range(1,101) if i % 7 == 0])) # 한 줄