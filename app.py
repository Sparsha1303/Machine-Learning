from flask import Flask
from housing.logger import logging
from housing.exception import HousingException
import sys
app = Flask(__name__)


@app.route('/',methods=['GET','POST'])
def index():
    try:
        raise Exception("This is a test exception")
    except Exception as e:
        housing_exception = HousingException(e, sys)
        logging.info(housing_exception.error_message)
        logging.info("Testing the logging functionality in the index route")
    return "Starting a Machine Learning Project with Flask"

if __name__ == '__main__':
    app.run(debug=True)