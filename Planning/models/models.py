class Treasure(models.Model):
    title = models.CharField(max_length=1000)
    description = models.CharField(max_length=1000)
    img_url = models.TextField()

    def __str__(self):
        return self.name

class User() ===> This is dictated by the Django User Class.