from django.contrib import admin
from tokaadmin.models import *

class newspaperAdmin(admin.ModelAdmin):
    class Media:
        js = ('temp.js', 'bootstrap.min.js')
    list_display = ['paper_name','ssid','phone_number','productor']


class SubscriberAdmin(admin.ModelAdmin):
    class Media:
        js = ('temp.js', 'bootstrap.min.js')
    list_display = ['sub_name','phone_n','sub_address','testdata']




admin.site.register(newspaper,newspaperAdmin)
admin.site.register(Subscriber,SubscriberAdmin)

admin.site.site_title = "订户订阅系统"
admin.site.site_header = "订户订阅系统"
