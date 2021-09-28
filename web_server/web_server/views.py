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
    return render(request, 'home.html',{'helppage':5})
#            data={client_id:"tmGXpMsmWnfAaQUWWckp3Z2wUjICYIA6JyMncvym",client_secret:"XuHR87IavxzivItmZho3udTveIaKgq30S7Lyg4jEcpQ4ZnbtYijSQ6lWBjKFcsQoqRDRe3r89my2bHaL9wfjWhsOPmFPKxTnwxdRyHGF4ZCLZCzjgS5IJoTTzhtmSEQM"}
#

#
#arnkDubHTi80QWcaMYJVmBNJtrqf3mBMmS2XkyHIWBkmNbgt7rwSkFU33RDGiUITL18WAUKgxWba7vQiQIgtXUMl4HJSGq0fjkZDBYNiRVLFKTOqgSlEn9GRCcZYYdnr
