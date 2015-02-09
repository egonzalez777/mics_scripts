# Hello World program in Python
from time import time


def parse(word):
    if word:
        for letter in word:
            if letter == '':
                return ''
            elif is_in_first_bucket(letter):
                return word[1:]  # If remainder, then it is invalid
            elif letter == 'Z':
                return parse(word[1:])
            elif is_in_second_bucket(letter):
                remains = parse(word[1:])
                return parse(remains)
            elif letter in str(range(9)):
                num = 0
                nlist = []
                count = 0

                # Retrieve the true count number
                for (i, k) in enumerate(word):
                    prev_int = str(word[i-1]).isdigit() or None
                    if str(k).isdigit() and prev_int\
                        or str(k).isdigit() and count == 0:
                        nlist.append(k)
                        count += 1

                # Get the word after the valid integer
                word = word[len(nlist):]
                num = int(''.join(nlist))
                for x in xrange(num):
                    word = parse(word)

                return word

            else:
                return 'INVALID'
    else:
        return 'INVALID'


def is_in_first_bucket(letter):
    return letter in ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j')


def is_in_second_bucket(letter):
    return letter in ('M', 'K', 'P', 'Q')


words = 'Qa KZfa ZMcc MZca KKfa 2aaa 3aaa 20aaaaaaaaaabbbbbbbbbb 10aaaa 3a2a K2aaa'


def is_word(word):
    parsed = parse(word)
    if parsed == '':
        return (word, 'VALID')
    else:
        return (word, 'INVALID')
start = time()
for word in words.split(' '):
    print is_word(word)
end = time() - start

print 'End time: %s' % (end)
