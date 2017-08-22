from random import randint
a=1
nl=sum(1 for line in open('levi.txt'))
while a:
    wl=randint(0,nl-1)
    with open('levi.txt') as f:
        l=f.readlines()
        if l[wl][0]=='0':
            vn=l[wl][0:7].split(':')
            sr=l[wl][8:-1].replace('\r','')
            for i in range(1,10):
                if l[wl+i][0]<>'0':
                    sr+=' '+l[wl+i][8:-1].replace('\r','')
                else:
                    a=0
                    break
print('Mt %d:%d - %s'%(int(vn[0]),int(vn[1]),sr))
