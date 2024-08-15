#Author : Sana Alyaseri
#Class software development
#Example 4: ACCESSING a global variable
count = 0
def increment():
    global count # Declare 'count' as global
    count += 1
    print(f"count inside the function: {count}")

    # call the function
    increment()
    increment()

    # Access the global variable
    print(f"count outside function: {count}")
    