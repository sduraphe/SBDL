class Log4J2:
    def __init__(self, spark):
        log4j2 = spark._jvm.org.apache.logging.log4j
        self.logger = log4j2.LogManager.getLogger("sbdl")

    def warn(self, message):
        self.logger.warn(message)

    def info(self, message):
        self.logger.info(message)

    def error(self, message):
        self.logger.error(message)

    def debug(self, message):
        self.logger.debug(message)
