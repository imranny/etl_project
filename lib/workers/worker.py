from ..clients.client import DbClient
from ..processors.processor import Processor

class Worker:
    """ Класс воркер для выполнения программы :
    """

    def __init__(self):
        self.client = DbClient()
        self.processor = Processor()

    def run(self, path: str) -> bool:
        print('worker hello')
        try:
            data = self.client.get_data(path)
            processed_data = self.processor.process(data)
            return self.client.put_data(path, processed_data)

        except Exception as e:
            print(f"Worker error: {e}")
            return False