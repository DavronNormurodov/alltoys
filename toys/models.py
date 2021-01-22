from django.db import models

# Create your models here.

class ActiveObjectsManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_active=True)

class User(models.Model):
    is_active = models.BooleanField(default=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.IntegerField()

    objects = models.Manager()
    active_objects = ActiveObjectsManager()

class Toy(models.Model):
    name = models.CharField(max_length=100)
    # user o'chirilsa toy ham o'chadi
    user = models.ForeignKey(User, related_name='toys', on_delete=models.CASCADE, null=True, blank=True)

    # # user o'chirilsa toylari null boladi
    # user = models.ForeignKey(User, related_name='toys', on_delete=models.SET_NULL, null=True, blank=True)

    # # userni o'chirmoqchi bo'lsak oldin uni toylarini o'chirishimizni so'raydi
    # user = models.ForeignKey(User, related_name='toys', on_delete=models.PROTECT, null=True, blank=True)
    description = models.TextField(null=True, blank=True)