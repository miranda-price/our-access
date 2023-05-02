edges = []
edges_names = []
edges_find_lengths = []        

class Edge:
    def __init__ (self, type, id, length, steps, stairs, manual_doors, non_wc_elevators, ada, dir, revDir, report, coords, location):
        self.type = type
        self.id = id
        self.length = length
        self.steps = steps
        self.stairs = stairs
        self.manual_doors = manual_doors
        self.non_wc_elevators = non_wc_elevators
        self.ada = ada
        self.dir = dir
        self.revDir = revDir
        self.report = report
        self.coords = coords
        self.location = location

    def setLength(self, length):
        if (length != ""):
            self.length = length
        else:
            edges_find_lengths.append(self.id)
    
    def setSteps(self, steps):
        if (steps == "no"):
            self.steps = "false"
    
    def setStairs(self, stairs):
        if (stairs == "no"):
            self.stairs = "false"
    
    def setDoors(self, doors):
        if (doors == "no"):
            self.manual_doors = "false"
    
    def setElevators(self, elevators):
        if (elevators == "no"):
            self.non_wc_elevators = "false"
    
    def setADA(self, ada):
        if (ada == "yes"):
            self.ada = "true"
    
    def setDir(self, dir):
        if (dir != ""):
            self.dir = "'" + dir + "'"
    
    def setRevDir(self, rev):
        if (rev != ""):
            self.revDir = "'" + rev + "'"

    def setReport(self, report):
        if (report != ""):
            report_strings = "', '".join(report.split(";"))
            report_strings = "['" + report_strings + "']"
            self.report = report_strings

    def setCoords(self, coords):
        if (coords != ""):
            coords = coords.rstrip()
            coords_strings = ", ".join(coords.split(";"))
            coords_strings = coords_strings.replace("][", "],[")
            if (coords_strings != ""):
                coords_strings = "[" + coords_strings + "]"
                self.coords = coords_strings
            else:
                self.coords = "null"

    def toString(self):
        # BR00_BR01 = new Edge('floor', 'BR00_BR01', 5, true, true, false, false, false, 'ground floor to first floor', 'first floor to ground floor', null, null);
        edge_string = self.id + " = new Edge('" + self.type + "', '" + self.id + "', " + self.length + ", " + self.steps + ", " + self.stairs + ", " + self.manual_doors + ", " + self.non_wc_elevators + ", " + self.ada + ", "  + self.dir + ", " + self.revDir + ", " + self.report + ", " + self.coords + ", '" + self.location + "');"
        return(edge_string)

def read_edges():
    dataFile = open('edges-data.csv', 'r')
    string = "nothing here"
    data = []
    dataFile.readline()
    while (string != ""):
        string = dataFile.readline()
        if(string == ""):
            break
        else:
            parse_data_edges(string)
    dataFile.close()
    return data

# type 0 id 1 length 2 steps 3 stairs 4 manual door 5 nonwc elevator 6 ada 7 directions 8 reverse 9 report 10 coords 11
def parse_data_edges(string):
    string_list = string.split(",")
    edge = Edge(str(string_list[0]), str(string_list[1]), "null", "true", "true", "true", "true", "false", "null", "null", "null", "null", string_list[12].rstrip())
    edge.setLength(str(string_list[2]))
    edge.setSteps(str(string_list[3]))
    edge.setStairs(str(string_list[4]))
    edge.setDoors(str(string_list[5]))
    edge.setElevators(str(string_list[6]))
    edge.setADA(str(string_list[7]))
    edge.setDir(str(string_list[8]))
    edge.setRevDir(str(string_list[9]))
    edge.setReport(str(string_list[10]))
    edge.setCoords(str(string_list[11]))
    edges_names.append(edge.id)
    edges.append(edge.toString())

def printEdges():
    for x in edges:
        print(x)
    print()
    all_edges = str(edges_names)
    all_edges = all_edges.replace("'", "")
    print("var all_edges = "+ all_edges +"")
    find_lengths = str(edges_find_lengths)
    find_lengths = find_lengths.replace("'", "")
    print("var edges_find_lengths = "+ find_lengths +"")





nodes = []
nodes_names = []

class Node:
    def __init__(self, building, level, id, edges, type, coords):
        self.building = building
        self.level = level
        self.id = id
        self.edges = edges
        self.type = type
        self.coords = coords
    
    def setLevel(self, level):
        if (level != ""):
            self.level = "'" + level + "'"

    def setCoords(self, lat, long):
        self.coords = "[" + lat + ", " + long.rstrip() + "]"

    def setEdges(self):
        node_edges = []
        for edge in edges_names:
            nodes = edge.split('_')
            for node in nodes:
                if (node == self.id):
                    node_edges.append(edge)
        self.edges = str(node_edges).replace("'", "")

    def toString(self):
        # BR00 = new Node("Burton", "0", "BR00", [BR00BR01,BR00BR02,BR00BR03,BR00BR00A], "floor", null, Math.min(), []);
        node_string = self.id + " = new Node('" + self.building + "', " + self.level + ", '" + self.id + "', " + str(self.edges) + ", '" + self.type + "', " + self.coords + ", Math.min(), []);"
        return node_string

def read_nodes():
    dataFile = open('nodes-data.csv', 'r')
    string = "nothing here"
    data = []
    dataFile.readline()
    while (string != ""):
        string = dataFile.readline()
        if(string == ""):
            break
        else:
            parse_data_nodes(string)
    dataFile.close()
    return data

# building 0 level 1 id 2 steps 4 stairs 5 manual door 6 nonwc elevator 7 ada 8 type 9 lat 10 long 11
def parse_data_nodes(string):
    # node = Node(building, level, id, [], type, null)
    string_list = string.split(",")
    node = Node(str(string_list[0]), "null", str(string_list[2]), [], str(string_list[9]), "null")
    node.setLevel(str(string_list[1]))
    node.setCoords(str(string_list[10]), str(string_list[11]))
    node.setEdges()
    nodes_names.append(node.id)
    nodes.append(node.toString())
    

def printNodes():
    for x in nodes:
        print(x)
    print()
    all_nodes = str(nodes_names)
    all_nodes = all_nodes.replace("'", "")
    print("var all_nodes = "+ all_nodes +"")


print("// define edges")
read_edges()
printEdges()
print()
print("edges_find_lengths.forEach(edge => {edge.findLength()});")
print()
print("// define nodes")
read_nodes()
printNodes()