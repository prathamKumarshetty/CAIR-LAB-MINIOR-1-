from django.contrib import admin
from django.urls import path
from home import views
urlpatterns = [
     path('admin/', admin.site.urls),
    path("",views.home,name="home"),
    path("about",views.about,name="about"),
    path("AIML",views.AIML,name="AIML"),
    path("CLOUD",views.CLOUD,name="CLOUD"),
    path("RU",views.RU,name="RU"),
    path("OTHER",views.OTHER,name="OTHER"),
    path("HPC",views.HPC,name="HPC"),
    path("home",views.home,name="home"),
    path("contact",views.contact,name="contact"),
]
