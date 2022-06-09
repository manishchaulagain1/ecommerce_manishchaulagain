# Lab Report 2

## Objectives

* Intitializing the product_module.
* Making different modules suitable as per needs and registering to database.

***

## Introduction 

A model is the single, definitive source of information about data. It contains the essential fields and behaviors of the data that is being stored. Generally, each model maps to a single database table.

The basics:

* Each model is a Python class that subclasses django.db.models.Model.
* Each attribute of the model represents a database field.
* With all of this, Django gives an automatically-generated database-access AP

***

## Procedure

1. In 'models.py' create a model for brands

        class Brand(models.Model):
        name = models.CharField(max_length=200)
        is_active = models.BooleanField()

2. Add the brand table to the database by

        python manage.py makemigrations
        python manage.py migrate

3. In the 'admin.py' which add the content ot the admin panel add the following code :

        from .models import Brand
        admin.site.register(Brand)

4. Run the server and verify the table by performing the CRUDE operation.

        python manage.py runserver 

5. In the 'models.py' edit the code for the brand model with the following code:

        class Brand(models.Model):
        name = models.CharField(max_length=200)
        is_active = models.BooleanField()

6. In the same edit the code for the category model

        class Category(models.Model):
        name = models.CharField(max_length=200)
        is_active = models.BooleanField()
        class Meta:
        verbose_name_plural = "Categories"

7. Add the necessary fields to the product model

        class Product(models.Model):
        name = models.CharField(max_length=200)
        price = models.FloatField()
        quantity = models.IntegerField()
        image_url = models.CharField(max_length=500)
        color_code = models.CharField(max_length=20)
        brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
        category = models.ForeignKey(Category, on_delete=models.CASCADE)
        registered_on = models.DateTimeField()
        is_active = models.BooleanField()

8. Save the changes to the database. 

9. To enable the category and product models in the admin interface, add the following code in 'admin.py'

        from .models import Brand, Category, Product
        admin.site.register(Brand)
        admin.site.register(Category)
        admin.site.register(Product)

10. Run the project server and verify the CRUD operations for brand, category and product respectively

        python manage.py runserver

***

## Output 

![](https://github.com/manishchaulagain1/ecommerce_manishchaulagain/blob/main/lab_manual/lab2/assets/lab2.1.png)
![](https://github.com/manishchaulagain1/ecommerce_manishchaulagain/blob/main/lab_manual/lab2/assets/lab2.2.png)
![](https://github.com/manishchaulagain1/ecommerce_manishchaulagain/blob/main/lab_manual/lab2/assets/lab2.3.png)

## Conclusion

Here from this lab session we got to know about how to create a model, edit the model in an appropriate manner, and enter and evaluate the entered data in the django server database.