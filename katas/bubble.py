my_list = [0, 29, 39, 49, 5, 20, 2, 6, 7, 10]
length = len(my_list)

for i in range(length):
    for j in range(length-1):
        if my_list[j] > my_list[j+1]:
            my_list[j], my_list[j+1] = my_list[j+1], my_list[j]
            print my_list
