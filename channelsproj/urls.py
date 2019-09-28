
from django.contrib import admin
from django.urls import path
from notifier.views import *

urlpatterns = [
    path('',HomeView.as_view()),
    path('notification/',NotificationView.as_view()),
    path('admin/', admin.site.urls),

]
