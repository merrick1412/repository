// gds_centrality.cypher
// StackOverflow Neo4j example – centrality & community characterization
// Assumes the StackOverflow graph (Users, Questions, Answers, Tags) is already loaded
// and build_stackoverflow_graph.py has created :RELATED_TAG relationships.

// =======================================================
// 1. DROP GRAPHS IF THEY EXIST
// =======================================================

CALL gds.graph.exists('TagQuestionGraph') YIELD exists AS tqExists;
CALL gds.graph.exists('UserAnswerQuestionGraph') YIELD exists AS uaqExists;

CALL gds.graph.drop('TagQuestionGraph', false) YIELD graphName
  WITH graphName
  WHERE tqExists = true;
CALL gds.graph.drop('UserAnswerQuestionGraph', false) YIELD graphName
  WITH graphName
  WHERE uaqExists = true;

// =======================================================
// 2. CREATE PROJECTED GRAPHS
// =======================================================

// Graph 1: TagQuestionGraph (Tag + Question + TAGGED + RELATED_TAG)
CALL gds.graph.project(
  'TagQuestionGraph',
  ['Tag', 'Question'],
  {
    TAGGED: {
      type: 'TAGGED',
      orientation: 'UNDIRECTED'
    },
    RELATED_TAG: {
      type: 'RELATED_TAG',
      orientation: 'UNDIRECTED'
    }
  }
);

// Graph 2: UserAnswerQuestionGraph (User, Answer, Question + PROVIDED, ANSWERED)
CALL gds.graph.project(
  'UserAnswerQuestionGraph',
  ['User', 'Answer', 'Question'],
  {
    PROVIDED: {
      type: 'PROVIDED',
      orientation: 'NATURAL'
    },
    ANSWERED: {
      type: 'ANSWERED',
      orientation: 'NATURAL'
    }
  }
);

// =======================================================
// 3. DEGREE
// =======================================================

// ---- TagQuestionGraph: DEGREE ----

// STREAM
CALL gds.degree.stream('TagQuestionGraph')
YIELD nodeId, score
RETURN gds.util.asNode(nodeId) AS node, labels(node) AS labels, score AS degree
ORDER BY degree DESC
LIMIT 20;

// WRITE
CALL gds.degree.write(
  'TagQuestionGraph',
  { writeProperty: 'degree_tq' }
)
YIELD nodePropertiesWritten;

// VIEW top 20 written
MATCH (n)
WHERE exists(n.degree_tq)
RETURN n, labels(n) AS labels, n.degree_tq AS degree
ORDER BY degree DESC
LIMIT 20;

// MUTATE
CALL gds.degree.mutate(
  'TagQuestionGraph',
  { mutateProperty: 'degree_tq_mut' }
)
YIELD nodePropertiesWritten;

// COMMENT DEGREE (TagQuestionGraph):
// Degree highlights tags and questions that are connected to many others.
// High-degree tags represent broad or popular topics, while high-degree questions
// may be those that share many tags or are connected to many related tags.

// ---- UserAnswerQuestionGraph: DEGREE ----

// STREAM
CALL gds.degree.stream('UserAnswerQuestionGraph')
YIELD nodeId, score
RETURN gds.util.asNode(nodeId) AS node, labels(node) AS labels, score AS degree
ORDER BY degree DESC
LIMIT 20;

// WRITE
CALL gds.degree.write(
  'UserAnswerQuestionGraph',
  { writeProperty: 'degree_uaq' }
)
YIELD nodePropertiesWritten;

// VIEW
MATCH (n)
WHERE exists(n.degree_uaq)
RETURN n, labels(n) AS labels, n.degree_uaq AS degree
ORDER BY degree DESC
LIMIT 20;

// MUTATE
CALL gds.degree.mutate(
  'UserAnswerQuestionGraph',
  { mutateProperty: 'degree_uaq_mut' }
)
YIELD nodePropertiesWritten;

// COMMENT DEGREE (UserAnswerQuestionGraph):
// In this graph, users or questions with high degree are heavily involved in Q&A activity,
// either by providing many answers or being associated with many answers.
// These nodes correspond to key participants and highly visible questions in the community.

// =======================================================
// 4. PAGERANK
// =======================================================

// ---- TagQuestionGraph: PageRank ----

// STREAM
CALL gds.pageRank.stream(
  'TagQuestionGraph',
  { maxIterations: 20, dampingFactor: 0.85 }
)
YIELD nodeId, score
RETURN gds.util.asNode(nodeId) AS node, labels(node) AS labels, score
ORDER BY score DESC
LIMIT 20;

// WRITE
CALL gds.pageRank.write(
  'TagQuestionGraph',
  {
    maxIterations: 20,
    dampingFactor: 0.85,
    writeProperty: 'pagerank_tq'
  }
)
YIELD nodePropertiesWritten;

// MUTATE
CALL gds.pageRank.mutate(
  'TagQuestionGraph',
  {
    maxIterations: 20,
    dampingFactor: 0.85,
    mutateProperty: 'pagerank_tq_mut'
  }
)
YIELD nodePropertiesWritten;

// COMMENT PAGERANK (TagQuestionGraph):
// PageRank rewards nodes that are connected to other important nodes.
// Tags or questions with high PageRank are central not just by count of links,
// but by being part of highly connected regions of the StackOverflow tag-question graph.

// ---- UserAnswerQuestionGraph: PageRank ----

// STREAM
CALL gds.pageRank.stream(
  'UserAnswerQuestionGraph',
  { maxIterations: 20, dampingFactor: 0.85 }
)
YIELD nodeId, score
RETURN gds.util.asNode(nodeId) AS node, labels(node) AS labels, score
ORDER BY score DESC
LIMIT 20;

// WRITE
CALL gds.pageRank.write(
  'UserAnswerQuestionGraph',
  {
    maxIterations: 20,
    dampingFactor: 0.85,
    writeProperty: 'pagerank_uaq'
  }
)
YIELD nodePropertiesWritten;

// MUTATE
CALL gds.pageRank.mutate(
  'UserAnswerQuestionGraph',
  {
    maxIterations: 20,
    dampingFactor: 0.85,
    mutateProperty: 'pagerank_uaq_mut'
  }
)
YIELD nodePropertiesWritten;

// COMMENT PAGERANK (UserAnswerQuestionGraph):
// In this Q&A-style graph, nodes with high PageRank are influential users or pivotal questions,
// since they participate in many answer chains connected to other central nodes.
// These results highlight experts and questions that attract high-value activity.

// =======================================================
// 5. BETWEENNESS CENTRALITY
// =======================================================

// ---- TagQuestionGraph: Betweenness ----

// STREAM
CALL gds.betweenness.stream('TagQuestionGraph')
YIELD nodeId, score
RETURN gds.util.asNode(nodeId) AS node, labels(node) AS labels, score
ORDER BY score DESC
LIMIT 20;

// WRITE
CALL gds.betweenness.write(
  'TagQuestionGraph',
  { writeProperty: 'betweenness_tq' }
)
YIELD nodePropertiesWritten;

// MUTATE
CALL gds.betweenness.mutate(
  'TagQuestionGraph',
  { mutateProperty: 'betweenness_tq_mut' }
)
YIELD nodePropertiesWritten;

// COMMENT BETWEENNESS (TagQuestionGraph):
// Nodes with high betweenness sit on many shortest paths between other nodes,
// acting as bridges between different tag or question clusters.
// Such tags or questions connect otherwise separate topics or communities.

// ---- UserAnswerQuestionGraph: Betweenness ----

// STREAM
CALL gds.betweenness.stream('UserAnswerQuestionGraph')
YIELD nodeId, score
RETURN gds.util.asNode(nodeId) AS node, labels(node) AS labels, score
ORDER BY score DESC
LIMIT 20;

// WRITE
CALL gds.betweenness.write(
  'UserAnswerQuestionGraph',
  { writeProperty: 'betweenness_uaq' }
)
YIELD nodePropertiesWritten;

// MUTATE
CALL gds.betweenness.mutate(
  'UserAnswerQuestionGraph',
  { mutateProperty: 'betweenness_uaq_mut' }
)
YIELD nodePropertiesWritten;

// COMMENT BETWEENNESS (UserAnswerQuestionGraph):
// Here, high-betweenness users and questions connect different sub-communities of the site.
// They tend to be "bridge" experts or cross-cutting questions that link otherwise separate
// groups of users and topics.

// =======================================================
// 6. WCC (Weakly Connected Components)
// =======================================================

// ---- TagQuestionGraph: WCC ----

// STREAM
CALL gds.wcc.stream('TagQuestionGraph')
YIELD nodeId, componentId
RETURN gds.util.asNode(nodeId) AS node, labels(node) AS labels, componentId
ORDER BY componentId ASC
LIMIT 20;

// WRITE
CALL gds.wcc.write(
  'TagQuestionGraph',
  { writeProperty: 'wcc_tq' }
)
YIELD nodePropertiesWritten, componentCount;

// MUTATE
CALL gds.wcc.mutate(
  'TagQuestionGraph',
  { mutateProperty: 'wcc_tq_mut' }
)
YIELD nodePropertiesWritten, componentCount;

// COMMENT WCC (TagQuestionGraph):
// WCC reveals disconnected regions of the tag-question graph.
// Separate components indicate groups of tags and questions that are not linked to the rest,
// often reflecting niche topics or isolated subsets of the dataset.

// ---- UserAnswerQuestionGraph: WCC ----

// STREAM
CALL gds.wcc.stream('UserAnswerQuestionGraph')
YIELD nodeId, componentId
RETURN gds.util.asNode(nodeId) AS node, labels(node) AS labels, componentId
ORDER BY componentId ASC
LIMIT 20;

// WRITE
CALL gds.wcc.write(
  'UserAnswerQuestionGraph',
  { writeProperty: 'wcc_uaq' }
)
YIELD nodePropertiesWritten, componentCount;

// MUTATE
CALL gds.wcc.mutate(
  'UserAnswerQuestionGraph',
  { mutateProperty: 'wcc_uaq_mut' }
)
YIELD nodePropertiesWritten, componentCount;

// COMMENT WCC (UserAnswerQuestionGraph):
// In the Q&A interaction graph, WCC shows user-answer-question clusters that are isolated
// from each other. Components can represent topic-specific communities or disconnected
// islands of Q&A activity.

// =======================================================
// 7. LOUVAIN COMMUNITY DETECTION
// =======================================================

// ---- TagQuestionGraph: Louvain ----

// STREAM
CALL gds.louvain.stream(
  'TagQuestionGraph',
  { includeIntermediateCommunities: false }
)
YIELD nodeId, communityId, score
RETURN gds.util.asNode(nodeId) AS node,
       labels(node) AS labels,
       communityId, score
ORDER BY score DESC
LIMIT 20;

// WRITE
CALL gds.louvain.write(
  'TagQuestionGraph',
  {
    writeProperty: 'louvain_tq',
    includeIntermediateCommunities: false
  }
)
YIELD communityCount, modularity, modularities;

// MUTATE
CALL gds.louvain.mutate(
  'TagQuestionGraph',
  {
    mutateProperty: 'louvain_tq_mut',
    includeIntermediateCommunities: false
  }
)
YIELD communityCount, modularity, modularities;

// COMMENT LOUVAIN (TagQuestionGraph):
// Louvain identifies communities where tags and questions are densely connected.
// These communities often correspond to topical clusters (e.g., related technologies),
// useful for organizing the knowledge graph and identifying related groups of questions.

// ---- UserAnswerQuestionGraph: Louvain ----

// STREAM
CALL gds.louvain.stream(
  'UserAnswerQuestionGraph',
  { includeIntermediateCommunities: false }
)
YIELD nodeId, communityId, score
RETURN gds.util.asNode(nodeId) AS node,
       labels(node) AS labels,
       communityId, score
ORDER BY score DESC
LIMIT 20;

// WRITE
CALL gds.louvain.write(
  'UserAnswerQuestionGraph',
  {
    writeProperty: 'louvain_uaq',
    includeIntermediateCommunities: false
  }
)
YIELD communityCount, modularity, modularities;

// MUTATE
CALL gds.louvain.mutate(
  'UserAnswerQuestionGraph',
  {
    mutateProperty: 'louvain_uaq_mut',
    includeIntermediateCommunities: false
  }
)
YIELD communityCount, modularity, modularities;

// COMMENT LOUVAIN (UserAnswerQuestionGraph):
// In this graph, Louvain groups users, answers, and questions into communities
// of dense interaction. These communities reveal natural clusters of users and topics,
// which can be leveraged for recommendation, moderation, or community analysis.
