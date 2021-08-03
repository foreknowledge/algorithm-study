package programmers.weekly_challenge

import java.lang.Long.max

class CalcLackOfMoney {
    fun solution(price: Int, money: Int, count: Int): Long {
        val answer: Long = price * ((count.toLong() * (count.toLong() + 1)) / 2) - money
        return max(answer, 0)
    }
}

fun main() {
    println(CalcLackOfMoney().solution(3, 20, 4))
}