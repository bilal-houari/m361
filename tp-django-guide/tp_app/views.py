from django.shortcuts import render

def index(request):
    context = {
        'name': 'bilal',
        'age': 64,
        'morrocan': True
    }
    return render(request, 'index.html', context)

def counter(request):
    text = request.POST['text']
    amount_of_words = len(text.split())
    return render(request, 'counter.html', {'amount': amount_of_words})