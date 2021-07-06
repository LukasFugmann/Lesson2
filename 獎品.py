print("What is your english score?")
print("What is your math score?")

english=int(input())
math=float(input())

if english>=90 and math>=90:
    print("有獎品!")
elif english and math<90:
    print("糟糕，有逞罰!")
else:
    print("再加油!")