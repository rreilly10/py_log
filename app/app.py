import logging


class Main:
    def __init__(self):
        self.logger = logging.getLogger('app.' + self.__class__.__name__)
        self.logger.info('creating an instance of ' + self.__class__.__name__)

    def do_something(self):
        self.logger.info('doing something')
        a = 1 + 1
        self.logger.info('done doing something %d' % a)


class Other:
    def __init__(self):
        self.logger = logging.getLogger('app.' + self.__class__.__name__)
        self.logger.info('creating an instance of ' + self.__class__.__name__ )

    def do_something(self):
        self.logger.info('doing something')
        a = 1 + 1
        self.logger.info('done doing something %d' % a)
