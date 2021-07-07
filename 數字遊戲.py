import random
ans=random.randint(1,20)

x=input("讓我們來玩一場猜數字遊戲!")
y=input("請開始猜。")



Guess=input("猜吧!")
Guess=int(Guess)






if Guess==ans:
    print("猜對了!")
    input("要不要繼續玩?")
    input("猜吧!")
elif Guess<ans:
    print("太小了!")
    input("猜吧!")
else:
    print("太大了!")
    input("猜吧!")












