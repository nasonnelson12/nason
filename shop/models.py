from ckeditor_uploader.fields import RichTextUploadingField
from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from django.db.models import Sum
from django.db.models import Count
from django.forms import ModelForm
from django.urls import reverse
from django.utils.safestring import mark_safe
from mptt.models import MPTTModel, TreeForeignKey
from django.db.models import Avg
 
# Create your models here.


class Category(MPTTModel):
    name = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(blank=True, null=True)
    photo = models.ImageField(upload_to='category_pc', blank=True, null=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    def __str__(self):
    	return self.name 

    class MPTTMeta:
        order_insertion_by = ['name']

class Product(models.Model):
	STATUS = (
		('New', 'New'),
		('True', 'True'),
		('False', 'False'),
	)
	SLIDER = (
		('True', 'True'),
		('False', 'False'),
	)
	status = models.CharField(max_length=10, choices=STATUS, default='New')
	slider = models.CharField(max_length=10, choices=SLIDER, default='False')
	category = models.ForeignKey(Category, related_name='item_set', on_delete=models.CASCADE)
	title = models.CharField(max_length=100)
	price = models.IntegerField()
	discount_price = models.IntegerField()
	discount_parcent = models.CharField(max_length=40, blank=True, null=True)
	slug = models.SlugField()
	description = models.TextField()
	details = models.TextField(blank=True, null=True)
	specifications = RichTextUploadingField(blank=True, null=True)
	availability = models.CharField(max_length=100, blank=True, null=True)
	shipping = models.CharField(max_length=50, blank=True, null=True)
	start_date = models.DateTimeField(auto_now_add=True)
	image = models.ImageField(upload_to='item_pc', blank=True, null=True)
	 

	def __str__(self):
		return self.title

	def image_tag(self):
		return mark_safe('<img src="{}" height="50"/>'.format(self.image.url))

	image_tag.short_descripion = 'Image'

	def get_absolute_url(self):
		return reverse("shop:shopdetails", kwargs={
			'slug': self.slug,
			'id': self.id
		})

	#def avaregereview(self):
	#	reviews = Comment.objects.filter(product=self, status='True').aggregate(avarage=Avg('rate')
	#	avg = 0
	#	if reviews["avarage"] is not None:
	#		avg = float(reviews["avarage"])
	#	return avg

	#def countreview(self):
	#	reviews = Comment.objects.filter(product=self, status='True').aggregate(count=Count('id')
	#	cnt=0
	#	if reviews["count"] is not None:
	#		cnt=int(reviews["count"])
	#	return cnt



class Images(models.Model):
	product = models.ForeignKey(Product, on_delete=models.CASCADE)
	title = models.CharField(max_length=100, blank=True, null=True)
	image = models.ImageField(upload_to='item_pc', blank=True, null=True)

	def __str__(self):
		return self.title



class VariationManager(models.Manager):
	def all(self):
		return super(VariationManager, self).filter(active=True)

	def sizes(self):
		return self.all().filter(category='size')

	def colors(self):
		return self.all().filter(category='color')


VAR_CATAGORIES = (
		('None', 'None'),
		('size', 'size'),
		('color', 'color'),
		('package', 'package'),
	)

class Variation(models.Model):
	title = models.CharField(max_length=100, blank=True, null=True)
	product = models.ForeignKey(Product, on_delete=models.CASCADE)
	category = models.CharField(max_length=120, choices=VAR_CATAGORIES, default='None')
	image_id = models.IntegerField(blank=True, null=True, default=0)
	quantity = models.IntegerField(default=1)
	active = models.BooleanField(default=True)

	objects = VariationManager()

	def __str__(self):
		return self.title

	def image(self):
		img = Images.objects.get(id=self.image_id)
		if img.id is not None:
			varimage=img.image.url
		else:
			varimage=""
		return varimage

	def image_tag(self):
		img = Images.objects.get(id=self.image_id)
		if img.id is not None:
			return mark_safe('<img src="{}" height="0"/>'.format(img.image.url))
		else:
			return ""


class Comment(models.Model):
	STATUS = (
		('New', 'New'),
		('True', 'True'),
		('False', 'False'),
	)
	product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	subject = models.CharField(max_length=100, blank=True, null=True)
	comment = models.CharField(max_length=300, blank=True, null=True)
	rate = models.IntegerField(default=1)
	ip = models.CharField(max_length=20, blank=True, null=True)
	status = models.CharField(max_length=10, choices=STATUS, default='New')
	create_at = models.DateTimeField(auto_now_add=True)
	update_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.subject

class CommentForm(ModelForm):
	class Meta:
		model = Comment
		fields = ['subject', 'comment']

class FAQ(models.Model):
	STATUS =(
		('True', 'True'),
		('False', 'False')
	)
	ordernumber = models.IntegerField()
	question = models.CharField(max_length=150)
	answer = models.TextField()
	status = models.CharField(max_length=10, choices=STATUS)
	create_at = models.DateTimeField(auto_now_add=True)
	update_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.question 

class ContactUs(models.Model):
	first_name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)
	email = models.EmailField(max_length=100)
	phone = models.CharField(max_length=100)
	massage = models.TextField()

	def __str__(self):
		return self.first_name
