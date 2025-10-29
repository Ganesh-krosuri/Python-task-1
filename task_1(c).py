import math
def calculate_area_in_acres(radius_in_feet):
    area_in_acres = math.pi*(radius_in_feet**2)/43560
    return area_in_acres
radius_in_feet = float(input("enter the radius of the field in feet:"))
area_in_acres = calculate_area_in_acres(radius_in_feet)
print(f"the ares of the field is :{area_in_acres:.2f} acres")
