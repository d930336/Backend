from django.db import models

# Create your models here.
class Coupon(models.Model):
    coupon_id = models.CharField(max_length=20,primary_key=True)
    coupon_title = models.CharField(max_length=150)
    coupon_class = models.CharField(max_length=20)
    coupon_content = models.CharField(max_length=200)
    coupon_create_at = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ('coupon_create_at',)

    def __str__(self):
        return self.coupon_title

class User(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    user_id = models.CharField(max_length=20)
    user_name = models.CharField(max_length=20)
    user_gender = models.CharField(max_length=1,choices=GENDER_CHOICES)
    user_create_at = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ('user_create_at',)

    def __str(self):
        return self.user_name