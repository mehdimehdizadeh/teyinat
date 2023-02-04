from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Subcategory(models.Model):
    subcategory = models.CharField(max_length=150,verbose_name="Subkateqoriya")
    
    def __str__(self):
        return self.subcategory
    class Meta:
        verbose_name = "Subkateqoriya"
        verbose_name_plural = "Subkateqoriyalar"
        ordering = ['-id']

class Category(models.Model):
    category = models.CharField(max_length=150,verbose_name="Kateqoriya")
    subcategory = models.ManyToManyField(Subcategory,blank=True,verbose_name="Subkateqoriya",related_name="subcategories")

    def __str__(self):
        return self.category
    
    class Meta:
        verbose_name = "Kateqoriya"
        verbose_name_plural = "Kateqoriyalar"
        ordering = ['-id']

class user(models.Model):
    name_and_surname = models.CharField(max_length=150,verbose_name="Ad və soyad")
    image = models.ImageField(blank = True,null=True,verbose_name="Şəkil")

    def __str__(self):
        return self.name_and_surname
    
    class Meta:
        verbose_name = "Yazar"
        verbose_name_plural = "Yazarlar"

class Article(models.Model):
    user = models.ManyToManyField(user,verbose_name="Yazar",blank=True,related_name="users")
    category = models.ManyToManyField(Category,verbose_name="Kateqoriya",blank=True)
    subcategory = models.ManyToManyField(Subcategory,verbose_name="Subkateqoriya",blank=True)
    title = models.CharField(max_length=150,verbose_name="Başlıq")
    subtitle = models.CharField(max_length=150,verbose_name="Altbaşlıq")
    image = models.ImageField(blank=True,null=True,verbose_name="Şəkil")
    content = RichTextField(verbose_name="Məzmun")
    like = models.IntegerField(default=0,verbose_name="Like")
    view = models.IntegerField(default=0,verbose_name="Baxış sayı")
    comment_count = models.IntegerField(verbose_name="Kommentsayı",default=0)
    created_date = models.DateTimeField(auto_now_add=True,verbose_name="Paylaşım vaxtı")

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Postlar"
        ordering = ['-created_date']

class indexpage(models.Model):
    title = models.CharField(max_length=150,verbose_name="Başlıq")
    icon  = models.ImageField(verbose_name="Icon",blank = True,null= True)
    logo  = models.ImageField(verbose_name="Logo",blank = True,null= True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Index səhifəsinin məlumatları"
        verbose_name_plural = "İndex səhifəsinin məlumatları"

class sosials(models.Model):
    code = models.CharField(max_length=150,verbose_name="Şəbəkənin adı (ingiliscə) ")
    link =  models.CharField(max_length=500,verbose_name="Link")

    def __str__(self):
        return self.code
    
    class Meta:
        verbose_name = "Sosial şəbəkə"
        verbose_name_plural = "Sosial şəbəkələr"

