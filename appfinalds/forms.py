from django import forms


class FormularioBase(forms.Form):
    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)

class AsesoresFormulario(FormularioBase, forms.Form):
    id_asesor = forms.CharField(max_length=30)
    
class EvaluadorFormulario(FormularioBase, forms.Form):
    id_evaluador = forms.CharField(max_length=30)
       
class EvaluacionFormulario(forms.Form):
    id_evaluador = forms.CharField(max_length=30)
    id_asesor = forms.CharField(max_length=30)
    id_evaluacion = forms.CharField(max_length=30)
    fecha_evaluacion = forms.DateField()