# program to check for order discount
#inputs
item_cost = 500
item_qty  = 3
special_client = 1                         # 1 > special             0 > not special


#processing
total_cost = item_cost * item_qty
discount_pct = 0
if total_cost >= 1000:
    if special_client == 1:
        discount_pct = 20
    else:
        discount_pct = 10


discount_val = discount_pct /100 * total_cost
print("total order cost before discount:", total_cost)
total_cost = total_cost - discount_val

print("discount pct = " , discount_pct)
print("discount value = ", discount_val)
print("total order cost after discount:", total_cost)
