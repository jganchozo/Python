wordToFind = "python"

text = input("Enter a text to analyze: ")
letters = list(input("Enter 3 letters: "))

first, second, third = letters
words = text.split()

dictionary = {True: 'is', False: 'is not'}

lowerText = text.lower()
pythonInText = 'python' in lowerText

print('\n')
print('QUANTITY OF LETTERS')

print(f"Letter '{first}' {lowerText.count(first)} times")
print(f"Letter '{second}' {lowerText.count(second)} times")
print(f"Letter '{third}' {lowerText.count(third)} times")

print('\n')
print('QUANTITY OF WORDS')
print(f"Total words: {len(words)}")

print('\n')
print('FIRST AND LAST LETTER')
print(f"First word '{text[0]}' Last word '{text[-1]}'")

print('\n')
print('REVERSE WORDS')
words.reverse()
print(' '.join(words))

print('\n')
print('WORD PYTHON IN THE TEXT')
print(f'Word python {dictionary[pythonInText]} in the text')
