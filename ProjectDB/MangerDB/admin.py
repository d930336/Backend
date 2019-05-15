from django.contrib import admin
from .models import Item

#增加顯示訊息
class PostAdmin(admin.ModelAdmin):
    list_display = ('id','title','MyClass','content')

# Register your models here.
admin.site.register(Item,PostAdmin)