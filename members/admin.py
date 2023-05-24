from django.contrib import admin
from .models import profile, client,Product, Invoice,Usercompany,Userpayment,Number,Product1


@admin.register(client)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['companyname', 'companycode', 'vatcode']
@admin.register(Product)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['title','totalprice','subtotal','sumtotal','sumprice']
@admin.register(Invoice)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['accountnumber','companyname']
@admin.register(Usercompany)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['name','vat']
@admin.register(Userpayment)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['bankname']
@admin.register(Number)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['quan']
@admin.register(Product1)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['price']