import logging

class Logit:
    def __init__ (self, logger:logging.Logger):
        self.logger = logger

    def log(self,loginMessage):
        self.logger.info(loginMessage)

def loginFunction(logLevel: int = logging.INFO):
    logging.basicConfig(level=logLevel)

def main():
    loginFunction()
    logger = logging.getLogger("dummy")
    log_it = Logit(logger)
    log_it.log("dummy message")

if __name__ == "__main__":
    main()