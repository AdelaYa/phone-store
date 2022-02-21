from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Phone, Review
from .forms import ReviewForm


class HomePageView(ListView):
    model = Phone
    template_name = 'home.html'


def phone_detail(request, slug):
    phone = get_object_or_404(Phone, slug=slug)
    reviews = phone.reviews.all()
    if request.method == 'POST':
        review_form = ReviewForm(data=request.POST)
        if review_form.is_valid():
            new_review = review_form.save(commit=False)
            new_review.phone = phone
            new_review.author = request.user
            new_review.save()
        return HttpResponseRedirect(request.path)
    else:
        review_form = ReviewForm()
    return render(request,
                  'phone/phone_detail.html',
                  {'phone': phone,
                   'reviews': reviews,
                   'review_form': review_form,
                   'slug': slug})


class PhoneCreateView(CreateView):
    model = Phone
    template_name = 'phone/phone_new.html'
    fields = '__all__'


class PhoneUpdateView(UpdateView):
    model = Phone
    template_name = 'phone/phone_edit.html'
    fields = '__all__'


class PhoneDeleteView(DeleteView):
    model = Phone
    template_name = 'phone/phone_delete.html'
    success_url = reverse_lazy('home')


def delete_review(request, id, slug):
    review = get_object_or_404(Review, id=id)
    review.delete()
    return redirect('phone_detail', slug)
