n = int(input())
data = list(map(int,input().split()))
data.sort()
result = 0
count = 0
for i in data:
  count += 1
  if count >= i:
    result +=1 #그룹 수
    count = 0 #모험가의 수 초기화
print(result)

#오름차순으로 정렬
#전체 인원 / 최대값