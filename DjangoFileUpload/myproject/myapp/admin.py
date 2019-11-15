from django.contrib import admin
from .models import ProfileUpload,MyDetails, Author, Document,Cars
# Register your models here.

admin.site.register(ProfileUpload)
admin.site.register(MyDetails)
admin.site.register(Author)
admin.site.register(Document)
admin.site.register(Cars)
