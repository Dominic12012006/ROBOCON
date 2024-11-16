import sys
while True:
    data = sys.stdin.readline().strip()
    '''list=[]
    l=len(data)
    index=-1
    for i in range(0,l):
        if data[i]=='#':
            list.append(data[(index+1):i])
            index=i
        if i==l-1:
            if data[i]!='#':
                list.append(data[(index+1):l])
    '''
    list=data.split('#')
    for i in list:
        print(i)
         

