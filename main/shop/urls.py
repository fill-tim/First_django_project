from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', OccupationList.as_view(), name='home'),
    path('cars/', CarList.as_view(), name='cars'),
    path('instructors/', InstructorList.as_view(), name='instructors'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('profile/<int:pk>', profile, name='profile'),
    path('instructor_add/', instructor_add, name='instructor_add'),
    path('instructors/delete/<int:id>/', instructor_delete, name='instructor_delete'),
    path('cars/profile/<int:id>/', car_profile, name='car_profile'),
    path('instructors/profile/<int:id>/', instructor_profile, name='instructor_profile'),
    path('delete_student/<int:pk>/', StudentDelete.as_view(), name='delete_student'),
    path('group/', GroupList.as_view(), name='group'),
    path('group_add/', GroupAdd.as_view(), name='group_add'),
    path('group_edit/<int:pk>', GroupEdit.as_view(), name='group_edit'),
    path('group_delete/<int:pk>', GroupDelete.as_view(), name='group_delete'),
    path('group_profile/<int:id>', StudentList.as_view(), name='group_profile'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
