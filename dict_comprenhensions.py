from ast import Import
import math
from multiprocessing.sharedctypes import Value


def run():

    # my_dict = {}
    
    # for i in range(1, 101):
    #     if i % 3 != 0: 
    #         my_dict[i] = i**3
    
    # my_dict = {i: i**3 for i in range(0, 101) if i % 3 != 0}
    
    # print(my_dict)
    
    my_dict = {i: round(math.sqrt(i), 2) for i in range(1, 100)}
    
    print(my_dict)
    
if __name__ == '__main__':
    run()