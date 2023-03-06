from django.shortcuts import render
from rest_framework.viewsets import ReadOnlyModelViewSet
from services.models import *
from services.serializers import SubscriptionSerializer


# Create your views here.
class SubscriptionView(ReadOnlyModelViewSet):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer