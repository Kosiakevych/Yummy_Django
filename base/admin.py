from django.contrib import admin
from .models import Categories, Dishes, About_Us, Stats, \
    Why_us, Home, Testimonials, Event, Chefs, Gallery, UserReservation, Contact, UserContact

# Register your models here.
admin.site.register(Categories)
admin.site.register(About_Us)
# admin.site.register(Dishes)
admin.site.register(Stats)
admin.site.register(Why_us)
admin.site.register(Home)
admin.site.register(Testimonials)
admin.site.register(Event)
admin.site.register(Chefs)
admin.site.register(Gallery)
admin.site.register(UserReservation)
admin.site.register(Contact)
admin.site.register(UserContact)


@admin.register(Dishes)
class DishAdmin(admin.ModelAdmin):
    list_filter = ('categories', )
    prepopulated_fields = {'slug': ('name', ), }
