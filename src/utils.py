from datetime import datetime, timezone
from src.logger import logging
from src.exception import CustomException
import sys


def get_current_utc_datetime():
    try:
        current_utc_datetime = datetime.now(timezone.utc)
        logging.info("current date time collected successfully")
        return current_utc_datetime
    except Exception as e:
        logging.error(f"An error occurred: {e}")
        raise CustomException(e,sys)


def extract_utc_date_and_time(utc_datetime):
    try:
        utc_date = utc_datetime.strftime('%Y-%m-%d')
        utc_time = utc_datetime.strftime('%H:%M:%S')
        logging.info("UTC date and UTC time colleceted")
        return utc_date, utc_time
    except Exception as e:
        logging.error(f"An error occurred: {e}")
        raise CustomException(e,sys)