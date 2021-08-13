package programmers.weekly_challenge

class Week2 {
    fun solution(scores: Array<IntArray>): String {
        var answer = ""

        for (i in scores.indices) {
            val received = scores.map { it[i] }
            val selfScore = scores[i][i]

            // 제외 조건
            val exCondition = (received.count { it == selfScore } == 1) &&
                    (selfScore == received.maxOrNull() || selfScore == received.minOrNull())

            val average = received.filter { !(it == selfScore && exCondition) }.average()

            val grade = when {
                average >= 90 -> "A"
                average >= 80 -> "B"
                average >= 70 -> "C"
                average >= 50 -> "D"
                else -> "F"
            }

            answer += grade
        }

        return answer
    }
}

fun main() {
    val week2 = Week2()
    println(week2.solution(arrayOf(
            intArrayOf(100,90,98,88,65),
            intArrayOf(50,45,99,85,77),
            intArrayOf(47,88,95,80,67),
            intArrayOf(61,57,100,80,65),
            intArrayOf(24,90,94,75,65)
    )))
    println(week2.solution(arrayOf(
            intArrayOf(50,90),
            intArrayOf(50,87)
    )))
    println(week2.solution(arrayOf(
            intArrayOf(70,49,90),
            intArrayOf(68,50,38),
            intArrayOf(73,31,100)
    )))
}