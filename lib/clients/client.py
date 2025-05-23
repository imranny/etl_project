from pathlib import Path
import pandas as pd


class DbClient():
    def __init__(self, base_path: str = "data"):
        self.base_path = Path(base_path)
        self.processed_dir = self.base_path / "processed"
        self.raw_dir = self.base_path / "raw"

<<<<<<< HEAD
    def get_data(self, path: str) -> pd.DataFrame:
        return pd.read_csv(self.raw_dir / path)

    def put_data(self, path: str, data: pd.DataFrame) -> bool:
        file_path = self.processed_dir / path
=======
    def get_data(self, file_output_name: str) -> pd.DataFrame:
        return pd.read_csv(self.raw_dir / file_output_name)

    def put_data(self, file_input_name: str, data: pd.DataFrame) -> bool:
        file_path = self.processed_dir / file_input_name
>>>>>>> branch_7
        file_path.parent.mkdir(parents=True, exist_ok=True)

        if not data.empty:
            data.to_csv(file_path, index=False)
            return True
        return False






    
