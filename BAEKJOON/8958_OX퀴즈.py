n = int(input())

for i in range(n):
  answer_list = list(input())
  sum_score =0
  score =0 
  # 초기화 해주는 걸 놓쳤었다. score도 answer_list의 마지막 답이 O일 경우를 대비해 초기화 시켜줘야 한다.
  for answer in answer_list:
    if answer == 'O':
      score += 1
      sum_score += score
    else:
      score = 0
  print(sum_score)