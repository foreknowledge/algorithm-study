package programmers.weekly_challenge

import java.util.*

class Week7 {
    fun solution(enter: IntArray, leave: IntArray): IntArray {
        val leaves: Queue<Int> = LinkedList(leave.toList())
        val meetingRoom = mutableListOf<Int>()
        val meet = enter.map { mutableSetOf<Int>() }.toList()

        var enterIndex = 0
        while (leaves.isNotEmpty()) {
            val person = enter[enterIndex++]
            meetingRoom.add(person)

            if (meetingRoom.size > 1) {
                for (i in 0 until meetingRoom.size - 1) {
                    val p = meetingRoom[i]
                    meet[p - 1].add(person)
                    meet[person - 1].add(p)
                }
            }

            while (leaves.peek() in meetingRoom)
                meetingRoom.remove(leaves.poll())
        }

        return meet.map { it.size }.toIntArray()
    }
}

fun main() {
    val week7 = Week7()
    println(week7.solution(intArrayOf(1, 3, 2), intArrayOf(1, 2, 3)).toList())
    println(week7.solution(intArrayOf(1, 4, 2, 3), intArrayOf(2, 1, 3, 4)).toList())
    println(week7.solution(intArrayOf(3, 2, 1), intArrayOf(2, 1, 3)).toList())
    println(week7.solution(intArrayOf(3, 2, 1), intArrayOf(1, 3, 2)).toList())
    println(week7.solution(intArrayOf(1, 4, 2, 3), intArrayOf(2, 1, 4, 3)).toList())
}