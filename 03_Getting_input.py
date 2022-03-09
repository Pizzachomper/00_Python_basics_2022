# Ask for the user for their name
print()
username = input("What is your name?")

# Ask the user for their favourite integer
fav_num = int(input("favourite number?"))

# Double, half and square the number
double = fav_num * 2
half = fav_num / 2
squared = fav_num * fav_num

print()
# Greet the user 
print("hi {}, your favourite number is {}.".format(username, fav_num))
print()

# Output the results of doubling, halving
# and squaring their favourite number
print("If we double your favourite number. ({}) we get {}.".format(fav_num, double))
print("If we half your favourite number. ({}) we get {}.".format(fav_num, half))
print("If we square your favourite number. ({}) we get {}.".format(fav_num, squared))