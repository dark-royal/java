def counter(sentence1):
    count = 0
    count1 = 0

    for character in sentence1:
        if character.isupper():
            count += 1
        if character.islower():
            count1 += 1

    return f"UPPER CASE{count} lower case{count1}"


sentence = "Hello world!"
print(counter(sentence))
