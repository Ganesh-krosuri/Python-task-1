SOFT_PER_ACRE = 43560
length  = float(input("enter the length of the field in feet:"))
width = float(input("enter the width of the field in feet:"))
area_sqft = length*width
acres = area_sqft / SOFT_PER_ACRE
print("the area of the field is",acres,"acres")
