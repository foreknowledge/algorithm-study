package programmers.level3

/**
 * 답안 참고
 */
class ExpressAsN {
    fun solution(N: Int, number: Int): Int {
        val results = (1..8).map {
            mutableSetOf(N.toString().repeat(it).toInt())
        }

        // 최적화 - 사칙연산 없이 만들 수 있는 경우 계산하지 않고 바로 리턴
        results.forEachIndexed { i, set ->
            if (number in set)
                return i + 1
        }

        for (i in 1..7) {
            for (n in 1..i) {
                val m = (i + 1) - n

                if (n > m) continue

                val set1 = results[n - 1]
                val set2 = results[m - 1]
                results[i] += calc(set1, set2)
            }
        }

        // 찾으면 해당 위치 리턴
        results.forEachIndexed { i, set ->
            if (number in set)
                return i + 1
        }

        // 못 찾으면 -1 리턴
        return -1
    }

    private fun calc(s1: Set<Int>, s2: Set<Int>): Set<Int> {
        val result = mutableSetOf<Int>()
        s1.forEach { a ->
            s2.forEach { b ->
                result.add(a + b)
                result.add(a - b)
                result.add(a * b)
                if (b != 0)
                    result.add(a / b)

                if (a != b) {
                    result.add(b - a)
                    if (a != 0)
                        result.add(b / a)
                }
            }
        }

        return result
    }
}

fun main() {
    val expressAsN = ExpressAsN()
    println(expressAsN.solution(5, 12))
    println(expressAsN.solution(5, 55))
    println(expressAsN.solution(2, 11))
}