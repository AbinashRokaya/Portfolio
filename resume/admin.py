from xml.dom.expatbuilder import Skipper

from django.contrib import admin
from .models import About,Education,Expericence,Services,Gallery,Client,Blog,Contact,Skill

# Register your models here.
admin.site.register(About)
admin.site.register(Education)
admin.site.register(Expericence)
admin.site.register(Services)
admin.site.register(Gallery)
admin.site.register(Client)
admin.site.register(Blog)
admin.site.register(Contact)
admin.site.register(Skill)
