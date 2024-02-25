from django.db import models

class Contact(models.Model):
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.name

'''
var myVariable = document.getElementById("myData").getAttribute("data-my-variable");

'''