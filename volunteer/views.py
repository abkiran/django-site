from django.shortcuts import render
from django.contrib.auth.decorators import login_required
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
    #send_mail(subject="test", message="Hiiiiii", from_email='abkiranreddy@gmail.com', recipient_list=['abkiranreddy@gmail.com'])
    test = {
        1 : 'afgfdgfdgfds',
        2 : "fgfgfdsgfdg",
        3 : "gfhddfg",
        'h': "I know"
    }
    #logger.error("PCH")
    return render(request, template_name='volunteer/dashboard.html', context={'user':request.user, 'test':test})
