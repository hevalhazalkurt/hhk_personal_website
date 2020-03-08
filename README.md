# Personal Webpage

My personal webpage project powered by Django (wip)


------

## Requirements

* `virtualenv`
* `django`
* `psycopg2-binary`
* `dotenv`
* PostgreSQL


<br>

-------
-------

### Install and run `virtualenv`

To run this project on your computer, first you need to create a virtual environment. If you don't have `virtualenv` pack in your computer use this command in your terminal :

```
pip3 install virtualenv
```

After install complete, go to the folder where the project will run and create a virtual environment with this command (our environment name is `myvenv` but you can choose anything) :

```
virtualenv myvenv
```

Run your virtual environment :

```
source myvenv/bin/activate
```

<br>

--------

<br>

### Setup your virtual environment

Install Django

```
pip install django
```

We use PostgreSQL in our project so we need to install `psycopg2-binary`

```
pip install psycopg2-binary
```

<br>

----------

<br>

### Create Django project

Now it's time to create a Django project. My project name is `hhk_web` you can choose anything you want.  

```
django-admin startproject hhk_web
```


Go to your project's settings file, the directory will be like `hhk_web/hhk_web/settings.py`, find the `SECRET_KEY` section and copy the key. The key should look something like this :

```
SECRET_KEY = "r76vmd5j1dw5weuhd22&h(#lif!_^pr68h39djiej(yi8_747j8@5%"
```

<br>

----

<br>

### Install and setup your `dotenv` settings

Install `dotenv`

```
pip install -U python-dotenv
```

In your terminal go to the folder where your project's settings file (for example : `hhk_web/hhk_web/settings.py`) in and run this command :

```
touch .env
```

Open your `.env` file in your IDE and add your settings like below :

```
DJANGO_SECRET_KEY="r76vmd5j1dw5weuhd22&h(#lif!_^pr68h39djiej(yi8_747j8@5%"
```
