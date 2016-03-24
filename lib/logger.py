import logging
import datetime

class LogConfig(object):
    """
    Configures application level loggers
    """

    def __init__(self):
        """
        Initializes project wide loggers
        :return: Nones
        """

        # create logger <app_names>
        logger = logging.getLogger('app')
        logger.setLevel(logging.DEBUG)

        # create file handler for log destination
        fh = logging.FileHandler('../logs/test.log')
        fh.setLevel(logging.DEBUG)

        # create console handler with a higher log level
        ch = logging.StreamHandler()  # if no stream is passed default is stderr
        ch.setLevel(logging.ERROR)  # console level is error to stderr

        # create formatter and add it to the handlers
        formatter = logging.Formatter('%(asctime)s : %(name)s : %(levelname)s : %(message)s')
        fh.setFormatter(formatter)  # logged to files
        ch.setFormatter(formatter)  # logged to handler

        # add the handlers to the logger
        # logger <app_name> now has a console logger (error)
        # and a file logger (debug -- ie catch all)
        logger.addHandler(fh)
        logger.addHandler(ch)
