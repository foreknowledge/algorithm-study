package test

import java.util.*
import kotlin.collections.HashMap

class FarthestNode {
    fun solution(n: Int, edge: Array<IntArray>): Int {
        val graph = hashMapOf<Int, MutableList<Int>>()
        for (e in edge) {
            if (graph.keys.contains(e[0])) {
                val temp = graph[e[0]]
                temp!!.add(e[1])
                graph[e[0]] = temp
            } else {
                graph[e[0]] = mutableListOf(e[1])
            }

            if (graph.keys.contains(e[1])) {
                val temp = graph[e[1]]
                temp!!.add(e[0])
                graph[e[1]] = temp
            } else {
                graph[e[1]] = mutableListOf(e[0])
            }
        }

        return bfs(graph)
    }

    private fun bfs(graph: HashMap<Int, MutableList<Int>>): Int {
        val queue: Queue<List<Int>> = LinkedList()
        queue.add(arrayListOf(1, 0))
        val visited = mutableSetOf<Int>()

        val answer = mutableListOf<Int>()
        while (queue.isNotEmpty()) {
            val q = queue.poll()

            if (!visited.contains(q[0])) {
                visited.add(q[0])
                answer.add(q[1])

                if (graph[q[0]] != null) {
                    if (graph[q[0]]!!.isEmpty()) {
                        answer.add(q[1])
                    }
                    for (g in graph[q[0]]!!.sorted()) {
                        queue.add(arrayListOf(g, q[1]+1))
                    }
                }
            }
        }
        val maxDepth = answer.max()
        return answer.filter { it == maxDepth }.size
    }
}

fun main() {
    val arr = arrayOf(intArrayOf(3, 6), intArrayOf(4, 3), intArrayOf(3, 2), intArrayOf(1, 3), intArrayOf(1, 2), intArrayOf(2, 4), intArrayOf(5, 2))
    print(FarthestNode().solution(6, arr))
}