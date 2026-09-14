fruit = [ 
    ("apple", 0.50),
    ("orange", 0.25),
    ("mango", 1.75),
]
total = 0
print("Welcome to my fruit shop!")
for fruit_name, fruit_price in fruit:
    print(f"{fruit_name} costs ${fruit_price:.2f}")
    total += fruit_price
print (f"Total cost: $ {total:.2f}")