from django.shortcuts import render
from django.http import JsonResponse, HttpResponseNotAllowed, Http404, HttpResponse
from .models import TagTracker
import datetime

def store_stock(request):
    if request.method == 'GET':
        tags = TagTracker.objects.store_stock()
        return render(request, 'tag_metrics/store_stock.html', context={'tags': tags})
    return HttpResponseNotAllowed(['GET'])

def tag_location(request):
    if request.method == 'GET':
        tags = TagTracker.objects.last_locations()
        return render(request, 'tag_metrics/tag_location.html', context={'tags': tags})
    return HttpResponseNotAllowed(['GET'])

def tag_flow_today(request):
    if request.method == 'GET':
        today = datetime.datetime.now()
        start_date = datetime.datetime.combine(today, datetime.time.min)
        end_date = datetime.datetime.combine(today, datetime.time.max)
        start_date = start_date.strftime('%Y-%m-%d %H:%M:%S')
        end_date = end_date.strftime('%Y-%m-%d %H:%M:%S')
        print(start_date, end_date)
        tags = TagTracker.objects.tag_flow(start_date, end_date)
        return render(request,
                      'tag_metrics/tag_flow.html',
                      context={'tags': tags,
                               'start_date': start_date,
                               'end_date': end_date
                               }
                      )
    return HttpResponseNotAllowed(['GET'])

def tag_flow_week(request):
    if request.method == 'GET':
        today = datetime.datetime.now()
        start_date = datetime.datetime.combine(today, datetime.time.min)
        start_date = start_date - datetime.timedelta(days=start_date.weekday())
        end_date = start_date + datetime.timedelta(days=6)
        end_date = datetime.datetime.combine(end_date, datetime.time.max)
        start_date = start_date.strftime('%Y-%m-%d %H:%M:%S')
        end_date = end_date.strftime('%Y-%m-%d %H:%M:%S')
        print(start_date, end_date)
        tags = TagTracker.objects.tag_flow(start_date, end_date)
        return render(request,
                      'tag_metrics/tag_flow.html',
                      context={'tags': tags,
                               'start_date': start_date,
                               'end_date': end_date
                               }
                      )
    return HttpResponseNotAllowed(['GET'])
