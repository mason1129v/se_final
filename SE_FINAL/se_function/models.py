from django.db import models

# Create your models here.

class Store(models.Model):
    store_id = models.AutoField("店家ID",primary_key=True)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    class Meta:
        verbose_name = "店家"
        verbose_name_plural = "店家"

    

class Member(models.Model):
    member_id = models.AutoField(primary_key=True)
    account = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    level = models.CharField(max_length=50)
    join_date = models.DateField()
    phone = models.CharField(max_length=20)
    email = models.EmailField()

    STATUS_CHOICES = [
        ('興趣', '興趣'),
        ('關注', '關注'),
        ('購買', '購買'),
    ]

    status = models.CharField(max_length=50, choices=STATUS_CHOICES )
    employee_id = models.IntegerField()
    store_id = models.IntegerField()

    class Meta:
        verbose_name = "會員"
        verbose_name_plural = "會員"

    def __str__(self):
        return self.name


class Employee(models.Model):
    employee_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)

    POSITION_CHOICES = [
        ('銷售', '銷售'),
        ('經理', '經理'),
    ]

    position = models.CharField(max_length=100, choices = POSITION_CHOICES)
    address = models.CharField(max_length=200)
    hire_date = models.DateField()
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    store_id = models.IntegerField()

    class Meta:
        verbose_name = "員工"
        verbose_name_plural = "員工"

    def __str__(self):
        return self.name


class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.IntegerField()
    stock = models.IntegerField()

    CATEGORY_CHOICES = [
        ('按摩椅', '按摩椅'),
    ]

    category = models.CharField(max_length=100, choices = CATEGORY_CHOICES )

    STATUS_CHOICES = [
        ('可購買', '可購買'),
        ('缺貨', '缺貨')
    ]

    status = models.CharField(max_length=50, choices = STATUS_CHOICES )
    store_id = models.IntegerField()

    class Meta:
        verbose_name = "商品"
        verbose_name_plural = "商品"

    def __str__(self):
        return self.name


class PurchaseRecord(models.Model):
    purchase_record_id = models.AutoField(primary_key=True)
    product_id = models.IntegerField()
    store_id = models.IntegerField()
    purchase_date = models.DateField()
    purchase_quantity = models.IntegerField()
    purchase_unit_price = models.IntegerField()
    total_price = models.IntegerField()

    class Meta:
        verbose_name = "進貨紀錄"
        verbose_name_plural = "進貨紀錄"

    def __str__(self):
        return f"Purchase Record ID: {self.purchase_record_id}"
    
from django.db import models

class SalesRecord(models.Model):
    sales_record_id = models.AutoField(primary_key=True)
    member_id = models.IntegerField()
    employee_id = models.IntegerField()
    product_id = models.IntegerField()
    store_id = models.IntegerField()
    sales_date = models.DateField()
    sales_quantity = models.IntegerField()
    product_unit_price = models.IntegerField()
    warranty_period = models.CharField( max_length = 100 )
    PAYMENT_CHOICES = [
        ('信用卡', '信用卡'),
        ('現金', '現金'),
    ]
    payment_method = models.CharField( max_length=100, choices=PAYMENT_CHOICES )
    total_amount = models.IntegerField()

    class Meta:
        verbose_name = "銷售紀錄"
        verbose_name_plural = "銷售紀錄"

    def __str__(self):
        return f"Sales Record ID: {self.sales_record_id}"


class SalesTechnique(models.Model):
    sales_technique_id = models.AutoField(primary_key=True)
    sales_technique_name = models.CharField(max_length=100)  # 可以加選項
    sales_technique_description = models.TextField()

    class Meta:
        verbose_name = "推銷手法"
        verbose_name_plural = "推銷手法"

    def __str__(self):
        return self.sales_technique_name


class StoreReview(models.Model):
    sreview_id = models.AutoField(primary_key=True)
    store_id = models.IntegerField()
    member_id = models.IntegerField()
    score = models.DecimalField(max_digits=3, decimal_places=1)
    review_content = models.TextField()
    review_date = models.DateField()

    class Meta:
        verbose_name = "店家評價"
        verbose_name_plural = "店家評價"

    def __str__(self):
        return f"Review ID: {self.sreview_id}"


class EmployeeServiceReview(models.Model):
    ereview_id = models.AutoField(primary_key=True)
    member_id = models.IntegerField()
    employee_id = models.IntegerField()
    score = models.DecimalField(max_digits=3, decimal_places=1)
    review_content = models.TextField()
    review_date = models.DateField()

    class Meta:
        verbose_name = "服務評價"
        verbose_name_plural = "服務評價"

    def __str__(self):
        return f"Review ID: {self.ereview_id}"


class StoreSalesTarget(models.Model):
    sales_target_id = models.AutoField(primary_key=True)
    store_id = models.IntegerField()
    target_year = models.IntegerField()
    target_month = models.IntegerField()
    target_amount = models.IntegerField()
    target_quantity = models.IntegerField()

    class Meta:
        verbose_name = "店家業績目標"
        verbose_name_plural = "店家業績目標"

    def __str__(self):
        return f"Sales Target ID: {self.sales_target_id}"


class EmployeeSalesTarget(models.Model):
    sales_target_id = models.AutoField(primary_key=True)
    employee_id = models.IntegerField()
    target_year = models.IntegerField()
    target_month = models.IntegerField()
    target_amount = models.IntegerField()
    target_quantity = models.IntegerField()

    class Meta:
        verbose_name = "員工業績目標"
        verbose_name_plural = "員工業績目標"

    def __str__(self):
        return f"Sales Target ID: {self.sales_target_id}"


class TransactionRecord(models.Model):
    sales_record_id = models.AutoField(primary_key=True)
    sales_date = models.DateField()
    member_id = models.IntegerField()
    employee_id = models.IntegerField()
    sales_technique_id = models.IntegerField()

    class Meta:
        verbose_name = "推銷紀錄"
        verbose_name_plural = "推銷紀錄"

    def __str__(self):
        return f"Sales Record ID: {self.sales_record_id}"


class PublicMassageChair(models.Model):
    chair_id = models.AutoField(primary_key=True)
    store_id = models.IntegerField()
    location_id = models.IntegerField()
    STATUS_CHOICES = [
        ('可使用', '可使用'),
        ('不可使用', '不可使用'),
    ]
    status = models.CharField(max_length=100, choices=STATUS_CHOICES)

    class Meta:
        verbose_name = "公共按摩椅"
        verbose_name_plural = "公共按摩椅"

    def __str__(self):
        return f"Chair ID: {self.chair_id}"


class PublicMassageChairUsageRecord(models.Model):
    usage_record_id = models.AutoField(primary_key=True)
    chair_id = models.IntegerField()
    member_id = models.IntegerField()
    usage_date = models.DateField()
    usage_time = models.IntegerField()
    fee = models.IntegerField()

    class Meta:
        verbose_name = "公共按摩椅使用紀錄"
        verbose_name_plural = "公共按摩椅使用紀錄"

    def __str__(self):
        return f"Usage Record ID: {self.usage_record_id}"


class PublicMassageChairLocation(models.Model):
    location_id = models.AutoField(primary_key=True)
    store_id = models.IntegerField()
    location_name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)

    class Meta:
        verbose_name = "公共按摩椅服務據點"
        verbose_name_plural = "公共按摩椅服務據點"

    def __str__(self):
        return self.location_name


class RevenueRecord(models.Model):
    record_id = models.AutoField(primary_key=True)
    store_id = models.IntegerField()
    revenue_year = models.IntegerField()
    revenue_month = models.IntegerField()
    revenue_amount = models.IntegerField()

    class Meta:
        verbose_name = "營收紀錄"
        verbose_name_plural = "營收紀錄"
    def __str__(self):
        return f"Record ID: {self.record_id}"

