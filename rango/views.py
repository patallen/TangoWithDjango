from django.shortcuts import render

def index(request):
    context_dict = {'bold_message': "I am bold font from the context"}
    return render(request, "rango/index.html", context_dict)
