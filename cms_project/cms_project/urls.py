from django.contrib import admin
from django.urls import path
from cmsapp.views import home,addmin,student,upload,add,view,ulogin,usignup,ulogout,main,tlogin,tlogout,tsignup,thome,remove
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/',admin.site.urls),
    path("",main,name="main"),
    path("home",home,name="home"),
    path("ulogin",ulogin,name="ulogin"),
    path("usignup",usignup,name="usignup"),
    path("ulogout",ulogout,name="ulogout"),
    path("tlogin",tlogin,name="tlogin"),
    path("tsignup",tsignup,name="tsignup"),    
    path("tlogout",tlogout,name="tlogout"),
    path("thome",thome,name="thome"),
    path("remove/<int:id>",remove,name="remove"),




    path("addmin",addmin,name="addmin"),
    path("student",student,name="student"),
    path("upload",upload,name="upload"),
    path("add",add,name="add"),
    path("view",view,name="view"),

] +static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
