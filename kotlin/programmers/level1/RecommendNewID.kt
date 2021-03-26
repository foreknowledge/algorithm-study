package programmers

import java.lang.StringBuilder

class RecommendNewID {
    fun solution(new_id: String): String {
        val level1 = StringBuilder()

        for (a in new_id.toLowerCase()) {
            // 1,2단계
            if (a in 'a'..'z' || a.isDigit() || a == '-' || a == '_' || a == '.') {
                level1.append(a)
            }
        }

        val level4 = level1.split(".")
                .filter { it.isNotEmpty() }
                .joinToString(".")

        val level5 = if (level4.isEmpty()) "a" else level4

        val level6 = if (level5.length > 15) {
            val result = level5.substring(0, 15)
            if (result.last() == '.') result.dropLast(1) else result
        } else level5

        return if (level6.length < 3) {
            level6 + level6.last().toString().repeat(3 - level6.length)
        } else level6
    }
}

fun main() {
    val recommendNewID = RecommendNewID()

    println(recommendNewID.solution("...!@BaT#*..y.abcdefghijklm"))
    println(recommendNewID.solution("z-+.^."))
    println(recommendNewID.solution("=.="))
    println(recommendNewID.solution("123_.def"))
    println(recommendNewID.solution("abcdefghijklmn.p"))
}