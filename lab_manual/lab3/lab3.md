# Lab Report 3

## Objectives

* To implement the search operations in the modeles.
* Implement the image tag to store and display image in the product model.

***

## Introduction 

In application, search works like a regular search engine.Users types their query and then can view their searched results as per the requirement.

***

## Procedure

1. In 'admin.py' implement the following code:

        class ProductAdmin(admin.ModelAdmin):
                list_display = ["name", "price", "brand", "category",]
                search_fields = ["name", "price", "brand__name", "category__name",]
                list_filter = ["brand","category",]
                readonly_fields = ["quantity",]
                class Meta:
                model = Product
        admin.site.register(Product, ProductAdmin)

In this code the "search_fiels" is implemeted for the usage of search of refrenced table i.e brand whose primary key is refrenced as a foreign key.

2. Similarly implement the same changes in other models as well:

        #Implementaion of search in the brand model:
        class BrandAdmin(admin.ModelAdmin):
                list_display = ["name",]
                search_fields = ["name",]
                class Meta:
                        model = Brand
        admin.site.register(Brand, BrandAdmin)

        #Implementation of search in the category model:
        class CategoryAdmin(admin.ModelAdmin):
                list_display = ["name",]
                search_fields = ["name",]
                class Meta:
                        model = Category
        admin.site.register(Category, CategoryAdmin)

3. Add the field for displaying the image in the list view. For this add a field "image_tag" to the product class in the 'models.py' to enter the image urls in the database.

        #import the mark_safe from the django.utils.html first:
        from django.utils.html import mark_safe

        #add the following code to add the image_url field in the model:
        class Product(models.Model):
        ...
                def image_tag(self):
                        return mark_safe(f'<img src="{self.image_url}" width="50" height="50" />')
                 image_tag.short_description = "Product"
                def __str__(self):
                        return self.name

Usage of mark_safe is to mark a custom string as a safe string for HTML/output rendering.      

4. In the class ProductAdmin in 'admin.py' implement the follwing changes:

        class ProductAdmin(admin.ModelAdmin):
                list_display = ["image_tag", "name", "price", "brand", "category",]
                search_fields = ["name", "price", "brand__name", "category__name",]
                list_filter = ["brand","category","price",]
                #readonly_fields = ["quantity",]
        class Meta:
        model = Product
        admin.site.register(Product, ProductAdmin)

5. Run the project and navigate to admin to check the reesult

        python manage.py runserver

***

## Output 


## Conclusion

Here from this lab session we got to know about how to implement the search engine in a particular module, inset the images in the database by entering the images link address and displaying it in the list view.