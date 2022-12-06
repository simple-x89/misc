#got tired of manually recalculating nothing fancy here
#KH 2016

def app_header():
    print ('-------------------------------------------------')
    print ('---------- Tank Weight Calculator----------------') 
    print ('-------------------------------------------------')
    return ()


def tank_math(thickness, density, dimension):
    width = dimension[0]  # I think I'm probably abusing arrays here...
    length = dimension[1]
    height = dimension[2]
    tank_volume = width*length*height
    volume = thickness * (((length*height)*2) + ((height*width)*2) + (length*width))  # calculate tank weight and volume
    weight = volume * density
    return weight, tank_volume


def rib_math(thickness, density):
    volume = thickness * 1418  # calculate weight of support structure. user can input 0 if no structure needed
    weight = volume * density
    return weight


def user_prompt():
    width = int(input('-tank width [inches]: '))
    length = int(input('-tank length [inches]: '))
    height = int(input('-tank height[inches]: '))
    dimensions = [width, length, height]
    tank_thickness = int(input('-tank wall thickness [inches]: '))  # getting data from user
    rib_thickness = int(input('-rib thickness [inches]: '))
    density = int(input('-material density [lbs/in^3]: '))
    return tank_thickness, rib_thickness, density, dimensions


i = 0  # while loop escape variable
x = 1  # while loop counter for clean 'UI'
while i != 1:

    if x == 1:
        app_header()  # added this logic to make final print out cleaner
    else:
        print('')
        print('')
        print ('-------------------------------------------------')
        print('')
        print('')

    tank_gauge, rib_gauge, material_density, tank_dimensions = user_prompt()
    rib_weight = rib_math(rib_gauge, material_density)
    tank_weight, tank_capacity = tank_math(tank_gauge, material_density, tank_dimensions)  
    total_weight = rib_weight + tank_weight                                   
    tank_capacity_gal = tank_capacity * .00433
    tank_weight_full = tank_capacity * .036
    working_capacity = tank_capacity_gal/1.5
    print('')
    print ("rib weight:", rib_weight, "lbs")
    print ('tank weight (empty):', tank_weight, 'lbs')
    print ('total weight (empty):', total_weight, 'lbs')
    print ('total weight (full):', tank_weight_full + tank_weight + rib_weight, 'lbs')
    print ('tank capacity:', tank_capacity_gal, 'gallons')
    print ('working tank capacity:', working_capacity, 'gallons')
    print('')
    i = input('recalculate?  0: yes   1: no')
    x += 1



