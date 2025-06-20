from lib.clients.client import DbClient
from lib.processors.processor import Processor

class Worker:
    """ Класс воркер для выполнения программы :
    """

    def __init__(self):
        self.client = DbClient()
        self.processor = Processor()

    def run(self, input: str, output: str) -> bool:
        try:
            data = self.client.get_data(input)
            print(f"Прочитано данных: {len(data)} строк")

            processed_data = self.processor.process(data)
            print(f"Обработано данных: {len(processed_data)} строк")


            return self.client.put_data(output, processed_data)

        except Exception as e:
            print(f"Ошибка: {str(e)}")
            return False
