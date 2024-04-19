# CPCS-331_CS1_AE
# AI Group Project: Solving Maze Problems
#
# Students:-
# Mahmued Alardawi - 2135209
# Ahmad Aljedaani - 2136071
# Abdullah Emad Almashharawi - 2136141
# Abdullah Abed Alharbi- 2135999

import networkx
from matplotlib import pyplot


def draw_graph(graph):
    pos = networkx.spring_layout(graph)
    networkx.draw(graph, pos, with_labels=True)
    labels = networkx.get_edge_attributes(graph, 'relationship')
    networkx.draw_networkx_edge_labels(graph, pos, edge_labels=labels)
    pyplot.show()


def draw_graph_with_target(graph, target_node, target_color='red', default_color='blue'):
    node_colors = [target_color if node == target_node else default_color for node in graph.nodes()]
    pos = networkx.spring_layout(graph)
    networkx.draw(graph, pos, node_color=node_colors, with_labels=True)
    pyplot.show()


def check_node(graph, node):
    if graph.has_node(node):
        print(f"The node '{node}' is in the graph.")
    else:
        print(f"The node '{node}' is not in the graph.")


def get_edges_of_node(graph, node):
    edges_and_relationships = [(n1, n2, data.get('relationship', None))
                               for n1, n2, data in graph.edges(node, data=True)]

    for edge1, edge2, relationship in edges_and_relationships:
        print(f"Edge: {edge1}, Edge: {edge2}, Relationship: {relationship}")

def create_subgraph_from_path(graph, path):
    subgraph = networkx.Graph()

    for i in range(len(path) - 1):
        node_start = path[i]
        node_end = path[i + 1]
        if graph.has_edge(node_start, node_end):
            edge_data = graph.get_edge_data(node_start, node_end)
            subgraph.add_edge(node_start, node_end, **edge_data)
        else:
            raise ValueError(f"The edge between {node_start} and {node_end} does not exist in the original graph.")

    return subgraph


def is_related(graph, start, end):
    if networkx.has_path(graph, start, end):
        path = networkx.shortest_path(graph, start, end)
    else:
        path = None
    return path

# Example usage:
# Assuming 'G' is a previously created NetworkX graph object


# Creating Graph
G = networkx.Graph()

# Adding Entities (Nodes):
G.add_nodes_from([
    "University", "Departments", "Faculty", "Students", "Administration", "Library",
    "Sports Teams", "Alumni", "Facilities", "Policies", "Courses", "Research",
    "Committees", "Grants", "Academic Papers", "Study Groups", "Seminars", "Labs",
    "Industry", "Equipment", "Publications", "Finances", "Services", "Workshops",
    "Databases", "Study Spaces", "Leagues", "Championships", "Reunions", "Networking Events",
    "Modules", "Various Formats", "Research Teams", "Patents", "Accreditation Bodies",
    "Organizations", "Learning Opportunities", "Partnerships", "Local Development",
    "Classrooms", "Recreational Areas", "Staff", "Conferences", "Cultural Activities", "Conduct",
    "Textbooks", "Lectures", "Exams", "Clubs", "Scholarships", "Community Service"
])

# Adding Relationships (Edges):
G.add_edge("University", "Departments", relationship="HAS")
G.add_edge("University", "Faculty", relationship="HAS")
G.add_edge("University", "Students", relationship="HAS")
G.add_edge("University", "Administration", relationship="HAS")
G.add_edge("University", "Library", relationship="HAS")
G.add_edge("University", "Sports Teams", relationship="HAS")
G.add_edge("University", "Alumni", relationship="HAS")
G.add_edge("University", "Facilities", relationship="HAS")
G.add_edge("University", "Policies", relationship="HAS")

G.add_edge("Faculty", "Courses", relationship="TEACHES")
G.add_edge("Faculty", "Research", relationship="CONDUCTS")
G.add_edge("Faculty", "Students", relationship="ADVISES")
G.add_edge("Faculty", "Committees", relationship="PARTICIPATES IN")
G.add_edge("Faculty", "Other Faculty", relationship="COLLABORATES WITH")
G.add_edge("Faculty", "Grants", relationship="WRITES")
G.add_edge("Faculty", "Academic Papers", relationship="REVIEWS")
G.add_edge("Faculty", "Departments", relationship="BELONGS TO")

G.add_edge("Students", "Courses", relationship="ENROLL IN")
G.add_edge("Students", "Library", relationship="USE")
G.add_edge("Students", "Sports Teams", relationship="JOIN")
G.add_edge("Students", "Alumni", relationship="BECOME")
G.add_edge("Students", "Research", relationship="PARTICIPATE IN")
G.add_edge("Students", "Clubs", relationship="PARTICIPATE IN")
G.add_edge("Students", "Study Groups", relationship="FORM")
G.add_edge("Students", "Scholarships", relationship="APPLY FOR")
G.add_edge("Students", "Lectures", relationship="ATTEND")
G.add_edge("Students", "Assignments", relationship="SUBMIT")
G.add_edge("Students", "Exams", relationship="TAKE")
G.add_edge("Students", "Community Service", relationship="VOLUNTEER IN")

G.add_edge("Departments", "Courses", relationship="OFFER")
G.add_edge("Departments", "Faculty", relationship="MANAGE")
G.add_edge("Departments", "Research", relationship="CONDUCT")
G.add_edge("Departments", "Majors", relationship="COORDINATE")
G.add_edge("Departments", "Curriculum", relationship="DEVELOP")
G.add_edge("Departments", "Seminars", relationship="HOST")
G.add_edge("Departments", "Labs", relationship="MAINTAIN")
G.add_edge("Departments", "Industry", relationship="COLLABORATE WITH")

G.add_edge("Courses", "Faculty", relationship="TAUGHT BY")
G.add_edge("Courses", "Students", relationship="TAKEN BY")
G.add_edge("Courses", "Departments", relationship="OFFERED BY")
G.add_edge("Courses", "Textbooks", relationship="REQUIRE")
G.add_edge("Courses", "Lectures", relationship="INCLUDE")
G.add_edge("Courses", "Exams", relationship="REQUIRE")
G.add_edge("Courses", "Credits", relationship="PROVIDE")
G.add_edge("Courses", "Prerequisites", relationship="HAVE")
G.add_edge("Courses", "Students", relationship="EVALUATE")
G.add_edge("Courses", "Modules", relationship="ARE STRUCTURED IN")
G.add_edge("Courses", "Various Formats", relationship="ARE DELIVERED IN")

G.add_edge("Research", "Faculty", relationship="CONDUCTED BY")
G.add_edge("Research", "Equipment", relationship="USES")
G.add_edge("Research", "Funding", relationship="RECEIVES")
G.add_edge("Research", "Publications", relationship="PRODUCES")
G.add_edge("Research", "Problems", relationship="ADDRESSES")
G.add_edge("Research", "Technologies", relationship="DEVELOPS")
G.add_edge("Research", "Faculty and Students", relationship="TEAMS CONSIST OF")
G.add_edge("Research", "Patents", relationship="RESULTS IN")
G.add_edge("Research", "Industry", relationship="INFLUENCES")

G.add_edge("Administration", "University", relationship="MANAGES")
G.add_edge("Administration", "Students", relationship="SUPPORTS")
G.add_edge("Administration", "Faculty", relationship="EMPLOYS")
G.add_edge("Administration", "Finances", relationship="OVERSEES")
G.add_edge("Administration", "Policies", relationship="ENFORCES")
G.add_edge("Administration", "Facilities", relationship="MAINTAINS")
G.add_edge("Administration", "Services", relationship="PROVIDES")
G.add_edge("Administration", "Events", relationship="COORDINATES")

G.add_edge("Library", "Resources", relationship="PROVIDES")
G.add_edge("Library", "Research", relationship="SUPPORTS")
G.add_edge("Library", "Students", relationship="USED BY")
G.add_edge("Library", "Publications", relationship="ARCHIVES")
G.add_edge("Library", "Workshops", relationship="ORGANIZES")
G.add_edge("Library", "Databases", relationship="MAINTAINS")
G.add_edge("Library", "Study Spaces", relationship="OFFERS")

G.add_edge("Sports Teams", "Students", relationship="COMPRISE OF")
G.add_edge("Sports Teams", "University", relationship="REPRESENT")
G.add_edge("Sports Teams", "Regular Practice", relationship="PRACTICE")
G.add_edge("Sports Teams", "Leagues", relationship="COMPETE IN")
G.add_edge("Sports Teams", "Championships", relationship="WIN")

G.add_edge("Alumni", "University", relationship="GRADUATED FROM")
G.add_edge("Alumni", "University", relationship="SUPPORT")
G.add_edge("Alumni", "Students", relationship="NETWORK WITH")
G.add_edge("Alumni", "University", relationship="DONATE TO")
G.add_edge("Alumni", "Students", relationship="MENTOR")
G.add_edge("Alumni", "Reunions", relationship="ATTEND")
G.add_edge("Alumni", "Scholarships", relationship="ESTABLISH")
G.add_edge("Alumni", "Networking Events", relationship="PARTICIPATE IN")

G.add_edge("Committees", "Faculty and Administration", relationship="INCLUDE")
G.add_edge("Committees", "Decisions", relationship="MAKE")
G.add_edge("Committees", "Policies", relationship="REVIEW")

G.add_edge("Majors", "A Set Of Courses", relationship="REQUIRE")
G.add_edge("Majors", "Students", relationship="PREPARE FOR Careers")
G.add_edge("Majors", "Accreditation Bodies", relationship="ARE RECOGNIZED BY")

G.add_edge("Scholarships", "Deserving Students", relationship="ARE AWARDED TO")
G.add_edge("Scholarships", "Alumni and Organizations", relationship="ARE FUNDED BY")
G.add_edge("Scholarships", "Students", relationship="SUPPORT")

G.add_edge("Community Service", "Learning Opportunities", relationship="PROVIDES")
G.add_edge("Community Service", "Partnerships", relationship="BUILDS")
G.add_edge("Community Service", "Local Development", relationship="CONTRIBUTES TO")

G.add_edge("Facilities", "Classrooms, Labs, and Recreational Areas", relationship="INCLUDE")
G.add_edge("Facilities", "Students and Faculty", relationship="ARE USED BY")
G.add_edge("Facilities", "Staff", relationship="ARE MAINTAINED BY")

G.add_edge("Events", "Conferences, Workshops, and Cultural Activities", relationship="INCLUDE")
G.add_edge("Events", "Students, Faculty, and Alumni", relationship="ARE ATTENDED BY")
G.add_edge("Events", "University Culture", relationship="PROMOTE")

G.add_edge("Policies", "Conduct", relationship="GOVERN")
G.add_edge("Policies", "Administration", relationship="ARE DEVELOPED BY")
G.add_edge("Policies", "Students and Faculty", relationship="ARE COMPLIED WITH")

# Plotting the graph
draw_graph(G)

# Plotting the graph with specific color to a node
draw_graph_with_target(G, "University", target_color="red")

# Removing nodes
G.remove_nodes_from(["Grants", "Research Teams", "Conferences", "Classrooms", "Organizations", "Cultural Activities",
                     "Study Groups", "Recreational Areas"])
draw_graph_with_target(G, "Events", target_color="red")

# Removing edges
G.remove_edges_from([("Policies", "Administration"), ("Policies", "Students and Faculty")])
draw_graph_with_target(G, "Policies", target_color="red")


# Check if node exists
check_node(G, "University")
print()

check_node(G, "Kharbosh")
print()

# Finding edges of node
get_edges_of_node(G, "University")
print()

# Finding a specific pattern
pattern = ["University", "Departments", "Courses", "Faculty", "Students", "Lectures"]
g1 = create_subgraph_from_path(G, pattern)
draw_graph(g1)

# Check if the nodes are related
path = is_related(G, "University", "Lectures")
if path is not None:
    g1 = create_subgraph_from_path(G, path)
    draw_graph(g1)
