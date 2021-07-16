k=1
mydict={'yoyo':'溜溜球','zoo':'動物園','Germany':'德國','England':'英格蘭','iPad':'平板'}
eng=mydict.keys()
chi=mydict.values()
while k!=3:
    print('**************************************************')
    print('請選擇下列功能:')
    q=int(input('1,設定.2,print單字.3,英翻中.4,中翻英.5,測驗.6,離開系統.'))
    if q==1:
        b=input('英文字')
        c=input('中文字')
        u=int(input('總字數'))
        mydict[b]=c
    if q==2:
        print(mydict)
    if q==3:
        a=str(input('輸入一個英文單字。'))
        x=a in mydict
        if x==True:
            print(mydict[a])   
        else:
            print('字彙表沒有這個字')
    if q==4:  
        i=str(input('輸入一個中文字。'))
        y=False
        for p,u in mydict.items():
            if u==i:
                print(p)
                y=True
        if y!=True:
            print('字彙表沒有這個字')
    if q==5:
        print('開始測驗。')
        for po in range(1):
            m=str(input('測驗題:''(有)',u,'(個)'))
            if m==eng[1,2,3,4,5,6]:
                print('答對了!')
            else:
                print('再加油!')
    if q==6:
        k=3



