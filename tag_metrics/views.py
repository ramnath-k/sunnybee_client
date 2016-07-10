from django.shortcuts import render
from django.http import JsonResponse, HttpResponseNotAllowed, Http404, HttpResponse
from django.utils.dateparse import parse_datetime
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from .models import TagTracker
import datetime
import json

@csrf_exempt
def update_tag_location(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
        except (ValueError, TypeError) as e:
            msg = 'unable to parse request body as json'
            result = {'error': {'error_code': 500, 'error_message': msg}}
            return JsonResponse(result, status=500)
        try:
            token = data['token']
            valid_token = token and token[:6] == 'Token ' and token[6:] in settings.VALID_TOKENS
        except KeyError:
            valid_token = False
        if not valid_token:
            return JsonResponse({'error': {'error_code': 401, 'error_message': 'Unauthorized'}}, status=401)
        try:
            tag_id = data['tag_id']
            antenna = data['antenna']
            reader = data['reader']
            found_time = data['found_time']
            found_time = parse_datetime(found_time)
            if not found_time:
                msg = 'unable to parse found_time as timezone aware datetime object'
                result = {'error': {'error_code': 500, 'error_message': msg}}
                return JsonResponse(result, status=500)
            TagTracker.objects.update_tag_location(tag_id, antenna, reader, found_time)
            result = {'ok': True}
            return JsonResponse(result, status=200)
        except KeyError:
            msg = 'Unable to parse tag_id, antenna, reader, or found_time from request body'
            result = {'error': {'error_code': 500, 'error_message': msg}}
            return JsonResponse(result, status=500)
    return HttpResponseNotAllowed(['POST'])

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
