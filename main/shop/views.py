from django.contrib.auth import login, logout
from django.contrib.auth.views import LoginView
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from .forms import *
from .models import *


# Удаление инструктора
def instructor_delete(request, id):
    try:
        instructor = Instructor.objects.get(id=id)
        car = Car.objects.get(id=instructor.car_id.id)
        transmission = Transmission.objects.get(id=car.transmission_id.id)
        model = Model.objects.get(id=car.model_id.id)
        brand = Brand.objects.get(id=model.brand_id.id)
        user = UserInfo.objects.get(id=instructor.user_id.id)
        passport = Passport.objects.get(id=user.passport_id.id)
        photo = FileSystemStorage()

        instructor.delete()
        car.delete()
        transmission.delete()
        model.delete()
        brand.delete()
        user.delete()
        passport.delete()
        if user.photo != '':
            photo.delete(user.photo.name)
        if car.photo != '':
            photo.delete(car.photo.name)
        return redirect('/instructors/')
    except Instructor.DoesNotExist:
        return redirect('/instructors/')


# Добавление инструктора
def instructor_add(request):
    if request.method == 'POST':
        form = InstructorAddForm(request.POST, request.FILES)
        # check whether it's valid:
        # if form.is_valid():
        # Создание объекта модели "Passport"
        passport = Passport()
        passport.save()

        # Сохранение фотки
        if request.FILES != {}:
            file = request.FILES['photo']
            fs = FileSystemStorage()
            fs.save(file.name, file)

        # Создание объекта модели "User"
        user = UserInfo()
        user.passport_id = passport
        user.surname = request.POST['surname']
        user.name = request.POST['name']
        user.patronymic = request.POST['patronymic']
        user.phone = request.POST['phone']
        user.email = request.POST['email']
        if request.FILES != {}:
            user.photo = file
        user.password = request.POST['password']
        user.save()

        # Создание объекта модели "Transmission"
        transmission = Transmission()
        transmission.save()

        # Создание объекта модели "Brand"
        brand = Brand()
        brand.save()

        # Создание объекта модели "Model"
        model = Model()
        model.brand_id = brand
        model.save()

        # Создание объекта модели "Car"
        car = Car()
        car.transmission_id = transmission
        car.model_id = model
        car.number = request.POST['number_car']
        car.save()

        # Создание объекта модели "Instructor"
        instructor = Instructor()
        instructor.user_id = user
        instructor.car_id = car
        instructor.driving_experience = request.POST["driving_experience"]
        instructor.save()

        return redirect('/instructors/')

    else:
        form = InstructorAddForm()

    return render(request, 'shop/instructor_add.html', {'form': form})


# Вывод главной страницы
class OccupationList(ListView):
    model = ProgramLearning
    context_object_name = 'program'
    template_name = 'shop/home.html'


# Регистрация пользователя
class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'shop/register.html'
    success_url = reverse_lazy('home')

    # Проверка на валидность формы
    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')


# Авторизация пользователя
class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'shop/login.html'
    success_url = reverse_lazy('home')

    # Перенаправление на главную страницу
    def get_success_url(self):
        return reverse_lazy('home')


# Выход с аккаунта
def logout_user(request):
    logout(request)
    return redirect('home')


# Вывод всех машин
class CarList(ListView):
    model = Instructor
    context_object_name = 'car'
    template_name = 'shop/car/cars.html'


# Вывод всех инструкторов
class InstructorList(ListView):
    model = Instructor
    context_object_name = 'instructor'
    template_name = 'shop/instructor/instructors.html'


# Открытие профиля / редактирование
def car_profile(request, id):
    if request.method == 'POST':
        model = Instructor.objects.get(car_id=id)
        form = (request.POST, request.FILES)

        user = UserInfo.objects.get(id=model.user_id.id)
        user.surname = request.POST['surname']
        user.name = request.POST['name']
        user.patronymic = request.POST['patronymic']
        user.save()

        car = Car.objects.get(id=model.car_id.id)
        car.color = request.POST['color']
        car.number = request.POST['number_car']
        if not request.POST['transmission'] == '':
            transmission = Transmission.objects.get(name=request.POST['transmission'])
            car.transmission_id = transmission

        if request.FILES != {}:
            photo = request.FILES['photo']
            fs = FileSystemStorage()
            if car.photo != '':
                fs.delete(car.photo.name)
            fs.save(photo.name, photo)
            car.photo = photo
        car.save()

        model = Model.objects.get(id=car.model_id.id)
        model.name = request.POST['model']

        brand = Brand.objects.get(id=model.brand_id.id)
        brand.name = request.POST['brand']

        return redirect('cars')

    else:
        form = (request.POST, request.FILES)
        model = Instructor.objects.get(car_id=id)

    return render(request, 'shop/car/car_profile.html', {'form': form, 'model': model})


def instructor_profile(request, id):
    if request.method == 'POST':

        model = Instructor.objects.get(id=id)

        # Объект UserInfo
        user = UserInfo.objects.get(id=model.user_id.id)
        user.surname = request.POST['surname']
        user.name = request.POST['name']
        user.patronymic = request.POST['patronymic']
        user.email = request.POST['email']

        if request.FILES != {}:
            photo = request.FILES['photo']
            fs = FileSystemStorage()
            if user.photo != '':
                fs.delete(user.photo.name)
            fs.save(photo.name, photo)
            user.photo = photo

        user.phone = request.POST['phone']
        user.save()

        # Объект Passport
        passport = Passport.objects.get(id=user.passport_id.id)
        passport.series = request.POST['series']
        passport.number = request.POST['number']
        passport.issued_by = request.POST['issued_by']
        passport.date_of_birth = request.POST['date_of_birth']
        passport.date_of_issue = request.POST['date_of_issue']
        passport.save()

        # Объект Car
        car = Car.objects.get(id=model.car_id.id)
        car.number = request.POST['number_car']
        car.save()

        return redirect('instructors')
    else:
        model = Instructor.objects.get(id=id)

    return render(request, 'shop/instructor/instructor_profile.html', {'model': model})


class GroupList(ListView):
    model = Group
    template_name = 'shop/group/group.html'
    context_object_name = 'model'


class StudentList(ListView):
    model = Student
    template_name = 'shop/group/group_profile.html'
    context_object_name = 'model'

    def get_queryset(self):
        return Student.objects.filter(group_id=self.kwargs['id'])


class StudentProfile(DetailView):
    model = Student
    template_name = 'shop/group/student_profile.html'
    context_object_name = 'model'


class GroupAdd(CreateView):
    form_class = GroupAddForm
    template_name = 'shop/group/group_add.html'
    success_url = reverse_lazy('group')


class GroupEdit(UpdateView):
    form_class = GroupEditForm
    template_name = 'shop/group/group_edit.html'
    success_url = reverse_lazy('group')

    def get_queryset(self):
        return Group.objects.filter(pk=self.kwargs['pk'])


class GroupDelete(DeleteView):
    model = Group
    template_name = 'shop/delete_page.html'
    success_url = reverse_lazy('group')


def profile(request, pk):
    model = UserInfo.objects.get(id=pk)
    if request.method == 'POST':
        form = (request.POST, request.FILES)

        model.surname = request.POST['surname']
        model.name = request.POST['name']
        model.patronymic = request.POST['patronymic']
        model.email = request.POST['email']
        model.phone = request.POST['phone']
        if not request.FILES == {}:
            photo = request.FILES['photo']
            file = FileSystemStorage()
            if not model.photo == '':
                file.delete(model.photo.name)
            file.save(photo.name, photo)
            model.photo = request.FILES['photo']

        model.save()

        passport = Passport.objects.get(id=model.passport_id.id)
        passport.series = request.POST['series']
        passport.number = request.POST['number']
        passport.issued_by = request.POST['issued_by']
        passport.date_of_issue = request.POST['date_of_issue']
        passport.date_of_birth = request.POST['date_of_birth']
        passport.save()

        return redirect('group')

    else:
        form = (request.POST, request.FILES)
    return render(request, 'shop/profile/profile.html', {'form': form, 'model': model})


class StudentDelete(DeleteView):
    model = Student
    template_name = 'shop/delete_student.html'
    success_url = '/group'
