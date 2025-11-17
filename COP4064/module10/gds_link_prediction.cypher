// gds_link_prediction.cypher
// StackOverflow Neo4j example – Link Prediction algorithms
// Using Tag + Question structure and User + Answer + Question structure.

// NOTE: We reuse the same underlying graph, but here we focus on candidate pairs
// and apply link prediction heuristics. We use gds.alpha.linkprediction.* where available,
// or simple Cypher expressions when needed.

// =======================================================
// 1. TOTAL NUMBER OF NEIGHBORS HEURISTIC (DEGREE SUM)
// =======================================================

// ---- TAG-TAG PAIRS: potential RELATED_TAG links ----
// Candidates: pairs of tags that do NOT currently have RELATED_TAG
MATCH (t1:Tag), (t2:Tag)
WHERE id(t1) < id(t2)
  AND NOT (t1)-[:RELATED_TAG]-(t2)
WITH t1, t2,
     size( (t1)--() ) AS deg1,
     size( (t2)--() ) AS deg2
RETURN t1, t2, (deg1 + deg2) AS score
ORDER BY score DESC
LIMIT 20;

// COMMENT TOTAL NEIGHBORS (Tag pairs):
// Tags with high combined degree are both highly connected in the graph,
// suggesting that popular tags are likely to become directly related in the future.
// This heuristic tends to predict links between already central, high-activity tags.


// ---- USER-QUESTION PAIRS: potential future interactions ----
// Candidates: User & Question with no direct answer chain yet
MATCH (u:User), (q:Question)
WHERE NOT ( (u)-[:PROVIDED]->(:Answer)-[:ANSWERED]->(q) )
WITH u, q,
     size( (u)--() ) AS degU,
     size( (q)--() ) AS degQ
RETURN u, q, (degU + degQ) AS score
ORDER BY score DESC
LIMIT 20;

// COMMENT TOTAL NEIGHBORS (User-Question pairs):
// High scores indicate very active users and highly connected questions,
// which are natural candidates for future interactions.
// This heuristic is useful for suggesting questions to top contributors or experts.

// =======================================================
// 2. COMMON NEIGHBORS (CN)
// =======================================================

// ---- TAG-TAG: common neighbors via questions or related structure ----
MATCH (t1:Tag), (t2:Tag)
WHERE id(t1) < id(t2)
  AND NOT (t1)-[:RELATED_TAG]-(t2)
WITH t1, t2,
     gds.alpha.linkprediction.commonNeighbors(t1, t2) AS score
RETURN t1, t2, score
ORDER BY score DESC
LIMIT 20;

// COMMENT CN (Tag pairs):
// The common neighbors heuristic counts how many nodes two tags share as neighbors,
// for example, co-tagged questions.
// High CN scores suggest that the tags frequently appear together and are strong
// candidates for a direct RELATED_TAG link.


// ---- USER-QUESTION: common neighbors ----
MATCH (u:User), (q:Question)
WHERE NOT ( (u)-[:PROVIDED]->(:Answer)-[:ANSWERED]->(q) )
WITH u, q,
     gds.alpha.linkprediction.commonNeighbors(u, q) AS score
RETURN u, q, score
ORDER BY score DESC
LIMIT 20;

// COMMENT CN (User-Question pairs):
// For user-question pairs, high CN scores reflect shared neighbors,
// such as tags, other users, or answers, connecting them in the graph.
// These pairs are likely to become actual Q&A interactions in the future.

// =======================================================
// 3. JACCARD COEFFICIENT
// =======================================================

// ---- TAG-TAG: Jaccard similarity of neighborhoods ----
MATCH (t1:Tag), (t2:Tag)
WHERE id(t1) < id(t2)
  AND NOT (t1)-[:RELATED_TAG]-(t2)
WITH t1, t2,
     gds.alpha.linkprediction.jaccard(t1, t2) AS score
RETURN t1, t2, score
ORDER BY score DESC
LIMIT 20;

// COMMENT JACCARD (Tag pairs):
// Jaccard normalizes common neighbors by the total size of both neighborhoods,
// emphasizing tag pairs with a high proportion of shared context.
// Tags with high Jaccard scores tend to belong to tightly overlapping topics or domains.


// ---- USER-QUESTION: Jaccard ----
MATCH (u:User), (q:Question)
WHERE NOT ( (u)-[:PROVIDED]->(:Answer)-[:ANSWERED]->(q) )
WITH u, q,
     gds.alpha.linkprediction.jaccard(u, q) AS score
RETURN u, q, score
ORDER BY score DESC
LIMIT 20;

// COMMENT JACCARD (User-Question pairs):
// High Jaccard scores show user-question pairs whose neighborhoods are very similar
// relative to their total connections.
// These pairs are promising for recommending questions that match a user's existing
// interests and activity patterns.

// =======================================================
// 4. PREFERENTIAL ATTACHMENT
// =======================================================

// ---- TAG-TAG: preferential attachment ----
MATCH (t1:Tag), (t2:Tag)
WHERE id(t1) < id(t2)
  AND NOT (t1)-[:RELATED_TAG]-(t2)
WITH t1, t2,
     gds.alpha.linkprediction.preferentialAttachment(t1, t2) AS score
RETURN t1, t2, score
ORDER BY score DESC
LIMIT 20;

// COMMENT PA (Tag pairs):
// Preferential Attachment favors tag pairs where both tags already have high degree,
// so popular tags tend to link to other popular tags.
// This reflects the "rich get richer" phenomenon in the tagging network.


// ---- USER-QUESTION: preferential attachment ----
MATCH (u:User), (q:Question)
WHERE NOT ( (u)-[:PROVIDED]->(:Answer)-[:ANSWERED]->(q) )
WITH u, q,
     gds.alpha.linkprediction.preferentialAttachment(u, q) AS score
RETURN u, q, score
ORDER BY score DESC
LIMIT 20;

// COMMENT PA (User-Question pairs):
// In the user-question setting, PA highlights interactions between very active users
// and highly connected questions.
// These are likely candidates for future answers from power users on hot questions.

// =======================================================
// 5. RESOURCE ALLOCATION HEURISTIC
// =======================================================

// ---- TAG-TAG: Resource Allocation ----
MATCH (t1:Tag), (t2:Tag)
WHERE id(t1) < id(t2)
  AND NOT (t1)-[:RELATED_TAG]-(t2)
WITH t1, t2,
     gds.alpha.linkprediction.resourceAllocation(t1, t2) AS score
RETURN t1, t2, score
ORDER BY score DESC
LIMIT 20;

// COMMENT RA (Tag pairs):
// Resource Allocation gives higher weight to common neighbors that are not themselves
// very connected, emphasizing rare or specific shared neighbors.
// High RA scores indicate tag pairs that share a small but distinctive set of questions.

// ---- USER-QUESTION: Resource Allocation ----
MATCH (u:User), (q:Question)
WHERE NOT ( (u)-[:PROVIDED]->(:Answer)-[:ANSWERED]->(q) )
WITH u, q,
     gds.alpha.linkprediction.resourceAllocation(u, q) AS score
RETURN u, q, score
ORDER BY score DESC
LIMIT 20;

// COMMENT RA (User-Question pairs):
// For user-question pairs, RA favors links where the user and question share
// fewer but more unique neighbors.
// These predictions can surface more specialized, less obvious recommendations
// instead of only popular content.

// =======================================================
// 6. ADAMIC-ADAR HEURISTIC
// =======================================================

// ---- TAG-TAG: Adamic-Adar ----
MATCH (t1:Tag), (t2:Tag)
WHERE id(t1) < id(t2)
  AND NOT (t1)-[:RELATED_TAG]-(t2)
WITH t1, t2,
     gds.alpha.linkprediction.adamicAdar(t1, t2) AS score
RETURN t1, t2, score
ORDER BY score DESC
LIMIT 20;

// COMMENT ADAMIC-ADAR (Tag pairs):
// Adamic-Adar, like RA, downweights very popular neighbors using a logarithmic factor,
// highlighting tag pairs connected through rare shared neighbors.
// High scores point to strong, specific relationships that might be missing
// from the explicit RELATED_TAG edges.

// ---- USER-QUESTION: Adamic-Adar ----
MATCH (u:User), (q:Question)
WHERE NOT ( (u)-[:PROVIDED]->(:Answer)-[:ANSWERED]->(q) )
WITH u, q,
     gds.alpha.linkprediction.adamicAdar(u, q) AS score
RETURN u, q, score
ORDER BY score DESC
LIMIT 20;

// COMMENT ADAMIC-ADAR (User-Question pairs):
// In the user-question graph, Adamic-Adar identifies potential links supported
// by uncommon but meaningful shared neighbors.
// These pairs are strong candidates for personalized recommendations, going beyond
// simple popularity-based suggestions.
