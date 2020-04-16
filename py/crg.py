import random
def quick_sort(list):
    if len(list)<=1 : return list
    pivot=list[len(list)//2]
    less_arr, equal_arr, big_arr=[],[],[]
    for i in list:
        if i<pivot : less_arr.append(i)
        elif i>pivot: big_arr.append(i)
        else: equal_arr.append(i)
    return quick_sort(less_arr) + equal_arr+ quick_sort(big_arr)

num=input('몇개의 숫자를 넣으시겠습니까?: ')
num=int(num)
all=[]
for i in range(1,num+1):
    all.append(i)
random.shuffle(all)
print('정렬 전 배열: ', all)
select=int(input())
if select==1:
    all.sort()
    print('정렬 후 배열: ',all)
elif select==2:
    for i in range(len(all)):
        for j in range(len(all)-1):
            if aljl[j]<all[j+1]:
                temp=all[j+1]
                all[j+1]=all[j]
                all[j]=temp
            else:
                pass
    print(all)
elif select==3:
    print(quick_sort(all))


elif select==4:
    print('종료')
