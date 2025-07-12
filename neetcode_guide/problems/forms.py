from django import forms
from .models import Attempt

class AttemptForm(forms.ModelForm):
    class Meta:
        model = Attempt
        fields = ['status', 'notes']
        widgets = {
            'notes': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Add your notes here...'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
        }