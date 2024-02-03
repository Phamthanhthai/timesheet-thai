from django import forms
from .models import TimesheetEntry

class TimesheetForm(forms.ModelForm):
    class Meta:
        model = TimesheetEntry
        fields = ['user' ,'date', 'hours_worked', 'activity']

    activity = forms.ChoiceField(widget=forms.RadioSelect, choices=TimesheetEntry.ACTIVITY_CHOICES)