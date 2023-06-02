for i in [1,2,3,4,5,6,7,8,9,10]:
    print(i)
    
# range(시작값, 종료값, 증감치)
print(range(1, 11))

for i in range(1, 11): # 1 ~ 10 까지
    print(i)
    
# 짝수만 10개 (출력 시 줄 바꿈)
for i in range(2, 21, 2): 
    print(i)
# 홀수만 10개 (출력 시 줄 바꿈)
for i in range(1, 20, 2): 
    print(i)
    

# 출력 시 줄 바꾸지 않음
print("줄 바꾸지 않고 출력: ", end = ' ')
print("옆에 나옴")

print("1~10 한 줄로 출력")
for i in range(1, 11):
    print(i, end = ' ')
print() # 이 때 줄 바꿈