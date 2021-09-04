package programmers.level1

import java.util.*

class CranePuppetGame {
    private lateinit var basket: Stack<Int>

    fun solution(board: Array<IntArray>, moves: IntArray): Int {
        basket = Stack()
        return moves.map { putAndErase(popTopItem(board, it - 1)) }.sum()
    }

    private fun putAndErase(item: Int?): Int {
        if (item == null) return 0

        if (basket.size != 0 && basket.peek() == item) {
            basket.pop()
            return 2
        }
        basket.push(item)

        return 0
    }

    private fun popTopItem(board: Array<IntArray>, col: Int): Int? {
        for (i in board[0].indices) {
            val topItem = board[i][col]
            if (topItem != 0) {
                board[i][col] = 0
                return topItem
            }
        }

        return null
    }
}

fun main() {
    val cranePuppetGame = CranePuppetGame()
    println(cranePuppetGame.solution(
            arrayOf(
                    intArrayOf(0, 0, 0, 0, 0),
                    intArrayOf(0, 0, 1, 0, 3),
                    intArrayOf(0, 2, 5, 0, 1),
                    intArrayOf(4, 2, 4, 4, 2),
                    intArrayOf(3, 5, 1, 3, 1)
            ),
            intArrayOf(1, 5, 3, 5, 1, 2, 1, 4)
    ))
}