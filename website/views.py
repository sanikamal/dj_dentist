from django.shortcuts import render
from django.core.mail import send_mail

def home(request):
    return render(request,'home.html',{})
def contact(request):
    if request.method == "POST":
        name=request.POST['name']
        email=request.POST['email']
        message=request.POST['message']

        # send email
        send_mail(
            name,
            message,
            email,
            ['djdentalcare@gmail.com'],
            fail_silently=False,
            

        )
        return render(request,'contact.html',{'name':name})

    else:
        return render(request,'contact.html',{})


def about(request):
    return render(request,'about.html',{})

def service(request):
    return render(request,'service.html',{})

def pricing(request):
    return render(request,'pricing.html',{})

def blog(request):
    return render(request,'blog.html',{})

def blog_detail(request):
    return render(request,'blog-details.html',{})