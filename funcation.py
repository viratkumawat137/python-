# a=[1,2,3,4,5,6,-32,-34,5,34,]
# sum      
# print(sum(a))


# min
# print(min(a))

# max
# print(max(a))


# for x in range(1,21):
#     print(x)



#stntax
# def funcation_name():
#     print("hello world")


# funcation_name()


# def my_func():
#     print("i am line 1")
#     print("i am line 2")
#     print("i am line 3")
#     print("i am line 4")
#     print("i am line 5")
# my_func()


# def print_coun ():
#     for x in range(1,20):
#         print(x)
# print_coun()

# def print_coun ():
#     for x in range(1,20):
#         print(x)
# print_coun()
# print_coun()
# print_coun()

# print_coun()


# def sum_numbers():
#     num1 = input("Pehla number likhiye: ")
#     num2 = input("Doosra number likhiye: ")
    
#     # Input ko number (integer) mein badalna aur sum karna
#     result = int(num1) + int(num2)
    
#     print("Inka total sum hai:", result)

# sum_numbers()


# def odd_even_checker():
#     a = int(input("enter a number"))
#     if a % 2 ==0:
#         print("even")
#     else:
#         print("odd")


# odd_even_checker()


#doc_string
# def my_func(name):
#     """ this is my funcation
#     """
#     print(name.upper())

# my_func("hello ")


# def test(a,b,c):
#     print(f"a:{a}, b:{b}, c:{c}")

# test(23,32,12)



# def display_info(name, age, city, college, number):
#     print(f"--- User Profile ---")
#     print(f"Name    : {name}")
#     print(f"Age     : {age}")
#     print(f"City    : {city}")
#     print(f"College : {college}")
#     print(f"Number  : {number}")

# # Calling with keyword arguments in a different order
# display_info(
#     number="8867755432", 
#     city="Jaipur", 
#     age=30, 
#     name="Diana", 
#     college="XYZ"
# )







# Valid Mix: First two are positional, last three are keywords
# display_info("Vipin", 45, city="Jaipur", college="Test", number=42424)

# Invalid Mix: You cannot "skip" or "reorder" once you start using keywords
# display_info(name="Vipin", 45, "Jaipur", ...) 


# def display_info(name, age, city="Jaipur", college="UOT", number="N/A"):
#     # Now you only HAVE to provide name and age. 
#     # City and College will default to Jaipur/UOT if you don't specify them.
#     print(f"{name}, {age}, {city}")

# display_info("Vipin", 20) # Works! Uses defaults for the rest.





# def greet(name):
#     print(f"hello,{name}")
# greet("Alice")

# def greet (name="vipin"):
#     print(f"hello,{name}")
# greet()

# def greet (name="vipin"):
#     print(f"hello,{name}")
# greet("sahil")


# def greet (age,name="vipin"):
#     print(f"hello,{name} ,your age  {age}")
# greet(25)


# def greet ( cast ,name="vipin",age=22, city="jaipur" ,collage="UOT", number="N/A"):
#     print(f"hello,{name} ,cast={cast}, age={age}, city={city}, college={collage}, number={number}")
# greet(cast="kumar")


