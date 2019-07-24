# Space Instagram

These project can help you if you need load pictures from SpaceX and Hubble and post it to your superspace account!

### How to install

You need to create `.env` file and write in file your login in `INSTALOGIN` param and your password in `INSTAPASSWORD` param like:
```
INSTALOGIN=MY_LOGIN
INSTAPASSWORD=MY_PASSWORD
```

Python3 should be already installed. 
Then use `pip` (or `pip3`, if there is a conflict with Python2) to install dependencies:
```
pip install -r requirements.txt
```

### How to use

Open command line (in windows `Win+R` and write `cmd` and `Ok`). Go to directory with program or just write in cmd:

`python <PATH TO PROGRAM>\space_insta.py --dir dir --insta_post insta_post [--launch_num launch_num] [--collection_name collection_name]`

where:

	`dir` - Directory, where you can save images. Directory will be created if not exists
	
	`insta_post` - Post images to instagram? True or False
	
	`launch_num` - SpaceX number of launch. If none images don''t be loaded from SpaceX (optional)
	
	`collection_name` - Hubble collection name. If none images don''t be loaded from Hubble (optional)

For helping you can write in cmd:

`python <PATH TO PROGRAM>\space_insta.py -h`

### References

[SpaceX API](https://github.com/r-spacex/SpaceX-API).

[Hubble API](http://hubblesite.org/api/documentation).

### Project Goals

The code is written for educational purposes on online-course for web-developers [dvmn.org](https://dvmn.org/).
