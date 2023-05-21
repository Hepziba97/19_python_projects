phrase = input('Input the phrase: ')
phrase = phrase.upper()

lookup = {
        'A': '4',
        'B': '8',
        'C': '(',
        'D': '|)',
        'E': '3',
        'F': '|=',
        'G': '6',
        'H': '#',
        'I': '1',
        'J': '_|',
        'K': '|<',
        'L': '|_',
        'M': '|\/|',
        'N': '|\|',
        'O': '0',
        'P': '|D',
        'Q': '(,)',
        'R': '|2',
        'S': '5',
        'T': '7',
        'U': '|_|',
        'V': '\/',
        'W': '|/\|',
        'X': '><',
        'Y': '`/',
        'Z': '2'
}

leet = ''
for char in phrase:
    leet += lookup.get(char, char)
print(leet)
