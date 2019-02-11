from django.shortcuts import render
from .models import Contact
import requests, json


def index(request):
    if request.method == 'POST':
        firstname = request.POST.get('fname')
        lastname = request.POST.get('lname')

        r = requests.get('http://api.icndb.com/jokes/random?firstName='+ firstname+ '&lastName=' + lastname)
        json_data = json.loads(r.text)
        joke = json_data.get('value').get('joke')

        context = {'joker': joke}
        return render(request, 'armansite/index.html', context)

    else:
        firstname = 'Arman'
        lastname = 'Shanto'

        r = requests.get('http://api.icndb.com/jokes/random?firstName=' + firstname + '&lastName=' + lastname)
        json_data = json.loads(r.text)
        joke = json_data.get('value').get('joke')

        context = {'joker': joke}
        return render(request, 'armansite/index.html', context)


def portfolio(request):
    return render(request, 'armansite/portfolio.html')


def contact(request):
    if request.method == 'POST':
        # DO-Some operations
        email_r = request.POST.get('email')
        subject_r = request.POST.get('subject')
        message_r = request.POST.get('message')
        everything = Contact(email=email_r, subject=subject_r, message=message_r)
        everything.save()
        return render(request, 'armansite/confirmation.html')

    else:
        return render(request, 'armansite/contact.html')


