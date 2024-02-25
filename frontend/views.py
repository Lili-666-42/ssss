from django.shortcuts import get_object_or_404, redirect, render
from .models import Contactt
from users.models import CustomUser
from PIL import Image
from io import BytesIO
from django.core.files.base import ContentFile
import numpy as np
from .ist.imgF import obr


def contact(request):
    brigh = 0
    contr = 0
    flag = False
    user = request.user
    if not user.is_authenticated:
        return redirect('home2')
    object = Contactt.objects.filter(user=user.id)
    limit_value = request.user.limit

    if limit_value>43:
       flag = True
       pred = 'Охуел???)))'
       return render(request, 'frontend/contact.html', {'pred':pred,'objects':object,'user':user, 'flag':flag, 'limit_value':limit_value})
    
    if request.method == 'POST':
        user.limit += 1
        user.save()
        if 'checkbox' in request.POST: brigh = 1
        if 'checkbox2' in request.POST: contr = 1

        uploaded_file = request.FILES.get('fileToUpload')  
        img = Image.open(uploaded_file).convert('RGB')
        img = np.array(img)
        img = obr(img, brigh, contr)

        img_modified = Image.fromarray(img)
        with BytesIO() as buffer:
            img_modified.save(buffer, format='JPEG') 
            image_data = buffer.getvalue()

        image_file = ContentFile(image_data, name='название_изображения.jpg')
        Contactt.objects.create(user=request.user, image=image_file)
        im = Contactt.objects.last()
        object = Contactt.objects.filter(user=user.id)

        return render(request, 'frontend/contact.html', {'objects':object, 'im':im, 'user':user, 'limit_value':limit_value})
    
    return render(request, 'frontend/contact.html', {'objects':object, 'user':user, 'limit_value':limit_value})


def art(request, art_id):
    user = request.user
    object = Contactt.objects.get(user=user.id, pk=art_id)

    if not user.is_authenticated:
        return render(request, 'frontend/contact2.html', {'user':user})
    
    if request.method == 'POST':
        if 'del' in request.POST:
            Contactt.objects.get(pk=art_id).delete()
        return  redirect('home')
    
    return render(request, 'frontend/img.html', {'obj':object, 'user':user})

def user(request):

    user = request.user
    if not user.is_authenticated:
        return redirect('home')
    
    if request.method == 'POST':
        user.delete()
        return  redirect('home')
    return render(request, 'frontend/user.html', {'obj':object, 'user':user})

def contact2(request):
    object = CustomUser.objects.all()[:5]
    return render(request, 'frontend/contact2.html', {'object':object})

def show(request, user_id):
    object = Contactt.objects.filter(user=user_id)
    user = get_object_or_404(CustomUser, pk=user_id)
    return render(request, 'frontend/show.html', {'objects':object, 'user':user})

    