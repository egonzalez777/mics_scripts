class FiloQueue(object):
    """Simple implementation of FILO system.

    Implementation:

        queue = FiloQueue()

        # Add items to the queue.
        queue.push('Item 1')
        queue.push('Item 2')

        # Remove last item from the queue
        last_item = queue.pop()

    """

    queue = []
    N = 0

    def push(self, item):
        self.queue.append(item)
        self.N = self.N + 1

    def is_empty(self):
        return self.N == 0

    def pop(self):
        if self.is_empty():
            return

        item = self.queue[-1]
        del self.queue[-1]
        return item
