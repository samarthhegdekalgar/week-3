# Write a function that takes an array(or list) as input and reduces
# it into a array of item representing the same range.
#
# Note: If the input is  - (2, 3) and (5, 7) representing a range of number between 2 to 3 and 5 to 7 respectively,
# the output should be (2, 3), (5, 7) However, if the input is - (5, 7) and (4, 10) the output should be (4,
# 10) as in this case there is an overlapping range of number. Similarly for the input - (1,4), (6, 6), (6, 8), (4,
# 5). The output should be: (1, 5), (6, 8)


def find_range(list_data,result_list):
    start = list_data[0]
    end = list_data[1]
    if start not in result_list or end not in result_list:
        for value in range(start,end+1):
            result_list.append(value)
    return result_list



if __name__ == '__main__':
    range_value = list()
    result = list()
    for _ in range(int(input('Enter how many range of element set?\t'))):
        first = int(input('Enter start element:\t'))
        second = int(input('Enter end element:\t'))
        range_value.append([first, second])
    for value in range_value:
        result.append(find_range(value, result))
    result = list(set(result))
    result.sort()
    start = result[0]
    for value in range(result[0], result[len(result)]):
        if value not in result:
            print(f'[{start},{value-1}]')
            start = value+1