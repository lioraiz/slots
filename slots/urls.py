from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth.views import login

from onlineslots import views
#from django.core.urlresolvers import reverse_lazy

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', include ('onlineslots.urls')),
    url(r'^register/', views.UserFormView, name='register'),
    url(r'^gameresult/$', views.game, name='result'),
    url(r'^login_in/$', views.login_in, name='login In'),
    url(r'^auth_view/$', views.auth_view, name='auth view'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^invalid_login/$', views.invalid_login, name='invalid login'),
    url(r'^game/$', views.game, name='game'),
]
