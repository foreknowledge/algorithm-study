package programmers.level3

/**
 * 답안 참고
 */
class Immigration {
    fun solution(n: Int, times: IntArray): Long {
        var min = 1L
        var max = n.toLong() * times.maxOrNull()!!.toLong()
        var answer = 0L

        while (min <= max) {
            val mid = (max + min) / 2

            val process = times.map { mid / it }.sum()
            when {
                process < n -> { // under
                    min = mid + 1
                }
                else -> { // over or same(더 작은 해)
                    max = mid - 1
                    answer = mid
                }
            }
        }

        return answer
    }
}

fun main() {
    val immigration = Immigration()
    println(immigration.solution(6, intArrayOf(7, 10)))
    println(immigration.solution(3, intArrayOf(1, 99, 99)))
    println(immigration.solution(2, intArrayOf(10, 15)))
}