package programmers.level1

import java.lang.StringBuilder
import kotlin.math.abs

class PressKeypad {
    private lateinit var lPos: Pos
    private lateinit var rPos: Pos
    private var hand: String = ""

    fun solution(numbers: IntArray, hand: String): String {
        lPos = Pos(0, 3)
        rPos = Pos(2, 3)
        this.hand = hand

        val answer = StringBuilder()
        numbers.forEach { n ->
            val h = when (n) {
                1, 4, 7 -> "L"
                3, 6, 9 -> "R"
                else -> closeHand(n)
            }
            answer.append(h)

            if (h == "L") lPos = getPos(n)
            else rPos = getPos(n)
        }

        return answer.toString()
    }

    private fun closeHand(n: Int): String {
        val p = getPos(n)
        val lDistance = lPos - p
        val rDistance = rPos - p

        return when {
            (lDistance < rDistance) -> "L"
            (lDistance > rDistance) -> "R"
            else -> if (hand == "left") "L" else "R"
        }
    }

    private fun getPos(n: Int): Pos {
        if (n == 0) return Pos(1, 3)

        val x = (n - 1) % 3
        val y = (n - 1) / 3
        return Pos(x, y)
    }

    data class Pos(val x: Int, val y: Int) {
        operator fun minus(other: Pos): Int {
            return abs(other.x - x) + abs(other.y - y)
        }
    }
}

fun main() {
    val pressKeypad = PressKeypad()

    println(pressKeypad.solution(intArrayOf(1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5), "right"))
    println(pressKeypad.solution(intArrayOf(7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2), "left"))
    println(pressKeypad.solution(intArrayOf(1, 2, 3, 4, 5, 6, 7, 8, 9, 0), "right"))
}