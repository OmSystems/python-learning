# ============================================
# Python Basics - Build a Bill Splitter
# FreeCodeCamp Python Course
# Author: Om Patel
# ============================================

# Number of friends splitting the bill
bill_total = 0
friend_count = 4

# Individual bill items
appetizer_cost = 37.89
main_course_cost = 57.34
dessert_cost = 39.39
drink_cost = 64.21

# Calculate total bill
bill_total += appetizer_cost + main_course_cost + dessert_cost + drink_cost
print('Total bill so far:', bill_total)

# Calculate 25% tip
tip_amount = bill_total * 0.25
print('Tip amount:', tip_amount)

# Add tip to total
bill_total += tip_amount
print('Total with tip:', bill_total)

# Split bill among friends
per_person = bill_total / friend_count
print('Bill per person:', per_person)
