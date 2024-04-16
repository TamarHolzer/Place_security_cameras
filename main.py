import find_line
import drafts.show_polygon as polygon

def main():
    cordinates = [(0, 0), (0, 20), (20, 30), (20, 0)]

    walls = []
    j = 0
    for i in cordinates:
        if(j < (len(cordinates)-1)):
            walls.append(find_line.find_line(cordinates[j], cordinates[j+1]))
        else:
            walls.append(find_line.find_line(cordinates[j], cordinates[0]))
        j += 1
    print(walls)

    polygon.print_polygon(cordinates)

    ####לסדר את באילוצים עם ההפחתה של צד ימין

main()