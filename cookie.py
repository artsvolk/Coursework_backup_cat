iimport requests

def get_cat_image(text):
    url = f"https://cataas.com/cat/says/{text}"
    response = requests.get(url)
    response.raise_for_status()
    return response.content