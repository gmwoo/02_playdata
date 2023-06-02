words = ['school', "assembly", "chair", "hospital", 
         "desk", "rain", "rainbow"]
print(words)
print("데이터 개수: ", len(words))

# 인덱싱
print(words[0])
print(words[1])
print(words[2])

words[3] = "house"

# for 문을 이용해 전부 출력
for w in words:
    print(w)

# 슬라이싱 - 파이썬 이후로 등장하는 문법, 리스트변수[시작:종료:증감치]
print(words[0:3]) # 0,1,2 마지막을 제외하고 출력
# [0:3:1] 마지막 생략하면 디폴트 1
print(words[0:5:2]) # 0,2,4 번 방만 출력

print(words[6:3:-1]) # 6, 5
print(words[::-1]) # 6,5,4,3,2,1,0

print(words[6:-1:-1]) # 파이썬 버전에 따라 동작, 현재 버전은 출력 X