from django.shortcuts import render, redirect
from django.urls import reverse_lazy,reverse
from .forms import aboutform, aboutpost, aboutcontact, aboutregister, aboutmultipleimage
from .models import mypost, myregister
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView, TemplateView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.models import User
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin
from multi_form_view import MultiModelFormView
# Create your views here.


class Index(DetailView):
    model = mypost
    pk_url_kwarg = 'bid'    
    template_name = "index.html"
    context_object_name = "data"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['topic'] = mypost.objects.all()
        context['author'] = mypost.objects.all()
        return context


class Home(ListView):
    model = mypost
    context_object_name = "data"
    template_name = "home.html"
    paginate_by = 2

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["users"] = myregister.objects.all()
        return context
    

class Contact(CreateView):
    form_class = aboutcontact
    template_name = "contact.html"
    success_url = "home"
    

class About(CreateView):
    form_class = aboutform
    template_name = "about.html"
    success_url = "home"


class Post(LoginRequiredMixin,CreateView):
    form_class = aboutpost
    template_name = "post.html"
    success_url = "home"


class UpdatePost(UpdateView):
    model = mypost
    form_class = aboutpost
    template_name = "post.html"
    success_url = reverse_lazy('home')


class DeletePost(DeleteView):
    model = mypost
    template_name = "delete.html"
    success_url = reverse_lazy('home')



class register(CreateView):
    form_class = aboutregister
    template_name = "register.html"
    success_url = "home"

    def form_valid(self, form):
        user = User.objects.create_user(form.cleaned_data.get('user_name'), form.cleaned_data.get(
            'user_email'), form.cleaned_data.get('user_password'))
        user.save()
        form.save(user)
        return super().form_valid(form)


class login(LoginView):
    # redirect_authenticated_user = True
    template_name = "login.html"
    # success_url = reverse_lazy("home")


class logout(LogoutView):
    template_name = "logout.html"
    success_url = "home"


class multipleimage(MultiModelFormView):
    form_classes = {
        'a':aboutmultipleimage,
        'b':aboutpost
        }
    template_name = 'mulimg.html'
    success_url = "home"
    def get_success_url(self):
        return reverse('home')
    
    def post(self, request, **kwargs):
        forms = self.get_forms() 
        self.forms_valid(forms)
        return super().post(request, **kwargs)
    

    # def forms_valid(self, forms):

    #     if forms['a'].is_valid():
    #         forms['a'].save()

    #     if forms['b'].is_valid():
    #         forms['b'].save()
    #     return super(multipleimage, self).forms_valid(forms)

# def login(request):
#     if request == "POST":
#         return render(request,"login.html")


# def index(request,bid):

#     data = mypost.objects.get(userid=bid)
#     all_data = mypost.objects.all()

#     return render(request,'index.html',{'data':data,"all_data":all_data})

# def home(request):

#     data = mypost.objects.all()
#     return render(request,'home.html',{'data':data})

# def contact(request):

#     if request.method == 'POST':
#         form = aboutcontact(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('/home')
#     else:
#         form = aboutcontact()
#     context = {
#         "form" : form
#     }
#     return render(request,'contact.html', context)

# class Contact(View):
#     # form_class = aboutcontact
#     # template_name = "contact.html"
#     # success_url = "home"
#     def post(self,request):
#         form = aboutcontact(request.POST)
#         print("fdfdsf",form)
#         if form.is_valid():
#             form.save()
#             return redirect('/home')
#         else:
#              return render(request,'contact.html')

#     def get(self,request):
#         form = aboutcontact()
#         context = {
#            "form" : form
#         }
#         print("abc")
#         return render(request,'contact.html', context)


# def about(request):
#     if request.method == 'POST':
#         form = aboutform(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('/home')
#     else:
#         form = aboutform()
#     context = {
#         "form" : form
#     }
#     return render(request,'about.html', context)


# def post(request):

#     if request.method == 'POST':
#         form = aboutpost(request.POST,request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('/home')
#     else:
#         form = aboutpost()
#     context = {
#         "form" : form,

#     }
#     return render(request,'post.html', context)

    # form = aboutpost()
    # context = {
    #     "form":form
    # }
    # return render(request, 'post.html',context)


# def register(request):
#     if request.method == 'POST':
#         form = aboutregister(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('/home')
#     else:
#         form = aboutregister()
#         context = {
#            "form" : form
#         }
#     return render(request,'register.html', context)
