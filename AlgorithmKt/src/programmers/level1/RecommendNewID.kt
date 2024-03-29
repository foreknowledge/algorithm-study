package programmers.level1

class RecommendNewID {
    fun solution(new_id: String): String {
        return new_id.toLowerCase()
                .filter { it.isLowerCase() || it.isDigit() || it == '-' || it == '_' || it == '.' }
                .split(".").filter { it.isNotEmpty() }.joinToString(".")
                .let { if (it.isEmpty()) "a" else it }
                .let { if (it.length > 15) it.substring(0, 15) else it }
                .let { if (it.last() == '.') it.dropLast(1) else it }
                .let {
                    if (it.length < 3) {
                        it + it.last().toString().repeat(3 - it.length)
                    } else it
                }
    }
}

fun main() {
    val recommendNewId = RecommendNewID()
    println(recommendNewId.solution("...!@BaT#*..y.abcdefghijklm"))
    println(recommendNewId.solution("z-+.^."))
    println(recommendNewId.solution("=.="))
    println(recommendNewId.solution("123_.def"))
    println(recommendNewId.solution("abcdefghijklmn.p"))
}