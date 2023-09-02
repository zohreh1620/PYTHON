#try-Except

list=[1,2,3,5]
#تلاش براي دسترسي به يک آيتم ناموجود در ليست

try:
    print(list[4])
except IndexError as e:
    print('Exception:' + str(e)+ ' has occured')
else:
    print('No Exception Occured')
finally:
    print("I will always execute no matter what")
