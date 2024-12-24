"""
Use Case: whenever we need a chain of events to happen and let the handler decide if wants to work on it or not.
Example: 
I think an app handling a request to order can have a CoR pattern. The flow can be
Authentication -> Authorization -> Cache Validation -> something else -> place order 
"""

# sample use case: Design logging system

from enum import IntEnum

class LogLevel(IntEnum):
    DEBUG = 1
    INFO = 2
    WARNING = 3
    ERROR = 4
    CRITICAL = 5

from abc import ABC, abstractmethod

class LoggerInterface(ABC):
    @abstractmethod
    def log(self, log_level, message):
        pass

class Logger(LoggerInterface):
    def __init__(self, next_logger):
        self.next_logger = next_logger
        self.min_log_level = LogLevel.WARNING

    def log(self, log_level, message):
        if self.next_logger:
            self.next_logger.log(log_level, message)

class DebugLogger(Logger):
    def __init__(self, next_logger):
        super().__init__(next_logger)

    def log(self, log_level, message):
        if log_level == LogLevel.DEBUG and log_level >= self.min_log_level:
            print("DEBUG : ", message)
        else:
            super().log(log_level, message)

class InfoLogger(Logger):
    def __init__(self, next_logger):
        super().__init__(next_logger)

    def log(self, log_level, message):
        if log_level == LogLevel.INFO and log_level >= self.min_log_level:
            print("INFO : ", message)
        else:
            super().log(log_level, message)

class WarningLogger(Logger):
    def __init__(self, next_logger):
        super().__init__(next_logger)

    def log(self, log_level, message):
        if log_level == LogLevel.WARNING and log_level >= self.min_log_level:
            print("WARNING : ", message)
        else:
            super().log(log_level, message)

class ErrorLogger(Logger):
    def __init__(self, next_logger):
        super().__init__(next_logger)

    def log(self, log_level, message):
        if log_level == LogLevel.ERROR and log_level >= self.min_log_level:
            print("ERROR : ", message)
        else:
            super().log(log_level, message)

class CriticalLogger(Logger):
    def __init__(self, next_logger):
        super().__init__(next_logger)

    def log(self, log_level, message):
        if log_level == LogLevel.CRITICAL and log_level >= self.min_log_level:
            print("CRITICAL : ", message)
        else:
            super().log(log_level, message)


default_logger = Logger(None)
logger = DebugLogger(InfoLogger(WarningLogger(ErrorLogger(CriticalLogger(default_logger)))))

logger.log(LogLevel.ERROR, "hello")
logger.log(LogLevel.DEBUG, "hello")
logger.log(LogLevel.CRITICAL, "hello")
logger.log(LogLevel.INFO, "hello")
logger.log(LogLevel.WARNING, "hello")
logger.log(LogLevel.INFO, "hello")
logger.log(LogLevel.ERROR, "hello")
logger.log(LogLevel.WARNING, "hello")
logger.log(LogLevel.DEBUG, "hello")
logger.log(LogLevel.CRITICAL, "hello")