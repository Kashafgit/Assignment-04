import random
def random_num():
    
    for i in range(10):
        num = random.randint(1,100)
        print(i + 1,num)
random_num()