print(len("These aren't the droids you're looking for."))
 #   or
string = "These aren't the droids you're looking for."
print(f'The length of this string is {(len(string))}.')
print()
print(f'confetti floating everywhere'.upper())
string = 'confetti floating everywhere'
upper_string = string.upper()
print(upper_string)
print()
name = 'Roger'
print(name.casefold() == 'RoGeR'.casefold())
print(name == 'DAVE')
print()
rhyme = """A pirate I was meant to be!
Trim the sails and roam the sea!"""
print(rhyme)
print()
rhyme2 = "A pirate I was meant to be!\nTrim the sails and roam the sea!"
print(rhyme2)
print()
char_sequence = 'TXkgaG92ZXJjcmFmdCBpcyBmdWxsIG9mIGVlbHMu'
print('x' in char_sequence)
print()
def is_empty(s):
    return s == ''
print(is_empty('mars'))
print(is_empty('   '))
print(is_empty(''))
print()
def is_empty(s):
    return len(s) == 0
print(is_empty('mars'))
print(is_empty('   '))
print(is_empty(''))
print()
def is_empty(s):
    return not s
print(is_empty('mars'))
print(is_empty('   '))
print(is_empty(''))
print()
def is_empty_or_blank(s):
    return s.strip('  ') == ''
print(is_empty_or_blank('mars'))
print(is_empty_or_blank('   '))
print(is_empty_or_blank(''))
print()
def is_empty_or_blank(s):
    return not s.strip(' ')
print(is_empty_or_blank('mars'))
print(is_empty_or_blank('   '))
print(is_empty_or_blank(''))
print()
print(f'launch school tech & talk'.title())
print()
def capitalize_words(string):
    words = string.split(' ')
    capitalize_words = []
    for word in words:
        capitalize_words.append(word.capitalize())
    return ' '.join(capitalize_words)
string = 'launch school tech & talk'
result = capitalize_words(string)
print(result)
print()
def starts_with(string, prefix):
    return string.startswith(prefix)
print(starts_with('launch', 'la'))
print(starts_with('school', 'sah'))
print(starts_with('school', 'sch'))
print()
def count_substrings(string, substring):
    return string.count(substring)
print(count_substrings("lemon lemon lemon", "lemon"))
print(count_substrings("laLAlaLA", "la"))
print(count_substrings("launch", "uno"))

