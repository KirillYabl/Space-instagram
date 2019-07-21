import os

import instabot
import dotenv

from fetch_spacex import fetch_spacex_some_launch
from fetch_hubble import fetch_hubble_imgs_from_collection

if __name__ == '__main__':
    dotenv.load_dotenv()
    instalogin = os.getenv('INSTALOGIN')
    instapassword = os.getenv('INSTAPASSWORD')

    # example start params
    directory = 'images'
    launch_num = 38
    collection_name = 'hubble_favorites_gallery'
    need_spacex_images = True  # true if you need spacex images
    need_hubble_images = True  # true if you need hubble images
    need_instagram_posting = True  # true if you need posting images to instagram

    if need_spacex_images:
        fetch_spacex_some_launch(directory, launch_num)

    if need_hubble_images:
        fetch_hubble_imgs_from_collection(directory, collection_name)

    if need_instagram_posting:
        bot = instabot.Bot()
        bot.login(username=instalogin, password=instapassword)

        my_images = os.listdir(directory)
        for img in my_images:
            path = f'{directory}/{img}'
            caption = img.split('.')[0]
            bot.upload_photo(photo=path, caption=caption)
        bot.logout()
