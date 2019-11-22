from django.forms import ModelForm
from core.models import Cliente

class FormClient(ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'