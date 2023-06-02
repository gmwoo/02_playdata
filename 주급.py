names = ["홍길동", "임꺽정", "장길산"]
work_times = [40, 30, 20]
per_pays = [20000, 15000, 30000]

pays = [] # 빈 리스트, 연산을 통해 데이터 추가
for i in range(0,3): # range(시작, 종료, 증강)
    pays.append(work_times[i] * per_pays[i])

# 출력
for i in range(0,3):
    print(names[i], "의 급여는 ", pays[i], "입니다.")