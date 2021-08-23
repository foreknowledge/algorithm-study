package programmers.weekly_challenge

import kotlin.test.assertEquals

class Week4 {
    fun solution(table: Array<String>, languages: Array<String>, preference: IntArray): String {
        val result = mutableMapOf<Int, List<String>>()
        table.map { row ->
            val element = row.split(" ")
            val occupation = element[0]
            val lank = listOf(element[5], element[4], element[3], element[2], element[1])

            val score = languages.mapIndexed { i, lang -> (lank.indexOf(lang) + 1) * preference[i] }.sum()

            result[score] = result[score]?.let { it + occupation } ?: listOf(occupation)
        }

        val maxScore = result.keys.maxOrNull()!!
        return result[maxScore]!!.sorted()[0]
    }
}

fun main() {
    assertEquals(
            Week4().solution(
            arrayOf(
                    "SI JAVA JAVASCRIPT SQL PYTHON C#",
                    "CONTENTS JAVASCRIPT JAVA PYTHON SQL C++",
                    "HARDWARE C C++ PYTHON JAVA JAVASCRIPT",
                    "PORTAL JAVA JAVASCRIPT PYTHON KOTLIN PHP",
                    "GAME C++ C# JAVASCRIPT C JAVA"
            ),
            arrayOf("PYTHON", "C++", "SQL"),
            intArrayOf(7, 5, 5))
    , "HARDWARE")

    assertEquals(
            Week4().solution(
            arrayOf(
                    "SI JAVA JAVASCRIPT SQL PYTHON C#",
                    "CONTENTS JAVASCRIPT JAVA PYTHON SQL C++",
                    "HARDWARE C C++ PYTHON JAVA JAVASCRIPT",
                    "PORTAL JAVA JAVASCRIPT PYTHON KOTLIN PHP",
                    "GAME C++ C# JAVASCRIPT C JAVA"
            ),
            arrayOf("JAVA", "JAVASCRIPT"),
            intArrayOf(7, 5))
    , "PORTAL")
}