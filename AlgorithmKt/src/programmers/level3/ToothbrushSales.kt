package programmers.level3

class ToothbrushSales {
    fun solution(enroll: Array<String>, referral: Array<String>, seller: Array<String>, amount: IntArray): IntArray {
        // 추천인 테이블
        val referralTable = mutableMapOf<String, String>()
        for (i in enroll zip referral) {
            referralTable[i.first] = i.second
        }

        // 이익 테이블
        val profitTable = mutableMapOf<String, Int>()
        for (e in enroll)
            profitTable[e] = 0

        for (i in seller zip amount.toList()) {
            val profit = i.second * 100
            var commission = profit / 10
            val pureProfit = profit - commission

            // 내 이익 추가
            profitTable[i.first] = profitTable[i.first]!! + pureProfit

            // 추천인에게 배분
            var next = i.first
            while (referralTable[next] != null) {
                val referee = referralTable[next]!!
                val nextCommission = commission / 10
                val pure = commission - nextCommission
                if (profitTable[referee] != null) {
                    profitTable[referee] = profitTable[referee]!! + pure
                }

                if (nextCommission == 0)
                    break

                next = referee
                commission = nextCommission
            }
        }

        return enroll.map { profitTable[it]!! }.toIntArray()
    }
}

fun main() {
    println(ToothbrushSales().solution(
            arrayOf("john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"),
            arrayOf("-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"),
            arrayOf("young", "john", "tod", "emily", "mary"),
            intArrayOf(12, 4, 2, 5, 10)).joinToString(", "))
}