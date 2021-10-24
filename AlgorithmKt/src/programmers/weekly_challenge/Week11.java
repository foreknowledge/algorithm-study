package programmers.weekly_challenge;

import java.util.Arrays;

public class Week11 {
    public int solution(int[][] rectangle, int characterX, int characterY, int itemX, int itemY) {
        // 사각형 좌표 2배 확대
        int[][] scaledRectangle = new int[rectangle.length][4];
        for (int i = 0; i < rectangle.length; i++) {
            int[] r = new int[4];
            for (int j = 0; j < 4; j++) {
                r[j] = rectangle[i][j] * 2;
            }
            scaledRectangle[i] = r;
        }

        // 위치 좌표 2배 확대
        Point characterPoint = new Point(characterX * 2, characterY * 2);
        Point itemPoint = new Point(itemX * 2, itemY * 2);

        int clockwiseDistance = calcDistance(scaledRectangle, characterPoint, itemPoint, true);
        int counterClockwiseDistance = calcDistance(scaledRectangle, characterPoint, itemPoint, false);

        // 결과 2배 축소
        return Math.min(clockwiseDistance, counterClockwiseDistance) / 2;
    }

    public int calcDistance(int[][] rectangles, Point characterPoint, Point itemPoint, boolean isClockwise) {
        Point curPoint = characterPoint;

        // 현재 point가 포함되어 있는 타겟 사각형 찾기
        int[] targetRectangle = rectangles[0];
        for (int[] r : rectangles) {
            if (curPoint.isEdgeOfRectangle(r)) {
                targetRectangle = r;
                break;
            }
        }

        int move = 0;
        while (!curPoint.equals(itemPoint)) {
            Point nextPoint = getNextPoint(targetRectangle, curPoint, isClockwise);

            // 이동 불가능한 경우 (다른 사각형의 내부로 이동하려는 경우) 체크
            boolean isInsideOtherRectangle = false;
            for (int[] r : rectangles) {
                if (Arrays.equals(targetRectangle, r)) continue;
                if (nextPoint.isInsideRectangle(r)) {
                    targetRectangle = r;
                    isInsideOtherRectangle = true;
                    break;
                }
            }
            if (isInsideOtherRectangle) continue;

            // 이동 가능한 경우
            curPoint = nextPoint;
            move += 1;

            // 다른 사각형의 엣지라면 타겟 사각형 변경
            for (int[] r : rectangles) {
                if (Arrays.equals(targetRectangle, r)) continue;
                if (nextPoint.isEdgeOfRectangle(r)) {
                    targetRectangle = r;
                    break;
                }
            }
        }
        return move;
    }

    private Point getNextPoint(int[] rectangle, Point point, boolean isClockwise) {
        Point bottomLeft = new Point(rectangle[0], rectangle[1]);
        Point rightTop = new Point(rectangle[2], rectangle[3]);

        if (point.x == bottomLeft.x) {
            if (point.y == bottomLeft.y) {
                if (isClockwise) return point.toUp();
                else return point.toRight();
            }
            if (point.y == rightTop.y) {
                if (isClockwise) return point.toRight();
                else return point.toDown();
            }
        }
        if (point.x == rightTop.x) {
            if (point.y == bottomLeft.y) {
                if (isClockwise) return point.toLeft();
                else return point.toUp();
            }
            if (point.y == rightTop.y) {
                if (isClockwise) return point.toDown();
                else return point.toLeft();
            }
        }
        if (point.x > bottomLeft.x && point.x < rightTop.x) {
            if (point.y == bottomLeft.y) {
                if (isClockwise) return point.toLeft();
                else return point.toRight();
            }
            if (point.y == rightTop.y) {
                if (isClockwise) return point.toRight();
                else return point.toLeft();
            }
        }
        if (point.y > bottomLeft.y && point.y < rightTop.y) {
            if (point.x == bottomLeft.x) {
                if (isClockwise) return point.toUp();
                else return point.toDown();
            }
            if (point.x == rightTop.x) {
                if (isClockwise) return point.toDown();
                else return point.toUp();
            }
        }

        return null;
    }

    static class Point {
        int x;
        int y;

        public Point(int x, int y) { this.x = x; this.y = y; }

        public Point toUp() { return new Point(x, y + 1); }
        public Point toDown() { return new Point(x, y - 1); }
        public Point toLeft() { return new Point(x - 1, y); }
        public Point toRight() { return new Point(x + 1, y); }

        @Override
        public boolean equals(Object obj) {
            return obj instanceof Point && ((Point) obj).x == x && ((Point) obj).y == y;
        }

        public boolean isInsideRectangle(int[] rectangle) {
            return (x > rectangle[0] && x < rectangle[2] && y > rectangle[1] && y < rectangle[3]);
        }

        public boolean isEdgeOfRectangle(int[] rectangle) {
            Point bottomLeft = new Point(rectangle[0], rectangle[1]);
            Point rightTop = new Point(rectangle[2], rectangle[3]);

            return ((x >= bottomLeft.x && x <= rightTop.x) && (y == bottomLeft.y || y == rightTop.y)) ||
                    ((y >= bottomLeft.y && y <= rightTop.y) && (x == bottomLeft.x || x == rightTop.x));
        }
    }

    public static void main(String[] args) {
        Week11 week11 = new Week11();
        System.out.println(week11.solution(
                new int[][]{{1, 1, 7, 4}, {3, 2, 5, 5}, {4, 3, 6, 9}, {2, 6, 8, 8}},
                1, 3, 7, 8
        ));
        System.out.println(week11.solution(
                new int[][]{{1, 1, 8, 4}, {2, 2, 4, 9}, {3, 6, 9, 8}, {6, 3, 7, 7}},
                9, 7, 6, 1
        ));
        System.out.println(week11.solution(
                new int[][]{{1, 1, 5, 7}},
                1, 1, 4, 7
        ));
        System.out.println(week11.solution(
                new int[][]{{2, 1, 7, 5}, {6, 4, 10, 10}},
                3, 1, 7, 10
        ));
        System.out.println(week11.solution(
                new int[][]{{2, 2, 5, 5}, {1, 3, 6, 4}, {3, 1, 4, 6}},
                1, 4, 1, 3
        ));
        System.out.println(week11.solution(
                new int[][]{{1, 1, 4, 3}, {2, 2, 3, 5}, {1, 4, 4, 6}},
                2, 4, 3, 3
        ));
        System.out.println(week11.solution(
                new int[][]{{1, 2, 3, 6}, {2, 1, 6, 3}, {5, 2, 7, 6}, {2, 5, 6, 7}},
                2, 6, 6, 6
        ));
        System.out.println(week11.solution(
                new int[][]{{3, 1, 6, 4}, {2, 3, 4, 6}, {1, 2, 5, 5}},
                3, 2, 5, 4
        ));
        System.out.println(week11.solution(
                new int[][]{{1, 2, 7, 3}, {2, 1, 3, 7}, {5, 1, 6, 7}, {1, 5, 7, 6}},
                2, 2, 3, 6
        ));
    }
}