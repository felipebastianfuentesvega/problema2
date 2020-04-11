from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import MultasEstacionamiento
from .forms import MultasEstacionamientoForm

def multasestacionamiento_list(request):
    multasestacionamientos = MultasEstacionamiento.objects.all
    return render(request, 'registromultas/multasestacionamiento_list.html', {'multasestacionamientos': multasestacionamientos})

def multasestacionamiento_detail(request, pk):
    multasestacionamiento = get_object_or_404(MultasEstacionamiento, pk=pk)
    return render(request, 'registromultas/multasestacionamiento_detail.html', {'multasestacionamiento': multasestacionamiento})

def multasestacionamiento_new(request):
    if request.method == "POST":
        form = MultasEstacionamientoForm(request.POST)
        if form.is_valid():
            multasestacionamiento = form.save(commit=False)
            multasestacionamiento.author = request.user
            multasestacionamiento.fechayhora = timezone.now()
            multasestacionamiento.save()
            return redirect('multasestacionamiento_detail', pk=multasestacionamiento.pk)
    else:
        form = MultasEstacionamientoForm()
    return render(request, 'registromultas/multasestacionamiento_edit.html', {'form': form})