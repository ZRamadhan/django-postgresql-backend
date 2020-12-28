from django.conf.urls import url
from api_test import views

urlpatterns = [
  url(r'^api_test/lists$', views.api_test_list),
  # url(r'âpi_test/lists/^\d{4}\-(0[1-9]|1[012])\-(0[1-9]|[12][0-9]|3[01])$+&+^\d{4}\-(0[1-9]|1[012])\-(0[1-9]|[12][0-9]|3[01])$')
]