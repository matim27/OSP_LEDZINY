from django.db import models


class DepotTip(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


class TipsImage(models.Model):
    image = models.ImageField(upload_to='tip_images/')
    depot_tip = models.ForeignKey(DepotTip, on_delete=models.CASCADE)
    