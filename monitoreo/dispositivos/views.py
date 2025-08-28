from django.shortcuts import render
# Import the models you want to use
from .models import Dispositivo, Medicion 

def inicio(request):
    # This view remains the same for now.
    return render(request, "dispositivos/inicio.html")

def panel_dispositivos(request):
    # 1. Get all 'Dispositivo' objects from the database.
    todos_los_dispositivos = Dispositivo.objects.all()
    
    # 2. You can also get other data, for example, the latest measurements.
    ultimas_mediciones = Medicion.objects.order_by('-timestamp')[:5] # Get the 5 most recent

    # 3. Pass the real data to the template.
    contexto = {
        "dispositivos": todos_los_dispositivos,
        "mediciones": ultimas_mediciones,
    }

    return render(request, "dispositivos/panel.html", contexto)
