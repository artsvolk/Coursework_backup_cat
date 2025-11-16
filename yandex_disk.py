import requests


class YandexDisk:
    API_URL = "https://cloud-api.yandex.net/v1/disk"

    def __init__(self, token):
        self.token = token
        self.headers = {"Authorization": f"OAuth {token}"}

    def create_folder(self, path):
        url = f"{self.API_URL}/resources"
        params = {"path": path}
        response = requests.put(url, headers=self.headers, params=params)
        if response.status_code in (201, 409):
            return True
        response.raise_for_status()
        return False

    def get_upload_link(self, path):
        url = f"{self.API_URL}/resources/upload"
        params = {"path": path}
        response = requests.get(url, headers=self.headers, params=params)
        response.raise_for_status()
        return response.json()["href"]

    def upload_file(self, path, file_name, file_data):
        upload_path = f"{path}/{file_name}"
        upload_url = self.get_upload_link(upload_path)
        response = requests.put(upload_url, data=file_data)
        response.raise_for_status()
        return self.get_file_info(upload_path)

    def get_file_info(self, path):
        url = f"{self.API_URL}/resources"
        params = {"path": path}
        response = requests.get(url, headers=self.headers, params=params)
        response.raise_for_status()
        return response.json()