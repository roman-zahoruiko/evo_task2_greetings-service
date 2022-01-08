from django.shortcuts import render
from .forms import UserDataForm
from .models import UserData
from django.views.decorators.cache import cache_page


@cache_page(60 * 2)
def index(request):
    if request.method == 'POST' and 'data' in request.POST:
        form = UserDataForm(request.POST)
        if form.is_valid():
            greet_data = request.POST['data']
            user_data, created = UserData.objects.get_or_create(data=greet_data)
            if not created:
                message = f"We've already met, dear {user_data}!"
            else:
                message = f'Hello, dear {user_data}!'
        else:
            message = form.errors
        return render(request, 'main_app/index.html', {'message': message})
    elif request.method == 'POST' and 'greeted_list' in request.POST:
        greeted_list = UserData.objects.all()[:200]
        return render(request, 'main_app/index.html', {'greeted_list': greeted_list})
    return render(request, 'main_app/index.html')
