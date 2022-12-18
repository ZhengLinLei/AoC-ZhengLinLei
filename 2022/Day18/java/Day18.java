// Part 1 an 2

// ZhengLinLei
import java.util.Arrays;
import java.util.List;
import java.nio.file.Files;
import java.nio.file.Paths;

public class Day18 {
    public record Point(int x, int y, int z) {
        @Override
        public String toString() {
            return x + "," + y + "," + z;
        }
    }
    public enum Tile {
        LAVA,
        AIR,
        AIR2
    }

    public static void main(String[] args) {
        // Part 1
        String text = Files.readString(Paths.get("../input.txt"));;
        // Find Area
        long area = 0;
        List<String> lines = Arrays.asList(text.split("\n"));
        for (String line : lines) {
            String[] parts = line.split(",");
            int x = Integer.parseInt(parts[0]);
            int y = Integer.parseInt(parts[1]);
            int z = Integer.parseInt(parts[2]);
            Point[] testPoints = new Point[]{
                    new Point(x + 1, y, z),
                    new Point(x - 1, y, z),
                    new Point(x, y + 1, z),
                    new Point(x, y - 1, z),
                    new Point(x, y, z + 1),
                    new Point(x, y, z - 1)
            };
            for (Point testPoint : testPoints) {
                if (!lines.contains(testPoint.toString())) {
                    area++;
                }
            }
        }
        System.out.println("Part 1: " + area);

        // Find Area
        int minX = Integer.MAX_VALUE;
        int maxX = Integer.MIN_VALUE;
        int minY = Integer.MAX_VALUE;
        int maxY = Integer.MIN_VALUE;
        int minZ = Integer.MAX_VALUE;
        int maxZ = Integer.MIN_VALUE;
        for (String line : lines) {
            String[] parts = line.split(",");
            int x = Integer.parseInt(parts[0]);
            minX = Math.min(minX, x);
            maxX = Math.max(maxX, x);
            int y = Integer.parseInt(parts[1]);
            minY = Math.min(minY, y);
            maxY = Math.max(maxY, y);
            int z = Integer.parseInt(parts[2]);
            minZ = Math.min(minZ, z);
            maxZ = Math.max(maxZ, z);
        }
        int borderWidth = 1;
        Tile[][][] map = new Tile[(maxX + 1) - minX + (borderWidth * 2)][(maxY + 1) - minY + (borderWidth * 2)][(maxZ + 1) - minZ + (borderWidth * 2)];
        for (String line : lines) {
            String[] parts = line.split(",");
            int x = Integer.parseInt(parts[0]);
            int y = Integer.parseInt(parts[1]);
            int z = Integer.parseInt(parts[2]);
            map[x - minX + borderWidth][y - minY + borderWidth][z - minZ + borderWidth] = Tile.LAVA;
        }
        map[0][0][0] = Tile.AIR;
        while (true) {
            int tilesChanged = 0;
            for (int x = 0; x < map.length; x++) {
                for (int y = 0; y < map[x].length; y++) {
                    for (int z = 0; z < map[x][y].length; z++) {
                        if (map[x][y][z] == Tile.AIR) {
                            int localTilesChanged = 0;
                            Point[] testPoints = new Point[]{
                                    new Point(x + 1, y, z),
                                    new Point(x - 1, y, z),
                                    new Point(x, y + 1, z),
                                    new Point(x, y - 1, z),
                                    new Point(x, y, z + 1),
                                    new Point(x, y, z - 1)
                            };
                            for (Point testPoint : testPoints) {
                                if (testPoint.x < 0) {
                                    continue;
                                }
                                if (testPoint.x >= map.length) {
                                    continue;
                                }
                                if (testPoint.y < 0) {
                                    continue;
                                }
                                if (testPoint.y >= map[x].length) {
                                    continue;
                                }
                                if (testPoint.z < 0) {
                                    continue;
                                }
                                if (testPoint.z >= map[x][y].length) {
                                    continue;
                                }
                                if (map[testPoint.x][testPoint.y][testPoint.z] == null) {
                                    map[testPoint.x][testPoint.y][testPoint.z] = Tile.AIR;
                                    localTilesChanged++;
                                }
                            }
                            if (localTilesChanged == 0) {
                                map[x][y][z] = Tile.AIR2;
                            } else {
                                tilesChanged += localTilesChanged;
                            }
                        }
                    }
                }
            }
            if (tilesChanged == 0) {
                break;
            }
        }
        area = 0;
        for (int x = 0; x < map.length; x++) {
            for (int y = 0; y < map[x].length; y++) {
                for (int z = 0; z < map[x][y].length; z++) {
                    if (map[x][y][z] == Tile.LAVA) {
                        Point[] testPoints = new Point[]{
                                new Point(x + 1, y, z),
                                new Point(x - 1, y, z),
                                new Point(x, y + 1, z),
                                new Point(x, y - 1, z),
                                new Point(x, y, z + 1),
                                new Point(x, y, z - 1)
                        };
                        for (Point testPoint : testPoints) {
                            if (map[testPoint.x][testPoint.y][testPoint.z] == Tile.AIR || map[testPoint.x][testPoint.y][testPoint.z] == Tile.AIR2) {
                                area++;
                            }
                        }
                    }
                }
            }
        }
        System.out.println("Part 2: " + area);
    }
}
