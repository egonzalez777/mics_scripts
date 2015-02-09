# -*-encoding: utf-8
import sys


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
       """

    word_list = []
    valid_lowercase_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
    valid_upper_letters = ['M', 'K', 'P', 'Q']
    results = []

    def __init__(self, message):
        """Sets up word_list and results list."""

        self.word_list = message.split(' ')

        # Generate word to be checked.
        for word in self.generate_word():
            self.results.append((word, self.is_valid_word(word)))

    def generate_word(self):
        """ Generate the word to be validated. """

        for word in self.word_list:
            yield word

    def is_valid_word(self, word):
        """Check to see if the provided word is infact valid."""

        is_valid = self.parse_word(word)

        if is_valid == '':
            return 'VALID'
        else:
            return 'INVALID'

    def parse_word(self, word):
        """ Check to see if the word fits the ruleset that makes it a valid
            word
            1. Every lower-case character in isolation is a valid message,
               e.g., 'a' is a valid message.
            2. If σ is a valid message then so is Zσ.
            3. If σ and τ are valid messages then so are Mστ, Kστ, Pστ, and Qστ.
        """
        # Check if word is none empty.
        if word:
            # Check each letter in the word provided.
            for letter in word:
                if letter == '':
                    return True
                elif self.is_valid_letter(letter):
                    # If remainder is not '', then it is invalid.
                    return word[1:]
                elif letter == 'Z':
                    return self.parse_word(word[1:])
                elif self.is_letter_upper(letter):
                    remains = self.parse_word(word[1:])
                    return self.parse_word(remains)
                else:
                    return 'INVALID'
        else:
            return 'INVALID'  # Return INVALID str to be consistent.

    def is_valid_letter(self, letter):
        """Check if letter is in 1st bucket (valid_lowercase_letters)."""

        return letter in self.valid_lowercase_letters

    def is_letter_upper(self, letter):
        """Check if letter is in 2nd bucket (valid_upper_letters)."""

        return letter in self.valid_upper_letters


def main():
    """Entry point to ParseMessage class"""

    if len(sys.argv) == 2:
        message = sys.argv[1]
    else:
        message = ('Qa Zj MZca Khfa KZfa KZf KMZa Zb Qa Zj MZca Khfa KZfa KZf '
                   'KMZa Qa Zj MZca Khfa KZfa KZf KMZa Zb Qa Zj MZca Khfa KZfa '
                   'KZf KMZa Zb')
    parse_message = ParseMessage(message)

    for (k, v) in parse_message.results:
        print k, v


if __name__ == '__main__':
    main()
