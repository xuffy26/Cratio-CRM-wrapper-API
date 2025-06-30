from django.urls import path
from .views import CodeyoungLeadAPIView

urlpatterns = [
    path('send-codeyoung-lead/', CodeyoungLeadAPIView.as_view(), name='send_codeyoung_lead'),
]
