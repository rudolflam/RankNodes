import argparse
import sys
import json
import graph_tool.all as gt
from ranker import get_centrality_maker, identity, make_graph, sorted_items, run, choices
            
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('infile', nargs='?', type=argparse.FileType('r'), default=sys.stdin)
    parser.add_argument('outfile', nargs='?', type=argparse.FileType('w'), default=sys.stdout)
    parser.add_argument('-d', '--degree', action='store_true', help='Get degree of the nodes')
    parser.add_argument('-b', '--betweenness', action='store_true', help='Get betweenness centrality')
    parser.add_argument('-c', '--closeness', action='store_true', help='Get closeness centrality')
    parser.add_argument('-pr', '--pagerank', action='store_true', help='Get pagerank centrality')
    parser.add_argument('-ev', '--eigenvector', action='store_true', help='Get eigenvector centrality')
    parser.add_argument('-kc', '--katz', action='store_true', help='Get katz centrality')
    parser.add_argument('-hc', '--HITS', action='store_true', help='Get HITS centrality')
    parser.add_argument('-et', '--eigentrust', action='store_true', help='Get eigentrust centrality')
    parser.add_argument('--nojson', action='store_true', help='List attributes in lexicographic order instead of json object')
    parser.add_argument('-r', '--rankby', type=str, choices=choices, help='Rank nodes by a choice of centrality')
    args = parser.parse_args()
    degree, betweenness, closeness, pagerank, eigenvector, katz, hits, eigentrust = args.degree, args.betweenness, args.closeness, args.pagerank, args.eigenvector, args.katz, args.HITS, args.eigentrust
    
    G, ids2nodes, nodes2ids = make_graph(args)
    run(G, ids2nodes, nodes2ids, degree, betweenness, closeness, pagerank, eigenvector, katz, hits, eigentrust, not args.nojson)
    
if __name__ == "__main__":
    main()