import os
import argparse

import instabot
import dotenv

from fetch_spacex import fetch_spacex_some_launch
from fetch_hubble import fetch_hubble_imgs_from_collection

if __name__ == '__main__':

    doc = '''
      The program allow load images of space from SpaceX by launch and from Hubble by collection.
      Also you can upload pictures to Instagram account.
      Usage: python space_insta.py dir insta_post [launch_num] [collection_name]
      '''

    dotenv.load_dotenv()
    instalogin = os.getenv('INSTALOGIN')
    instapassword = os.getenv('INSTAPASSWORD')

    # initialize parser
    parser = argparse.ArgumentParser(description=doc, formatter_class=argparse.RawTextHelpFormatter)
    # positional args
    parser.add_argument('dir', help='Directory, where you can save images. Directory will be created if not exists')
    parser.add_argument('insta_post', action='store_true', help='Post images to instagram? True or False')
    # optional args
    parser.add_argument('--launch_num', help='SpaceX number of launch. If none images don''t be loaded from SpaceX')
    parser.add_argument('--collection_name', help='Hubble collection name. If none images don''t be loaded from Hubble')
    args = parser.parse_args()

    os.makedirs(args.directory, exist_ok=True)

    if args.launch_num is not None:
        fetch_spacex_some_launch(args.directory, args.launch_num)

    if args.collection_name is not None:
        fetch_hubble_imgs_from_collection(args.directory, args.collection_name)

    if args.insta_post:
        bot = instabot.Bot()
        bot.login(username=instalogin, password=instapassword)

        my_images = os.listdir(args.directory)
        for img in my_images:
            path = f'{args.directory}/{img}'
            caption = img.split('.')[0]
            bot.upload_photo(photo=path, caption=caption)
        bot.logout()
