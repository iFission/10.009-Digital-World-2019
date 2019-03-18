def sum_list(ls):
    sum = 0
    for n in ls:
        sum += n
    return sum


def find_average(lst):
    list_avg = []
    running_sum = 0
    running_numbers_tally = 0
    list_inner_avg = []
    for list_inner in lst:
        # print(list_inner)
        if len(list_inner) == 0:
            list_inner_avg.append(0.0)
        else:
            running_numbers_tally += len(list_inner)
            temp = sum_list(list_inner) / len(list_inner)
            running_sum += sum_list(list_inner)
            # print(type(temp))
            list_inner_avg.append(temp)
    list_avg.append(list_inner_avg)
    # print(running_sum, running_numbers_tally)
    list_avg.append(running_sum / running_numbers_tally)
    average = running_sum / running_numbers_tally
    return list_inner_avg, average


find_average([[13.13, 1.1, 1.1], [], [1, 1, 0.67]])