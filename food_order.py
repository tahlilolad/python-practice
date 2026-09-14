foods = ["burger","pizza","tacos","chicken","pasta","salad",]
while True:
    chosen_food = input("What would you like to order? ").strip().lower()
    if chosen_food in foods:
        print(f"You ordered {chosen_food}!")
        break #food is on menu. selected exit loop.
    else:
        user_answer1 = input("Sorry, that item is not on the menu! Would you like to order something else? (Yes/No): ").lower().strip()
        if user_answer1 == "no":
            print("Thanks for stopping by!")
            break #customer does not want to order
            