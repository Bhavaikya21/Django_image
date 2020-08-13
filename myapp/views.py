from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail

def get_demo(request):
    name = request.GET.get('name')
    return render(request, "myapp/get_demo.html", {'name' : name})

def post_demo(request):
    if request.method == "POST":
        name = request.POST.get('name')
        return HttpResponse("<h1>Thanks for submission {}</h1>".format(name))
    return render(request, "myapp/post_demo.html")

def form(request):
    if request.method=="POST":
        first_name=request.POST.get("first_name")
        last_name=request.POST.get("last_name")
        email=request.POST.get("email")
        password=request.POST.get("pwd")
        phno=request.POST.get("phno")
        date=request.POST.get("birthday_day")
        month=request.POST.get("birthday_month")
        year=request.POST.get("birthday_year")
        gender=request.POST.get("sex")
        if gender=="1":
            gender="Female"
        else:
            gender="Male"
        send_mail ("Thanks For Registration","Hello Mr./Ms.{} {}\n Thanks for Registering!!!".format(first_name,last_name),
                    "bhavaikya21@gmail.com",[email,],fail_silently=False)
        return HttpResponse("{}<br>{}<br>{}<br>{}<br>{}<br>{}<br>{}<br>{}<br>{}<br>".format(first_name,last_name,email,password,phno,gender,date,month,year))
    return render(request,"myapp/form.html")

from django.core.files.storage import FileSystemStorage
#uploading and displaying image

def img(request):
    return render(request,"image_upload.html")

def image_display(request):
    file_url=False
    if request.method=="POST" and request.FILES:
        image=request.FILES['sam']
        print(image) #it comes in cmd prompt img name
        fs=FileSystemStorage()
        file=fs.save(image.name,image)
        file_url=fs.url(file)
    return render(request,"image_display.html",context={'file_url':file_url})
