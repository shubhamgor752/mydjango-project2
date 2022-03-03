from django.db import models
from django.utils import timezone

# Create your models here.

class Contact(models.Model):
	name=models.CharField(max_length=100)
	phonenumber=models.CharField(max_length=100)
	email=models.CharField(max_length=100)
	address=models.TextField()

	def __str__(self):
		return self.name

class User(models.Model):
	fname=models.CharField(max_length=100)
	lname=models.CharField(max_length=100)
	email=models.CharField(max_length=100)
	mobile=models.CharField(max_length=100)
	address=models.TextField()
	password=models.CharField(max_length=100)
	usertype=models.CharField(max_length=100,default="user")


	def __str__(self):
		return self.fname

class Product(models.Model):
	CHOICE=(
		('Nike','Nike'),
		('Fasttrack','Fasttrack'),
		('G Shock','G Shock'),
		('Puma','Puma'),
		('Hublot','Hublot'),
		('Alleny Solly','Alleny Solly'),
		('Raymond','Raymond'),
		)
	seller=models.ForeignKey(User,on_delete=models.CASCADE)
	product_category=models.CharField(max_length=100,choices=CHOICE)
	product_model=models.CharField(max_length=100)
	product_price=models.IntegerField()
	product_desc=models.TextField()
	product_image=models.ImageField(upload_to="product_images/")	


	def __str__(self):
		return self.seller.fname+" - "+self.product_category


class Wishlist(models.Model):
	user=models.ForeignKey(User,on_delete=models.CASCADE)
	product=models.ForeignKey(Product,on_delete=models.CASCADE)
	date=models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.user.fname+" - "+self.product.product_category

class Cart(models.Model):
	user=models.ForeignKey(User,on_delete=models.CASCADE)
	product=models.ForeignKey(Product,on_delete=models.CASCADE)
	date=models.DateTimeField(default=timezone.now)
	product_price=models.IntegerField()
	product_qty=models.IntegerField(default=1)
	total_price=models.IntegerField()
	status=models.BooleanField(default=False)

	def __str__(self):
		return self.user.fname+" - "+self.product.product_category

class Transaction(models.Model):
    made_by = models.ForeignKey(User, related_name='transactions',on_delete=models.CASCADE)
    made_on = models.DateTimeField(auto_now_add=True)
    amount = models.IntegerField()
    order_id = models.CharField(unique=True, max_length=100, null=True, blank=True)
    checksum = models.CharField(max_length=100, null=True, blank=True)

    def save(self, *args, **kwargs):
        if self.order_id is None and self.made_on and self.id:
            self.order_id = self.made_on.strftime('PAY2ME%Y%m%dODR') + str(self.id)
        return super().save(*args, **kwargs)
