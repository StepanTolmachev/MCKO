fin =open('songs.csv','r',encoding='utf-8')
tittle=fin.readline()
print(tittle)
songs=[x.strip().split(',')for x in fin]
fin.close()
summ={}
cnt={}
for x in songs:
    if x[4]!='None':
        if x[3]in summ:
            summ[x[3]]+=int(x[4])
            cnt[x[3]]+=1
        else:
            summ[x[3]]=int(x[4])
            cnt[x[3]]=1
        fio= x[1].split()
        