def multiply(a, b):
    return a * b
print(multiply(12, 4))

print()
def bruce_eckel_quote():
    print("Python is executalbe pseudocode.")

bruce_eckel_quote()
print(bruce_eckel_quote())

print()
def cite(author, quote):
    print(f'{author} said: "{quote}"')

cite('Bruce Eckel', 'Python is executalbe pseudocode.')

print()

def squared_number(num):
    return num * num # num**2
print(squared_number(3))
print()
def multiples_of_three():
    divisor = 1
    for dividend in range(3, 31, 3):
        print(f'{dividend} / {divisor} = 3')
        divisor += 1
multiples_of_three()
print()
def compare_by_length(a, b):
    if len(a) < len(b):
        print('-1')
    elif len(a) > len(b):
        print('1')
    else:
        print('0')

compare_by_length('patience', 'perseverance')
compare_by_length('strength', 'dignity')
compare_by_length('humor', 'grace')
print()
print('Captain Ruby'.replace('Ruby', 'Python'))
print('Captain Ruby'[0:8]) #stoping at index 8
print('Captain Ruby'[:8] + 'Python')
print('Captain Ruby'.split(' '))
print('Captain Ruby'.split(' ')[1])
print('Captain Ruby'.split(' ')[0] + ' Python')
print()
print('ISO 639-1 language code')
def greet(language_code):
    match language_code:
        case 'en':          # English
            return 'Hi!'
        case 'fr':          # French
            return 'Salut!'
        case 'pt':          # Portuguese
            return 'Olá!'
        case 'de':          # German
            return 'Hallo!'
        case 'sv':          # Swedish
            return 'Hej!'
        case 'af':          # Afrikaans
            return 'Haai!'
print(greet('de'))
print()
def extract_language(locale):
    return locale.split('_')[0]
print(extract_language('en_US.UTF-8'))
print(extract_language('en_GB.UTF-8'))
print(extract_language('ko_KR.UTF-16'))
print()
def extract_region(locale):
    return locale.split('.')[0].split('_')[1]
print(extract_region('en_US.UTF-8'))
print(extract_region('en_GB.UTF-8'))
print(extract_region('ko_KR.UTF-16'))
print()
def local_greet(locale):
    language = extract_language(locale)
    region = extract_region(locale)

    match (language, region):
        case ('en', 'US'):
            return 'Hey!'
        case ('en', 'GB'):
            return 'Hello!'
        case ('er', 'AU'):
            return 'Howdy!'
        case _:
            return greet(language)

print(local_greet('en_US.UTF-8'))       
print(local_greet('en_GB.UTF-8')) 
print(local_greet('en_AU.UTF-8')) 
print()
print(local_greet('fr_FR.UTF-8'))  
print(local_greet('fr_CA.UTF-8'))  
print(local_greet('fr_MA.UTF-8')) 