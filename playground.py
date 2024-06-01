

#
# f = open('red_cards.txt', 'r')
#
# data = f.readlines()
# f.close()
# print(data)
# Open the file in read mode
f = open('red_cards.txt', 'r', encoding='utf-8')

# Read all lines from the file
data = f.readlines()

# Close the file
f.close()

# Print the data
print(data)
