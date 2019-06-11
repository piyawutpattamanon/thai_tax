import thai_tax

income = 2400000
print(income)
print(thai_tax.get_tax_deduction(income))
print(thai_tax.get_tax_rate(income))
print(thai_tax.get_income_after_tax(income))

print(thai_tax.get_income_before_tax(2000000))

current_income_before_tax = 1844400
current_income_after_tax = thai_tax.get_income_after_tax(current_income_before_tax)
increase_after_tax = 0.3
desired_income_after_tax = current_income_after_tax * (1 + increase_after_tax)
desired_income_before_tax = thai_tax.get_income_before_tax(desired_income_after_tax)

print('annual current before  tax: {:12,.0f} ({:5.2f}% tax)'.format(
    current_income_before_tax,
    thai_tax.get_tax_rate(current_income_before_tax) * 100
))

print('annual current after   tax: {:12,.0f}'.format(current_income_after_tax))


print('increase +{:.0f}%             : {:+12,.0f}'.format(
    increase_after_tax * 100,
    increase_after_tax * current_income_after_tax
))

print('annual desired after   tax: {:12,.0f}'.format(desired_income_after_tax))
print('annual desired before  tax: {:12,.0f} ({:5.2f}% tax)'.format(
    desired_income_before_tax,
    thai_tax.get_tax_rate(desired_income_before_tax) * 100
))
print('monthly desired before tax: {:12,.0f}'.format(desired_income_before_tax / 12))