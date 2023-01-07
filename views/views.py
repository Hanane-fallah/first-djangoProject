from django.http import HttpResponse
from django.shortcuts import render


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
    print('guess: ', g)
    context = {
        'guess': g
    }
    return render(request, 'views/danger.html', context)
