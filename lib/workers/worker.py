from lib.clients.client import DbClient
from lib.processors.processor import Processor

class Worker:
    """ Класс воркер для выполнения программы :
    """

    def __init__(self):
        self.client = DbClient()
        self.processor = Processor()

    def run(self, path: str) -> bool:
        try:
            data = self.client.get_data(path)
            processed_data = self.processor.process(data)
            return self.client.put_data(path, processed_data)

        except Exception as e:
            return False
