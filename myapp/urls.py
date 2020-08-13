from django.urls import path
from myapp import views
app_name = "myapp"

urlpatterns = [
    path('get_demo/', views.get_demo, name="get_demo"),
    path('post_demo/', views.post_demo, name="post_demo"),
    path('form/', views.form, name="form"),
    path('img/',views.img,name="img"),
    path('image_display',views.image_display,name="image_display")
]
