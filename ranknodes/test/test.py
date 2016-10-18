import unittest
import ranknodes

class LoadTest(unittest.TestCase):
    def loadtest(self):
        class Args(object):
            pass
        args = Args()
        args.infile = open('test_input.dat')
        args.degree, args.betweenness, args.closeness, args.pagerank, args.eigenvector, args.katz, args.HITS, args.eigentrust =[True]*8
        G, ids2nodes, nodes2ids = ranknodes.ranker.make_graph(args)
        
        self.assertTrue(len(list(G.edges())) == 10)
        self.assertTrue(len(list(G.vertices())) == 7)
        self.assertTrue(len(ids2nodes) == 7 )
        self.assertTrue(len(nodes2ids) == 7 )
        self.assertTrue(set(ids2nodes.values()) == set(nodes2ids.keys()))
        self.assertTrue(set(nodes2ids.values()) == set(ids2nodes.keys()))
        self.assertTrue({int(v) for v in G.vertices()} == set(nodes2ids.values()))
        
class CentralityTest(unittest.TestCase):
    def centralityTest(self):
        class Args(object):
            pass
        args = Args()
        args.infile = open('test_input.dat')
        args.degree, args.betweenness, args.closeness, args.pagerank, args.eigenvector, args.katz, args.HITS, args.eigentrust =[True]*8
        G, ids2nodes, nodes2ids = ranknodes.ranker.make_graph(args)
        ranked = ranknodes.ranker.sorted_items(G, betweenness=True, closeness=True)
        for v, values in ranked:
            self.assertTrue(len(values)==2)
            self.assertTrue('closeness' in values.keys())
            self.assertTrue('betweenness' in values.keys())
        self.assertTrue({int(k) for k, v in ranked} == set(ids2nodes.keys()))
        