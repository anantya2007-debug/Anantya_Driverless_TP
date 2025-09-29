from collections import defaultdict
num_map = defaultdict(list)

def input_coordinates():
    coords = []
    n = int(input("How many coordinates? "))
    for i in range(n):
        coord_str = input(f"Enter coordinate #{i+1} as x,y: ")
        x_str, y_str = coord_str.split(',')
        coords.append((float(x_str.strip()), float(y_str.strip())))
    return coords

def get_coordinate():
    coord_str = input("Enter a coordinate as x,y: ")
    x_str, y_str = coord_str.split(',')
    return (float(x_str.strip()), float(y_str.strip()))

def sort_coord():
    coords = input_coordinates()
    cord = get_coordinate()
    
    dist_list = []  
    
    for coord in coords:
        d = ((coord[0] - cord[0])**2 + (coord[1] - cord[1])**2)**0.5
        num_map[d].append(coord)

    dist_list=sorted(num_map.items())
    
    return dist_list

a=sort_coord()
print(a)




