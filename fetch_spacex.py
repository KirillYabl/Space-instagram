import requests
import os

from load_image import load_image


def fetch_spacex_some_launch(directory, launch_num):
    """Fetch pictures from some SpaceX launch.

    Params
    --------------------------------------------
    :param directory: str
      Name of directory for pictures.
    :param launch_num: int or str
      Number of launch.
    --------------------------------------------
    """

    url = f'https://api.spacexdata.com/v3/launches/{launch_num}'

    response = requests.get(url)
    images_urls = response.json()['links']['flickr_images']

    if not os.path.exists(directory):
        os.makedirs(directory)

    for num_jpg, image_url in enumerate(images_urls):
        path = f'{directory}/spacex_{launch_num}_{num_jpg}.jpg'
        load_image(image_url, path)


if __name__ == '__main__':
    directory = 'images'
    launch_num = 45

    fetch_spacex_some_launch(directory, launch_num)
