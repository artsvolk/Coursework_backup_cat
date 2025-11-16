import logging
import time
from settings import get_token
from backup_manager import BackupManager
from metadata_manager import MetadataManager


def setup_logging():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        handlers=[
            logging.FileHandler("backup.log", encoding="utf-8"),
            logging.StreamHandler()
        ]
    )


def main():
    setup_logging()
    logger = logging.getLogger(__name__)

    try:
        text = "pd-fpy-136"
        group_name = "pd-fpy-136"

        try:
            token = get_token()
        except:
            token = "y0__xDMk-GcAhjblgMg87qWlhUw3MDi6wdXmbwzxYCrtgtFZVsvv48xhm4ehg"

        backup_manager = BackupManager(group_name)
        metadata = backup_manager.backup_cat_image(text, token)

        metadata_manager = MetadataManager()
        metadata_manager.save_metadata(metadata)

        print("\n" + "=" * 50)
        print("РЕЗЕРВНОЕ КОПИРОВАНИЕ ЗАВЕРШЕНО УСПЕШНО")
        print("=" * 50)
        print(f"Файл '{text}' загружен в папку '{group_name}' на Яндекс.Диске")
        print(f"Размер файла: {metadata['file_size']} байт")
        print(f"Путь на диске: {metadata['disk_path']}")
        print(f"Метаданные сохранены в файл: metadata_{time.strftime('%Y%m%d_%H%M%S')}.json")
        print("=" * 50)

    except Exception as e:
        print("\n" + "=" * 50)
        print("ОШИБКА: Не удалось выполнить резервное копирование")
        print(f"Подробности: {str(e)}")
        raise SystemExit(1)


if __name__ == "__main__":
    main()