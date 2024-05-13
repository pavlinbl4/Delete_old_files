import os
import sys
import time
from datetime import datetime, timedelta
from loguru import logger

# Получаем путь к директории скрипта
script_dir = os.path.dirname(os.path.abspath(sys.argv[0]))
log_file_path = os.path.join(script_dir, "deleted_from_downloads_files.log")

logger.add(log_file_path, format="{time} {level} {message}", level="INFO")


def delete_old_files(directory, extensions, days):
    logger.info("Check old files in folder")
    """
    Удаляет файлы с указанными расширениями в заданной директории,
    если они были созданы или изменены раньше, чем указанное число дней от текущей даты.

    Args:
        directory (str): Путь к директории.
        extensions (list): Список расширений файлов для удаления (например, ['.tmp', '.log']).
        days (int): Количество дней, после которых файлы будут удалены.
    """
    cutoff_date = datetime.now() - timedelta(days=days)
    count = 0
    for ext in extensions:
        files = [os.path.join(directory, f) for f in os.listdir(directory) if f.endswith(ext.lower())]
        for file in files:
            modified_date = datetime.fromtimestamp(os.path.getmtime(file))
            if modified_date < cutoff_date:
                if os.path.isfile(file):
                    os.remove(file)
                    logger.info(f"Удален файл: {file}")
                    count += 1

        time.sleep(1)  # Задержка в 1 секунду для визуализации
    logger.info(f"{count} files were deleted")


if __name__ == '__main__':
    delete_old_files('/Volumes/big4photo/Downloads', [
        'pdf',
        'xlsx',
        'doc',
        'docx',
        'bz2',
        'txt',
        'png',
        'jpg',
        'jpeg',
        'PDF',
        'docx',
        'JPG'
    ], 1)
