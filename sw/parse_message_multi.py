# -*-encoding: utf-8
import logging
import sys

# Set Logging basic config
logging.basicConfig()
log = logging.getLogger(__name__)


class ParseMessage(object):
    """class ParseMessage
    Parses the message provided and validates each word.

    Usage:
        message = 'Qa Zj MZca Khfa'
        parsed_message = ParseMessage(message)

        # Print out output
        for (result, is_valid) in parsed_message.results:
            print result, is_valid

    Output:
        Qa INVALID
        Zj VALID
        MZcA VALID
        Khfa INVALID
        2aaa INVALID
        3aaa VALID
    """

    # List of words retrieved from message.
    word_list = []
    # Valid set of letters from a-j.
    valid_lowercase_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
    # Valid set of upper case letters.
    valid_upper_letters = ['M', 'K', 'P', 'Q']
    # Variable that holds the word and it if is valid or not: ('Qa', 'INVALID').
    results = []

    def __init__(self, message):
        """Sets up word_list and results list.

        :param: message: str
        :return: void
        """

        # Create the list of words from passed in message.
        self.word_list = message.split(' ')

        # Generate word to be checked.
        for word in self.generate_word():
            self.results.append((word, self.is_valid_word(word)))

    def generate_word(self):
        """ Generate the word to be validated.

        :param: void
        :return: str
        """

        for word in self.word_list:
            yield word

    def is_valid_word(self, word):
        """Check to see if the provided word is infact valid.

        :param: word: str
        :return: str
        """

        is_valid = self.parse_word(word)
        if is_valid == '':
            return 'VALID'
        else:
            log.error('Method parse_word returned a remainder. Valid words '
                      'do not return remainders. Returned "%s"!' % is_valid)
            return 'INVALID'

    def parse_word(self, word):
        """ Check to see if the word fits the ruleset that makes it a valid
            word
            1. Every lower-case character in isolation is a valid message,
               e.g., 'a' is a valid message.
            2. If σ is a valid message then so is Zσ.
            3. If σ and τ are valid messages then so are Mστ, Kστ, Pστ, and Qστ.

            :param: word: str
            :return: str
        """

        # Check if word is none empty.
        if word:
            # Check each letter in the word provided.
            for letter in word:
                if letter == '':
                    return ''
                elif self.is_valid_letter(letter):
                    return word[1:]
                elif letter == 'Z':
                    return self.parse_word(word[1:])
                elif self.is_letter_upper(letter):
                    remains = self.parse_word(word[1:])
                    return self.parse_word(remains)
                elif letter in str(range(10)):
                    """An improvement on this is to check if the first
                    letter after N is the same for N amount of times."""

                    word = self._validate_multi_letter_word(word)
                    return word
                else:
                    log.error('%s is not valid' % letter)
                    return 'INVALID'
        else:
            log.error('None provided, not a valid word.')
            return 'INVALID'

    def is_valid_letter(self, letter):
        """Check if letter is in 1st bucket (valid_lowercase_letters).

        :Param: letter: str
        :Return: bool
        """

        return letter in self.valid_lowercase_letters

    def is_letter_upper(self, letter):
        """Check if letter is in 2nd bucket (valid_upper_letters).

        :param:letter: str
        :return: bool
        """

        return letter in self.valid_upper_letters

    def _validate_multi_letter_word(self, word):
        """Retrieve N and check to see if word correlates with N.

        :param: word: str
        :return: word: str
        """

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
            word = self.parse_word(word)
        return word


def main():
    """Entry point to ParseMessage class"""
    # If args are supplied, use those. Otherwise use the predefined below.
    if len(sys.argv) == 2:
        message = sys.argv[1]
    else:
        message = ('Qa Zj MZca Khfa KZfa KZf KMZa 10aaaaaaaaaa 5aabba 3cef 3ec '
                   'KMZa 2aaa 5bbca MZ5aa K2aaa 2ZaMbb')

    parse_message = ParseMessage(message)
    for (k, v) in parse_message.results:
        print k, v


if __name__ == '__main__':
    main()
