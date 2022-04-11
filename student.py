def main():
    #your code goes here
   # UNIT 2 ACTIVITY 3.2
    num = int(input("What Is The Number\n"))

    if num % 15 == 0:
      print("FizzBuzz")

    elif num % 5 == 0:
       print("buzz")

    elif num % 3 == 0:
      print ("Fizz")

    else:
      print(num)

if __name__ =='__main__':
    main()
