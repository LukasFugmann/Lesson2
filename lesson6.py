#lesson6:使用方法三來建立全班數學成績列表，找出最高分、最低分、平均分數，並列出最高分及最低分的名字。
score_name=[]
sum=0
max=0
name_max=''
name_min=''
min=100
n=int(input('How many students?'))
for z in range(n):
    name=str(input('name?'))
    print('number:',z+1,'name:',name)
    score=int(input('score?'))
    score_name.append([name,score])
print(score_name)
for j in range(n):
    score=score_name[j][1]
    name=score_name[j][0]
    sum=sum+score
    if score>max:
        max=score
        name_max=name
    if score<min:        
        min=score
        name_min=name
print("sum=",sum)
print("avg=",sum/n)
print("max=",max,name_max)
print("min=",min,name_min)