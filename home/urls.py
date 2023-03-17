from django.urls import path
from django.conf.urls.static import static
from testproject import settings
from . import views
from . import context_processor
urlpatterns = [
    path("<int:bid>",views.Index.as_view(),name="index"),
    path("home",views.Home.as_view(),name="home"),
    path("contact",views.Contact.as_view(),name="contact"),
    path("about",views.About.as_view(),name="about"),
    path("post",views.Post.as_view(),name="post"),
    path("edit/<int:pk>/",views.UpdatePost.as_view(),name="Updatepost"),
    path("delete/<int:pk>/",views.DeletePost.as_view(),name="Deletepost"),
    path("login",views.login.as_view(),name="login"),
    path("register",views.register.as_view(),name="register"),
    path("logout",views.logout.as_view(),name="logout"),
    path("mul",views.multipleimage.as_view(),name="mul"),
    # path("search",views.multipleimage.as_view(),name="mul"),
    # path("search",context_processor.my_search,name="search")



]

if settings.DEBUG:  # new
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)