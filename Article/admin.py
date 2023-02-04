from django.contrib import admin
from .models import *
# Register your models here.

class SubcategoryAdmin(admin.ModelAdmin):
    list_display = ['subcategory']

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['category']

class UserAdmin(admin.ModelAdmin):
    list_display = ['name_and_surname']

class PostAdmin(admin.ModelAdmin):
    list_display = ['title','like','view','comment_count','created_date']
    list_filter = ['created_date']
    search_fields = ['title']

class indexpageadmin(admin.ModelAdmin):
    list_display = ['title']

class sosialadmin(admin.ModelAdmin):
    list_display = ['code','link']
    list_editable = ['link']

admin.site.register(sosials,sosialadmin)
admin.site.register(indexpage,indexpageadmin)
admin.site.register(Category,CategoryAdmin)
admin.site.register(Subcategory,SubcategoryAdmin)
admin.site.register(Article,PostAdmin)
admin.site.register(user,UserAdmin)
