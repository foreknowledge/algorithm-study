package programmers.level2

class PlainSquare {
    fun solution(w: Int, h: Int): Long {
        val total = w.toLong() * h.toLong()
        return total - (w + h - gcd(w, h))
    }

    private fun gcd(a: Int, b: Int): Long {
        var aa = a.toLong()
        var bb = b.toLong()
        while (bb != 0L) {
            val r: Long = aa % bb
            aa = bb
            bb = r
        }

        return aa
    }
}

fun main() {
    val plainSquare = PlainSquare()
    println(plainSquare.solution(8, 12))
}