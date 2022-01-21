#현재 나이트의 위치 입력받기
input_data = input()
row = int(input_data[1])
column = int(ord(input_data[0])) - int(ord('a')) + 1
#나이트가 이동할 수잇는 8가지 방향 정의
steps = [(-1,-2),(-1,2),(-2,-1),(-2,1),(2,1),(2,-1),(1,2),(1,-2)]
result = 0
# 8가지 방향에 대하여 각 위치로 이동이 가능한지 확인
for step in steps:
  #이동하고자 하는 위치 확인
  next_row = row + step[0]
  next_column = column + step[1]
  #
  if next_row >=1 and next_row <= 8 and next_column >=1 and next_column <=8:
    result += 1

print(result)