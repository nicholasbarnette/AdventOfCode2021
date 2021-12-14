import unittest
from Map import Map

# python -m unittest test_map


class TestMap(unittest.TestCase):

    def test_map_init(self):
        m = Map(['start-A',
                 'start-b',
                 'A-c',
                 'A-b',
                 'b-d',
                 'A-end',
                 'b-end'
                 ])
        self.assertEqual(m.get_nodes(), 6)
        self.assertEqual(m.get_connections(), 14)
        self.assertEqual(str(
            m), 'start-A\nstart-b\nA-start\nA-c\nA-b\nA-end\nb-start\nb-A\nb-d\nb-end\nc-A\nd-b\nend-A\nend-b\n')

    def test_map_get_paths(self):
        m = Map(['start-A',
                 'start-b',
                 'A-c',
                 'A-b',
                 'b-d',
                 'A-end',
                 'b-end'
                 ])

        actual = m.find_paths()
        actual.sort()
        expected = ['start,A,b,A,c,A,end',
                    'start,A,b,A,end',
                    'start,A,b,end',
                    'start,A,c,A,b,A,end',
                    'start,A,c,A,b,end',
                    'start,A,c,A,end',
                    'start,A,end',
                    'start,b,A,c,A,end',
                    'start,b,A,end',
                    'start,b,end']
        expected.sort()
        self.assertEqual(len(actual), 10)
        self.assertEqual(actual, expected)

    def test_map_get_paths_larger(self):
        m = Map(['dc-end',
                'HN-start',
                 'start-kj',
                 'dc-start',
                 'dc-HN',
                 'LN-dc',
                 'HN-end',
                 'kj-sa',
                 'kj-HN',
                 'kj-dc'
                 ])

        actual = m.find_paths()
        actual.sort()
        expected = ['start,HN,dc,HN,end',
                    'start,HN,dc,HN,kj,HN,end',
                    'start,HN,dc,end',
                    'start,HN,dc,kj,HN,end',
                    'start,HN,end',
                    'start,HN,kj,HN,dc,HN,end',
                    'start,HN,kj,HN,dc,end',
                    'start,HN,kj,HN,end',
                    'start,HN,kj,dc,HN,end',
                    'start,HN,kj,dc,end',
                    'start,dc,HN,end',
                    'start,dc,HN,kj,HN,end',
                    'start,dc,end',
                    'start,dc,kj,HN,end',
                    'start,kj,HN,dc,HN,end',
                    'start,kj,HN,dc,end',
                    'start,kj,HN,end',
                    'start,kj,dc,HN,end',
                    'start,kj,dc,end']
        expected.sort()
        self.assertEqual(len(actual), 19)
        self.assertEqual(actual.sort(), expected)

    def test_map_get_paths_larger(self):
        m = Map(['fs-end',
                 'he-DX',
                 'fs-he',
                 'start-DX',
                 'pj-DX',
                 'end-zg',
                 'zg-sl',
                 'zg-pj',
                 'pj-he',
                 'RW-he',
                 'fs-DX',
                 'pj-RW',
                 'zg-RW',
                 'start-pj',
                 'he-WI',
                 'zg-he',
                 'pj-fs',
                 'start-RW'
                 ])
        self.assertEqual(len(m.find_paths()), 226)


if __name__ == '__main__':
    unittest.main()
