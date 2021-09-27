package programmers.weekly_challenge

import kotlin.math.max
import kotlin.math.min

class Week8 {
    fun solution(sizes: Array<IntArray>): Int {
        val widths = mutableListOf<Int>()
        val heights = mutableListOf<Int>()

        sizes.forEach {
            widths.add(max(it[0], it[1]))
            heights.add(min(it[0], it[1]))
        }

        return widths.maxOrNull()!! * heights.maxOrNull()!!
    }
}

fun main() {
    val week8 = Week8()

    println(week8.solution(arrayOf(
            intArrayOf(60, 50),
            intArrayOf(30, 70),
            intArrayOf(60, 30),
            intArrayOf(80, 40)
    )))

    println(week8.solution(arrayOf(
            intArrayOf(10, 7),
            intArrayOf(12, 3),
            intArrayOf(8, 15),
            intArrayOf(14, 7),
            intArrayOf(5, 15)
    )))

    println(week8.solution(arrayOf(
            intArrayOf(14, 4),
            intArrayOf(19, 6),
            intArrayOf(6, 16),
            intArrayOf(18, 7),
            intArrayOf(7, 11)
    )))
}