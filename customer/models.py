from django.contrib.auth.models import AbstractUser
from django.db import models

from products.models import Product


class User(AbstractUser):
    """
    Overriden model for users.
    """
    username = models.CharField('Username', blank=False, max_length=100, unique=True)
    email = models.EmailField('Email', default=False, blank=False)
    phone = models.CharField('Phone', max_length=12)

    REQUIRED_FIELDS = ['first_name', 'last_name', 'email', 'phone']
    USERNAME_FIELD = 'username'

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
        indexes = [models.Index(
            fields=['id', 'password', 'last_login', 'is_superuser', 'first_name', 'last_name', 'is_staff', 'is_active',
                    'date_joined', 'username', 'email', 'phone'])]

    def __str__(self):
        return self.username


class Order(models.Model):
    """
    Model for orders.
    """
    customer = models.ForeignKey(to=User, verbose_name='Customer', on_delete=models.SET_NULL, null=True, blank=True)
    date_ordered = models.DateTimeField('Date ordered', auto_now_add=True)
    completed = models.BooleanField('Completed', default=False)
    session = models.ForeignKey(to='sessions.Session', on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'
        indexes = [models.Index(fields=['id', 'date_ordered', 'completed', 'customer_id', 'session_id'])]

    @property
    def get_cart_total(self):
        order_items = self.orderitem_set.all()
        total = sum([item.get_total for item in order_items])
        return f"{total:.2f}"

    @property
    def get_cart_items(self):
        order_items = self.orderitem_set.all()
        total = sum([item.quantity for item in order_items])
        return total

    def __str__(self):
        if self.customer:
            customer = self.customer.username
        else:
            customer = "Anonymous user"
        return "Order number: " + str(self.id) + f", Customer: {customer}," + " Finished - " + str(self.completed)


class OrderItem(models.Model):
    """
    Model for order items.
    """
    product = models.ForeignKey(to=Product, verbose_name='Product', on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(to=Order, verbose_name='Order', on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField('Quantity', default=0, null=True, blank=True)
    date_added = models.DateTimeField('Date added', auto_now_add=True)

    class Meta:
        verbose_name = 'Order item'
        verbose_name_plural = 'Order items'
        indexes = [models.Index(fields=['id', 'quantity', 'date_added', 'order_id', 'product_id'])]

    @property
    def get_total(self):
        product_price = self.product.current_price if self.product.discount else self.product.price
        total = product_price * self.quantity
        return total

    def __str__(self):
        return f'{self.product}, {self.order}'


class LikedProduct(models.Model):
    """
    Model for liked products.
    """
    customer = models.ForeignKey(to=User, verbose_name='Customer', on_delete=models.CASCADE, null=True)
    session = models.ForeignKey(to='sessions.Session', verbose_name='Session', on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(to=Product, verbose_name='Product', on_delete=models.CASCADE, null=False)

    class Meta:
        verbose_name = 'Liked Product'
        verbose_name_plural = 'Liked Products'
        indexes = [models.Index(fields=['id', 'customer_id', 'product_id', 'session_id'])]

    def __str__(self):
        if self.customer:
            customer = self.customer.username
        else:
            customer = "Anonymous user"
        return f'{customer}, {self.product.name}'


class ProductReview(models.Model):
    """
    Model for product reviews.
    """
    review = models.TextField('Review', blank=False, null=False)
    customer = models.ForeignKey(to=User, verbose_name='Customer', on_delete=models.CASCADE)
    product = models.ForeignKey(to=Product, verbose_name='Product', on_delete=models.CASCADE)
    rating = models.FloatField('Rating', null=True)
    date_written = models.DateTimeField('Date written', auto_now_add=True)

    class Meta:
        verbose_name = 'Product Review'
        verbose_name_plural = 'Product Reviews'
        indexes = [models.Index(fields=['id', 'review', 'customer_id', 'product_id', 'date_written', 'rating'])]

    def __str__(self):
        return f'Customer: {self.customer}, Product: {self.product.name}, Rating: {self.rating}'


class ShippingDetails(models.Model):
    """
    Model for shipping details.
    """

    class PaymentType(models.IntegerChoices):
        PAYME = 1, 'PayMe'
        CLICK = 2, 'Click'

    customer = models.ForeignKey(to=User, verbose_name='Customer', on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(to=Order, verbose_name='Order', on_delete=models.SET_NULL, null=True)
    address = models.CharField('Address', max_length=200, null=False)
    city = models.CharField('City', max_length=200, null=False)
    state = models.CharField('State', max_length=200, null=False)
    zipcode = models.CharField('Zipcode', max_length=200, null=False)
    payment_type = models.SmallIntegerField('Payment type', choices=PaymentType.choices)
    date_added = models.DateTimeField('Date added', auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Shipping Details'

    def __str__(self):
        if self.payment_type == 1:
            payment_type = 'PayMe'
        else:
            payment_type = 'Click'
        return f'Customer: {self.customer.username}, Payment method: {payment_type}, Order #: {self.order_id}, ' \
               f'State: {self.state}, City: {self.city}, Address: {self.address}, Zipcode: {self.zipcode} '


class EmailSubscription(models.Model):
    """
    Model for email subscriptions.
    """
    email = models.EmailField('Email', unique=True)

    class Meta:
        verbose_name = 'Email Subscription'
        verbose_name_plural = 'Email Subscriptions'

    def __str__(self):
        return self.email


class ContactMessage(models.Model):
    """
    Model for contact messages.
    """
    name = models.CharField('Name', max_length=30, null=False)
    contact_email = models.EmailField('Email')
    message = models.TextField('Message', max_length=200, null=False)

    class Meta:
        verbose_name = 'Contact Message'
        verbose_name_plural = 'Contact Messages'

    def __str__(self):
        return f'{self.name}, {self.contact_email}'
