from django import forms 
from .models import Machine

class signinForm(forms.Form):
    CHOICE = [
        ("Male","Male"),
        ("Age","Age"),
        ("Female","Female"),
    ]
    SearchEquipment = forms.ChoiceField(
        label = "Search Equipment",
        choices = CHOICE,
        widget = forms.Select(attrs = {
         'class':'form-control'
        })
    ) 

    EquipmentNo = forms.IntegerField(
        label = "Equipment No."
    )
 
    EqpDescription = forms.CharField(
        max_length = 50,
        label = "Eqp.Description",
        required=True,
        widget = forms.TextInput(attrs = {
            #  'class':'form-control'
            "rows":3
            
        }),
        initial="DIESEL GENERATOR SET (400KVA) AT 33/11KV SUBSTATION RCF/RBL/LLJ",
        # help_text = "Please enter your full name"
    )
    
    Short_Name = forms.CharField(
        max_length = 200,
        label = "Short Name",
        required=True,
        widget = forms.TextInput(attrs = {
            # 'class':'form-control'
        }),
        initial="DG SET (400KVA)",
        # help_text = "Please enter your full name"
    )

    emp_salary = forms.IntegerField(

    )
    
    