# # vowel print kerwane kee leye 
# a="i live in jaipur"
# length=len(a)
# counter = 0
# while counter < length:
#     if a [counter] in "ieouaAIEOU":
#         print(a[counter])
# counter += 1



# a="i live in jaipur"
# length=len(a)
# counter = 0
# sum=0
# while counter < length:
#     if a [counter] in "ieouaAIEOU":
#       counter += 1
# sum +=1
# print(sum)




# # space count krnee ke leyee 
# a = "my name is virat and i live in india."
# print( a.count (" "))

#list

# numbers = [0,1,2,3,4,5,6,7,8,9]
# print(numbers)


# data=[12,12.2,False,"virat",True]
# print(data)

# #data manipulation in list 
# data=[12,12.2,False,"virat",True]
# data[0]=90
# print(data)

# data=[ 12, 12, False, "virat", True ]
# print=( data[0] + data[1] )

# a=[ 12, 12, False, "virat", True ]
# print(a[3][1])


# a=[[[[137]]]]
# print(a[0] [0][0][0])


# a=["virat",
#    25,
#    "jaipur",
#    303830,
#    ["test",34,[47689,[635856]]]
#    ]

# print(a[-1][-1][-1][-1])

# a=["virat",
#    25,
#    "jaipur",
#    303830,
#    ["test",34,[47689,[635856]]]
#    ]

# print(a[-1][-1][-1][-1][-1])


# refrence verible
# a=["sdf",1,2,3,4,6,8]
# b=a
# print(a,b)
# b[0] = "virat"
# print(a,b)



#sliceing
# number=[0,1,2,3,4,5,6,7,8,9]
# print (number[ : ])
# print ( f"slice [2:6]:{number[2:6]}")
# print ( f"slice [:6]:{number[:6]}")
# print ( f"slice [2:]:{number[2:]}")
# print ( f"slice [-1: :-1]:{number[: :-1]}")
# print ( f"slice [2:7:2]:{number[2: 7:2]}")
# print ( f"slice [: :2]:{number[: :2]}")
# print ( f"slice [-8:-1:2]:{number[-8: -1:2]}")

# homework 
# numbers = [123, 34, 5, 23, 5, 23, 566, 88, 98]
# print(numbers[-3: -8 : -2])



# a=["graps","mango","orange","cherry"]
# a[1]="date"
# print(f" total item :{a}")

# print(a[1:3])
# print(a[1][1:3])



# #sliceing


# string="computer"
# print(string[:7])
# print(string[2:])
# print(string[2:6])



# i="0123456789"
# print(i[-6:-3])
# print(i[1:10])
# print(i[2:3])
# print(i[-8:-1])



##start ,end,difference
# i="0123456789"
# print(i [: :2])
# print(i [: :-1])
# print(i [: :-2])
# print(i [2: 7:2])
# print(i [-9: -2:2])

##lenth kee leyee 
# i="hello virat "
# print(len(i))

#membership opraters
# i="hello virat "
# print("h" in i)

# i="hello virat "
# print("f" in i)

# i="hello virat "
# print(" " in i)



# #agr kisi world ko aad krna ho tb ==>
# a="wello"
# a ="H" + a[ 1 : ]
# print(a)



# #small letters kee leye 
# a="HELLO viRAT"
# print(a.lower()) #output:hello 

#space ko hatane kee leye (remove)
# a="  hello sir    "
# print(a.strip())

# my_string="--sahil kumawat--"
# print(my_string.strip("-"))


# my_string="--sahil--kumawat--"
# print(my_string.strip("-"))

# my_string="--sahil--kumawat***--"
# print(my_string.strip("-*"))


# my_string="--sahil--kumawat***--"
# print(my_string.lstrip("-"))

# my_string="--sahil--kumawat***--"
# print(my_string.rstrip("-"))


# my_string="sahil--kumawat***--"
# print(my_string.startswith("sahil"))



# my_string="sahil--kumawat***--"
# print(my_string.startswith("ahil"))



# my_string="sahil--kumawat bye."
# print(my_string.endswith("bye."))


# #justifiy the string
# print("acbsabs".rjust(100," "))

# print("acbsabs".rjust(10,"+"))

# print("acbsabs".ljust(10,"+"))



# my_string="sahil--kumawat bye."
# print(my_string.replace("s", "S"))




# test="hii hello virat kumawat "
# print("not" in test )


# my_string= "hello world"
# print(my_string . find( "o" ) )

# print("hello sir virat kumawat".find( " ",6))


# a="i am belong to jaipur "
# print(a.count("a"))
# print(a.count(" "))


# # ISUPPER
# a="VIRAT "
# print(a.isupper())


# a="VIRAt12 "
# print(a.isupper())

# ISlower
# a="viratt12 "
# print(a.islower())



# #isalnum
# a="jds223rjsf"
# print(a.isalnum())

# isnumeric
# a="373947937"
# print(a.isnumeric())


# a="-3-73947937"
# print(a.isnumeric())

# a="i am virat"
# print(a.capitalize())

# # title 
# a="i am virat"
# print(a.title())


# a="This is a test string"
# print(a[0])
# print(a[1])
# print(a[2])
# print(a[3])
# print(a[4])


# a="INDIA"
# length=len(a)
# print(length)

# counter=0
# while counter < length:
#     print(a[counter])
#     counter+=1


# a="india is my country"
# print(a.split())

# a="13/1/2008"
# print(a.split("/"))


#join mehthod


# a={ "my", "name", "is", "sahil", "kumawat"}
# print(" ".join(a))
# print("-----".join(a))

# a=('13','01','2008')
# print(" / ".join(a))


#an  empty tuple

# a=(1,2,3,4,5,6,7,8,9,10)
# print(f"over tuple is .{a}")

# # nusted_tuple
# a=(1,[6,3],4,5,"test")
# # print(a[1][0])
# a[1][0]=2
# a[1][1]=3
# print(a)


# a=[2,4]
# b=[6,8]

# a.append(b)
# print(a)

# a.extend(b)
# print(a)

# a=(5)
# print(f"over tuple is .{a},type:{type(a)}")


# a=(5 ,)
# print(f"over tuple is .{a},type:{type(a)}")


#tuple packing and unpacking 
# a=2,34.5,"sahil",[56]
# print(type(a))

# a,b,c=1,2,3
# print(a,b,c)

# my_tuple=(1,2,3,4,5)
# a,b,c,d,e=my_tuple
# print(a,b,c,d,e)

# my_tuple=(1,2,3,4,5)
# unique=a,b,c,d,e=my_tuple
# print(unique)

# my_tuple=(1,2,3,4,5)
# unique=a,b,c,d=my_tuple
# print(unique)

# number=(1,2,3,4,5,6,7,8,9)
# print(f"slice[2:6] : {number[2:6]}")



# tuple1=(1,2)
# tuple2=(3,4)
# tuple3=tuple1+tuple2
# print(tuple3)


# tuple1=(1,2)
# tuple2=(3,4)
# tuple3=tuple2+tuple1
# print(tuple3)

# tuple1=(1,2)
# tuple2=(3,4)
# tuple3=tuple2*2
# print(tuple3)

# a=(1,[3,5],8)
# a[1].append(7)
# print(a)


# a=(1,[3,5],8)
# a[1].append(7)
# print(a)


# swapping

# a=3
# b=7
# print(a,b)

# c=a
# a=b
# b=c
# print(a,b)


# a=3
# b=7
# print(a,b)

# a,b=b,a
# print(a,b)

###########homework 7-4-2026
# Write a python program to swap two values.

# input1=input("enter first value:")
# input2=input("enter second value:")
# print(f"Befor swapping: input1 = {input1}, input2 = {input2}")

# # Swapping the values
# input1, input2 = input2, input1
# print(f"After  swapping: input1 = {input1}, input2 = {input2}")


# uniq=(1,2,3,4,5,6,7,8,9,10)
# a,b,c,d,*e=uniq
# print(a,b,c,d,e)

# uniq=(1,2,3,4,5,6,7,8,9,10)
# *a,b,c,d,e=uniq
# print(a,b,c,d,e)


# a="hfebujcdhjfsdb"
# b=tuple(a)
# print(f"list of tuple:{b} , type:{type(b)}")


# a=(1,2,3,2,2,3,2,2,3)
# print(a.count(2))


# a=(1,2,3,2,2,3,2,2,3)
# print(a.index(2))

# a=" my name is viratkumawat and my adition is 13/01/2008 "
# b=a.split()
# c=tuple(b)
# print(c.count("is"))

# a="this is my pen and my name is virat  "
# b=a.split()
# c=tuple(b)
# print(c.count("is"))



# a="this is my pen and my name is virat  "
# print(a.count("is"))













