package programmers.weekly_challenge

import java.util.*
import kotlin.math.abs

class Week9 {
    fun solution(n: Int, wires: Array<IntArray>): Int {
        val linkedList = mutableMapOf<Int, MutableList<Int>>()
        wires.forEach {
            addItem(linkedList, it[0], it[1])
            addItem(linkedList, it[1], it[0])
        }

        val diff = mutableListOf<Int>()
        wires.forEach {
            linkedList[it[0]]!!.remove(it[1])
            linkedList[it[1]]!!.remove(it[0])
            diff += abs(findConnectedNodes(linkedList, it[0]).size - findConnectedNodes(linkedList, it[1]).size)
            linkedList[it[0]]!!.add(it[1])
            linkedList[it[1]]!!.add(it[0])
        }

        return diff.minOrNull()!!
    }

    private fun addItem(list: MutableMap<Int, MutableList<Int>>, key: Int, value: Int) {
        if (list.containsKey(key)) list[key]!!.add(value)
        else list[key] = mutableListOf(value)
    }

    private fun findConnectedNodes(list: Map<Int, List<Int>>, start: Int): List<Int> {
        val queue: Queue<Int> = LinkedList()
        queue += start
        val connected = mutableListOf<Int>()
        while (queue.isNotEmpty()) {
            val target = queue.poll()
            connected += target

            list[target]?.filter { it !in connected }
                    ?.forEach { queue += it }
        }

        return connected
    }
}

fun main() {
    val week9 = Week9()
    println(week9.solution(9, arrayOf(
            intArrayOf(1, 3),
            intArrayOf(2, 3),
            intArrayOf(3, 4),
            intArrayOf(4, 5),
            intArrayOf(4, 6),
            intArrayOf(4, 7),
            intArrayOf(7, 8),
            intArrayOf(7, 9)
    )))
    println(week9.solution(4, arrayOf(
            intArrayOf(1, 2),
            intArrayOf(2, 3),
            intArrayOf(3, 4)
    )))
    println(week9.solution(7, arrayOf(
            intArrayOf(1, 2),
            intArrayOf(2, 7),
            intArrayOf(3, 7),
            intArrayOf(3, 4),
            intArrayOf(4, 5),
            intArrayOf(6, 7)
    )))
}