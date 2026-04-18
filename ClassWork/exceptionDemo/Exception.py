# print("Program started")
# try :
#     a = 10
#     b = a/0
#     print(b)
# except Exception as e:
#     print("EXCEPTION OCCURRED: ", e)
# else :
#     print("Successfully executed")
# finally :
#     print("Program ended")            


print("Program started")
# try :
#     a = 10
#     b = a/0
#     print(b)
# except ZeroDivisionError as e:
#     print("EXCEPTION OCCURRED: ", e)
# except Exception as e:
#     print("EXCEPTION OCCURRED: ", e)
# else :
#     print("Successfully executed")
# finally :
#     print("Program ended")

try :
    a = 10
    b = a + "ufugg"
    print(b)
except TypeError as e:
    print("EXCEPTION OCCURRED: ", e)
except Exception as e:
    print("EXCEPTION OCCURRED: ", e)
else :
    print("Successfully executed")
finally :   
    print("Program ended")    