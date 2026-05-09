def triangle_checking(a, b, c):
   for a in range(1,11) :
         for b in range(1,11) :
              for c in range(1,11) :
                 if a + b > c and a + c > b and b + c > a:
                      print("Yes")
                 else:
                      print("No")
                 break
    


       
print(triangle_checking(3, 4, 5))  