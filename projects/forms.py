from django import forms
from .models import Project

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['project_number', 'project_title', 'start_date', 'end_date', 'scope_of_work', 'approved_hours', 'product_number', 'trigger', 'client_name','status','project_leader']
