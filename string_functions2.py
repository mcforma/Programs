#string_functions2.py

string_spaces = " space string "
print(string_spaces)
print(string_spaces.lstrip())
print(string_spaces.rstrip())
print(string_spaces.strip())

string_char = "&&&string char&&&"
print(string_char.lstrip("&"))
print(string_char.rstrip("&"))
print(string_char.strip("&"))

new_string_char = string_char.strip("&")
print(new_string_char)

print(new_string_char.upper())
upper_string = new_string_char.upper() 

print(string_char.startswith("&")) # returns True because new_string_char does start with &
print(new_string_char.endswith("&")) # returns False because new_string_char does not end with &

print(string_char.find("&")) # returns index of first match

print(string_char.find(".")) # -1 means no match found

print(string_char.find("&&")) # returns index of the first character of the first match

print(string_char.replace("&&&","***")) # replaces all exact matches

new_string2 = "Mississippi"
print(new_string2 * 3) # repetition operator






