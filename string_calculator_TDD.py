def add(numbers: str) -> int:  # Implementation: input is a string and output is an integer 
    if numbers == "":      # empty string 
        return 0 

    delimiter = ","   # default delimiter
    if numbers.startswith("//"):
      delimiter = numbers[2]        # "//;\n" → ";" at index 2
      numbers = numbers[4:]         # skip "//;\n"

    numbers = numbers.replace("\n", delimiter)

    if delimiter not in numbers:
      return int(numbers)

    total = 0
    for num in numbers.split(delimiter):
        if num:
            total+=int(num)
    return total

 

 
 

    
     


  