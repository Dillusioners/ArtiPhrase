word1 = input("Enter a word: ")
article = input("Enter an article: ")

word = word1.lower().split()

def getValue(word, article):
    if article == 'a' and article == 'an' and article == 'the':
        if word[0] in 'aeiou' and article == 'an':
            print(f'{article} {word}')
            print("This is correct")

        elif word[0] in 'aeiou' and article == 'a':
            print(f'{article} {word}')
            print("This is wrong")

        elif word[0] not in 'aeiou' and article == 'an':
            print(f'{article} {word}')
            print("This is wrong")

        elif word[0] not in 'aeiou' and article == 'a':
            print(f'{article} {word}')
            print("This is correct")

        elif article == 'the':
            print(f'{article} {word}')
            print("'The' is always correct with any word.")

        else:
            print("Invalid input")

print('Here is your result:')
getValue(word, article)