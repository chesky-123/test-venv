import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
format1 = logging.Formatter("%(asctime)s | %(levelname)s" \
                    " | %(message)s")


filehandler = logging.FileHandler("system.log")
filehandler.setFormatter(format1)
logger.addHandler(filehandler)

streamhendler = logging.StreamHandler()
streamhendler.setFormatter(format1)
logger.addHandler(streamhendler)
# logger.info("testing")
