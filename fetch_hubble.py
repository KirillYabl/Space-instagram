import requests
import os

from load_image import load_image


def fetch_hubble_imgs_by_id(directory, img_id, save_last=True):
    """Fetch pictures from Hubble by id.

    Params
    --------------------------------------------
    :param directory: str
      Name of directory for pictures.
    :param img_id: int or str
      Id of image.
    :param save_last: boolean
      Save only last version of picture if true.
      Last picture usually have higher resolution.
    --------------------------------------------
    """

    url = f'http://hubblesite.org/api/v3/image/{img_id}'

    # list of dicts with image url and extension
    imgs_urls_extensions = []

    response = requests.get(url)

    # check HTTPError
    response.raise_for_status()
    # some sites can return 200 and write error in body
    if 'error' in response:
        raise requests.exceptions.HTTPError(response['error'])

    hubble_images = response.json()['image_files']

    for hubble_img in hubble_images:
        img_url = hubble_img['file_url']
        # API hubble give strange url for images
        img_url = img_url.replace('//imgsrc.', 'https://').replace('/hvi', '')
        file_extension = img_url.split('.')[-1]

        img_info = {
            'url': img_url,
            'file_extension': file_extension
        }

        imgs_urls_extensions.append(img_info)

    if save_last:
        imgs_urls_extensions = [imgs_urls_extensions[-1]]

    for img_num, img_info in enumerate(imgs_urls_extensions):
        img_url = img_info['url']
        img_extension = img_info['file_extension']
        path = f'{directory}/hubble_{img_id}_{img_num}.{img_extension}'
        load_image(img_url, path)


def fetch_hubble_imgs_from_collection(directory, collection_name, save_last=True):
    """Fetch pictures from Hubble by collection name.

    Params
    --------------------------------------------
    :param directory: str
      Name of directory for pictures.
    :param collection_name: str
      Name of collection with images.
      If name unknown for API that API return empty list.
    :param save_last: boolean
      Save only last version of picture if true.
      Last picture usually have higher resolution.
    --------------------------------------------
    """

    url = f'http://hubblesite.org/api/v3/images/{collection_name}'
    response = requests.get(url)

    # check HTTPError
    response.raise_for_status()
    # some sites can return 200 and write error in body
    if 'error' in response:
        raise requests.exceptions.HTTPError(response['error'])

    collections_ids = [img_info['id'] for img_info in response.json()]
    collection_len = len(collections_ids)

    print(f'The size of collection: {collection_len} images')

    for img_num, img_id in enumerate(collections_ids):
        print(f'Starting load image number {img_num + 1} from {collection_len}')
        fetch_hubble_imgs_by_id(directory, img_id, save_last)


if __name__ == '__main__':
    directory = 'images'
    collection_name = 'hubble_favorites_gallery'

    fetch_hubble_imgs_from_collection(directory, collection_name)
