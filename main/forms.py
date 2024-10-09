from django.forms import ModelForm
from main.models import Product
from django.utils.html import strip_tags

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ["name", "price", "description", "type", "materials"]

    def clean_name(self):
        name = self.cleaned_data["name"]
        return strip_tags(name)

    def clean_type(self):
        type = self.cleaned_data["type"]
        return strip_tags(type)
    
    def clean_description(self):
        description = self.cleaned_data["description"]
        return strip_tags(description)
    
    def clean_materials(self):
        materials = self.cleaned_data["materials"]
        return strip_tags(materials)