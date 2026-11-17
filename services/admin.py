from django.contrib import admin

# Register your models here.
from .models import Service,Project,ContactRequest,SiteSettings,Testimonial,FAQ

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "is_active", "created_at")
    list_display_links = ("id",)
    list_editable = ("title", "is_active")
    list_filter = ("is_active",)
    search_fields = ("title", "description")
    ordering = ("-created_at",)
    list_per_page = 20
    
    
@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("id","title","is_published","created_at")
    list_editable = ("is_published",)
    list_filter = ("is_published", "created_at")
    search_fields = ("title", "description")
    ordering = ("-created_at",)
    

@admin.register(ContactRequest)
class ContactRequestAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "email", "phone", "is_read", "created_at")
    list_editable = ("is_read",)
    list_filter = ("is_read", "created_at")
    search_fields = ("name", "email", "phone")
    ordering = ("-created_at",)
    readonly_fields = ("created_at",)
    
@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    list_display = ("id", "company_name", "email", "phone")
    search_fields = ("company_name", "email")
#нельзя было создать несколько наборов настроек одного сайта
    def has_add_permission(self, request):
        return not SiteSettings.objects.exists()


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ("id", "client_name", "company", "rating", "is_published", "created_at")
    list_editable = ("is_published",)#чтобы можно было публиковать отзывы прямо из таблицы.
    list_filter = ("rating","is_published") #чтобы фильтровать по статусу публикации и рейтингу.
    search_fields = ("client_name", "company", "text")#чтобы искать по имени клиента, компании и тексту отзыва.
    ordering = ("-created_at",)
    
    
    #Часто задаваемые вопросы
@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    #показывает поля в таблице
    list_display = ("id", "question", "order", "is_active")
    #позволяет менять порядок вопросов и их активность прямо в таблице.
    list_editable = ("order", "is_active")
    list_filter = ("is_active",)
    search_fields = ("question", "answer")
    ordering = ("order",)
    
    
    