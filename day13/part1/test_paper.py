import unittest
from Paper import Paper

# python -m unittest test_paper


class TestPaper(unittest.TestCase):

    def test_paper_init(self):
        p = Paper([[0, 0], [0, 2], [2, 0]])
        self.assertEqual(len(p), 3)
        self.assertEqual(str(p), '#.#\n...\n#..\n')
        self.assertEqual(p.get_visible_dots(), 3)

    def test_paper_data(self):
        p = Paper([[6, 10],
                   [0, 14],
                   [9, 10],
                   [0, 3],
                   [10, 4],
                   [4, 11],
                   [6, 0],
                   [6, 12],
                   [4, 1],
                   [0, 13],
                   [10, 12],
                   [3, 4],
                   [3, 0],
                   [8, 4],
                   [1, 10],
                   [2, 14],
                   [8, 10],
                   [9, 0], ])
        self.assertEqual(len(p), 18)
        self.assertEqual(str(p), '...#..#..#.\n....#......\n...........\n#..........\n...#....#.#\n...........\n...........\n...........\n...........\n...........\n.#....#.##.\n....#......\n......#...#\n#..........\n#.#........\n')
        self.assertEqual(p.get_visible_dots(), 18)

    def test_fold_vertically_even(self):
        p = Paper([[0, 0], [0, 2], [2, 0]])
        self.assertEqual(len(p), 3)
        self.assertEqual(str(p), '#.#\n...\n#..\n')
        self.assertEqual(p.get_visible_dots(), 3)
        p.fold([0, 1])
        self.assertEqual(len(p), 3)
        self.assertEqual(str(p), '#.#\n')
        self.assertEqual(p.get_visible_dots(), 2)

    def test_fold_vertically_odd(self):
        p = Paper([[0, 0], [0, 3], [3, 0]])
        self.assertEqual(len(p), 3)
        self.assertEqual(str(p), '#..#\n....\n....\n#...\n')
        self.assertEqual(p.get_visible_dots(), 3)
        p.fold([0, 1])
        self.assertEqual(len(p), 3)
        self.assertEqual(str(p), '#..#\n')
        self.assertEqual(p.get_visible_dots(), 2)

    def test_fold_horizontally_odd(self):
        p = Paper([[0, 0], [0, 2], [2, 0]])
        self.assertEqual(len(p), 3)
        self.assertEqual(str(p), '#.#\n...\n#..\n')
        self.assertEqual(p.get_visible_dots(), 3)
        p.fold([1, 0])
        self.assertEqual(len(p), 3)
        self.assertEqual(str(p), '#\n.\n#\n')
        self.assertEqual(p.get_visible_dots(), 2)

    def test_fold_horizontally_even(self):
        p = Paper([[0, 0], [0, 3], [3, 0]])
        self.assertEqual(len(p), 3)
        self.assertEqual(str(p), '#..#\n....\n....\n#...\n')
        self.assertEqual(p.get_visible_dots(), 3)
        p.fold([1, 0])
        self.assertEqual(len(p), 3)
        self.assertEqual(str(p), '#\n.\n.\n#\n')
        self.assertEqual(p.get_visible_dots(), 2)

    def test_paper_full(self):
        p = Paper([[6, 10],
                   [0, 14],
                   [9, 10],
                   [0, 3],
                   [10, 4],
                   [4, 11],
                   [6, 0],
                   [6, 12],
                   [4, 1],
                   [0, 13],
                   [10, 12],
                   [3, 4],
                   [3, 0],
                   [8, 4],
                   [1, 10],
                   [2, 14],
                   [8, 10],
                   [9, 0], ])
        self.assertEqual(len(p), 18)
        self.assertEqual(p.get_visible_dots(), 18)
        self.assertEqual(str(p), '...#..#..#.\n....#......\n...........\n#..........\n...#....#.#\n...........\n...........\n...........\n...........\n...........\n.#....#.##.\n....#......\n......#...#\n#..........\n#.#........\n')
        p.fold([0, 7])
        self.assertEqual(str(
            p), '#.##..#..#.\n#...#......\n......#...#\n#...#......\n.#.#..#.###\n...........\n...........\n')
        self.assertEqual(p.get_visible_dots(), 17)
        p.fold([5, 0])
        self.assertEqual(str(
            p), '#####\n#...#\n#...#\n#...#\n#####\n.....\n.....\n')
        self.assertEqual(p.get_visible_dots(), 16)


if __name__ == '__main__':
    unittest.main()
