from django.contrib import admin
from .models import Store, Member, Employee, Product, PurchaseRecord, SalesRecord, SalesTechnique, StoreReview, EmployeeServiceReview, StoreSalesTarget, EmployeeSalesTarget, TransactionRecord, PublicMassageChair, PublicMassageChairUsageRecord, PublicMassageChairLocation, RevenueRecord

class StoreAdmin(admin.ModelAdmin):
    list_display = ('store_id', 'name', 'address', 'phone', 'email')
    ordering = ('store_id',)

class MemberAdmin(admin.ModelAdmin):
    list_display = ('member_id', 'account', 'password', 'name', 'address', 'level', 'join_date', 'phone', 'email', 'status', 'employee_id', 'store_id')
    ordering = ('member_id',)

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('employee_id', 'name', 'position', 'address', 'hire_date', 'phone', 'email', 'store_id')
    ordering = ('employee_id',)

class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_id', 'name', 'description', 'price', 'stock', 'category', 'status', 'store_id')
    ordering = ('product_id',)

class PurchaseRecordAdmin(admin.ModelAdmin):
    list_display = ('purchase_record_id', 'product_id', 'store_id', 'purchase_date', 'purchase_quantity', 'purchase_unit_price', 'total_price')
    ordering = ('purchase_record_id',)

class SalesRecordAdmin(admin.ModelAdmin):
    list_display = ('sales_record_id', 'member_id', 'employee_id', 'product_id', 'store_id', 'sales_date', 'sales_quantity', 'product_unit_price', 'warranty_period', 'payment_method', 'total_amount')
    ordering = ('sales_record_id',)

class SalesTechniqueAdmin(admin.ModelAdmin):
    list_display = ('sales_technique_id', 'sales_technique_name', 'sales_technique_description')
    ordering = ('sales_technique_id',)

class StoreReviewAdmin(admin.ModelAdmin):
    list_display = ('sreview_id', 'store_id', 'member_id', 'score', 'review_content', 'review_date')
    ordering = ('sreview_id',)

class EmployeeServiceReviewAdmin(admin.ModelAdmin):
    list_display = ('ereview_id', 'member_id', 'employee_id', 'score', 'review_content', 'review_date')
    ordering = ('ereview_id',)

class StoreSalesTargetAdmin(admin.ModelAdmin):
    list_display = ('sales_target_id', 'store_id', 'target_year', 'target_month', 'target_amount', 'target_quantity')
    ordering = ('sales_target_id',)

class EmployeeSalesTargetAdmin(admin.ModelAdmin):
    list_display = ('sales_target_id', 'employee_id', 'target_year', 'target_month', 'target_amount', 'target_quantity')
    ordering = ('sales_target_id',)

class TransactionRecordAdmin(admin.ModelAdmin):
    list_display = ('sales_record_id', 'sales_date', 'member_id', 'employee_id', 'sales_technique_id')
    ordering = ('sales_record_id',)

class PublicMassageChairAdmin(admin.ModelAdmin):
    list_display = ('chair_id', 'store_id', 'location_id', 'status')
    ordering = ('chair_id',)

class PublicMassageChairUsageRecordAdmin(admin.ModelAdmin):
    list_display = ('usage_record_id', 'chair_id', 'member_id', 'usage_date', 'usage_time', 'fee')
    ordering = ('usage_record_id',)

class PublicMassageChairLocationAdmin(admin.ModelAdmin):
    list_display = ('location_id', 'store_id', 'location_name', 'address')
    ordering = ('location_id',)

class RevenueRecordAdmin(admin.ModelAdmin):
    list_display = ('record_id', 'store_id', 'revenue_year', 'revenue_month', 'revenue_amount')
    ordering = ('record_id',)

# Register your models here.
admin.site.register(Store, StoreAdmin)
admin.site.register(Member, MemberAdmin)
admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(PurchaseRecord, PurchaseRecordAdmin)
admin.site.register(SalesRecord, SalesRecordAdmin)
admin.site.register(SalesTechnique, SalesTechniqueAdmin)
admin.site.register(StoreReview, StoreReviewAdmin)
admin.site.register(EmployeeServiceReview, EmployeeServiceReviewAdmin)
admin.site.register(StoreSalesTarget, StoreSalesTargetAdmin)
admin.site.register(EmployeeSalesTarget, EmployeeSalesTargetAdmin)
admin.site.register(TransactionRecord, TransactionRecordAdmin)
admin.site.register(PublicMassageChair, PublicMassageChairAdmin)
admin.site.register(PublicMassageChairUsageRecord, PublicMassageChairUsageRecordAdmin)
admin.site.register(PublicMassageChairLocation, PublicMassageChairLocationAdmin)
admin.site.register(RevenueRecord, RevenueRecordAdmin)

