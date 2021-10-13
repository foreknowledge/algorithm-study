package programmers.weekly_challenge

class Week10 {
    fun solution(line: Array<IntArray>): Array<String> {
        val intersections = mutableListOf<Point>()
        for (i in 0 until line.size - 1) {
            for (j in i + 1 until line.size) {
                val line1 = line[i].map { it.toLong() }
                val line2 = line[j].map { it.toLong() }
                findIntersectionPoint(line1, line2)?.let { intersections += it }
            }
        }

        val xList = intersections.map { it.x }
        val yList = intersections.map { it.y }

        val minX = xList.minOrNull()!!
        val maxX = xList.maxOrNull()!!
        val minY = yList.minOrNull()!!
        val maxY = yList.maxOrNull()!!

        return (minY .. maxY).reversed().map { h ->
            (minX .. maxX).joinToString("") { w ->
                if (Point(w, h) in intersections) "*"
                else "."
            }
        }.toTypedArray()
    }

    private fun findIntersectionPoint(line1: List<Long>, line2: List<Long>): Point? {
        val det = line1[0] * line2[1] - line1[1] * line2[0]

        // 평행인 경우 pass (일치는 주어지지 않음)
        if (det == 0L) return null

        val xNumerator = line1[1] * line2[2] - line1[2] * line2[1]
        val yNumerator = line1[2] * line2[0] - line1[0] * line2[2]

        // 교점이 소수인 경우 pass
        if (xNumerator % det != 0L) return null
        if (yNumerator % det != 0L) return null

        return Point((xNumerator / det).toInt(), (yNumerator / det).toInt())
    }

    data class Point(val x: Int, val y: Int)
}

fun main() {
    val week10 = Week10()
    println(week10.solution(arrayOf(
            intArrayOf(2, -1, 4),
            intArrayOf(-2, -1, 4),
            intArrayOf(0, -1, 1),
            intArrayOf(5, -8, -12),
            intArrayOf(5, 8, 12)
    )))
    println(week10.solution(arrayOf(
            intArrayOf(0, 1, -1),
            intArrayOf(1, 0, -1),
            intArrayOf(1, 0, 1)
    )))
    println(week10.solution(arrayOf(
            intArrayOf(1, -1, 0),
            intArrayOf(2, -1, 0)
    )))
    println(week10.solution(arrayOf(
            intArrayOf(1, -1, 0),
            intArrayOf(2, -1, 0),
            intArrayOf(4, -1, 0)
    )))
}