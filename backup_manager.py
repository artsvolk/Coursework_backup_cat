from cat_api import CatAPI
from yandex_disk import YandexDisk
import time


class BackupManager:
    def __init__(self, group_name):
        self.group_name = group_name

    def backup_cat_image(self, text, token):
        try:
            cat_api = CatAPI()
            image_data = cat_api.get_image(text)

            yandex_disk = YandexDisk(token)
            yandex_disk.create_folder(self.group_name)

            # Проверка списка файлов в папке
            files = yandex_disk.get_file_info(self.group_name)
            file_count = 0

            if "embedded" in files and "items" in files["embedded"]:
                for item in files["embedded"]["items"]:
                    if item["name"].startswith(text):
                        file_count += 1

            # Формирование имени файла
            if file_count == 0:
                unique_file_name = text
            else:
                timestamp = time.strftime("%Y%m%d_%H%M%S")
                unique_file_name = f"{text}_{timestamp}"

            # Проверка существования файла с таким же именем
            try:
                yandex_disk.get_file_info(f"{self.group_name}/{unique_file_name}")
                # Добавление временной метки ,если файл существует
                timestamp = time.strftime("%Y%m%d_%H%M%S")
                unique_file_name = f"{text}_{timestamp}"
            except:
                pass

            file_info = yandex_disk.upload_file(self.group_name, unique_file_name, image_data)

            return {
                "original_name": text,
                "file_name": unique_file_name,
                "file_size": file_info["size"],
                "disk_path": file_info["path"],
                "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
            }

        except Exception as e:
            raise