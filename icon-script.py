filename = 'icons-data.csv'
steps = []
stairs = []
benches = []
ramps = []
wcElevators = []
nonwcElevators = []

def read_data():
    dataFile = open(filename, 'r')
    string = "nothing here"
    data = []
    dataFile.readline()
    while (string != ""):
        string = dataFile.readline()
        if(string == ""):
            break
        else:
            parse_data(string)
    dataFile.close()
    return data

# icon 1 lat 2 long 3 loc 4 notes 5
def parse_data(string):
    # L.marker([43.1276125, -77.6291051], {icon: ElevatorWCIcon}),
    string_list = string.split(",")
    type = str(string_list[0])
    report = ""
    icon = ""
    list = steps
    if (type == "bench"):
        icon = "benchIcon"
        list = benches
    elif (type == "ramp"):
        icon = "rampIcon"
        list = ramps
    elif (type == "steps"):
        icon = "stepsIcon"
        list = steps
    elif (type == "stairs"):
        icon = "stairsIcon"
        list = stairs
    elif (type == "WC accessible"):
        icon = "ElevatorWCIcon"
        list = wcElevators
        report = string_list[4].rstrip()
    elif (type == "WC inaccessible"):
        icon = "ElevatorNotWCIcon"
        list = nonwcElevators
        report = string_list[4].rstrip()
    else:
        print("Error with " + string_list)

    # create marker string and add to list
    if (report == ""):
        marker_string = "L.marker([" + str(string_list[1]) + ", " + str(string_list[2]) + "], {icon:" + icon + "}),"
    else:
        marker_string = "L.marker([" + str(string_list[1]) + ", " + str(string_list[2]) + "], {icon:" + icon + "}).addEventListener('click', function() {reportIcon('" + report + "')}),"
    list.append(marker_string)

def printLayerGroup(name, list):
    print("var " + name + " = L.layerGroup([")
    for line in list:
        print(line)
    print("])")
    print()
        

read_data()
printLayerGroup("elevatorsWC", wcElevators)
printLayerGroup("elevatorsNotWC", nonwcElevators)
printLayerGroup("stairs", stairs)
printLayerGroup("steps", steps)
printLayerGroup("ramps", ramps)
printLayerGroup("benches", benches)