from ninja import NinjaAPI, Schema
from typing import List, Dict

from cards.models import Card, RequestAttempt
from django.shortcuts import get_object_or_404
from datetime import date, datetime, timedelta
from django.db.models import Count, Q
api = NinjaAPI()

# @api.get("/hello")
# def hello(request):
#     return "Hello world"

class CardOut(Schema):
    card_val: str

class CardIn(Schema):
    card_val: str

class AttemptsOut(Schema):
    total_attempts: int

class DailyAttemptsOut(Schema):
    date: date
    attempts: int

class MonthlySeriesOut(Schema):
    xAxis: List[int]
    successful: List[int]
    failed: List[int]


@api.post("/card")
def create_card(request, payload: CardIn):
    card = Card.objects.create(**payload.dict())
    return {"card": card.card_val}


@api.get("/card/{card_value}", response=CardOut)
def check_card(request, card_value: str):
    card = get_object_or_404(Card, card_val = card_value)
    return card


@api.get("/cards", response=List[CardOut])
def list_cards(request):
    qs = Card.objects.all()
    return qs


@api.put("/cards/{card_value}")
def update_card(request, card_value: str, payload: CardIn):
    card = get_object_or_404(Card, card_val = card_value)
    for attr, value in payload.dict().items():
        setattr(card, attr, value)
    card.save()
    return {"success": True}


@api.delete("/cards/{card_value}")
def delete_card(request, card_value: str):
    card = get_object_or_404(Card,card_val = card_value)
    card.delete()
    return {"success": True}


# New endpoints
@api.post("/attempt")
def create_attempt(request, successornot):
    card = RequestAttempt.objects.create(successful = successornot)
    return {"attempt": card.successful}



@api.get("/attempts/total", response=AttemptsOut)
def get_total_attempts(request):
    total_attempts = RequestAttempt.objects.count()
    return {"total_attempts": total_attempts}

@api.get("/attempts/today", response=AttemptsOut)
def get_attempts_today(request):
    today = date.today()
    attempts_today = RequestAttempt.objects.filter(timestamp__date=today).count()
    return {"total_attempts": attempts_today}

@api.get("/attempts/monthly_summary", response=MonthlySeriesOut)
def get_monthly_summary(request):
    today = date.today()
    start_date = today.replace(day=1)  # First day of the current month

    # Calculate the number of days in the current month
    days_in_month = (start_date.replace(month=start_date.month % 12 + 1, day=1) - timedelta(days=1)).day

    # Initialize data containers
    days = [start_date + timedelta(days=i) for i in range(days_in_month)]
    successful_data = [0] * days_in_month
    failed_data = [0] * days_in_month

    # Fetch the count of successful and failed attempts grouped by date
    summary = RequestAttempt.objects.filter(timestamp__date__gte=start_date).values('timestamp__date').annotate(
        successful_count=Count('id', filter=Q(successful=True)),
        failed_count=Count('id', filter=Q(successful=False))
    ).order_by('timestamp__date')

    for entry in summary:
        index = (entry['timestamp__date'] - start_date).days
        successful_data[index] = entry['successful_count']
        failed_data[index] = entry['failed_count']

    xAxis = [day.day for day in days]

    return {
        "xAxis": xAxis,
        "successful": successful_data,
        "failed": failed_data,
    }