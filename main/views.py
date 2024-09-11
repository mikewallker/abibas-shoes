from django.shortcuts import render

def show_main(request):
    context = {
        'name': 'Pak Bepe',
        'class': 'PBP E'
    }

    return render(request, "main.html", context)
