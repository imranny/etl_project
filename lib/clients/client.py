import os
import pandas as pd
import psycopg2
from sqlalchemy import create_engine
from typing import Optional
from logg import LoggInfo


class DbClient:
    def __init__(self):
        logg = LoggInfo()
        self.db_params = {
            "dbname": logg.POSTGRES_DB,
            "user": logg.POSTGRES_USER,
            "password": logg.POSTGRES_PASSWORD,
            "host": logg.POSTGRES_HOST,
            "port": logg.POSTGRES_PORT
        }
        self.engine = create_engine(
            f"postgresql+psycopg2://{self.db_params['user']}:{self.db_params['password']}@"
            f"{self.db_params['host']}:{self.db_params['port']}/{self.db_params['dbname']}"
        )

    def get_data(self, table_name: str) -> Optional[pd.DataFrame]:
        try:
            with self.engine.connect() as conn:
                return pd.read_sql_table(table_name, conn)
        except Exception as e:
            print(f"Ошибка при чтении данных: {str(e)}")
            return None

    def put_data(self, table_name: str, data: pd.DataFrame) -> bool:
        if not isinstance(data, pd.DataFrame) or data.empty:
            return False
        try:
            with self.engine.begin() as conn:
                data.to_sql(
                    name=table_name,
                    con=conn,
                    if_exists='replace',
                    index=False
                )
            return True
        except Exception as e:
            print(f"Ошибка при записи данных: {str(e)}")
            return False
