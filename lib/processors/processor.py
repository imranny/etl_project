from datetime import datetime
from

class Processor:
    """Класс процессор для обработки данных и 
        преобразования числа в нужный формат
    """
    @staticmethod
    def convertion_to_number_date(number: str) -> str:
        """ основной метод который использует strftime и текущее время
            возвращает число_текущее время
        """
        operation = datetime.now().strftime("%d-%m-%Y")
        return f"{number}_{ONE}_{operation}"
