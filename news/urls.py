urlpatterns = [
    path('hw/create/', views.HomeworkCreate.as_view()),
python
    path('',include('news.urls')),
python
    path('', views.HomeworkCreate.as_view()),