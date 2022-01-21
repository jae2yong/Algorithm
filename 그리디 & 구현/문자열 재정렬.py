string = list(input())
result = []
value = 0
for x in string:
  if x.isalpha():
    result.append(x)
  else:
    value += int(x)
result.sort()
print(''.join(result)+str(value))

