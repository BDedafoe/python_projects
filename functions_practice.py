#function 1
def hello():
    print("Welcome back user")

#function 2
def pack (notebook, pen, eraser):
    return [notebook, pen, eraser]

#function 3
def eat_lunch (list):
    if len(list) == 0:
        print("Mom, my lunchbox is empty!")
    else:
        for i in range(len(list)):
         if i == 0:
          print(f"First I eat my {list[0]}")
         else:
          print(f"Next I eat my {list[i]}")

#Call the functions
hello()
print(pack("notebook", "pen", "eraser"))
print(pack(1, 2, 3))
eat_lunch([])
eat_lunch(["wrap"])
eat_lunch(["banana", "milkshake", "wrap", "chicken"])