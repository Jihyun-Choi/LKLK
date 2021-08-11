from django.contrib import admin

# Register your models here.
from feedapp.models import Feed

#관리자 페이지에서 DB관리할 수 있도록
admin.site.register(Feed)