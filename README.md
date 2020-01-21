فایل های پروژه بر روی گیت هاب در دسترس است که با دستور زیر میتوان آن هارا روی سیستم مورد نظر دریافت کرد:
git clone https://github.com/milad3867/project-management.git


برای پیاده سازی نیاز است که پایتون ورژن 3.8.1 بر روی سیستم نصب شود
python 3.8.1


لیست تمام بسته های موردنیاز پروژه در فایل
requrements.txt
در فولدر اصلی پروژه قرار دارد و می توان تمام آن هارا با دستور زیر نصب کرد
pip install -r requirements.txt


در دایرکتوری
project_management\
که فایل
manage.py
در آن قرار دارد دستورات زیر را به همین ترتیب برای پیاده سازی مدل های دیتابیس اجرا کنید
python manage.py migrate
python manage.py makemigrations webSite
python manage.py migrate


برای پیاده سازی روی سرور باید آدرس یا آی پی وبسایت را به دیکشنری
ALLOWED_HOSTS
در فایل
settings.py
در دایرکتوری
project_management\project_management
اضافه کنید
مثال:
اگر آدرس
website.com
باشد آن را به صورت زیر اضافه کنید
ALLOWED_HOSTS = [website.com]


در فایل
settings.py
در دایرکتوری
project_management\project_management
متغیر
Debug
باید برابر
False
باشد


در دایرکتوری
project_management\
با دستور زیر میتوانید  کاربر ادمین ایجاد کنید
python manage.py createsuperuser
