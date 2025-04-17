# main.py

from pet import Pet

# Create Abu
my_pet = Pet("Abu")

print("🐶 Welcome to the Abu Digital Pet Game!")

while True:
    print("\nWhat would you like Abu to do?")
    print("1. Eat")
    print("2. Sleep")
    print("3. Play")
    print("4. Train a new trick")
    print("5. Show tricks")
    print("6. Show status")
    print("7. Exit")
    
    choice = input("Enter your choice (1–7): ")

    if choice == "1":
        my_pet.eat()
        print("Abu ate some food. 🥩")
    elif choice == "2":
        my_pet.sleep()
        print("Abu had a good nap. 😴")
    elif choice == "3":
        my_pet.play()
        print("You played with Abu! 🎾")
    elif choice == "4":
        trick = input("Enter a trick to teach Abu: ")
        my_pet.train(trick)
    elif choice == "5":
        my_pet.show_tricks()
    elif choice == "6":
        my_pet.get_status()
    elif choice == "7":
        print("Thanks for playing with Abu! 👋")
        break
    else:
        print("Invalid choice. Please enter a number from 1 to 7.")

