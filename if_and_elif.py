age = str(input("input your age:  "))
print(age.lower())

if age >= 18:
    print("You can watch all movies.")
elif age >= 16:
    print("Sorry, you can not watch 18 rated movies, but you can watch all other movies.")
elif age >= 13:
    print("Sorry, you can not watch 18 and 15 rated movies, but you can watch all other movies.")
elif age >= 8:
    print("Sorry, you can not watch 18, 15 and 12 rated movies, but you can watch all other movies.")
else:
    print("You can only watch U rated movies.")