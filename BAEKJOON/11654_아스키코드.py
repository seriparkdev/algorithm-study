n = input()
result = 0

if type(n) is int: # type을 비교할 땐 is로
  result = chr(n) # chr는 숫자를 아스키코드로
else:
  result = ord(n) # ord는 문자를 아스키코드로
  
print(result)