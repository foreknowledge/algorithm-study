package programmers.weekly_challenge

import java.util.*

class Week3 {
    fun solution(game_board: Array<IntArray>, table: Array<IntArray>): Int {
        var answer = 0

        // 빈 공간을 구조화
        val spaces = structure(game_board, 0)
        // 블럭들을 구조화
        val blocks = structure(table, 1)

        // 블럭들을 돌면서 빈 공간에 들어갈 수 있는지 확인
        blocks.forEach { block ->
            for (space in spaces) {
                // 넓이 or 사각형 영역이 다른 경우 들어갈 수 없다.
                if (block.size != space.size) continue
                if (block.rect != space.rect) continue

                // block을 돌려가며 space와 동일한 모양인지 확인
                if (block.coords == space.coords ||
                        block.rotate90().coords == space.coords ||
                        block.rotate90().coords == space.coords ||
                        block.rotate90().coords == space.coords) {
                    answer += block.size
                    spaces.remove(space)
                    break
                }
            }
        }

        return answer
    }

    private fun structure(table: Array<IntArray>, filled: Int): MutableList<Block> {
        val N = table.size
        // 구조화 된 블럭 리스트
        val blockList = mutableListOf<Block>()
        // 현재 위치를 체크 했는지 확인
        val checked = Array(N) { Array(N) { 0 } }
        // 연결된 다음 체크 포인트
        val queue: Queue<Point> = LinkedList()

        for (i in table.indices) {
            for (j in table[i].indices) {
                if (checked[i][j] == 1) continue
                checked[i][j] = 1

                // 검사 시작 위치를 찾은 경우
                if (table[i][j] == filled) {
                    val block = Block(mutableSetOf(Point(i, j)))
                    blockList.add(block)

                    // 오른쪽, 아래쪽이 연결 되어 있는지 확인
                    if (j + 1 < N && table[i][j + 1] == filled)
                        queue.add(Point(i, j + 1))
                    if (i + 1 < N && table[i + 1][j] == filled)
                        queue.add(Point(i + 1, j))

                    while (queue.isNotEmpty()) {
                        val (x, y) = queue.poll()
                        if (checked[x][y] == 1) continue
                        checked[x][y] = 1

                        // 블럭 정보 업데이트
                        block.coords.add(Point(x, y))

                        // 상하좌우가 연결 되어 있는지 확인
                        if (x - 1 > -1 && table[x - 1][y] == filled)
                            queue.add(Point(x - 1, y))
                        if (y - 1 > -1 && table[x][y - 1] == filled)
                            queue.add(Point(x, y - 1))
                        if (x + 1 < N && table[x + 1][y] == filled)
                            queue.add(Point(x + 1, y))
                        if (y + 1 < N && table[x][y + 1] == filled)
                            queue.add(Point(x, y + 1))
                    }
                }
            }
        }

        // 각 블럭의 좌표 변환 (global coords -> local coords)
        blockList.forEach { it.localize() }

        return blockList
    }

    data class Block(var coords: MutableSet<Point>) {
        val size get() = coords.size
        var rect: Rect = Rect(1, 1)

        fun localize() {
            val xList = coords.map { it.x }
            val yList = coords.map { it.y }
            val minX = xList.minOrNull() ?: 0
            val minY = yList.minOrNull() ?: 0
            val maxX = xList.maxOrNull() ?: 0
            val maxY = yList.maxOrNull() ?: 0

            coords = coords.map {
                Point(it.x - minX, it.y - minY)
            }.toMutableSet()

            rect = Rect(maxX - minX + 1, maxY - minY + 1)
        }

        fun rotate90(): Block {
            coords = coords.map {
                val newX = rect.height - 1 - it.y
                val newY = it.x
                Point(newX, newY)
            }.toMutableSet()

            rect = Rect(rect.height, rect.width)

            return this
        }
    }

    data class Point(val x: Int, val y: Int)

    data class Rect(val width: Int, val height: Int) {
        override fun equals(other: Any?): Boolean {
            if (other !is Rect) return false

            return (width == other.width && height == other.height) ||
                    (width == other.height && height == other.width)
        }

        override fun hashCode(): Int {
            var result = width
            result = 31 * result + height
            return result
        }
    }
}

fun main() {
    val week3 = Week3()
    println(week3.solution(
            arrayOf(
                    intArrayOf(1, 1, 0, 0, 1, 0),
                    intArrayOf(0, 0, 1, 0, 1, 0),
                    intArrayOf(0, 1, 1, 0, 0, 1),
                    intArrayOf(1, 1, 0, 1, 1, 1),
                    intArrayOf(1, 0, 0, 0, 1, 0),
                    intArrayOf(0, 1, 1, 1, 0, 0)
            ),
            arrayOf(
                    intArrayOf(1, 0, 0, 1, 1, 0),
                    intArrayOf(1, 0, 1, 0, 1, 0),
                    intArrayOf(0, 1, 1, 0, 1, 1),
                    intArrayOf(0, 0, 1, 0, 0, 0),
                    intArrayOf(1, 1, 0, 1, 1, 0),
                    intArrayOf(0, 1, 0, 0, 0, 0)
            )
    ))
    println(week3.solution(
            arrayOf(
                    intArrayOf(0, 0, 0),
                    intArrayOf(1, 1, 0),
                    intArrayOf(1, 1, 1)
            ),
            arrayOf(
                    intArrayOf(1, 1, 1),
                    intArrayOf(1, 0, 0),
                    intArrayOf(0, 0, 0)
            )
    ))
}