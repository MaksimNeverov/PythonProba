from django.shortcuts import render
from .models import Person


def home(request):
    person = [
        {
            'name': 'Alice',
            'age': 30,
            'hobbies': {'reading', 'traveling', 'swimming'}
        },
        {
            'name': 'Bob',
            'age': 25,
            'hobbies': {'gaming', 'reading'}
        }
    ]

    data = {

        'person': Person.objects.all(),
        'title': 'Домашняя страница'

    }

    return render(request, 'blog/home.html', data)


def contacti(request):
    return render(request, 'blog/contacti.html', {'title': 'Страница контакты'})
