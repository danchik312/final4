from django.db import models

class Slogan(models.Model):
    text = models.CharField(max_length=200)

    def __str__(self):
        return self.text

class YouTubeVideo(models.Model):
    title = models.CharField(max_length=200)
    video_url = models.URLField()

    def __str__(self):
        return self.title

class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')
    author = models.CharField(max_length=100)
    content = models.TextField()

    def __str__(self):
        return f'Review by {self.author} for {self.product.name}'
