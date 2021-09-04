package programmers.level3

class ConnectIsland {
    fun solution(n: Int, costs: Array<IntArray>): Int {
        var answer = 0
        val visited = mutableSetOf(0)

        while (visited.size < n) {
            for ((start, end, cost) in costs.sortedBy { it[2] }) {
                if (start in visited || end in visited) {
                    if (start in visited && end in visited)
                        continue

                    visited += start
                    visited += end
                    answer += cost
                    break
                }
            }
        }
        return answer
    }
}

fun main() {
    val arr = arrayOf(
            intArrayOf(0, 1, 1),
            intArrayOf(0, 2, 2),
            intArrayOf(1, 2, 5),
            intArrayOf(1, 3, 1),
            intArrayOf(2, 3, 8)
    )
    println(ConnectIsland().solution(4, arr))
}