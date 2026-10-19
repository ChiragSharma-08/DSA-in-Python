def eat_mangoes(count):
    # Base case
    if count == 0:
        print("Hand is empty. Done")
        return

    # Recursion case
    print(f"I have {count} mangoes. eating one")
    eat_mangoes(count - 1)
    
eat_mangoes(3)