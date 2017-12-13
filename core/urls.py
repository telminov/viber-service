from django.conf.urls import url

from rest_framework_swagger.views import get_swagger_view

from .views import rest

urlpatterns = [
    url(r'^docs/$', get_swagger_view(title='API')),

    url(r'^api/send_text/$', rest.SendText.as_view(), name='send_text'),
    url(r'^api/send_image/$', rest.SendImage.as_view(), name='send_image'),
    url(r'^api/send_text_and_button/$', rest.SendTextAndButton.as_view(), name='send_text_and_button'),

    url(r'^api/check_status_messages/$', rest.CheckStatusMessages.as_view(), name='check_status_messages'),
]