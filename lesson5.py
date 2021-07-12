n=int(input('How many students?'))
min=100
max=0
sum=0
for k in range(n):
    math_score=int(input('math score?'))
    sum=sum+math_score
    if math_score>max:
        max=math_score
    if math_score<min:
        min=math_score
print("avg=",sum/n)
print("max=",max)
print("min=",min)    