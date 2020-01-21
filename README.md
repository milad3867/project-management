## <div dir="rtl">پروژه درس مدیریت پروژه</div>

### <div dir="rtl">وبسایت روند دفاع دانشجویان</div>
<div>

  <p dir="rtl">
  فایل های پروژه بر روی گیت هاب در دسترس است که با دستور زیر میتوان آن هارا روی سیستم مورد نظر دریافت کرد:
  </p>
  <code dir="ltr"> git clone https://github.com/milad3867/project-management.git </code>
  
  <p dir="rtl">
برای پیاده سازی نیاز است که پایتون ورژن 3.8.1 بر روی سیستم نصب شده باشد.
  </p>
  <code dir="ltr"> python 3.8.1 </code>
  
  <p dir="rtl">
لیست تمام بسته های موردنیاز پروژه در فایل <code>requrements.txt</code> در فولدر اصلی پروژه قرار دارد و می توان تمام آن‌ها را با دستور زیر نصب کرد.
  </p>
  <code dir="ltr"> pip install -r requirements.txt </code>
  
  <p dir="rtl">
  در دایرکتوری
  <code dir="ltr">project_management\</code>
که فایل
  <code>manage.py</code>
در آن قرار دارد دستورات زیر را به همین ترتیب برای پیاده سازی مدل های دیتابیس اجرا کنید.
  </p>
</div>


```
python manage.py migrate
python manage.py makemigrations webSite
python manage.py migrate
```


<div>
<p dir="rtl">
برای پیاده سازی روی سرور باید آدرس یا آی پی وبسایت را به دیکشنری
<code dir="ltr">ALLOWED_HOSTS</code>
در فایل
<code dir="ltr">settings.py</code>
در دایرکتوری
<code dir="ltr">project_management\project_management</code>
اضافه کنید.
<br>
مثال:
اگر آدرس
<code dir="ltr">website.com</code>
باشد آن را به صورت زیر اضافه کنید
<code dir="ltr">ALLOWED_HOSTS = [website.com]</code>
<br>
در فایل
<code dir="ltr">settings.py</code>
در دایرکتوری
<code dir="ltr">project_management\project_management</code>
متغیر
<code dir="ltr">Debug</code>
باید برابر
<code dir="ltr">False</code>
باشد.
</p>
<p dir="rtl">
در دایرکتوری
<code dir="ltr">project_management\</code>
با دستور زیر میتوانید  کاربر ادمین ایجاد کنید.
</p>
<code dir="ltr">python manage.py createsuperuser</code>

</div>
