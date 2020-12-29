建个新application： news
在程序包里头找到设置文件添加上述应用
```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'polls',
    'news',
]
```
然后配置一下models数据模型
```pyhton
from django.db import models

class Reporter(models.Model):
    full_name = models.CharField(max_length=70)

    def __str__(self):
        return self.full_name

class Article(models.Model):
    pub_date = models.DateField()
    headline = models.CharField(max_length=200)
    content = models.TextField()
    reporter = models.ForeignKey(Reporter, on_delete=models.CASCADE)

    def __str__(self):
        return self.headline
```

然后对数据库进行迁移
```python
python manage.py makemigrations
python manage.py migrate
```
继续配置 news 中的 admin
```python
from django.contrib import admin

from . import models

admin.site.register(models.Article)
```
下一步： 创建superadmin 并设置密码
用户名：aijnaij 邮件地址：9795931263@qq.com
python manage.py createsuperuser
在news/admin.py中创建Repoter模型，并在news文档中建立 `urls.py` 来配置跟路由
```python
from django.urls import path

from . import views

urlpatterns = [
    path('articles/<int:year>/', views.year_archive),
    path('articles/<int:year>/<int:month>/', views.month_archive),
    path('articles/<int:year>/<int:month>/<int:pk>/', views.article_detail),
]
```
然后在news/views.py里面配置view函数
```python
from django.shortcuts import render

from .models import Article

def year_archive(request, year):
    a_list = Article.objects.filter(pub_date__year=year)
    context = {'year': year, 'article_list': a_list}
    return render(request, 'news/year_archive.html', context)
```
下一步：创建文件`news/templates/news/year_archive.html`来编写html页面样式
```html
{% extends "base.html" %}

{% block title %}Articles for {{ year }}{% endblock %}

{% block content %}
<h1>Articles for {{ year }}</h1>

{% for article in article_list %}
    <p>{{ article.headline }}</p>
    <p>By {{ article.reporter.full_name }}</p>
    <p>Published {{ article.pub_date|date:"F j, Y" }}</p>
{% endfor %}
{% endblock %}
```
然后创建文件`news/templates/base.html`来编写页面样式
```html
{% load static %}
<html>
<head>
    <title>{% block title %}{% endblock %}</title>
</head>
<body>
    <img src="http://www.cuc.edu.cn/_upload/site/00/05/5/logo.png" alt="Logo">
    {% block content %}{% endblock %}
</body>
</html>
```
下一步： 在 clouddisk/urls.py 里头建立命令对 news 应用的地址进行配置
```python
    path('news/', include('news.urls')),
```
上传到仓库