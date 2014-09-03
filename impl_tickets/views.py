from django.shortcuts import render_to_response
from django.core import serializers

from django.http import HttpResponse
from impl_tickets.models import Items, ItemStatus
import json

def index(request):
    items=serializers.serialize("json", Items.objects.all())
    return render_to_response('index.html')

def get_items(request):
    items=serializers.serialize("json", Items.objects.all())
    return HttpResponse(items, content_type='application/json')

def add_item(request):
    params = request.GET
    p=Items(description=params['description'], status_customer='Новое', status_solvo='Новое')
    p.save()

    items=serializers.serialize("json", Items.objects.all())
    return HttpResponse(items, content_type='application/json')