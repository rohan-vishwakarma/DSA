import logging
logging.basicConfig(level=logging.INFO,format='%(asctime)s - %(levelname)s - %(message)s',filename='app.log',filemode='a')

logger = logging.getLogger(__name__)

class Student:

    def __new__(cls, *args, **kwargs):
        instance = super().__new__(cls)
        print(f"creating new instance {cls.__name__}")
        return instance

    def __init__(self):
        print("initialising new object ")


n = Student()
