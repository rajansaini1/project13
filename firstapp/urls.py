from firstapp import views
from django.conf.urls import url

app_name='firstapp'

urlpatterns = [
    url(r'^home/$',views.home,name="home"),
    url(r'^about/$', views.userrole,name="about"),
    url(r'^contentt/$', views.testcontent,name="content1"),
    url(r'^contentt2/$', views.testcontent2,name="contentt2"),
    url(r'^signup/$', views.signup,name="signup"),
    url(r'^viewdata/$', views.datafetch,name="fetch"),
    url(r'^filterdatav/$', views.datafetch1,name="fetch1"),
    url(r'^photo/$', views.photo,name="photo"),
    url(r'^viewget/$', views.get,name="viewphoto"),
    url(r'^updatedata/$',views.update,name="update"),
    url(r'^delete/$',views.delete,name="delete"),
    url(r'^editvalue/$',views.edit,name="edit"),
    url(r'^updatephoto/$',views.updatephoto),
    url(r'^viewphoto/$',views.photofetch),
    url(r'^editimage/$',views.editphoto)





]
