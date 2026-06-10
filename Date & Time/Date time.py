import datetime
a = datetime.datetime.now()
# print(a)
# print(a.strftime("%a"))  # week name/short version.
# print(a.strftime("%A"))  # full version week name
# print(a.strftime("%d"))  # just date show.
# print(a.strftime("%b"))  # month short name version.
# # print(a.strftime("%B"))  # month full name version.
print(a.strftime("%u"))  # week day version.
print(a.strftime("%X"))  # Local time  version.
print(a.strftime("%x"))  # Local full date version.