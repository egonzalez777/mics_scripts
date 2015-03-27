#bubble sort

from random import shuffle

def get_list():
    err = True
    print("Enter your numbers.\nLeave a space between each one.")
    while err==True:
        err = False
        temp = input("Data: ")
        my_list = temp.split()
        for item in my_list:
            try:
                item = float(item)
            except:
                print("Try again. Only numbers and spaces.")
                err = True
                break
    return my_list

if __name__ == '__main__':
    print("Welcome to bubble sort.")
    unsorted = get_list()
    print unsorted
