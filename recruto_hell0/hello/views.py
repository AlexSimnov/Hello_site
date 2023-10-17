from django.shortcuts import render


def hello_page(request):
    name = request.GET.get('name')
    message = request.GET.get('message')
    context = {
        'name': name,
        'message': message
    }
    return render(request, 'hello/main_page.html', context)
