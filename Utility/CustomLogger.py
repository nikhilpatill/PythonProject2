import logging
import os

class LogGenerator:
    @staticmethod
    def loggen():
        # Ensure the 'logs' directory exists
        log_folder = os.path.join(os.getcwd(), "logs")
        if not os.path.exists(log_folder):
            os.makedirs(log_folder)

        log_file = os.path.join(log_folder, "automation.log")

        # Remove existing handlers to reconfigure (important for reusable loggers)
        for handler in logging.root.handlers[:]:
            logging.root.removeHandler(handler)

        # Configure logging
        logging.basicConfig(
            filename=log_file,
            format='%(asctime)s: %(levelname)s: %(message)s',
            datefmt='%m/%d/%Y %I:%M:%S %p',
            level=logging.INFO
        )

        logger = logging.getLogger()
        return logger
