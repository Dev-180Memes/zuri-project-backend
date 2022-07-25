from django.db import models


class Product(models.Model):
    title       = models.CharField(max_length=120)
    slug        = models.SlugField(unique=True)
    category    = models.ForeignKey('Category', on_delete=models.CASCADE) 
    description = models.TextField(blank=True,null=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Product,self).save(*args, **kwargs)

    def get_absolute_url(self):
        return self.slug

class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    parent = models.ForeignKey('self',blank=True, null=True,related_name='child', on_delete=models.CASCADE)
    class Meta:
        unique_together = ('slug', 'parent',)    
        verbose_name_plural = "categories"   

    def __str__(self):                           
        full_path = [self.name]            
        k = self.parent
        while k is not None:
            full_path.append(k.name)
            k = k.parent

        return ' -> '.join(full_path[::-1])




