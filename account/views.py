from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse("welcom")


def Signupview(request):
    if request.method =='POST':
        title=request.POST.get('title')
        name=request.POST.get("name")
        username =request.POST.get("username")
        gender =request.Post.get("gender")
        phone = request.POST.get("phone")
        email =request.POST.get("email")
        password=request.POST.get("pwd")
        obj = Signup(title=title,name=name,username=username,gender=gender,phone=phone,email=email,password=password)
        obj.save()
    return render(request,'signup.html')