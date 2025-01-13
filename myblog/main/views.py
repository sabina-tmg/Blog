from django.shortcuts import redirect, render, HttpResponse
from django.urls import reverse
from .models import Blog, Comment
from django.contrib import messages
from .models import Contact
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.db.models import Q




# Create your views here.
def home(request):
    return render(request, 'main/index.html')

def blog(request):
    blogs = Blog.objects.all()
    context = {
        'blogs': blogs
    }
    # return HttpResponse("This is Blog")
    return render(request, 'main/bloghome.html', context)

def blogpost(request,slug):
    blog = Blog.objects.filter(slug=slug).first()
    comments = Comment.objects.filter(post=blog)


    
    # comments = Comment.objects.filter(post=post)
    context = {
        'blog': blog,
        'comments': comments,
    }
    return render(request, 'main/blogpost.html', context)
    # return HttpResponse(f"You are visiting {slug}")

def PostComment(request):
    if request.method=="POST":
        post = Blog.objects.get(slug=request.POST.get('post_id'))
        comment = request.POST.get('comment')
        name = request.POST.get('name')
        print('name', name)
        print(request.POST.get('post_id'))
        comment = Comment(Comment=comment, name=name,post=post)
        comment.save()
        messages.success(request, "You have Successfully commented.")
        return redirect(reverse('blogpost', kwargs={'slug': post.slug}))


def search(request):
    if request.method=='POST':
        searched=request.POST['searched']
        finds=Blog.objects.filter[Q(title_icontains=searched)]
    return render(request, 'main/search.html')

def main(request):
    return render(request, 'main/home.html')

from django.core.mail import send_mail
from django.contrib import messages
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from .models import Contact

def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        msg = request.POST['message']
        phone = request.POST['phone']
        
        # Create the Contact object
        data = Contact.objects.create(name=name, email=email, message=msg, phone=phone)
        
        # Prepare email content
        subject = "Welcome to our code"
        message = render_to_string('main/msg.html', {'name': name, 'data': data})
        from_email = "syangtansabina8@gmail.com"
        recipient_list = [email]
        
        try:
            # Attempt to send the email
            send_mail(subject, message, from_email, recipient_list, fail_silently=False)
            # On success, display success message
            messages.success(request, f"Hi {name}, your message is successfully submitted! Please check your email.")
            return redirect('contact')  # Redirect after successful form submission
        except Exception as e:
            # If email sending fails, display an error message
            messages.error(request, "There was an error sending the email. Please try again later.")
    
    return render(request, 'main/contact.html')
