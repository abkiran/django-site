from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
import pprint as pp

@login_required()
def welcome(request):
    pp.pprint(request)
    test = {
        1 : 'afgfdgfdgfds',
        2 : "fgfgfdsgfdg",
        3 : "gfhddfg"
    }
    return render(test, content_type="application/json")
    # return HttpResponse("Welcome to chicago - VA")

@login_required()
def dashboard(request):
    pp.pprint(request)
    test = {
        1 : 'afgfdgfdgfds',
        2 : "fgfgfdsgfdg",
        3 : "gfhddfg",
        'h': "I know"
    }
    return render(request, template_name='volunteer/dashboard.html', context={'user':request.user, 'test':test})
