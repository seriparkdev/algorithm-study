# 내가 처음 풀이한 방식
n = int(input())
score_list = list(map(int, input().split()))
# list()로 list를 만들자
max_score = max(score_list)

score = 0
sum = 0 
result = 0 # 변수 초기화해서 사용하기 

for i in score:
  sum += i / max_score * 100

result = sum / n
print(result)


# 조금 더 배열의 특성을 이용한 방식
n = int(input())
score_list = list(map(int, input().split()))
max_score = max(score_list)
newScore_list = []

for i in score_list:
  newScore_list.append(i / max_score * 100)
# sum 대신 list기에 append를 이용할 수 있다.

avg = sum(newScore_list) / n
# list는 sum을 해줄 수 있다.
print(avg)