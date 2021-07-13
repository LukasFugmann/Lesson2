n=input("How many students?")
n=int(n)
score=[]
for i in range(n):
    scoren=int(input("What is your score?"))    
    score.append(scoren)
maxmum=max(score)
minmum=min(score)
summation=sum(score)
print("sum,總分:",summation)
print("avg,平均:",summation/n)
print("max,最高:",maxmum)
print("min,最低:",minmum)