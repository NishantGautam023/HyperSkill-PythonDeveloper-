import math
import sys
arg = sys.argv


def count_months():
    global arg
    principal = int(arg[2].split('=')[1])
    month_pay = int(arg[3].split('=')[1])
    interest = float(arg[4].split('=')[1])
    nominal_int = interest / (12 * 100)
    count = month_pay / (month_pay - nominal_int * principal)
    if count < 0:
        print('Incorrect parameters')
        exit()
    months = math.ceil(math.log(count, 1 + nominal_int))
    overpayment = (math.ceil(month_pay) * months) - principal
    years = math.floor(months / 12)
    months %= 12
    if years == 0:
        if months == 1:
            print(f'You need {months} month to repay this credit!')
        else:
            print(f'You need {months} months to repay this credit!')
    elif months == 0:
        if months == 1:
            print(f'You need {years} year to repay this credit!')
        else:
            print(f'You need {years} years to repay this credit!')
    else:
        print(f'You need {years} years and {months} months to repay this credit!')

    print(f'Overpayment = {math.ceil(overpayment)}')


def monthly_payments():
    principal = int(arg[2].split('=')[1])
    months = int(arg[3].split('=')[1])
    interest = float(arg[4].split('=')[1])
    nominal_int = interest / (12 * 100)
    payment = principal * (nominal_int * ((1 + nominal_int) ** months)) / (((1 + nominal_int) ** months) - 1)
    print(f'Your annuity payment = {math.ceil(payment)}!')
    overpayment = (math.ceil(payment) * months) - principal
    print(f'Overpayment = {math.ceil(overpayment)}')


def credit_principal():
    print('Enter monthly payment:')
    month_pay = int(arg[2].split('=')[1])
    print('Enter count of periods:')
    months = int(arg[3].split('=')[1])
    print('Enter credit interest:')
    interest = float(arg[4].split('=')[1])
    nominal_int = interest / (12 * 100)
    principal = month_pay / ((nominal_int * ((1 + nominal_int) ** months)) / ((1 + nominal_int) ** months - 1))
    print(f'Your credit principal = {principal}!')
    overpayment = (month_pay * months) - principal
    print(f'Overpayment = {math.ceil(overpayment)}')


def diff():
    p = int(arg[2].split('=')[1])
    n = int(arg[3].split('=')[1])
    interest = float(arg[4].split('=')[1])
    print(p,n,interest)
    if p * n * interest < 0:
        print('Incorrect parameters')
        exit()
    i = interest / (12 * 100)
    count = 0
    for m in range(1, n+1):
        d = (p / n) + (i * (p - ((p * (m - 1)) / n)))
        count += math.ceil(d - p / n)
        print(f'Month {m}: paid out {math.ceil(d)}')
    print(f'\nOverpayment = {math.ceil(count)}')


if len(arg) == 5:
    type__ = arg[1].split('=')[1]
    if type__ == 'diff':
        diff()
    elif type__ == 'annuity':
        arga = [arg[2].split('=')[0], arg[3].split('=')[0], arg[4].split('=')[0]]
        arga1 = [arg[2].split('=')[1], arg[3].split('=')[1], arg[4].split('=')[1]]
        for x in arga1:
            if float(x) < 0:
                print('Incorrect parameters')
                exit()
        if '--principal' not in arga:
            credit_principal()
        elif '--periods' not in arga:
            count_months()
        elif '--payment' not in arga:
            monthly_payments()
    else:
        print('Incorrect parameters')
        exit()
else:
    print('Incorrect parameters')
    exit()
