from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import *

class LeaveRequestForm(forms.ModelForm):
    class Meta:
        model = LeaveRequest
        fields = ['Start_date','End_date','Matter']