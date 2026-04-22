from pathlib import Path
import shutil

SOURCE = Path('/mnt/data')
TARGET = Path(__file__).resolve().parents[1] / 'data_raw'
TARGET.mkdir(parents=True, exist_ok=True)

for csv_file in SOURCE.glob('*.csv'):
    shutil.copy2(csv_file, TARGET / csv_file.name)
    print(f'Copiado: {csv_file.name}')
