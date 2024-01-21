try:
  print("\nLet's review those multiplications\n")
  while(True):
    while(True):
        try:
          #we request the 2 numbers
          print("Please enter numbers from 0 to 10")
          n = int(input("Type the first number of the multiplication: "))
          m = int(input("Type the second number of the multiplication: "))
          line = (m)

          #Validate the range
          if (n < 0 or n > 10):
            print("\nThe first number is not inside the provided range")
            print("Try again please\n\n")
            break
          if (m < 0 or m > 10):
            print("\nThe second number is not inside the provided rangeo")
            print("Try again please\n\n")
            break

          #open and read the lines
          nameFile = (f"table-{n}.txt")
          doc = open(nameFile,"r")
          lecture = doc.readlines()

          print("\nThe result is: ")
          print(lecture[line])
          doc.close()

        #This helps that if the file is not created yet it notifies the user
        except FileNotFoundError:
          print("\nSorry, the multiplication file is not created yet")
          print("\t== We will generate the file required ==")

          nameFile = f"table-{n}.txt"
          doc = open(nameFile,"w")

          for number in range(0,11):
            multi = n*number
            doc.write(f"{n} x {number} = {multi} \n")

          doc.close()
          print(f"\t== All done! You can now use the file: {nameFile} ==")
          print()

except KeyboardInterrupt:
  print("\n\t#### Program has been stoped by the user ####\n")