# # Python Lambda
# # x = lambda a,b: a + b
# # print(x(30 , 50))

# # addition in 4 Summarize argument 
# y = lambda a, b, c, d: a + b + c + d
# print(y(30,40,60,30))


mult = []
for i in range(3):
          mult.append(lambda x:x *i)
          print(mult[0](2))
          print(mult[1](2))