import logging
import sys

logging.basicConfig(level=logging.DEBUG)
sys.modules[__name__] = logging.getLogger(__name__)
