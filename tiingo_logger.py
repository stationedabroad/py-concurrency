import logging

logging.basicConfig(                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
        level=logging.INFO,
        filename='pylog.log',
        format='%(asctime)s: %(process)d - %(levelname)s - %(message)s',
        datefmt='%d-%b-%yy %H:%M:%S'
)

logger = logging.getLogger(__name__)