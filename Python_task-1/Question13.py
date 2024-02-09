"""13   print the following patterns
(a)
	        *
           * *
          * * *
         * * * *

(b)		o
		1 2
		3 4 5
		6 7 8 9


(c)		o
		1 1
		2 2 2
		3 3 3 3

(d)		*
		* *
		* * *
		* * * *
"""

# (b)

# Pattern (b)

# Pattern
num = 1
for i in range(4):
    print(" " * i, end="")
    for j in range(i + 1):
        print(num, end=" ")
        num += 1
    print()




# (c)

# number=int(input("Enter the number of rows: "))
# for i in range(0,number+1):
#     for j in range(i + 1):
#         print(i, end=" ")
#     print()


# (d)

# number=int(input("Enter the number of rows: "))
# for i in range(1,number+1):
#     for j in range(1,i+1):
#         print("*",end="")
#     print()



