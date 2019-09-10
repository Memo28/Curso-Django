from django.shortcuts import render
from django.http import HttpResponse

from datetime import datetime
# Create your views here.

posts = [
    {
        'title' : 'Forest',
        'user' : {
            'name' : 'Pepito',
            'picture' : 'https://picsum.photos/id/933/200/200'
        },
        'timestamp' : datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'photo' : 'https://picsum.photos/id/933/200/200'
    },
    {
        'title' : 'River',
        'user' : {
            'name' : 'Pepito',
            'picture' : 'https://picsum.photos/id/56/200/200'
        },
        'timestamp' : datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'photo' : 'https://picsum.photos/id/55/200/200'
    },
    {
        'title' : 'City',
        'user' : {
            'name' : 'Pepito',
            'picture' : 'https://picsum.photos/id/12/200/200'
        },
        'timestamp' : datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'photo' : 'https://picsum.photos/id/56/200/200'
    },

]


def list_views(request):
    return render(request,'feed.html', {'posts' : posts})



