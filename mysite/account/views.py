from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User


def login_request(request):
    if request.user.is_authenticated:
        return redirect("home")

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            return render(request, "account/login.html", {"error":
                                                          "username ya da parola yanlış"})
    return render(request, "account/login.html")


def register_request(request):
    if request.user.is_authenticated:
        return redirect("home")
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        firstname = request.POST.get("firstname")
        lastname = request.POST.get("lastname")
        password = request.POST.get("password")
        repassword = request.POST.get("repassword")

        if password == repassword:
            if User.objects.filter(username=username).exists():
                return render(request, "account/register.html", {
                    "error": "Böyle bir kullanıcı adı var. Başka bir kullanıcı adı seçin !!",
                    "username": username,
                    "email": email,
                    "firstname": firstname,
                    "lastname": lastname
                })
            else:
                if User.objects.filter(email=email).exists():
                    return render(request, "account/register.html", {"error": "Böyle bir email var. Başka email seçin !!",
                                                                     "username": username,
                                                                     "email": email,
                                                                     "firstname": firstname,
                                                                     "lastname": lastname})
                else:
                    user = User.objects.create_user(
                        username=username, email=email, first_name=firstname, last_name=lastname, password=password)
                    user.save()
                    return redirect("home")

        else:
            return render(request, "account/register.html", {"error": "Parola Eşleşmiyor!!",
                                                             "username": username,
                                                             "email": email,
                                                             "firstname": firstname,
                                                             "lastname": lastname})
    return render(request, "account/register.html")


def logout_request(request):
    logout(request)
    return redirect("home")
