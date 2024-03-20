new_list = []


def element_occurence(numbers):
    count = 0
    for index in numbers:
        for index1 in numbers:
            if index == index1:
                new_list.append(index)
                count += 1

    return f'{count},{new_list}'
