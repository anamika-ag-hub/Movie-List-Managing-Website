from django.shortcuts import render,redirect
from.models import MovieInfo
from.forms import MovieForm
from django.contrib.auth.decorators import login_required

# Create your views here. 
@login_required(login_url='login')
def create(request): 
    
    if request.POST: 
       print("hi") 
    frm=MovieForm(request.POST,request.FILES) 
    print(request.FILES) 
    if frm.is_valid(): 
        frm.save() 
        return redirect('list') 
    else: 
        frm=MovieForm() 
 
    return render(request,'create.html',{'frm':frm,'action': 'Create' }) 
  
@login_required(login_url='login')
def list(request): 
    movie_set=MovieInfo.objects.all()
    print(movie_set)

    return render(request,'list.html',{'movies':movie_set}) 
def edit(request, pk):
    instance_to_be_edited = MovieInfo.objects.get(pk=pk)
    
    if request.method == 'POST':
        frm = MovieForm(request.POST, request.FILES, instance=instance_to_be_edited)
        if frm.is_valid():
            frm.save()  # Save the updated instance
            # Optionally, redirect to a success page or the updated movie's detail page
            return redirect('list')   # example redirect
        
    else:
        frm = MovieForm(instance=instance_to_be_edited)
    
    return render(request, 'create.html', {'frm': frm, 'action': 'Edit'})

 

@login_required(login_url='login')
def delete(request,pk): 
   instance=MovieInfo.objects.get(pk=pk)
   instance.delete()
   movie_set=MovieInfo.objects.all()


   return render(request,'list.html',{'movies':movie_set}) 