
def first_display(number):
    if number[0] == '1':
        return '& & & & &'
    if number[0] == '0':
        return '         '


def second_display(number):
    if number[3] == '1':
        return '& & & & &'
    if number[3] == '0':
        return '         '


def third_display(number):
    if number[6] == '1':
        return '& & & & &'
    if number[6] == '0':
        return '         '


def fourth_display(number):
    if number[1] == '1' and number[5] == '1':
        return '&       &'

    if number[1] == '0' and number[5] == '0':
        return '         '
    if number[1] == '1' and number[5] == '0':
        return '&        '

    if number[1] == '0' and number[5] == '1':
        return '        &'


def fifth_display(number):
    if number[2] == '1' and number[4] == '1':
        return '&       &'

    if number[2] == '0' and number[4] == '0':
        return '         '
    if number[2] == '1' and number[4] == '0':
        return '&        '
    if number[2] == '0' and number[4] == '1':
        return '        &'


def validate_user_input(user_input):
    if len(user_input) != 7:
        raise ValueError("number should have a length of seven")

    for count in user_input:
        if count != ('0', '1'):
            raise ValueError("number should be between 0 and 1")


def validate_on_and_off(number):
    if number[7] == '1':
        return True
    return False


def display(number):
    if validate_on_and_off(number):
        return (f'{first_display(number)}\n{fourth_display(number)}\n'
                f'{second_display(number)}\n{fifth_display(number)}\n' +
                f'{third_display(number)}')


def print_out(number):
    print(display(number))


print_out('00111001')
