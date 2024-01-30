from django.db import models


class Auto(models.Model):
    STATUS_CHOICES = (
        ('Free', 'free'),
        ('In rent', 'in rent'),
    )

    user = models.ForeignKey('AutoUser', on_delete=models.CASCADE)
    model = models.ForeignKey('AutoModel', on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Free')
    vin_number = models.CharField(max_length=25)

    # def __str__(self):
    #     return f'()'


class AutoModel(models.Model):
    brand = models.ForeignKey('AutoBrand', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.brand})'


class AutoBrand(models.Model):
    logo = models.ImageField(upload_to='')
    name = models.CharField(max_length=15)


class AutoUser(models.Model):
    phone_number = models.CharField(max_length=15)
    name = models.CharField(max_length=255)
