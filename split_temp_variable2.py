# By Kami Bigdely
# Split temp variable

def save_into_db(info):
    print("saved into databse")


username = input('Please enter your username: ')
save_into_db(username)
date_of_birth = int(input('Please enter your birth year: '))
age = 2020 - date_of_birth
print("You are",age, "years old.")