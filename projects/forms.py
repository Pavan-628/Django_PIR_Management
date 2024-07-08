from django import forms
from .models import Project
from account.models import User


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['project_number', 'project_title', 'start_date', 'end_date', 'scope_of_work', 'approved_hours', 'product_number', 'trigger', 'client_name','status','project_leader']
        widgets = {
            'project_number': forms.TextInput(attrs={
                'class': 'form-input mt-1 block w-full',
                'placeholder': 'Project Number'
            }),
            'project_title': forms.TextInput(attrs={
                'class': 'form-input mt-1 block w-full',
                'placeholder': 'Project Title'
            }),
            'project_leader': forms.Select(attrs={
                'class': 'form-select mt-1 block w-full'
            }),
            'start_date': forms.DateInput(attrs={
                'class': 'form-input mt-1 block w-full',
                #'placeholder': 'Start Date'
                'type':'date'
            }),
            'end_date': forms.DateInput(attrs={
                'class': 'form-input mt-1 block w-full',
                #'placeholder': 'End Date'
                'type':'date'
            }),
            'scope_of_work': forms.Textarea(attrs={
                'class': 'form-textarea mt-1 block w-full',
                'placeholder': 'Project Scope of Work'
            }),
            'approved_hours': forms.NumberInput(attrs={
                'class': 'form-input mt-1 block w-full',
                'placeholder': 'Number of Hours Approved'
            }),
            'product_number': forms.NumberInput(attrs={
                'class': 'form-input mt-1 block w-full',
                'placeholder': 'Product Group'
            }),
            'trigger': forms.TextInput(attrs={
                'class': 'form-input mt-1 block w-full',
                'placeholder': 'Trigger'
            }),
            'client_name': forms.TextInput(attrs={
                'class': 'form-input mt-1 block w-full',
                'placeholder': 'Unit'
            }),
            'status': forms.Select(attrs={
                'class': 'form-select mt-1 block w-full'
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['project_leader'].queryset = User.objects.all()
        self.fields['project_leader'].label_from_instance = lambda obj: obj.name
        
