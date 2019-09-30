from django.shortcuts import render,HttpResponse,redirect
from firstapp.forms import SiteUserForm,UserRoleForm,UserPhotoForm
from firstapp.models import SiteUser,UserRole,UserPhoto
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.hashers import make_password,check_password
import os
# Create your views here.

def index(request):
    return HttpResponse("<marquee><h1>welcome to first response</h1></marquee>")

def home(request):
    return render(request,"home.html")

def about(request):
    name="rajan"
    names=["rajan","tushar","naveen"]

    return render(request,"about.html",{'n':name,'l':names})

def testcontent(request):
    return render(request,"contentt.html")

def testcontent2(request):
    return render(request,"contentt2.html")

def signup(request):
    if request.method=="POST":

        form= SiteUserForm(request.POST)
        f=form.save(commit=False)
        f.userFullName=request.POST["name"]
        f.userEmail = request.POST["email"]
        f.userPassword = make_password(request.POST["password"])
        f.userMobile = request.POST["mobile"]
        f.isActive = True
        f.roleid_id= 2
        f.save()
        return render(request, "signup.html", {'success': True})
    return render(request,"signup.html")


def userrole(request):
    if request.method == "POST":
        form = UserRoleForm(request.POST)
        f = form.save(commit=False)
        f.rolename = request.POST["n1"]
        f.isActive = True
        f.save()
        return render(request, "about.html", {'use': True})
    return render(request,"about.html")

def photo(request):
    if request.method=="POST":
        form= UserPhotoForm(request.POST)
        try:
            if request.FILES["img"]:
                my_file=request.FILES["img"]
                fs=FileSystemStorage()
                file_name=fs.save(my_file.name,my_file)
                img=fs.url(file_name)
                img=my_file.name
        except:
            pass
        f = form.save(commit=False)
        f.userFullName=request.POST["name"]
        f.userEmail = request.POST["email"]
        f.userPassword = request.POST["password"]
        f.userMobile = request.POST["mobile"]
        f.isActive = True
        f.photo=img
        f.roleid_id= 2
        f.save()
        return render(request, "photo.html", {'p': True})
    return render(request,"photo.html")

def update(request):
    if request.method=="POST":
        name=request.POST["name"]
        email=request.POST["email"]
        password=request.POST["password"]
        mobile=request.POST["mobile"]

        updatedata=SiteUser(userEmail=email,userPassword=password,userMobile=mobile)
        updatedata.save(
            update_fields=["userPassword",
                           "userMobile"])

        return render(request,"updatedata.html",{'u':updatedata})
    return render(request, "updatedata.html")

def delete(request):
    emailid=request.GET["id"]
    deletedata=SiteUser.objects.get(userEmail=emailid)
    deletedata.delete()

    return redirect("/user/viewdata/")

def edit(request):
    emailid=request.GET["email"]
    data = SiteUser.objects.get(userEmail=emailid)
    if request.method=="POST":
        name=request.POST["name"]
        email=request.POST["email"]
        password=request.POST["password"]
        mobile=request.POST["mobile"]

        updatedata=SiteUser(userEmail=email,userFullName=name,userPassword=password,userMobile=mobile)
        updatedata.save(
            update_fields=["userPassword",
                           "userMobile",
                           "userFullName",
                           ])


        return render(request,"edit.html",{'c':updatedata,'e':data})
    return render(request , "edit.html", {'e': data})

def updatephoto(request):
    if request.method=="POST":
        try:
            if request.FILES["img1"]:
                my_file=request.FILES["img1"]
                fs=FileSystemStorage()
                file_name=fs.save(my_file.name,my_file)
                img=fs.url(file_name)
                img=my_file.name
        except:
            pass
        name=request.POST["name"]
        email=request.POST["email"]
        password=request.POST["password"]
        mobile=request.POST["mobile"]
        pic=img
        updatepic=UserPhoto(userEmail=email,userFullName=name,userPassword=password,userMobile=mobile,photo=pic)
        updatepic.save(
            update_fields=[ "userFullName",
                            "userPassword",
                            "userMobile",
                            "photo",
                           ])
        return render(request,"updatephoto.html",{'poto':updatepic})
    return render(request, "updatephoto.html")

def editphoto(request):
    emailid = request.GET["pic"]
    data=UserPhoto.objects.get(userEmail=emailid)
    if request.method=="POST":
        try:
            if request.FILES["newpic"]:
                os.remove("media/"+data.image)
                my_file=request.FILES["newpic"]
                fs=FileSystemStorage()
                file_name=fs.save(my_file.name,my_file)
                img=fs.url(file_name)
                img=my_file.name
        except:
            pass
        name=request.POST["name"]
        email=request.POST["email"]
        password=request.POST["password"]
        mobile=request.POST["mobile"]
        pic=img
        updatepic=UserPhoto(userEmail=email,userFullName=name,userPassword=password,userMobile=mobile,photo=pic)
        updatepic.save(
            update_fields=[ "userFullName",
                            "userPassword",
                            "userMobile",
                            "photo",
                           ])
        return render(request,"editimage.html",{'picedit':updatepic,'ep':data})
    return render(request, "editimage.html" ,{'ep':data})








def datafetch(request):
    data=SiteUser.objects.all()
    return render(request,"viewdata.html",{'d':data})


def photofetch(request):
    data=UserPhoto.objects.all()
    return render(request,"viewphoto.html",{'d':data})


def datafetch1(request):
    data=UserRole.objects.filter(isActive=1)
    return render(request,"filterdatav.html",{'d1':data})

def get(request):
    data=SiteUser.objects.get(userEmail="rrajanynrsaini@gmail.com")
    return render(request,"viewget.html",{'g':data})
