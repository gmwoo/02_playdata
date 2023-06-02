colors = {"red": "빨간색", "blue": "파란색", "green": "초록색", 
          "black": "검정색"}
print(colors['red']) # red, blue, black 값 등을 key. key를 통해 데이터 접근
print(colors['blue']) # 인덱싱, 슬라이싱 적용안됨
print(colors['green'])
print(colors['black']) 

# dict 타입은 추가 키 값이 이미 존재했다면 수정, 값 바꿔치기, 없었으면 추가
colors['pink'] = "분홍색"  # 추가
colors['black'] = "검은색"
print(colors)

# 삭제
del colors['red']
print(colors)

# 키 값 목록만 - 키 값 순서는 내부적으로 알아서, 입력한 순서대로 나오지 않음
for key in colors:
    print(key, colors[key])