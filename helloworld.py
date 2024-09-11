import sys

# input to get user's name
#user_name = sys.argv[1]
# print greeting
#print(f"Hello, {user_name}!")

# Print greeting for each name passed
for i in range(1,len(sys.argv)):
    print(f"Hello, {sys.argv[i]}!")
