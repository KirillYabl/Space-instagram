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

    # check HTTPError
    response.raise_for_status()
    # some sites can return 200 and write error in body
    if 'error' in response:
        raise requests.exceptions.HTTPError(response['error'])

    with open(path, 'wb') as f:
        f.write(response.content)
