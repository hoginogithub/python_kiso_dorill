from pathlib import Path

check_folder = Path('.')
python_pg_list = [file.stem for file in list(check_folder.glob('*.py'))]
print(python_pg_list)