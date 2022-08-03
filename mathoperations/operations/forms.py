from django import forms

class OperationForm(forms.Form):
    num1=forms.CharField()
    num2=forms.CharField()
    def clean(self):
        cleaned_data=super().clean()
        num1=int(cleaned_data.get('num1'))
        num2=int(cleaned_data.get('num2'))
        if num1<0:
            message="Please enter a valid number"
            self.add_error('num1',message)
        if num2<0:
            message = "Please enter a valid number"
            self.add_error('num2',message)
class StarForm(forms.Form):
    num=forms.CharField()
    def clean(self):
        cleaned_data=super().clean()
        num=int(cleaned_data.get('num'))
        if num==0:
            message="Please enter a positive number"
            self.add_error('num',message)