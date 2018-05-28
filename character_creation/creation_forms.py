from django import forms

class CreationForm(forms.Form):
    ''' Form for the character creation '''
    char_name = forms.CharField(label="Character Name", max_length=100)
    strength = forms.IntegerField(label="Strength")
    intelligence = forms.IntegerField(label="Intelligence")
    dexterity = forms.IntegerField(label="Dexterity")
    faith = forms.IntegerField(label="Faith")
    vitality = forms.IntegerField(label="Vitality")
    endurance = forms.IntegerField(label="Endurance")
