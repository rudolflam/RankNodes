# RankNodes
RankNodes is a simple utility based on graph-tool that takes a tsv for a graph and outputs a tsv listing the centralities of each node in that graph.
<br><br>
**Requirement** Ubuntu 14.04+
<b> Dependancies: python 2.7, graph-tool</b>
## Installation

### To install:
Install python 2.7
```
sudo apt-get install python2.7 
```
Download and extract
```
git clone git://github.com/rudolflam/RankNodes.git 
```
Go to your directory
```
cd RankNodes
```
Install the package and dependancies
```
make install
```


To uninstall:
Go to your directory
```
cd {your_RankNodes_directory}
```
Install the package and dependancies
```
make uninstall
```
## Usage
The tool takes as input an edge list in the format of a tsv. Each edge may be followed by a json object to add additional attributes to the edge. Each each is by default directed, so it can be made undirected by setting "directed" attribute to false. A line in the file looks like this:

```
ex.
vertex1 vertex0 {"weight": 9, "directed": false}
```

An example file is provided in the ranknodes/test/test_input.dat. Try it by:
```
cat ranknodes/test/test_input.dat | ranknodes -ev -b -d -hc --nojson -r eigenvector
```
This will get the *eigenvector centrality* (-e), *betweenness centrality* (-b), *vertex degrees* (-d), and *HITS centralities* (-hc). By default, the output has 2 columns. The first column is the vertex id and the second is the json object with the centralities labels as key and the corresponding centrality values as the value of the dictionary. With the --json option the json is decomposed into columns sorted by the labels' lexicographical orders. For our example, we will get output in the following format:
```
vertexid betweenness  eigenvector hits_authority hit_hubs in_degree out_degree
```
Using the -r option will allow you to choose how to rank the nodes. In the above example we use eigenvector centrality. If you do not specify how to rank the nodes, the lexicographically first element will be chosen. Using our example again, we will use betweenness centrality as the ranking method.

The full description of the utility is:
```
usage: ranknodes [-h] [-d] [-b] [-c] [-pr] [-ev] [-kc] [-hc] [-et] [--nojson]
                 [-r {PageRank,betweenness,closeness,eigenvector,katz,HITS authority,HITS hubs,eigentrust}]
                 [infile] [outfile]

positional arguments:
  infile
  outfile

optional arguments:
  -h, --help            show this help message and exit
  -d, --degree          Get degree of the nodes
  -b, --betweenness     Get betweenness centrality
  -c, --closeness       Get closeness centrality
  -pr, --pagerank       Get pagerank centrality
  -ev, --eigenvector    Get eigenvector centrality
  -kc, --katz           Get katz centrality
  -hc, --HITS           Get HITS centrality
  -et, --eigentrust     Get eigentrust centrality
  --nojson              List attributes in lexicographic order instead of json
                        object
  -r {PageRank,betweenness,closeness,eigenvector,katz,HITS authority,HITS hubs,eigentrust}, --rankby {PageRank,betweenness,closeness,eigenvector,katz,HITS authority,HITS hubs,eigentrust}
                        Rank nodes by a choice of centrality
```
