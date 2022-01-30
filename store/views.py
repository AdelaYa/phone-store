from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Phone


class HomePageView(ListView):
    model = Phone
    template_name = 'home.html'


class PhoneDetailView(DetailView):
    model = Phone
    template_name = 'phone/phone_detail.html'
    context_object_name = 'phone'


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
