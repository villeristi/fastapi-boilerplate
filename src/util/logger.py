import sys
import logging

from src.config import settings

console = logging.StreamHandler(stream=sys.stdout)
console.setFormatter(
    logging.Formatter("[{asctime} {levelname}/{name} - {filename} line {lineno}] {message}", style="{")
)

logger = logging.getLogger("application")
logger.propagate = False
logger.addHandler(console)
logger.setLevel(settings.log_level)
