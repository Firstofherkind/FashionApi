from django.db import models

# Create your models here.


class Category(models.Model):
    title = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.title


class Product(models.Model):
    name = models.CharField(max_length=20)
    product_tag = models.CharField(max_length=50)
    category = models.ForeignKey(Category,related_name='products', on_delete=models.CASCADE)
    status = models.BooleanField(default=True)
    stock  = models.IntegerField()
    price = models.IntegerField()
    image_url = models.URLField()
    date_posted = models.DateField(auto_now_add=True)
    colour = models.CharField(max_length=20, default='Black')
    

    class Meta:
        ordering = ['-date_posted']

    def __str__(self):
        return '{} {} {}'.format(self.product_tag, self.name, self.price)