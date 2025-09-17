def add(numbers: str) -> int:  # Implementation: input is a string and output is an integer 
 if numbers == "":      # empty string 
   return 0 
 elif "," not in numbers:
     return int(numbers)
 else:
     total = 0
     for num in numbers.split(","):
         total+=int (num)
     return total

    
     


  