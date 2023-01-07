from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views import View


# Create your views here.
def funky(request):
    # response = """
    # <h1> funky function sample </h1>
    # <form
    # <input type="text" name="guess">
    # """
    # return HttpResponse(response)
    return render(request, 'views/funky.html')


def danger(request):
    g = request.POST["guess"]
    context = {
        'guess': g
    }
    return render(request, 'views/danger.html', context)


def rest(request, guess):
    context = {
        'guess': guess
    }
    return render(request, 'views/rest.html', context)


class RestMainView(View):
    def get(self, request, guess):
        print('guess', guess)
        context = {
            'guess': guess
        }
        return render(request, 'views/remainview.html', context)


def bounce(request):
    return  HttpResponseRedirect('http://127.0.0.1:8000/views/funky')