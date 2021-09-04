package programmers.level3

import java.util.*
import kotlin.collections.HashMap

class FarthestNode {
    fun solution(n: Int, edge: Array<IntArray>): Int {
        return bfs(makeGraph(edge))
    }

    private fun makeGraph(edge: Array<IntArray>): HashMap<Int, List<Int>> {
        val graph = hashMapOf<Int, List<Int>>()
        edge.forEach { e ->
            graph[e[0]] = if (e[0] in graph.keys)
                graph[e[0]]!! + e[1]
            else
                mutableListOf(e[1])

            graph[e[1]] = if (e[1] in graph.keys)
                graph[e[1]]!! + e[0]
            else
                mutableListOf(e[0])
        }

        return graph
    }

    private fun bfs(graph: HashMap<Int, List<Int>>): Int {
        val queue: Queue<List<Int>> = LinkedList()
        queue += listOf(1, 0)
        val visited = mutableSetOf<Int>()

        val answer = mutableListOf<Int>()
        while (queue.isNotEmpty()) {
            val q = queue.poll()

            if (q[0] !in visited) {
                visited += q[0]
                answer += q[1]

                if (graph[q[0]] != null) {
                    if (graph[q[0]]!!.isEmpty())
                        answer += q[1]

                    graph[q[0]]!!.sorted().forEach { g ->
                        queue += listOf(g, q[1] + 1)
                    }
                }
            }
        }
        val maxDepth = answer.maxOrNull()
        return answer.filter { it == maxDepth }.size
    }
}

fun main() {
    val arr = arrayOf(
            intArrayOf(3, 6), intArrayOf(4, 3),
            intArrayOf(3, 2), intArrayOf(1, 3),
            intArrayOf(1, 2), intArrayOf(2, 4),
            intArrayOf(5, 2)
    )
    print(FarthestNode().solution(6, arr))
}