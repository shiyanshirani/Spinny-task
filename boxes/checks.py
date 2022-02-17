# Django imports
from django.db.models import Avg
from django.utils import timezone

# Project imports
from boxes.models import Box
from Spinny.settings import A1, V1, L1, L2

# Packages import
from datetime import timedelta, datetime


def validation(user):
    if Box.objects.all().count() == 0:
        return True

    area = Box.objects.all().aggregate(Avg("area"))
    if area["area__avg"] > A1:
        return False

    volume = Box.objects.all().aggregate(Avg("volume"))
    if volume["volume__avg"] > V1:
        return False

    datetime_oneweekago = timezone.now().date() - timedelta(days=7)

    boxes_last_week = Box.objects.filter(date_created__gt=datetime_oneweekago).count()
    if boxes_last_week > L1:
        return False

    boxes_lastweek_user = Box.objects.filter(
        created_by=user, date_created__gt=datetime_oneweekago
    ).count()
    if boxes_lastweek_user > L2:
        return False

    return True
