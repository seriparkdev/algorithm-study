n = int(input())
avg = 0 

for i in range(n):
  n_score_list = list(map(int, input().split()))
  avg = sum(n_score_list[1:]) / n_score_list[0]
  above = 0
  for i in n_score_list[1:]:
    if(i > avg):
      above += 1
    result = above / n_score_list[0]* 100
  print(f"{result:.3f}%") # 소수 셋째자리까지 출력하는 방법