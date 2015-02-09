# -*- coding: utf-8 -*-
import pprint


def parse_url(url):
    """Parse URL's query string and return as a dictionary."""

    # Split the url into a GET param list.
    q_params = url.split('?')[-1].split('&')
    collection = {}
    for item in q_params:
        """Value is a=1, we need to split one more time in order to get the
        key, value pairs of the current item."""
        items = item.split('=')

        """Check if current item has been cataloged in our collection dict.
        Ideally, all key values should be of same type. In this case, we have
        both int, float, and str as keys."""
        if items[0] not in collection:
            collection[items[0]] = items[1]
        else:
            """If we need to typecast into int, then we need to check further
            on the current value."""
            if isinstance(collection[items[0]], list):
                collection[items[0]].append(items[1])
            else:
                """A list is only created if there is more then one match for
                the current key."""
                old_val = collection.get(items[0])
                collection[items[0]] = [old_val]
                collection[items[0]].append(items[1])

    return collection


if __name__ == '__main__':

    url = ("http://www.neurotrack.com/blah/?a=1&b=2&c=hello&d=2&ad=8&f=1.05&a=7"
           "&9=4&9.01=brain&c=blank")
    pp = pprint.PrettyPrinter(indent=0)
    pp.pprint(parse_url(url))
