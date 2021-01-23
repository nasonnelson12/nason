from django.contrib import admin
from shop.models import Category, Product, Images, Comment, FAQ, Variation, ContactUs 


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'parent']
    list_filter = ['name']

#@admin_thumbnails.thumbnail('image')
class ProductImageInline(admin.TabularInline):
    model = Images
    readonly_fields = ('id',)
    extra = 1

class ProductVariationsInline(admin.TabularInline):
    model = Variation
    readonly_fields = ('image_tag',)
    extra = 1
    show_change_link = True

#@admin_thumbnails.thumbnail('image')
class ImagesAdmin(admin.ModelAdmin):
    list_display = ['image', 'title', 'image_thumbnail']


class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'image_tag', 'status']
    list_filter = ['status', 'category']
    readonly_fields = ('image_tag',)
    inlines = [ProductImageInline,ProductVariationsInline]
    prepopulated_fields = {'slug': ('title',)}

class CmmentAdmin(admin.ModelAdmin):
    list_display = ['user', 'subject', 'comment', 'status', 'create_at']
    list_filter = ['status']
    readonly_fields = ('user', 'subject')

class FAQAdmin(admin.ModelAdmin):
    list_display = ['ordernumber', 'question', 'status', 'create_at', 'update_at']
    list_filter = ['status']

class VariantstAdmin(admin.ModelAdmin):
    list_display = ['title', 'product', 'image_tag']


# Register your models here.
admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Images)
admin.site.register(Comment, CmmentAdmin)
admin.site.register(ContactUs)
admin.site.register(FAQ, FAQAdmin)
admin.site.register(Variation, VariantstAdmin)

