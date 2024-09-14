from django.shortcuts import render

def show_main(request):
    context = {
        'name': 'Yosia Joseph Chandra',
        'class': 'PBP F'
    }

    return render(request, "main.html", context)
