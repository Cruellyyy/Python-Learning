grocery_list = ["milk", "eggs", "bread", "butter", "cheese", "apples", "bananas", "oranges", "grapes", "tomatoes", "potatoes", "onions", "carrots", "spinach", "broccoli", "chicken", "beef", "fish", "rice", "pasta"]
print(f"This the list of all the items we need for this month{grocery_list}")

grocery_already_have = ["milk", "spinach", "fish", "potatoes", "bananas", "apples"]

for i in range(0,5):
    item_remove = grocery_already_have[i]
    grocery_list.remove(item_remove)
    print(f"{item_remove} is already available and removing from the list.")
    
print(grocery_list)


'''Here’s what I mean:

for i in range(0,5):
    item_remove = grocery_already_have[i]
    grocery_list.remove(item_remove)


You hardcoded range(0,5) → but grocery_already_have has 6 items. That means the last one (apples) is ignored.

If tomorrow the list size changes (maybe you add 10 items you already have), your code will break or skip items.

A safer way is to loop directly through the list:

grocery_list = ["milk", "eggs", "bread", "butter", "cheese", "apples", "bananas", 
                "oranges", "grapes", "tomatoes", "potatoes", "onions", "carrots", 
                "spinach", "broccoli", "chicken", "beef", "fish", "rice", "pasta"]

print(f"This is the list of all the items we need for this month:\n{grocery_list}")

grocery_already_have = ["milk", "spinach", "fish", "potatoes", "bananas", "apples"]

for item in grocery_already_have:
    if item in grocery_list:   # extra safety
        grocery_list.remove(item)
        print(f"{item} is already available and removing from the list.")

print("\nUpdated grocery list:", grocery_list)

Output would look like:
milk is already available and removing from the list.
spinach is already available and removing from the list.
fish is already available and removing from the list.
potatoes is already available and removing from the list.
bananas is already available and removing from the list.
apples is already available and removing from the list.

Updated grocery list: ['eggs', 'bread', 'butter', 'cheese', 'oranges', 'grapes', 'tomatoes', 'onions', 'carrots', 'broccoli', 'chicken', 'beef', 'rice', 'pasta']

🔑 Key lesson:

Never hardcode indexes unless you know the list will always have that length.

Loop directly over elements → makes the code future-proof.

Always check if item in grocery_list before .remove() → avoids ValueError if some item isn’t found.'''