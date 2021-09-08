package programmers.weekly_challenge

class Week6First {
    fun solution(weights: IntArray, head2head: Array<String>): IntArray {
        val result = mutableListOf<Record>()

        head2head.forEachIndexed { i, results ->
            val winCount = results.filter { it == 'W' }.count()
            val gameCount = results.filter { it != 'N' }.count()
            val winRate = if (gameCount == 0) 0.0 else winCount.toDouble() / gameCount
            val winHeavier = results.filterIndexed { j, result -> weights[i] < weights[j] && result == 'W' }.count()
            result += Record(i + 1, winRate, winHeavier, weights[i])
        }
        result.forEach { println(it) }

        return result.sortedByDescending { it.player }
                .sortedBy { it.weight }
                .sortedBy { it.winHeavier }
                .sortedBy { it.winRate }
                .reversed()
                .map { it.player }
                .toIntArray()
    }

    data class Record(val player: Int, val winRate: Double, val winHeavier: Int, val weight: Int)
}

fun main() {
    val week6First = Week6First()
    println(week6First.solution(intArrayOf(50, 82, 75, 120), arrayOf("NLWL", "WNLL", "LWNW", "WWLN")).joinToString())
    println(week6First.solution(intArrayOf(145, 92, 86), arrayOf("NLW", "WNL", "LWN")).joinToString())
    println(week6First.solution(intArrayOf(60, 70, 60), arrayOf("NNN", "NNN", "NNN")).joinToString())
}