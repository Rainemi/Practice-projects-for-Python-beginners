

#you create a function that takes a list and taget parameter (lets say the elements of the list)
#create multiple variables e.g middle, start, end, steps
#you can use recursion or while loop to iterate through the list
#increase the step each time a split is done
#condition to track the target position


def binary_search(list,element):
    middle = 0
    start = 0
    end = len(list)
    steps = 0

    while (start<=end):
        search = "Steps", steps, ":", str(list[ start: end +1])
        print(search) 

        steps = steps + 1
        middle = (start + end) // 2
        if element == list[middle]:
            return middle 
        elif element < list[middle]:
            end = middle - 1
        else:
            start = middle + 1

    return -1

my_list = list(input("Enter your list : "))
element = input("Enter the element you want to search for : ")

binary_search(my_list,element)

