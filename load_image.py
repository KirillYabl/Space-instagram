import requests


def load_image(url, path):
    """Load image by url to file.

    Params
    --------------------------------------------
    :param url: str
      Url with image.
    :param path: str
      Path, where image will be saved.
    --------------------------------------------
    """
    response = requests.get(url)
    with open(path, 'wb') as f:
        f.write(response.content)
