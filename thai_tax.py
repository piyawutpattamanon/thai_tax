def get_tax_deduction(income):
    income_levels = [150000, 300000, 500000, 750000, 1000000, 2000000, 5000000, 100000000]
    tax_levels =    [     0,   0.05,    0.1,   0.15,    0.20,    0.25,    0.30,      0.35]
    
    total_tax = 0
    for i in range(len(income_levels)-1):
        if income > income_levels[i]:
            tranch_income = income - income_levels[i]
            tranch_income = min(income_levels[i+1] - income_levels[i], tranch_income)
            total_tax += tax_levels[i+1] * tranch_income
    return total_tax

def get_tax_rate(income):
    tax_deduction = get_tax_deduction(income)
    return tax_deduction / income

def get_income_after_tax(income):
    return income - get_tax_deduction(income)

def get_income_before_tax(income_after_tax):
    """
    use bisection algorithm to find the answer
    """
    left = 0
    right = income_after_tax * 2
    mid = (left+right)/2
    for i in range(100):
        mid_ibt = get_income_after_tax(mid)
        if mid_ibt == income_after_tax:
            return mid
        if mid_ibt < income_after_tax:
            left = mid
        else:
            right = mid
            
        mid = (left+right)/2
            
    return mid


