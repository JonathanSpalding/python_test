#Adding comment to test pushing to github again.
message = "Hello Python world!"
print(message)

message = "Hello Python Crash Course world!"
print(message)

#testing if title() method works on strings rather than just variables.
#Turns out the title method doesn't properly make a title, it does "title case" which is capitalizing first letter of each word.
print("testing titles here the of if and jon".title())

first_name = "jon"
last_name = "spalding"
full_name = f"{first_name} {last_name}"
full_name_caps = f"{first_name} {last_name}".title()
full_name_all_caps = f"{first_name} {last_name}".upper()
full_name_lower_case = f"{first_name} {last_name}".lower()

print(full_name_caps)

#Testing removeprefix()
jonspalding_url = "https://jonspalding.com"
print(jonspalding_url.removeprefix("https://"))

1 + 2
#using underscores _ can help define large numbers as it's not included in the output.
universe_age = 14_000_000_000
print(universe_age) #output 14000000000

#multiple variable assignment and printing
x, y, z = 1, 2, 3
a, b, c, = "one", "two", "three"
print(x, a, y, b, z, c)
#output 1 one 2 two 3 three

