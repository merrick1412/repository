"""
build_stackoverflow_graph.py

Python script that connects to the Neo4j StackOverflow example database
and builds additional graph structure:

Nodes (already in the dump):
  - User
  - Question
  - Answer
  - Tag

Relationships (already in the dump):
  - (Question)-[:TAGGED]->(Tag)
  - (Answer)-[:ANSWERED]->(Question)
  - (User)-[:PROVIDED]->(Answer)

New relationship created by this script:
  - (t1:Tag)-[r:RELATED_TAG {weight: <int>}]- (t2:Tag)
    * Undirected (we will query as '-[:RELATED_TAG]-')
    * Weighted: 'weight' = number of Questions sharing both tags

This satisfies:
  - at least 3 different node labels
  - at least 2 different relationship types
  - at least 1 undirected relationship
  - at least 1 relationship with a weight attribute
"""

from neo4j import GraphDatabase

# ------------------ CONFIG ------------------ #
URI = "neo4j://localhost:7687"
USER = "mwmoncure@gmail.com"
PASSWORD = "password"           # <-- change to your Neo4j password
# -------------------------------------------- #


def get_driver():
    return GraphDatabase.driver(URI, auth=(USER, PASSWORD))


def create_constraints(session):
    """
    Optional but nice: add uniqueness constraints for core labels.
    Adjust if constraints already exist.
    """
    session.run("""
        CREATE CONSTRAINT IF NOT EXISTS
        FOR (t:Tag)
        REQUIRE t.name IS UNIQUE
    """)
    session.run("""
        CREATE CONSTRAINT IF NOT EXISTS
        FOR (q:Question)
        REQUIRE q.id IS UNIQUE
    """)
    session.run("""
        CREATE CONSTRAINT IF NOT EXISTS
        FOR (u:User)
        REQUIRE u.id IS UNIQUE
    """)
    session.run("""
        CREATE CONSTRAINT IF NOT EXISTS
        FOR (a:Answer)
        REQUIRE a.id IS UNIQUE
    """)


def create_related_tag_relationships(session):
    """
    Create RELATED_TAG relationships between Tag pairs that co-occur
    on at least one Question. The weight is the number of Questions
    that use both tags.
    """
    # Delete old RELATED_TAG if re-running
    session.run("""
        MATCH ()-[r:RELATED_TAG]-()
        DELETE r
    """)

    # Create new weighted, undirected relationships
    session.run("""
        MATCH (q:Question)-[:TAGGED]->(t1:Tag),
              (q)-[:TAGGED]->(t2:Tag)
        WHERE id(t1) < id(t2)
        WITH t1, t2, count(DISTINCT q) AS commonQuestions
        MERGE (t1)-[r:RELATED_TAG]-(t2)
        SET r.weight = commonQuestions
    """)


def main():
    driver = get_driver()
    with driver.session() as session:
        print("Creating constraints (if not already present)...")
        create_constraints(session)

        print("Creating RELATED_TAG relationships with weight property...")
        create_related_tag_relationships(session)

        print("Done building additional StackOverflow graph structure.")

    driver.close()


if __name__ == "__main__":
    main()
