from django.db import models


class Customer(models.Model):
    customer_id = models.AutoField("ID", primary_key=True)
    email = models.EmailField("E-mail", max_length=128)
    first_name = models.CharField("First Name", max_length=128)
    last_name = models.CharField("Last Name", max_length=128)

    def __str__(self):
        return '%s %s' % (self.first_name, self.last_name)


class Order(models.Model):
    order_id = models.AutoField("ID", primary_key=True)
    product = models.CharField("Product", max_length=128)
    order_date = models.DateField("Order Date")
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)

    def __str__(self):
        return '%s %s' % (self.order_id, self.product)
