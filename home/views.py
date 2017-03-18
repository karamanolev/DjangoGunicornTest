import os
import random
import time

from django.http.response import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST


def index(request):
    key = 'MODIFY THIS TO TEST CODE RELOADING'
    env = dict(os.environ)
    return render(request, 'index.html', {
        'key': key,
        'env': env,
    })


@require_POST
@csrf_exempt
def complicated(request):
    time.sleep(0.5 + random.random() * 0.5)
    return HttpResponse('ok')
