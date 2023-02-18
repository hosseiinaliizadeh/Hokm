dicttest1={'n':1,'b':6,'c':9,'d':9}
listtest1=list(dicttest1.keys())
print(dicttest1[listtest1[1]])
print((sorted(dicttest1.values())))






listtest3=[]
listtest2=[('heart',6,2),('spade',4,1),('diamond',12,1),('club',12,2)]
listtest2.sort(key=lambda a:a[1])
print(listtest2)
for i in listtest2:
    if i[1]==(listtest2[3])[1]:
        listtest3.append(i)
print(listtest3)
(listtest3.sort(key=lambda a:a[1]))
print(listtest3[len(listtest3)-1])











