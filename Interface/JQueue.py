class JQueue():
    def __init__(self, index = 0):
        self.queue =[]

    def add(self, value):
        self.queue.append(value)

    def dequeue(self):
        hold = self.queue[0]
        self.queue.pop(0)
        return hold

    def elemenets(self):
        return self.queue

    def is_empty(self):
        if self.queue:
            return False
        else:
            return True

if __name__ == '__main__':
    q = JQueue()
    print(q.elemenets())
    q.add('jack')
    q.add('crazy')
    q.add('king')
    print(q.dequeue())
    print(q.elemenets())
    print(q.dequeue())