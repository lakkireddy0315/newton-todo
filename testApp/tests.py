from django.test import TestCase
from .models import BlogCategory

class FirstTestCase(TestCase):
    def setUp(self):
        print("setup called")

    def test_equals(self):
        self.assertEqual(1,1)

    def test_blog_category(self):
        categories=['Abc','Def']
        for category in categories:
            obj=BlogCategory.objects.create(
                category_name=category
                )
            self.assertEquals(category,obj.category_name)

        objs=BlogCategory.objects.all()
        self.assertEqual(objs.count(),2)
