phrase = input("Enter your phrase ..Please Use Spaces")
words = phrase.split()
phrase_list = words
n = 0
error_count = 0
result = " "
for n in range(len(phrase_list)):
    if phrase_list[n] == "an":
        result = phrase_list[n+1]
        if result[0] != 'a' or result[0] != 'e' or result[0] != 'i' or result[0] != 'o' or result[0] != 'u':
            error_count += 1
    elif phrase_list[n] == "a":
        result = phrase_list[n+1]
        if result[0] == 'a' or result[0] == 'e' or result[0] == 'i' or result[0] == 'o' or result[0] == 'u':
            error_count += 1

if error_count == 0:
    print("No errors in your phrase")
else:
    print("Go learn grammar stupid!!")



