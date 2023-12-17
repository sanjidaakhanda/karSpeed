from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from  .forms import CarForm
from .forms import CommentForm
from . import models
from django.views.generic import CreateView,DeleteView,UpdateView,DetailView
from . import forms




@login_required
def add_car(request):
    if request.method == 'POST':
        form = CarForm(request.POST)
        if form.is_valid():
            form.instance.user =request.user
            form.save()
            return redirect('home')
    else:
        form = CarForm()

    return render(request, 'detail.html', {'form': form})

class CarDetailView(DetailView):
    model = models.Car
    template_name = 'viewDetail.html'
    pk_url_kwarg ='id'

    def post(self,request,*args,**kwargs):
       if self.request.method == 'POST':
        post = self.get_object()
        comment_form = forms.CommentForm( data = self.request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.car = post
            new_comment.save()
        return self.get(request,*args,**kwargs)
        
    def get_context_data(self, **kwargs):
         context = super().get_context_data(**kwargs)
         car = self.object
         comments = car.comments.all()
         comment_form = forms.CommentForm()
         context['comments']= comments
         context['comment_form'] = comment_form
         return context
   



