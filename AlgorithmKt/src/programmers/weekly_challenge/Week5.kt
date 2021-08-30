package programmers.weekly_challenge

import kotlin.math.pow

class Week5 {
    fun solution(word: String): Int {
        val list = listOf('A', 'E', 'I', 'O', 'U')
        return word.mapIndexed { i, w ->
            getSum(5 - i) * list.indexOf(w)
        }.sum() + word.length
    }

    // 등비 급수 (S_n)
    private fun getSum(n: Int) = (((5.0).pow(n) - 1) / (5 - 1)).toInt()
}

fun main() {
    val week5 = Week5()
    println(week5.solution("AAAAE"))
    println(week5.solution("AAAE"))
    println(week5.solution("I"))
    println(week5.solution("EIO"))
}