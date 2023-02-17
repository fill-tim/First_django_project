from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from django.forms import *
from .models import Group


class RegisterUserForm(UserCreationForm):
    username = CharField(
        label='Логин',
        widget=TextInput(
            attrs={
                'class': 'form-input'
            }
        )
    )
    email = CharField(
        label='Почта',
        widget=EmailInput(
            attrs={
                'class': 'form-input'
            }
        )
    )
    password1 = CharField(
        label='Пароль',
        widget=PasswordInput(
            attrs={
                'class': 'form-input'
            }
        )
    )
    password2 = CharField(
        label='Повторный пароль',
        widget=PasswordInput(
            attrs={
                'class': 'form-input'
            }
        )
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class LoginUserForm(AuthenticationForm):
    username = CharField(
        label='Логин',
        widget=TextInput(
            attrs={
                'class': 'form-input'
            }
        )
    )
    password = CharField(
        label='Пароль',
        widget=PasswordInput(
            attrs={
                'class': 'form-input'
            }
        )
    )

    class Meta:
        model = User
        fields = ['username', 'password']


class InstructorAddForm(Form):
    surname = CharField(
        label='Фамилия',
        widget=TextInput(
            attrs={
                'class': 'form-control rounded '
            }
        )
    )
    name = CharField(
        label='Имя',
        widget=TextInput(
            attrs={
                'class': 'form-control rounded '
            }
        )
    )
    patronymic = CharField(
        label='Отчество',
        widget=TextInput(
            attrs={
                'class': 'form-control rounded '
            }
        )
    )
    phone = FileField(
        label='Телефон',
        widget=TextInput(
            attrs={
                'class': 'form-control rounded '
            }
        )
    )
    email = CharField(
        label='Почта',
        widget=EmailInput(
            attrs={
                'class': 'form-control rounded '
            }
        )
    )
    driving_experience = CharField(
        label='Стаж',
        widget=NumberInput(
            attrs={
                'class': 'form-control rounded '
            }
        )
    )
    photo = ImageField(required=False)
    number_car = CharField(
        label='Номер машины',
        widget=TextInput(
            attrs={
                'class': 'form-control rounded '
            }
        )
    )
    password = CharField(
        label='Пароль',
        required=False,
        widget=PasswordInput(
            attrs={
                'class': 'form-control rounded '
            }
        )
    )


class GroupAddForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['format_learning_id'].empty_label = 'Формат не выбран'
        self.fields['program_learning_id'].empty_label = 'Программа не выбрана'

    class Meta:
        model = Group
        fields = ['name', 'format_learning_id', 'program_learning_id']


class GroupEditForm(ModelForm):
    class Meta:
        model = Group
        fields = ['name', 'format_learning_id', 'program_learning_id']


