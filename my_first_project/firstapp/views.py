from django.forms import ValidationError
from django.shortcuts import render
from django.http import HttpResponse
from matplotlib import artist
from firstapp.models import musician,album
from django.core import validators
from firstapp import forms
from django.db.models import Avg
def index(request):
    musician_list = musician.objects.order_by('first_name')
    diction = {'title': "Home page",'musician_list':musician_list}
    return render(request,'firstapp/index.html',context=diction)

def album_list(request, musician_id):
    musician_info = musician.objects.get(pk=musician_id)
    album_list = album.objects.filter(artist=musician_id).order_by('name','release_date')
    artist_rating = album.objects.filter(artist=musician_id).aggregate(Avg('num_star'))
    diction ={'title':"List of albums",'musician_info':musician_info,'album_list':album_list,'artist_rating':artist_rating}
    return render(request,'firstapp/album_list.html',context=diction)

def musician_form(request):
    form = forms.musician_form()

    if request.method == 'POST':
        form = forms.musician_form(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)

    diction={'title':"Add musician",'musician_form':form}
    return render(request,'firstapp/musician_form.html',context=diction)

def album_form(request):
    form = forms.album_form()

    if request.method == 'POST':
        form = forms.album_form(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return index(request)
    diction={'title':"Add album",'album_form':form}
    return render(request,'firstapp/album_form.html',context=diction) 


def edit_artist(request,artist_id):
    artist_info= musician.objects.get(pk=artist_id)
    form=forms.musician_form(instance=artist_info)
    if request.method == 'POST':
        form=forms.musician_form(request.POST,instance=artist_info)
        if form.is_valid():
            form.save(commit=True)
            return album_list(request,artist_id)
    diction={'edit_form':form}
    return render(request,'firstapp/edit_artist.html',context=diction)


def edit_album(request,album_id):
    album_info = album.objects.get(pk=album_id)
    form=forms.album_form(instance=album_info)
    diction={}
    if request.method == 'POST':
        form=forms.album_form(request.POST,instance=album_info)
        if form.is_valid:
            form.save(commit=True)
            diction.update({'success_msg':'Successfully Updated!!'})
    diction.update({'edit_album':form})
    diction.update({'album_id':album_id})
    return render(request,'firstapp/edit_album.html',context=diction)

def delete_album(request,album_id):
    album_obj=album.objects.get(pk=album_id).delete()
    diction={'success_msg':"Album Deleted Successfully"}
    return render(request,'firstapp/delete_album.html',context=diction)

def delete_artist(request,artist_id):
    musician_obj=musician.objects.get(pk=artist_id).delete()
    diction={'success_msg':"Musician Deleted Successfully"}
    return render(request,'firstapp/delete_artist.html',context=diction)
# Create your views here.
