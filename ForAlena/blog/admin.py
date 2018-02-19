from django.contrib import admin
from .models import SignUp, UserprofileInfo, Lecture
from .forms import SignUpForm

class SignUpAdmin(admin.ModelAdmin):
    list_display = ['full_name','email','timestamp']
    form = SignUpForm

    # class Meta:
    #     model = SignUp


admin.site.register(SignUp, SignUpAdmin)


class UserprofileInfoAdmin(admin.ModelAdmin):

    class Meta():
        list_display = ('full_name','email')
        model = UserprofileInfo
admin.site.register(UserprofileInfo, UserprofileInfoAdmin)


admin.site.register(Lecture)
