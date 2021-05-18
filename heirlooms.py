import random
# import collections
# import matplotlib.pyplot as plt
# list1 = []
list2 = []
def heirlooms():
    list1 = []
    count = 0
    #     set_gacha = set()
    for i in range(1,10001):
        while True:
            tousen = 1
            random_takara = random.randint(1,501)   
            list1.append(random_takara)
            count = count + 1
            if tousen in list1:
                break
        return(count)
# print(heirlooms())
for j in range(1,101):
    list2.append(heirlooms())
print('average:',sum(list2)/len(list2),' min:',min(list2),' max:',max(list2)) 
# plt.hist(list2,30)
# plt.show()