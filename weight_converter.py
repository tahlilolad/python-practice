user_weight = float(input("What's your weight? "))
unit = input("Is that in kg or lbs? ").strip().lower()
if unit == "kg":
    final_weight = (user_weight * 2.205)
    print(f"Your weight in lbs is {final_weight: .2f} lbs")
elif unit == "lbs":
    final_weight = (user_weight/2.205)
    print(f"Your weight in kg is {final_weight: .2f} kg")