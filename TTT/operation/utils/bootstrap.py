
from ensurepip import bootstrap
from django import forms

class BootStrap:
    bootstrap_exclude_fields=[]
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        #循环Modelform中的所有字段，给每个字段的插件设置
        for name,field in self.fields.item():
            if name in self.bootstrap_exclude_fields:
                continue
            if field.widget.attrs:
                field.widget.attrs["class"]="form-control"
                field.widget.attrs["placeholder"]=field.label
            else:
                field.widget.attrs={
                    "class":"form-control",
                    "placeholder":field.label
                }

class BootStrapModelForm(BootStrap,forms.ModelForm):
    pass

class BootStrapForm(BootStrap,forms.Form):
    pass
