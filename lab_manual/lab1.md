# Lab Report 1

## Objectives

* To create local and remote git repository and perform necessary git commands
* To prepare development environment, and run a simple project.

***

## Introduction 

Our first lab was a introductory session on how to start the project.It mainly focused on setting up the development environment to run the Django ecommerce project. The lab also foused on creating local and remote repository using Git and performing basic Git commands.

**Git**

Git is a software for tracking changes in any set of files, usually used for coordinating work among programmers collaboratvely developing source code during software development. Its goals includes speed, data integrity, and support for distributed, non-linear workflows.

**Visual Studio Code**

Visual Studio Code, also commonly referred to as VS Code, is a source-code editor made by Microsoft for Windows, Linxu and macOS. Features include support for debugging, suntax highlighting, intelligent code completion, snippets, code refactoring, and embedded Git.

**Django**

Django is a Python-based web framework, free and open-source, that follows the model-template-views architectural pattern.

***

## Procedure

1. Initialize django project 

        django-admin startprojectecommerce_yourname
        cd ecommerce_yourname

2. Open generated folder in VS code and inspect the created files/folders 

        code .

3. Ensure required database and tables are initialized correctly

        python manage.py migrate
        python manage.py createsuperuser

4. Verify that you have configured correctly

        python manage.py runserver 

    a. Verify frontend in browser: Open 'http://127.0.0.1:8000'

    b. Verify admin backend in browser: Open 'http://127.0.0.1:8000/admin'

5. Add a module product_module

        python manage.py startapp
        product_module

6. Go to settings.py and add the module to INSTALLED_APPS list 

        INSTALLED_APPS = [...,'product_module']

7. In the module, open "modules.py" and add code for Brand model 

        class Brand(models.Model):
            name = models.CharField(max_length=200)
            is_active = models.BooleanField()

8. Ensure database table for added model is created properly 

        python manage.py makemigrations
        python manage.py migrate

9. Goto “admin.py” and add the following code

        from .models import Brand
        admin.site.register(Brand)

10. Run the server and verify CRUD operation

        python manage.py runserver

11. Git add

        git add .

12. Git commit

        git commit -m "message"

13. Git push

        git push

***

## Output 

We performed basic setup and configured the necessary settings for further progress in the ecommerce project.The database and tables have been initialized and created. We can verify and check the output by going to the admin backend in the browser 'http://127.0.0.1:8000/admin'.Also, we were able to perform any CRUD operation as desired in the Brand section.

## Conclusion

In the very first lab, we set our development environmant and started our django project.After the neccessary database and tables initialized and created, we added a product module and performed CRUD operations in the server.Finally, we pushed our local repository to remote repository in GitHub using Git commands.