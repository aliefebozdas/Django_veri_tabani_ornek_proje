from django.urls import path
from . import views
# http://127.0.0.1:8000/                  => homepage
# http://127.0.0.1:8000/index             => homepage
# http://127.0.0.1:8000/blogs             => blogs
# http://127.0.0.1:8000/blogs/3           => blogs-details.html

urlpatterns = [
    path("", view=views.index, name="home"),
    path("index", view=views.index,),
    path("blogs", view=views.blogs, name="blogs"),
    path("category/<slug:slug>", view=views.blogs_by_category,
         name="blogs_by_category"),
    path("blogs/<slug:slug>", view=views.blogsDetails, name="blogs_details")
]
