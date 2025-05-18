from datetime import datetime
import pandas as pd
from lib.constants.constants import ONE, COLUMN_NAME

class Processor:
    """ Класс процессор для обработки данных и
        преобразования числа в нужный формат
    """

    def process(self, data: pd.DataFrame) -> pd.DataFrame:
        """
        Обрабатывает DataFrame, добавляя новый столбец с преобразованными данными
        """
        processed_data =[]
        for index, row in data.iterrows():
            number = row[COLUMN_NAME]
            result = self.convertion_to_number_date(number)
            processed_data.append(result)

        return pd.DataFrame({COLUMN_NAME: processed_data})


    @staticmethod
    def convertion_to_number_date(number: str) -> str:
        """ основной метод который использует strftime и текущее время
            возвращает число_текущее время
        """
        operation = datetime.now().strftime("%d-%m-%Y")
        return f"{number}_{ONE}_{operation}"



