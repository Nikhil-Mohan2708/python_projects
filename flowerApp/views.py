from django.db.models.functions import Upper
from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from .forms import CustomUserCreationForm
from .models import Category, Flower, District, City
from django.contrib.auth import authenticate, login, logout


def home(request):
    districts = District.objects.all()
    return render(request,'homePage.html',{'districts':districts})


def get_cities(request):
    district_id = request.GET.get('district_id')  # Get the district ID from the AJAX request
    if district_id:
        cities = City.objects.filter(district_id=district_id)  # Filter cities by district ID
        city_list = [{'id': city.id, 'name': city.name} for city in cities]  # Create a list of cities
        return JsonResponse({'cities': city_list})  # Return a JSON response with the list of cities
    else:
        return JsonResponse({'error': 'Invalid district ID'})  # Return an error response if district ID is not provided


def category_list(request):
    categories = Category.objects.all()
    context = {'categories': categories}
    return render(request, 'category_list.html', context)


def flower_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    flowers = Flower.objects.all()

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        flowers = flowers.filter(category=category)

    colors = Flower.objects.order_by('color').values_list('color', flat=True).distinct()

    selected_colors = request.GET.getlist('color')

    if selected_colors:
        flowers = flowers.filter(color__in=selected_colors)

    context = {
        'category': category,
        'categories': categories,
        'flowers': flowers,
        'colors': colors,
        'selected_colors': selected_colors
    }
    return render(request, 'flower_list.html', context)


def flower_details(request, flower_id):
    flower = get_object_or_404(Flower, pk=flower_id)
    context = {
        'flower': flower
    }
    return render(request, 'flower_details.html', context)


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('flowerApp:categories')
        else:
            error_message = 'Invalid username or password'
    else:
        error_message = ''
    return render(request, 'login.html', {'error_message': error_message})


def logout_view(request):
    logout(request)
    return redirect('flowerApp:home')


def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            print("Form is valid")
            user = form.save()
            print("User saved:", user)
            return redirect('flowerApp:login')
        else:
            error_message = "There are errors in the form: "
            for field in form:
                for error in field.errors:
                    error_message += f"{field.label}: {error}; "
            print(error_message)
    else:
        error_message = ''
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form, 'error_message': error_message})




