# mortgage.py
#
# Exercise 1.7
principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
n = 0

while principal > 0:
    principal = principal * (1+rate/12) - payment
    total_paid = total_paid + payment
    n += 1

print('Total paid:', total_paid, '\nLeft principal:', principal)
print('No. months:', n)

print('\nExercise 1.8: Extra payments')
principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
n = 0
while principal > 0 and n < 12:
    principal = principal * (1+rate/12) - payment - 1000
    total_paid = total_paid + payment + 1000
    n += 1
while principal > 0:
    principal = principal * (1+rate/12) - payment
    total_paid = total_paid + payment
    n += 1
print('Total paid:', total_paid, '\nLeft principal:', principal)
print('No. months:', n)

print('\nExercise 1.9: Making an Extra Payment Calculator')
def extrapay(start, end, extra):
    principal = 500000.0
    rate = 0.05
    payment = 2684.11
    total_paid = 0.0
    n = 0
    while principal > 0 and int(n) < int(start - 1):
        principal = principal * (1 + rate / 12) - payment
        total_paid = total_paid + payment
        n += 1

    while principal > 0 and int(n) < int(end):
        principal = principal * (1 + rate / 12) - payment - extra
        total_paid = total_paid + payment + extra
        n += 1

    while principal > 0:
        principal = principal * (1 + rate / 12) - payment
        total_paid = total_paid + payment
        n += 1
    print('Total paid:', total_paid, '\nLeft principal:', principal)
    print('No. months:', n)

print('start61, end108, extra1000')
extrapay(61, 108, 1000)


print('\nExercise 1.10: Making a table')
def extrapay_withtable(start, end, extra):
    principal = 500000.0
    rate = 0.05
    payment = 2684.11
    total_paid = 0.0
    n = 0
    print('month', 'Total paid', 'Remaining principal')
    while principal > 0 and int(n) < int(start - 1):
        principal = principal * (1 + rate / 12) - payment
        total_paid = total_paid + payment
        n += 1
        print(n, f'{total_paid:<.4f}', f'{principal:<.4f}')

    while principal > 0 and int(n) < int(end):
        principal = principal * (1 + rate / 12) - payment - extra
        total_paid = total_paid + payment + extra
        n += 1
        print(n, f'{total_paid:<.4f}', f'{principal:<.4f}')

    while principal > 0:
        principal = principal * (1 + rate / 12) - payment
        total_paid = total_paid + payment
        n += 1
        print(n, f'{total_paid:<.4f}', f'{principal:<.4f}')

    print('Total paid:', total_paid, '\nLeft principal:', principal)
    print('No. months:', n)

print('start61, end108, extra1000')
extrapay_withtable(61, 108, 1000)

print('\ncorrect for the overpayment')
def extrapay_withtable2(start, end, extra):
    principal = 500000.0
    rate = 0.05
    payment = 2684.11
    total_paid = 0.0
    n = 0
    print('month', 'Total paid', 'Remaining principal')
    while principal > 0 and int(n) < int(start - 1):
        principal = principal * (1 + rate / 12) - payment
        total_paid = total_paid + payment
        n += 1
        print(n, f'{total_paid:<.4f}', f'{principal:<.4f}')

    while principal > 0 and int(n) < int(end):
        principal = principal * (1 + rate / 12) - payment - extra
        if principal < 0:
            total_paid = total_paid + payment + extra + principal
            principal = 0
            n+=1
            print(n, f'{total_paid:<.4f}', f'{principal:<.4f}')
        else:
            total_paid = total_paid + payment + extra
            n += 1
            print(n, f'{total_paid:<.4f}', f'{principal:<.4f}')

    while principal > 0:
        principal = principal * (1 + rate / 12) - payment
        if principal < 0:
            total_paid = total_paid + payment + principal
            principal = 0
            n+=1
            print(n, f'{total_paid:<.4f}', f'{principal:<.4f}')
        else:
            total_paid = total_paid + payment
            n += 1
            print(n, f'{total_paid:<.4f}', f'{principal:<.4f}')

    print('Total paid:', total_paid, '\nLeft principal:', principal)
    print('No. months:', n)

print('start61, end108, extra1000')
extrapay_withtable2(61, 108, 1000)

print('\na mystery')
print('bool(chr(0)):', bool(chr(0)))
print('bool(''):', bool(''))
print('bool([])', bool([]))
print('bool()', bool())