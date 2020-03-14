
from django.http import HttpResponse
from datetime import datetime
import json

def hello(request):
    now = datetime.now().strftime('%b %dth, %Y - %H:%M hrs')
    return HttpResponse('Current server time {now}'.format(now=str(now)))

def sorted(request):
    #Get the string of numbers
    numbers = (request.GET['numbers'])
    #Convert the string to int and map it to int using as separator the '',
    numbers = list(map(int,request.GET['numbers'].split(',')))
    #Sort the array
    numbers.sort()
    #Return the data

    data = {
        'status' : 'OK',
        'numbers' :  numbers,
        'message' : 'Integers sorted successfully'

    }
    return HttpResponse(json.dumps(data, indent=4), content_type='application/json')

def hi(request,name,age):
    if age < 12:
        message = 'Sorry {} you are not allow here'.format(name)
    else:
        message = 'Hello {} Welcom to Platzigram'.format(name)
    
    return HttpResponse(message)
