def count_numbers_and_letters(sentence1):
    counter = 0
    counter1 = 0

    for i in sentence1:
        if i.isnumeric():
            counter += 1
        if i.isalpha():
            counter1 += 1
    return f"LETTERS{counter1} Digit{counter}"


sentence = "hello world! 123"


print(count_numbers_and_letters(sentence))
