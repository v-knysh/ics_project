# EatCat

>У даній роботі розроблено програму – систему контролю харчування кота.
Створена програма дозволяє слідкувати за правильним харчуванням
домашнього улюбленця, збалансовано та вчасно його годувати.

## Build Setup for frontend

``` bash
# install dependencies
cd frontend
npm install

# serve with hot reload at localhost:8080
npm run dev

# build for production with minification
npm run build
```
## Build Setup for backend

``` bash
# install virtualenv
virtualenv -p python3 venv
source venv/bin/active

# install dependencies
pip install -r requirements.txt

# install db
python manage.py migrate
python manage.py createsuperuser

# start serve localhost:8000
python manage.py migrate
```

## run docker
```
docker build -t app .
cd frontend
docker build -t frontend .
docker run -p 8000:8000 app
docker run -it -p 8080:8080 frontend
```