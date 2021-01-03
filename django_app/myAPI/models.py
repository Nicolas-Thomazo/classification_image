
class satellite(models.Model):

    
    pixel1=models.IntegerField(default=0)
    pixel2=models.IntegerField(default=0)
    pixel3=models.IntegerField(default=0)
    pixel4=models.IntegerField(default=0)

def __str__(self):
		return '{}, {}'.format(self.pixel1, self.pixel2)




#class satellite(models.Model):
    