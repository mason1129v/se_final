from django.shortcuts import render
from django.db.models import Sum, Avg
from decimal import Decimal, ROUND_HALF_UP
from collections import Counter
from .models import *
# Create your views here.

month = 5


def index_view(request):

    try:
        April = RevenueRecord.objects.get(revenue_month = (month - 1 ) )
        May = RevenueRecord.objects.get(revenue_month = month )
        m = May.revenue_amount
        a = April.revenue_amount
        t1 = StoreSalesTarget.objects.get(target_month = month )
        t = t1.target_amount
        t_number = '{:,}'.format(t)
        previous_month_amount = '{:.2f}'.format( m / t * 100 )
        r1 = StoreReview.objects.filter(store_id = 1 )
        total_score = round(r1.aggregate(average=Avg('score'))['average'], 1)
        count = StoreReview.objects.filter( store_id = 1 ).count()

        employee_ids = Employee.objects.values_list('employee_id', flat=True)
        employee_data = []
        for employee_id in employee_ids:
            employee = Employee.objects.get(employee_id=employee_id)
            tar = employee.monthly_target
            sold = SalesRecord.objects.filter(employee_id=employee_id)
            soldamount = sold.aggregate(average=Sum('total_amount'))['average']
            if soldamount is not None and tar is not None:
                percent = soldamount / tar * 100
            else:
                percent = 0  # 设置默认值或采取其他处理方法
            
            reviews = EmployeeServiceReview.objects.filter(employee_id=employee_id)
            average_score = reviews.aggregate(average=Avg('score'))['average']
            rounded_average = round(average_score, 1) if average_score is not None else None
            employee_data.append({
                'employee_id': employee.employee_id,
                'name': employee.name,
                'score': rounded_average,
                'percent' : percent

        })
            
        locations = PublicMassageChairLocation.objects.all()
        locations_data = []
        for location in locations:
            location_name = location.location_name
            location_id = location.location_id
            chair_count = PublicMassageChair.objects.filter(location_id=location_id).count()
            locations_data.append({
                'location_name': location_name,
                'chair_count': chair_count
        })

    except RevenueRecord.DoesNotExist:
        m = None
        a = None
        t = None

    status_s = Member.objects.all()
    status_list = [entry.status for entry in status_s]
    status_counts = Counter(status_list)
    total_count = sum(status_counts.values())
    percentages = [(count / total_count) * 100 for count in status_counts.values()]
    rounded_percentages = [round(percentage) for percentage in percentages]
    counts_list = [count for status, count in status_counts.items()]
    categories_list = list(status_counts.keys())
    record = RevenueRecord.objects.all()
    revenue_amount_list = [entry.revenue_amount for entry in record]
    print(tuple(categories_list))
    print(tuple(counts_list))
    print(rounded_percentages)
    print(status_list)
    print(previous_month_amount) 
    return render(request, 'index.html', locals())


def client_view(request):
    member = Member.objects.all()
    # esr = EmployeeServiceReview.objects.all()
    # sr = StoreReview.objects.all()
    return render(request, 'client.html', locals())

def client_search(request):
    member = Member.objects.all()
    if request.method == 'GET':
        member_search = request.GET.get('member', '蔡小英')
        
    print(member_search)
    ser_member = Member.objects.get( name = member_search )
    sname = ser_member.name
    id = ser_member.member_id
    esr = EmployeeServiceReview.objects.filter( member_id = id )
    sr = StoreReview.objects.filter( member_id = id )
    saler = SalesRecord.objects.filter( member_id = id )
    pmc = PublicMassageChairUsageRecord.objects.filter( member_id = id )
    return render(request, 'client.html', locals())



def product_mc_view(request):
    product = Product.objects.all()
    PR = PurchaseRecord.objects.all()
    SR = SalesRecord.objects.all()
    return render(request, 'product_mc.html', locals())


def public_mc_view(request):
    pmc = PublicMassageChair.objects.all()
    pmcur = PublicMassageChairUsageRecord.objects.all()
    pmcl = PublicMassageChairLocation.objects.all()
    return render(request, 'public_mc.html', locals())


def sales_view(request):
    status_s = Member.objects.all()
    status_list = [entry.status for entry in status_s]
    status_counts = Counter(status_list)
    total_count = sum(status_counts.values())
    percentages = [(count / total_count) * 100 for count in status_counts.values()]
    rounded_percentages = [round(percentage) for percentage in percentages]
    counts_list = [count for status, count in status_counts.items()]
    categories_list = list(status_counts.keys())
    record = RevenueRecord.objects.all()
    revenue_amount_list = [entry.revenue_amount for entry in record]

    total_count = Employee.objects.all().count()
    employee = Employee.objects.all()
    employee1 = Employee.objects.get( employee_id = 1)
    employee2 = Employee.objects.get( employee_id = 2)
    employee3 = Employee.objects.get( employee_id = 3)
    employee4 = Employee.objects.get( employee_id = 4)
    employee5 = Employee.objects.get( employee_id = 5)
    e1 = SalesRecord.objects.filter( employee_id = 1 )
    e2 = SalesRecord.objects.filter( employee_id = 2 )
    e3 = SalesRecord.objects.filter( employee_id = 3 )
    e4 = SalesRecord.objects.filter( employee_id = 4 )
    e5 = SalesRecord.objects.filter( employee_id = 5 )
    s1 = EmployeeServiceReview.objects.filter( employee_id = 1 )
    s2 = EmployeeServiceReview.objects.filter( employee_id = 2 )
    s3 = EmployeeServiceReview.objects.filter( employee_id = 3 )
    s4 = EmployeeServiceReview.objects.filter( employee_id = 4 )
    s5 = EmployeeServiceReview.objects.filter( employee_id = 5 )

    r1 = EmployeeServiceReview.objects.filter( employee_id = 1 )
    total_score1 = round(r1.aggregate(average=Avg('score'))['average'], 1)

    r2 = EmployeeServiceReview.objects.filter( employee_id = 2 )
    total_score2 = round(r2.aggregate(average=Avg('score'))['average'], 1)

    r3 = EmployeeServiceReview.objects.filter( employee_id = 3 )
    if r3.exists():
        average_score = r3.aggregate(average=Avg('score'))['average']
        total_score3 = round(average_score, 1) if average_score is not None else None
    else:
        total_score3 = None

    r4 = EmployeeServiceReview.objects.filter( employee_id = 4 )
    if r4.exists():
        average_score = r4.aggregate(average=Avg('score'))['average']
        total_score4 = round(average_score, 1) if average_score is not None else None
    else:
        total_score4 = None       
    r5 = EmployeeServiceReview.objects.filter( employee_id = 5 )
    if r5.exists():
        average_score = r5.aggregate(average=Avg('score'))['average']
        total_score5 = round(average_score, 1) if average_score is not None else None
    else:
        total_score5 = None

    return render(request, 'sales.html', locals())


def store_view(request):
    status_s = Member.objects.all()
    status_list = [entry.status for entry in status_s]
    status_counts = Counter(status_list)
    total_count = sum(status_counts.values())
    percentages = [(count / total_count) * 100 for count in status_counts.values()]
    rounded_percentages = [round(percentage) for percentage in percentages]
    counts_list = [count for status, count in status_counts.items()]
    categories_list = list(status_counts.keys())
    record = RevenueRecord.objects.all()
    revenue_amount_list = [entry.revenue_amount for entry in record]


    pmc1 = PublicMassageChair.objects.filter( location_id = 1 ).count()
    pmc2 = PublicMassageChair.objects.filter( location_id = 2 ).count()
    pmc3 = PublicMassageChair.objects.filter( location_id = 3 ).count()

    sr1 = StoreReview.objects.filter( store_id = 1 )
    return render(request, 'store.html', locals())
