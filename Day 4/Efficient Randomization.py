import numpy as np
import math as math
i=1
num_list = [i for i in range(10001)]

length_of_list = len(num_list)
for j in range(0,int( length_of_list / 2)):
    print(length_of_list/2)
    randomly_selected = np.random.random_integers(0, int(length_of_list/2))
    print(randomly_selected)
    temp=num_list[randomly_selected]
    num_list[randomly_selected] = num_list[length_of_list-j-1]
    num_list[len(num_list) - j-1]= temp


print(num_list)