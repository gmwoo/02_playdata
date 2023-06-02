# 검색(search) - 데이터가 있는 곳의 위치를 찾는 것을 말함
# 선형검색, 이분검색, 해쉬검색
# 시스템이 제공하는 검색을 사용

fruits = ["사과", "참외", "오렌지", "바나나", "사과", "딸기", "사과", "포도", "배"]
# 단어 in 리스트:  해당 리스트에 단어가 존재하면 True, 없으면 False 반환

print("사과" in fruits) # 사과라는 단어가 fruits 안에 있느냐 있으면 True 없으면 False 출력
print("망고" in fruits) # False

print(fruits.index("사과")) # 위치값 반환
# print(fruits.index("망고")) # 요소 없으면 에러, in연산자, count함수와 함께 사용

# count: 요소 개수를 출력
print(fruits.count("사과"))
print(fruits.count("망고"))
print(fruits.count("딸기"))
print(fruits.count("포도"))

if "망고" in fruits:
    print("망고 위치: ", fruits.index("망고"))
else:
    print("망고는 없음")
    
if fruits.count("사과") > 0:
    print("사과의 위치: ", fruits.index("사과"))
else:
    print("사과는 없음")
    
