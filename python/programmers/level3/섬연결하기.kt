package test

class ConnectIsland {
    fun solution(n: Int, costs: Array<IntArray>): Int {
        val sortedCosts = costs.sortedBy { it[2] }
        val visited = mutableSetOf(0)

        var answer = 0
        while (visited.size < n) {
            for ((s, e, c) in sortedCosts) {
                if (visited.contains(s) or visited.contains(e)) {
                    if (visited.contains(s) and visited.contains(e)) {
                        continue
                    }
                    visited.add(s)
                    visited.add(e)
                    answer += c
                    break
                }
            }
        }
        return answer
    }
}

fun main() {
    val arr = arrayOf(
        intArrayOf(0,1,1),
        intArrayOf(0,2,2),
        intArrayOf(1,2,5),
        intArrayOf(1,3,1),
        intArrayOf(2,3,8)
    )
    println(ConnectIsland().solution(4, arr))
}