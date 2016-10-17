import argparse
import sys
import graph_tool

def main():
	parser = argparse.ArgumentParser()
	pagerank = True
	betweenness = True
	closeness = True
	eigenvector = True
	katz = True
	hits = True
	eigentrust = True
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
	parser.add_argument('-r', '--rankby', type=str, choices=['PageRank', 'betweenness', 'closeness', 'eigenvector', 'katz','HITS authority', 'HITS hubs', 'eigentrust'], help='Rank nodes by a choice of centrality')
	args = parser.parse_args()
	degree, betweenness, closeness, pagerank, eigenvector, katz, hits, eigentrust = args.degree, args.betweenness, args.closeness, args.pagerank, args.eigenvector, args.katz, args.HITS, args.eigentrust
	
	import json
	import graph_tool.all as gt
	G = gt.Graph()
	edges2properties = {}
	total_properties = {}
	E = set()
	V = set()
	eids = {}
	for line in args.infile:
		elements = line.split()
		if len(elements)>2:
			u,v, properties = elements[0], elements[1], elements[2:]
			properties = json.loads(' '.join(properties))
		elif len(elements)==2:
			u,v = elements[0], elements[1]
			properties = None
		V.add(u)
		V.add(v)
		E.add((u,v))
		try:
			if properties['directed'] == False:
				E.add((v,u))
		except KeyError:
			pass
		edges2properties[(u,v)] = properties
		total_properties.update(properties)
	nodes2ids = {v:i for i, v in enumerate(V)}
	ids2nodes = {v:k for k,v in nodes2ids.items()}
	for e in E:
		G.add_edge(*tuple([nodes2ids[u] for u in e]))
	for key, sample in total_properties.items():
		p = G.new_edge_property(type(sample).__name__)
		total_properties[key] = p
	for edge, properties in edges2properties.items():
		for p, v in properties.items():
			total_properties[p][tuple([nodes2ids[u] for u in e])] = v
	
	vertex_values = {}
	def get_centrality(G, get_vp, ranker, centrality_name):
		vp = get_vp(ranker(G))
		for v in G.vertices():
			try:
				vertex_values[v][centrality_name] = vp[v]
			except KeyError:
				vertex_values[v] = {centrality_name:vp[v]}
	def identity(x):
		return x
	if degree:
		in_degree_name = 'In Degree'
		out_degree_name = 'Out Degree'
		for v in G.vertices():
			try:
				vertex_values[v][in_degree_name] = v.in_degree()
				vertex_values[v][out_degree_name] = v.out_degree()
			except KeyError:
				vertex_values[v] = {in_degree_name:v.in_degree(),out_degree_name:v.out_degree()}
	if pagerank:
		get_centrality(G, identity, gt.pagerank, 'PageRank')
	if betweenness:
		get_centrality(G, lambda x: x[0], gt.betweenness, 'betweenness')
	if closeness:
		get_centrality(G, identity, gt.closeness, 'closeness')
	if eigenvector:
		get_centrality(G, lambda x: x[1], gt.eigenvector, 'eigenvector')
	if katz:
		get_centrality(G, identity, gt.katz, 'katz')
	if hits:
		get_centrality(G, lambda (eigenvalue, authority, hub): authority, gt.hits, 'HITS authority')
		get_centrality(G, lambda (eigenvalue, authority, hub): hub, gt.hits, 'HITS hubs')
	if eigentrust:
		w = total_properties['weight']
		get_centrality(G, identity, lambda G: gt.eigentrust(G, w), 'eigentrust')	
	
	rank_by = args.rankby if args.rankby else sorted(vertex_values.items())[0][1].keys()[0]

	items = sorted(vertex_values.items(), key=lambda (k,v): v[rank_by], reverse=True)
	if args.nojson:
		for v, props in items:
			print('\t'.join([ids2nodes[int(v)], '\t'.join([str(value) for name, value in sorted(props.items())])]))
	else:
		for v, props in items:
			print('\t'.join([ids2nodes[int(v)], json.dumps(props, sort_keys=True)]))
if __name__ == "__main__":
	main()