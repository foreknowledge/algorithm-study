package programmers.weekly_challenge

class Week12 {
    fun solution(k: Int, dungeons: Array<IntArray>): Int {
        return explore(k, dungeons.toMutableList(), 0)
    }

    private fun explore(k: Int, dungeons: MutableList<IntArray>, depth: Int): Int {
        return dungeons.map {
            if (k >= it[0]) { // 다음 던전 탐험할 수 있는 경우
                val rest = (dungeons - it).toMutableList()
                explore(k - it[1], rest, depth + 1)
            } else depth
        }.maxOrNull() ?: depth
    }
}

fun main() {
    val week12 = Week12()
    println(week12.solution(80, arrayOf(intArrayOf(80,20),intArrayOf(50,40),intArrayOf(30,10))))
}