class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        return len({
            ''.join(s) for r in range(1, len(tiles) + 1)
            for s in itertools.permutations(tiles, r)
        })