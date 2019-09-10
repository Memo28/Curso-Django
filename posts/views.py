from django.shortcuts import render
from django.http import HttpResponse

from datetime import datetime
# Create your views here.

posts = [
    {
        'name' : 'Forest',
        'user' : 'Pepito Ruiz',
        'timestamp' : datetime.now().strftime('%b %dth, %Y - $H %M hrs'),
        'picture' : 'https://picsum.photos/id/933/200/200'
    },
    {
        'name' : 'River',
        'user' : 'Pepito Ruiz',
        'timestamp' : datetime.now().strftime('%b %dth, %Y - $H %M hrs'),
        'picture' : 'https://picsum.photos/id/50/200/200'
    },
    {
        'name' : 'City',
        'user' : 'Pepito Ruiz',
        'timestamp' : datetime.now().strftime('%b %dth, %Y - $H %M hrs'),
        'picture' : 'https://picsum.photos/id/89/200/200'
    }

]


def list_views(request):

    content = []
    for post in posts:
        content.append("""
            <p><strong>{name}</stron></p>
            <p><small>{user} - <i> {timestamp}</i></small></p>
            <figure><img src="{picture}"/></figure>
        """.format(**post))

    return HttpResponse('<br>'.join(content))



