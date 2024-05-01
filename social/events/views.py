from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import AddUserForm
from . models import *
from django.http import HttpResponse
# for pdf file 
from django.http import FileResponse
import io
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter

# Create your views here.
def home(request):
    return render(request, 'events/home.html')

def view_list(request):
    lists = AddUser.objects.all()
    context = {'lists': lists}
    return render(request, 'events/view_list.html', context)

def add_user(request):
    form = AddUserForm()
    if request.method == 'POST':
        form = AddUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Added Successfully!')
            return redirect('add-user')
    context = {'form': form}
    return render(request, 'events/add_user.html', context)

def delete_user(request, pk):
    lists = AddUser.objects.get(id=pk)
    context = {'items': lists}
    if request.method == 'GET':
        return render(request, 'events/delete.html', context)
    elif request.method == 'POST':
        lists.delete()
        messages.success(request, 'User deleted successfully')
        return redirect('view-list')

def update_user(request, pk):
    lists = AddUser.objects.get(id=pk)
    form = AddUserForm(instance=lists)
    context = {'form': form}
    if request.method == 'GET':
        return render(request, 'events/update.html', context)
    elif request.method == 'POST':
        form = AddUserForm(request.POST, instance=lists)
        if form.is_valid():
            form.save()
            messages.info(request, 'The post has been updated  successfully')
            return redirect('view-list')
        
def view_text(request):
    response = HttpResponse(content_type = 'text/plain')
    response['Content-Disposition'] = 'attachment; filename= view.text'
    lists = AddUser.objects.all()
    lines = []
    for list in lists:
        lines.append(f'{list.firstname}\n{list.lastname}\n{list.email}\n{list.phone}\n{list.address}\n{list.relationship}\n{"--------"}\n\n')
    response.writelines(lines)
    return response

def view_pdf(request):
    # create a bytestream buffer 
    buf = io.BytesIO()
    # creat a canvas 
    c = canvas.Canvas(buf, pagesize=letter, bottomup=0)
    # create a text object 
    textob = c.beginText()
    textob.setTextOrigin(inch, inch)
    textob.setFont("Helvetica", 14)

    # DeSIGNATE THE MODEL 
    list = AddUser.objects.all()
    # creat blank lines
    lines = []
    for list in list:
        lines.append(list.firstname)
        lines.append(list.lastname)
        lines.append(list.email)
        lines.append(list.phone)
        lines.append(list.address)
        lines.append(list.relationship)
        lines.append("--------------")
    # loop 
    for line in lines:
        textob.textLine(line)

    # Finish Up 
    c.drawText(textob)
    c.showPage()
    c.save()
    buf.seek(0)
    
    # Return somethin 
    return FileResponse(buf, as_attachment=True, filename='view.pdf')

