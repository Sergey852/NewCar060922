from django.db import models

# Create your models here.
#============================Base===============================
class HomeSlider(models.Model):
    name1 = models.CharField('Slider name1', max_length=30)
    name2 = models.CharField('Slider name2', max_length=30)
    about = models.TextField('Slider about')
    img = models.ImageField('Slider image', upload_to='media')

    def __str__(self):
        return self.name1

    class Meta:
        verbose_name = 'HomeSlider'
        verbose_name_plural = 'HomeSliders'
class Banner(models.Model):
    banner_title = models.CharField('Banner title', max_length=30)
    description = models.TextField('Banner description')
    Banner_url = models.URLField('Banner video url', max_length = 200)

    def __str__(self):
        return self.banner_title

    class Meta:
        verbose_name = 'Banner'
        verbose_name_plural = 'Banners'

class Social(models.Model):
    facebook = models.URLField('Facebook url', max_length = 200)
    twitter = models.URLField('Twitter url', max_length = 200)
    linkedin = models.URLField('Linkedin url', max_length = 200)
    youtube = models.URLField('Youtube url', max_length = 200)
    be = models.URLField('Be url', max_length = 200)

    def __str__(self):
        return self.facebook

    class Meta:
        verbose_name = 'Social'
        verbose_name_plural = 'Socials'
#==================================================================
#======================Hom page==================================
class HomeOnecolumn(models.Model):
    image = models.ImageField('Column image', upload_to = 'media')
    title = models.CharField('Column title', max_length=30)
    text = models.TextField('Column text')
    text1 = models.TextField('Column text1')
    onecolumnurl = models.URLField('Column url', max_length = 200)
    about = models.TextField("Detals")


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'HomeOnecolumn'
        verbose_name_plural = 'HomeOnecolumns'

class HomeTwocolumns(models.Model):
    image = models.ImageField('Column image', upload_to = 'media')
    title = models.CharField('Column title', max_length=30)
    text = models.TextField('Column text')
    text1 = models.TextField('Column text1')
    onecolumnurl = models.URLField('Column url', max_length = 200)
    about = models.TextField("Detals")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'HomeTwocolumns'
        verbose_name_plural = 'HomeTwocolumns'

class HomeThreecolumns(models.Model):
    image = models.ImageField('Column image', upload_to = 'media')
    title = models.CharField('Column title', max_length=30)
    text = models.TextField('Column text')
    text1 = models.TextField('Column text1')
    onecolumnurl = models.URLField('Column url', max_length = 200)
    about = models.TextField("Detals")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'HomeThreecolumns'
        verbose_name_plural = 'HomeThreecolumns'

class Callus(models.Model):
    image = models.ImageField('Product image', upload_to = 'media')
    title = models.CharField('Product name', max_length=30)
    tell = models.CharField('Tell number', max_length=30)
    
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Callus'
        verbose_name_plural = 'Callus'
#============================================================
#======================Products===========================
class Newcategory(models.Model):
    title = models.CharField('Category name', max_length=30)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Newcategory'
        verbose_name_plural = 'Newcategorys'

class Car(models.Model):
    category = models.ManyToManyField(Newcategory, related_name='carcateg1')
    image = models.ImageField('Car image', upload_to = 'media')
    title = models.TextField('Car about')
    price = models.CharField('Car price', max_length=30)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Car'
        verbose_name_plural = 'Cars'
#======================================================

#========================Services==========================
class Customer_services(models.Model):
    title = models.CharField("Customer_services title", max_length = 30)
    about = models.TextField("Customer_services about")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Customer_services'
        verbose_name_plural = 'Customer_services'

class Services_second_column(models.Model):
    image = models.ImageField('Services_second_column image', upload_to = 'media')
    title = models.CharField('Services_second_column title', max_length=30)
    text = models.TextField('Services_second_column text')
    columnurl = models.URLField('Services_second_column url', max_length = 200)
    about = models.TextField("Detals")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Services_second_column'
        verbose_name_plural = 'Services_second_columns'

#=================================================================
#===========================Gallery============================
class Galleryphoto(models.Model):
    img = models.ImageField("Galleryphoto image", upload_to = "media")
    modclass = models.CharField("Galleryphoto class", max_length=30)
    title = models.CharField("Galleryphoto title", max_length=30)
    about = models.TextField('Galleryphotoabout about')

    
    def __str__(self):
        return self.title

    class Meta:
        verbose_name ="Galleryphoto"
        verbose_name_plural="Galleryphotos"


class Aboutus(models.Model):
    img = models.ImageField("Aboutus image", upload_to="media")
    title = models.CharField("Aboutus title", max_length=40)
    text1 = models.TextField("Aboutus text1")
    text2 = models.TextField("Aboutus text2")
    details = models.TextField("Aboutus about")
    
    def __str__(self):
        return self.title

    class Meta:
        verbose_name ="Aboutus"
        verbose_name_plural="Aboutuss"

class Aboutus2(models.Model):
    img = models.ImageField("Aboutus image", upload_to="media")
    title = models.CharField("Aboutus title", max_length=40)
    text2 = models.TextField("Aboutus text2")
    details = models.TextField("Aboutus about")
    
    def __str__(self):
        return self.title

    class Meta:
        verbose_name ="Aboutus2"
        verbose_name_plural="Aboutuss2"