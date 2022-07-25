from django.contrib import admin
from loginSignup.models import LoginSignup

class LoginSignupAdmin(admin.ModelAdmin):
    list_display = ('login_email','login_password')
    list_display = ('signup_email','signup_password')


admin.site.register(LoginSignup,LoginSignupAdmin)


# Register your models here.
