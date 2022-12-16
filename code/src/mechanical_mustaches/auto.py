from mechanical_mustaches.timer import Timer

"""
Archie is a super villian trying to take over tele-op
He is a slow virus that works with most of the agents
He also works in his main lair autonomous
"""

class Auto:
    def __init__(self, *, name='archie', mode='auto', loop=False):
        self.name = name
        print(f" {name} IS MY NAME")
        self.bookmark = 0
        self.book = []
        self.running = False
        self.mode = mode  # 'single_shot' or 'auto',
        self.timer = Timer()
        self.loop = loop
        self.retired = False


    def check(self):
        if retired: # was target and is now dead. Wait for garbage collector
            return
        
        returned = self.book[self.bookmark]()
        # if self.book[self.bookmark]() is False:
        if self.mode == 'auto':
            try:
                if returned is False:  # compare
                    return None  # leaving
                else:
                    self.bookmark += 1
                    self.check()
            except IndexError:
                if self.loop:
                    self.bookmark = 0
                    self.check()
                else:
                    self.running = False
                    print('finished book')
            return None
        elif self.mode == 'single_shot':  # must be single shot
            self.bookmark += 1
            if self.bookmark > len(self.book) and self.loop:
                self.bookmark = 0
            return
        

    def run(self, new_book: list[any], start=True, loop=False, **kwargs):
        self.rerired = False
        self.book = new_book
        self.bookmark = 0
        self.running = True
        self.loop = loop
        if not start:
            return
        self.check()
