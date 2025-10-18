users = [
     {"id": 1, "name": "John", "discount":"P10", "amount": 450},
     {"id": 2, "name": "Jane", "discount":"P20", "amount": 90},
     {"id": 3, "name": "Bob", "discount":"P30", "amount": 800},
 ]

discounts = [
    {"code": "P10", "value": 0.10},
    {"code": "P20", "value": 0.20},
    {"code": "P30", "value": 0.30},
]

for user in users:
    discountPer = 0
    for disc in discounts:
        if disc.get('code', "N/A") == user['discount']:
            discountPer = disc.get("value", 0)
    user['discounted_amount']= user['amount'] - (user['amount'] * discountPer)

print(f"{users[0]}")