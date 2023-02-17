from django.db import models


# Create your models here.

class FormatLearning(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Формат обучения'


class ProgramLearning(models.Model):
    category = models.CharField(max_length=255)
    cost = models.IntegerField()

    def __str__(self):
        return self.category

    class Meta:
        verbose_name = 'Программа обучения'


class Brand(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Марка'


class Model(models.Model):
    name = models.CharField(max_length=255)
    brand_id = models.ForeignKey(Brand, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Модель'


class Transmission(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Коробки передач'


class Car(models.Model):
    photo = models.ImageField(upload_to='media_car/%Y/%m/%d/')
    number = models.CharField(max_length=255)
    color = models.CharField(max_length=255)
    transmission_id = models.ForeignKey(Transmission, on_delete=models.DO_NOTHING)
    model_id = models.ForeignKey(Model, on_delete=models.CASCADE)

    def __str__(self):
        return f'Номер автомобиля: {self.number}'

    class Meta:
        verbose_name = 'Автомобили'


class Passport(models.Model):
    series = models.CharField(max_length=255, null=True)
    number = models.CharField(max_length=255, null=True)
    date_of_issue = models.DateField(max_length=255, null=True)
    place_of_birth = models.CharField(max_length=255, null=True)
    issued_by = models.CharField(max_length=255, null=True)
    date_of_birth = models.DateField(max_length=255, null=True)

    def __str__(self):
        return f'Серия: {self.series}, Номер: {self.number}'

    class Meta:
        verbose_name = 'Паспорты'


class UserInfo(models.Model):
    # user_id = models.OneToOneField(User, on_delete=models.DO_NOTHING)
    surname = models.CharField(max_length=255, null=True)
    name = models.CharField(max_length=255, null=True)
    patronymic = models.CharField(max_length=255, null=True)
    phone = models.CharField(max_length=255, null=True)
    email = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='media_user/%Y/%m/%d/', null=True)
    passport_id = models.ForeignKey(Passport, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.surname} {self.name} {self.patronymic}'

    class Meta:
        verbose_name = 'Пользователь'


class Instructor(models.Model):
    driving_experience = models.IntegerField()
    car_id = models.ForeignKey(Car, on_delete=models.CASCADE)
    user_id = models.ForeignKey(UserInfo, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user_id.name}'

    class Meta:
        verbose_name = 'Инструктор'


class Group(models.Model):
    name = models.CharField(max_length=255)
    program_learning_id = models.ForeignKey(ProgramLearning, on_delete=models.DO_NOTHING)
    format_learning_id = models.ForeignKey(FormatLearning, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Группа'


class Student(models.Model):
    user_id = models.ForeignKey(UserInfo, on_delete=models.CASCADE)
    instructor_id = models.ForeignKey(Instructor, on_delete=models.DO_NOTHING)
    start_date_of_training = models.DateField(auto_now=True, max_length=255)
    end_date_of_training = models.DateField(max_length=255, blank=True)
    group_id = models.ForeignKey(Group, on_delete=models.DO_NOTHING)

    def __str__(self):
        return f'{self.user_id.name}'

    class Meta:
        verbose_name = 'Студент'
