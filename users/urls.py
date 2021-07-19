from django.conf.urls import url,include
from users import views


urlpatterns = [
    url(r'inside/',views.upload_file,name='upload_file'),
    url(r"^accounts/",include("django.contrib.auth.urls")),
    url(r'',views.dashboard,name="dashboard"),
]
