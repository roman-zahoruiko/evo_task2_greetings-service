from django.db import models


class UserData(models.Model):
    data = models.CharField(max_length=50)

    def __str__(self):
        return self.data[:15]

    class Meta:
        ordering = ('-pk',)

