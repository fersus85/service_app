import datetime
import time
from celery import shared_task
from celery_singleton import Singleton
from django.db.models import F


@shared_task
def set_price(subscription_id):
    from services.models import Subscription

    time.sleep(5)

    subscription = Subscription.objects.filter(id=subscription_id).annotate(
        ann_price=F('service__full_price') - F('service__full_price') * F('plan__discount_percent') / 100
    ).first()
    subscription.price = subscription.ann_price
    subscription.save()


@shared_task(base=Singleton)
def set_price(subscription_id):
    from services.models import Subscription

    time.sleep(5)

    subscription = Subscription.objects.get(id=subscription_id)
    subscription.comments = str(datetime.datetime.now())
    subscription.save()
