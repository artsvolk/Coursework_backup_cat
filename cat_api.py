import requests
import urllib.parse


class CatAPI:
    BASE_URL = "https://cataas.com"

    def get_image(self, text="pd-fpy-136"):
        encoded_text = urllib.parse.quote(text)
        url = f"{self.BASE_URL}/cat/says/{encoded_text}?fontColor=orange&size=110"
        response = requests.get(url, timeout=30)
        response.raise_for_status()
        return response.content