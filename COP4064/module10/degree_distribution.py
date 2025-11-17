"""
degree_distribution.py

Builds and displays the node degree distribution for Tag nodes
in the Neo4j StackOverflow graph.

Degree = number of relationships (of any type) connected to a Tag.
"""

from neo4j import GraphDatabase
import matplotlib.pyplot as plt

URI = "neo4j://localhost:7687"  # or "bolt://localhost:7687"
USER = "neo4j"
PASSWORD = "password"           # <-- change


def get_driver():
    return GraphDatabase.driver(URI, auth=(USER, PASSWORD))


def fetch_tag_degrees():
    """
    Returns a list of integer degrees for all Tag nodes.
    """
    driver = get_driver()
    degrees = []

    with driver.session() as session:
        result = session.run("""
            MATCH (t:Tag)
            RETURN size( (t)--() ) AS degree
        """)

        for record in result:
            degrees.append(record["degree"])

    driver.close()
    return degrees


def plot_degree_distribution(degrees):
    plt.figure()
    plt.hist(degrees, bins=20)
    plt.xlabel("Degree")
    plt.ylabel("Number of Tag nodes")
    plt.title("Degree Distribution for Tag Nodes (StackOverflow Graph)")
    plt.grid(True)
    plt.show()


def main():
    degrees = fetch_tag_degrees()
    print(f"Fetched degrees for {len(degrees)} Tag nodes.")
    if degrees:
        plot_degree_distribution(degrees)
    else:
        print("No Tag nodes found.")


if __name__ == "__main__":
    main()
