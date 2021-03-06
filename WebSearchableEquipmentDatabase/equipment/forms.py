from django.core.validators import MinValueValidator
from django.forms import ModelForm
from .models import Equipment


class EquipmentForm(ModelForm):
    """Equipment form that enables user to create a form with fields associated with equipment"""
    class Meta:
        model = Equipment
        fields = ['name', 'model', 'manufacturer', 'year', 'permission', 'pi', 'center_lab', 'location', 'contact',
                  'url', 'description', 'photo']
