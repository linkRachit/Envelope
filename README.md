# Envelope-Schedule Your Posts



## User Manual 

```console

	apt-get update
	apt-get upgrade
	apt-get install build-essential
	sudo apt-get install python
	sudo easy_install pip

	cd Desktop
	mkdir project

	sudo pip install virtualenv

	virtualenv pro

	source pro/bin/activate

```	

Clone the git repo  

```console

	git clone https://github.com/linkrachit/Envelope
	cd Envelope 
	pip install django
	pip install django-auth
	pip install twitter
	pip install pytz

```

Firstly, you need the python-dev package because Pillow needs compile headers defined.

```console

	sudo apt-get install python-dev

```

On Ubuntu 14.04 you need few extra packages to get pillow working. Install all of them with the command:

```console

	sudo apt-get install libtiff5-dev libjpeg8-dev zlib1g-dev libfreetype6-dev liblcms2-dev libwebp-dev tcl8.6-dev tk8.6-dev python-tk

```

This will work for both python 2.x and python 3.x. You might not need all of these, but at the very least you should install libjpeg8-dev and zlib1g-dev for JPEG and PNG support.

If you are using Ubuntu 12.04, use the following command.

```console

	sudo apt-get install libtiff4-dev libjpeg8-dev zlib1g-dev libfreetype6-dev liblcms2-dev libwebp-dev tcl8.5-dev tk8.5-dev python-tk

```

```console

	pip install Pillow

	sudo apt-get install sqlite3 libsqlite3-dev
	Create the db schema
	sqlite3 schema.db

	.databases
	.quit

```

Create a local.py file under the smp/smp directory to change it.

```console

	python manage.py migrate 

```
Run the dev server.  

```console

	python manage.py runserver 

```

ctrl + c 

Create an admin user  

```console
	
	python manage.py createsuperuser 

```

name 
email
password

Login to the admin page at http://localhost:8000/admin/

add site
name domain
address http://localhost:8000

http://localhost:8000/admin/socialaccount/socialapp/
 seperate for fb and twitter

Setup a crontab script that runs the following command every minute  

```console

	SHELL=/bin/bash
	* * * * * cd /home/rachit/Desktop/project/smp && source /home/rachit/Desktop/project/pro/bin/activate && python manage.py autopost | /bin/bash 

```