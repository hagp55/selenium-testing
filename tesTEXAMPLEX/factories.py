import factory
from django.contrib.auth.models import User
from faker import Faker

from core.app1.models import Category, Product

fake = Faker()


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = fake.name()
    is_staff = True



class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model  = Category
    name = 'Django'


class ProductFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Product
    title = 'Product title'
    category = factory.SubFactory(CategoryFactory)
    description = fake.text()
    slug = 'product_slug'
    regular_price = '9.99'
    discount_price = '4.99'