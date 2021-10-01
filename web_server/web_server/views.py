from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.shortcuts import redirect
from datetime import datetime, timezone

from django.views import generic
from django.utils import timezone



from django.http import JsonResponse


import json
from django.core.serializers.json import DjangoJSONEncoder

import random
import string
from django.core import serializers
def home(request):
    return render(request, 'home.html')
def login(request):
    return render(request, 'authentication/login.html')
def test(request):
    return render(request, 'test.html')
def test_inputs(request):
    return render(request, 'test_inputs.html',{'base_id':'employee_input_table'})
