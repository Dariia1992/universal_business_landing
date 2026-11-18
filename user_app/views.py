
# Функция для отображения HTML-шаблонов
from django.shortcuts import render

# FormView — класс для работы с формами
# RedirectView — класс для перенаправления пользователя
from django.views.generic import FormView, RedirectView

# login — авторизует пользователя и создаёт сессию
from django.contrib.auth import login

# LoginView — готовый класс Django для входа
# LogoutView — готовый класс Django для выхода
from django.contrib.auth.views import LoginView, LogoutView

# reverse_lazy — получает URL по его имени,
# когда он понадобится, а не сразу при загрузке файла
from django.urls import reverse_lazy

# Импортируем наши собственные формы
# CustomUserCreationForm — регистрация пользователя
# CustomAuthenticationForm — авторизация пользователя
from .forms import CustomUserCreationForm, CustomAuthenticationForm


# ==========================================
# РЕГИСТРАЦИЯ ПОЛЬЗОВАТЕЛЯ
# ==========================================

# Наследуем FormView, чтобы работать с формой
class RegisterView(FormView):

    # HTML-страница с формой регистрации
    template_name = 'user_app/register.html'

    # Указываем, какую форму использовать
    form_class = CustomUserCreationForm

    # Куда перенаправить после успешной регистрации
    success_url = reverse_lazy('login')

    # Метод вызывается, если форма прошла проверку
    def form_valid(self, form):

        # Сохраняем нового пользователя в базу данных
        # form.save() возвращает созданный объект пользователя
        user = form.save()

        # Автоматически авторизуем нового пользователя
        # self.request — текущий HTTP-запрос
        # user — пользователь, которого только что создали
        login(self.request, user)

        # Вызываем родительский метод FormView
        # Он перенаправляет на success_url
        return super().form_valid(form)


# ==========================================
# ВХОД ПОЛЬЗОВАТЕЛЯ
# ==========================================

# Наследуем готовый класс LoginView из Django
class CustomLoginView(LoginView):

    # HTML-страница с формой входа
    template_name = 'user_app/login.html'

    # Используем нашу форму авторизации
    authentication_form = CustomAuthenticationForm

    # Если пользователь уже авторизован,
    # не показываем форму входа, а перенаправляем
    redirect_authenticated_user = True

    # Адрес, куда отправить после успешного входа
    success_url = reverse_lazy('home')

    # Переопределяем метод получения адреса
    def get_success_url(self):

        # Возвращаем адрес для перенаправления
        return self.success_url


# ==========================================
# ВЫХОД ПОЛЬЗОВАТЕЛЯ
# ==========================================

# Наследуем готовый класс LogoutView из Django
class CustomLogoutView(LogoutView):

    # После выхода перенаправляем на страницу входа
    next_page = reverse_lazy('login')
