from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField('Name',max_length=200)
    create_date = models.DateField('Created On')
    def __str__(self):
        return self.name


class Expense(models.Model):
    category = models.ForeignKey(Category,models.SET_NULL,blank=True,null=True)
    name = models.CharField('Name',max_length=200)
    amount = models.DecimalField('Amount',max_digits=10, decimal_places=2)
    date = models.DateField('Occured On')
    notes = models.CharField('Notes',max_length=500)
    def __str__(self):
        return self.name + ' | ' + str(self.amount)
