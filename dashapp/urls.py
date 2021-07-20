from django.urls import path

from dashapp.views import InstaDataView

app_name = 'dashapp'

urlpatterns = [
    path('', InstaDataView.as_view(), name='dashapp'),
]