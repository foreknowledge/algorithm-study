package programmers.level1

class MockExam {
    fun solution(answers: IntArray): IntArray {
        val one = intArrayOf(1, 2, 3, 4, 5)
        val two = intArrayOf(2, 1, 2, 3, 2, 4, 2, 5, 2, 1, 2, 3, 2, 4, 2, 5)
        val three = intArrayOf(3, 3, 1, 1, 2, 2, 4, 4, 5, 5)

        var score1 = 0
        var score2 = 0
        var score3 = 0
        for ((i, a) in answers.withIndex()) {
            if (a == one[i % one.size]) score1 += 1
            if (a == two[i % two.size]) score2 += 1
            if (a == three[i % three.size]) score3 += 1
        }

        val scoreArr = intArrayOf(score1, score2, score3)
        val maxScore = scoreArr.maxOrNull()

        val answer = mutableListOf<Int>()
        for ((i, s) in scoreArr.withIndex()) {
            if (s == maxScore)
                answer += i + 1
        }

        return answer.toIntArray()
    }
}

fun main() {
    println(MockExam().solution(intArrayOf(1,2,3,4,5)).joinToString(","))
    println(MockExam().solution(intArrayOf(1,3,2,4,2)).joinToString(","))
}