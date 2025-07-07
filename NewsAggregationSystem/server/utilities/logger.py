import logging
import sys
import os

class Logger:
    def __init__(self, name=__name__):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.INFO)
        formatter = logging.Formatter('[%(asctime)s] %(levelname)s in %(module)s: %(message)s')

        # Stream handler (console)
        stream_handler = logging.StreamHandler(sys.stdout)
        stream_handler.setFormatter(formatter)
        if not any(isinstance(h, logging.StreamHandler) for h in self.logger.handlers):
            self.logger.addHandler(stream_handler)

        # File handler
        log_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../app.log')
        file_handler = logging.FileHandler(log_file_path)
        file_handler.setFormatter(formatter)
        if not any(isinstance(h, logging.FileHandler) for h in self.logger.handlers):
            self.logger.addHandler(file_handler)

        self.logger.propagate = False

    def get_logger(self):
        return self.logger

logger = Logger(__name__).get_logger() 