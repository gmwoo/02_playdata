# list 관련 문제
""""
 1. flower 변수에 다음 꽃들을 입력하세요.
 작약, 국화, 목련, 목단, 장미, 해바라기
 2. 0, 2, 4 번 데이터 출력하기 (인덱싱, 슬라이싱 둘 다 사용하기)
 3. 해바라기 => 백일홍으로 수정하기
 4. 사루비아, 맨드라미 두 종류 추가하기
 5. 목련 삭제
 6. 현재 데이터 개수 출력하기
 7. 마지막 데이터 삭제

"""
# 1번
flower = ["작약", "국화", "목련", "목단", "장미", "해바라기"]
print(flower)

# 2번
print(flower[0],flower[2],flower[4])
print(flower[0:5:2]) 

# 3번
flower[-1] = "백일홍" 
print(flower)

# 4번
flower.append("사루비아")
flower.append("맨드라미")
print(flower) 

# 5번
flower.remove("목련")
print(flower)

# 6번
print(len(flower))

# 7번
del flower[-1]
print(flower)
