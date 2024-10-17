string = input("Enter a string: ")

if len(string) <= 1:
  print("Modified string:", string)
else:
  first_char = string[0]
  last_char = string[-1]
  middle_part = string[1:-1]
  modified_string = last_char + middle_part + first_char
  print("Modified string:", modified_string)
