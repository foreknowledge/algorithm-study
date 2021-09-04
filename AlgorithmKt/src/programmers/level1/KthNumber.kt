package programmers.level1

class KthNumber {
    fun solution(array: IntArray, commands: Array<IntArray>): IntArray {
        val answer = mutableListOf<Int>()

        commands.forEach { c ->
            val a = array.slice(IntRange(c[0]-1, c[1]-1)).sorted()
            answer += a[c[2]-1]
        }

        return answer.toIntArray()
    }
}

fun main() {
    val arr1 = intArrayOf(1, 5, 2, 6, 3, 7, 4)
    val arr2 = arrayOf(
        intArrayOf(2, 5, 3),
        intArrayOf(4, 4, 1),
        intArrayOf(1, 7, 3)
    )
    println(KthNumber().solution(arr1, arr2))
}