from datetime import datetime
import logging
import os


class Log:
    def __init__(self):
        if not os.path.exists("./_logs/"):
            os.makedirs("./_logs/")

        self.timestamp = "{:%y-%m-%d}".format(datetime.now())
        logging.getLogger("seleniumwire").setLevel(logging.CRITICAL)
        logging.getLogger("seleniumwire").propagate = False
        logging.getLogger("selenium").setLevel(logging.CRITICAL)
        logging.getLogger("selenium").propagate = False
        logging.getLogger("urllib3").setLevel(logging.CRITICAL)
        logging.getLogger("urllib3").propagate = False
        logging.getLogger("pysftp").setLevel(logging.CRITICAL)
        logging.getLogger("pysftp").propagate = False
        logging.getLogger("hpack").setLevel(logging.CRITICAL)
        logging.getLogger("hpack").propagate = False
        self.filename = f"./_logs/Execution Result {self.timestamp}.log"
        logging.basicConfig(
            encoding="UTF-8",
            filename=self.filename,
            filemode="a",
            level=logging.DEBUG,
            format="%(asctime)s; %(levelname)s; %(message)s;",
            datefmt="%Y/%m/%d %I:%M:%S",
        )
        self.logger = logging.getLogger("main")
        self.logger.raiseExceptions = False

    def exception(self, id_relatorio=None, error=None):
        if not os.path.exists(self.filename):
            with open(self.filename, "w"):
                pass

        error = f"{id_relatorio}; {error}"
        self.logger.error(error)

    def debug(self, id_relatorio=None, error=None):
        if not os.path.exists(self.filename):
            with open(self.filename, "w"):
                pass

        error = f"{id_relatorio}; {error}"
        self.logger.debug(error)
