import datetime

from django.shortcuts import render_to_response
from django.core import serializers

from django.http import HttpResponse
from impl_tickets.models import Items, ItemStatus

from django.utils import timezone
from collections import defaultdict
import json

def index(request):
    items=serializers.serialize("json", Items.objects.all())
    return render_to_response('index.html')

def get_items(request):
    items=serializers.serialize("json", Items.objects.all())
    print(items)
    return HttpResponse(items, content_type='application/json')

def add_item(request):
    params = request.GET
    today = datetime.date.today().strftime('%d.%m.%Y')
    date_to_fix = datetime.datetime.strptime(params['date_to_fix'] or (today), '%d.%m.%Y')
    p=Items(description=params['description'], submitted_by=params['submitted_by'], responsible=params['responsible'],date_to_fix=date_to_fix,)
    print(params)
    print(params['date_to_fix'])
    print(date_to_fix)
    p.save()

    items=serializers.serialize("json", Items.objects.all())
    return HttpResponse(items, content_type='application/json')

def fix_item(request):
    params = request.GET
    pks=[]
    for param, value in params.items():
        pks.append(value)
    print(pks)
    Items.objects.filter(pk__in=pks).update(date_fixed=timezone.now(), fixed='true')

    items=serializers.serialize("json", Items.objects.all())
    print(items)
    return HttpResponse(items, content_type='application/json')

def delete_item(request):
    params = request.GET
    pks=[]
    for param, value in params.items():
        pks.append(value)
    print(pks)
    p=Items.objects.filter(pk__in=pks).delete()

    items=serializers.serialize("json", Items.objects.all())
    return HttpResponse(items, content_type='application/json')