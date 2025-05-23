<<<<<<< HEAD
from ..clients.client import DbClient
from ..processors.processor import Processor
=======
from lib.clients.client import DbClient
from lib.processors.processor import Processor
>>>>>>> branch_7

class Worker:
    """ Класс воркер для выполнения программы :
    """

    def __init__(self):
        self.client = DbClient()
        self.processor = Processor()

    def run(self, path: str) -> bool:
<<<<<<< HEAD
        print('worker hello')
=======
>>>>>>> branch_7
        try:
            data = self.client.get_data(path)
            processed_data = self.processor.process(data)
            return self.client.put_data(path, processed_data)

        except Exception as e:
<<<<<<< HEAD
            print(f"Worker error: {e}")
            return False
=======
            return False
>>>>>>> branch_7
