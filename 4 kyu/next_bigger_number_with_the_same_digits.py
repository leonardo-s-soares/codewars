'''
Create a function that takes a positive integer and returns the next bigger number that can be formed by rearranging its digits. For example:

  12 ==> 21
 513 ==> 531
2017 ==> 2071

If the digits can't be rearranged to form a bigger number, return -1 (or nil in Swift, None in Rust):

  9 ==> -1
111 ==> -1
531 ==> -1


'''

def next_bigger(n):
    n_list = [
        int(num) for num in str(n)
    ]
    smaller_num, smaller_num_index = smaller_than_the_previous(n_list) 
    smallest_right_num, smallest_right_num_index = smallest_digit_on_right(
                                                    n_list, smaller_num_index)
    
    n_list[smallest_right_num_index] = smaller_num
    n_list[smaller_num_index] = smallest_right_num
    
    n_list_sorted = n_list[:smaller_num_index +1]
    for num in sorted(n_list[smaller_num_index +1:]):
        n_list_sorted.append(num)
    
    output = int(''.join(str(num) for num in n_list_sorted))
    if output <= n:
        output = -1
    return output
    
def smaller_than_the_previous(lst):
    for index in reversed(range(len(lst))):
        if lst[index -1] < lst[index]:
            smaller_num_index = index - 1
            smaller_num = lst[smaller_num_index]
            break
        else:
            smaller_num = min(lst)
            smaller_num_index = lst.index(smaller_num)
    return smaller_num, smaller_num_index
    
def smallest_digit_on_right(lst, smaller_num_index):
    number_index = 0
    number = 0
    for index in range(smaller_num_index, len(lst)):
        if lst[index] > lst[smaller_num_index] and min(lst[index:]) <= lst[index]:
            number_index = index
            number = lst[number_index]
    return number, number_index
    
