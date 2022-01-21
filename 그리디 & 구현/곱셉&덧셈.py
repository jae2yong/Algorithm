s = input()
print(s)
print(len(s))
print(s[1])
result = int(s[0])
for i in range(1,len(s)):
  k = int(s[i])
  if result<=1 or k<=1:
    result += k
  else:
    result *= k
print(result)
  # if s[i] == '0' or s[i] == '1':
  #   s += int(s[i])
  # else:
  #   s *= int(s[i])

# while True:
#   a = str[0]
#   b = str[1]
#   c = str[2]
  #0이나 1일 경우 더하고 
  #2 이상일 경우에는 곱하기