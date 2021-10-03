from django.urls import path
from users import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path ('register/', views.TeacherSignUpView.as_view(), name='teacher_register'),
    #path ('login/', userLogin, name='login'),
    path("logout/", LogoutView.as_view(), name="logout"),

]