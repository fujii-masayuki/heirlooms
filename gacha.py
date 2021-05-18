import random
# import collections
# import matplotlib.pyplot as plt
list = []
def gacha():
    count = 0
    set_gacha = set()
    for i in range(1,1001):
        while len(set_gacha) < 4:
            random_gacha = random.randint(1,100)
            if random_gacha <= 70:
                set_gacha.add('normal')
            elif  70 < random_gacha   and random_gacha <= 90:
                set_gacha.add('rare')
            elif  90 < random_gacha   and random_gacha <= 98: 
                set_gacha.add('SR')
            else:
                set_gacha.add('SSR')   
            count = count + 1 
    return(count)
            
for j in range(1,1001):
    list.append(gacha())
print('average:',sum(list)/len(list),' min:',min(list),' max:',max(list))
# plt.hist(list,60)
# plt.xlim(0,100)
# plt.show()       
  







        

