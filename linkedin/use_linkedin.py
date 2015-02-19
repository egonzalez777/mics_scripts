import configparser
import sys

from linkedin import LinkedinAPI

# Load configuration
config = configparser.ConfigParser()
config.read_file(open('config.ini'))

# These items are passed on by the client that uses this library.
CONSUMER_KEY = config.get('linkedin', 'consumer_key')
CONSUMER_SECRET = config.get('linkedin', 'consumer_secret')
redirect_url = config.get('linkedin', 'redirect_url')


def main(args):

    linkedin = LinkedinAPI(CONSUMER_KEY, CONSUMER_SECRET, redirect_url)
    linkedin.get_access_token(str(args[1]), redirect_url)


if __name__ == '__main__':
    main(sys.argv)
