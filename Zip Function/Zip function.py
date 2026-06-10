# Python zip() Function,first and 2nd list marge.zip ing,

list1 = ["google", "microsoft", "linkedin", "facebook"]
list2 = ["github", "messenger", "instagam", "whatsapp"]

x = zip(list1,list2)
print(list(x))

a = ("John", "Charles", "Mike")
b = ("Jenny", "Christy", "Monica", "Vicky")

x = zip(a, b)

#use the tuple() function to display a readable version of the result:
print(tuple(x))
