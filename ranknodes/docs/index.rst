.. ranknodes documentation master file, created by
   sphinx-quickstart on Mon Oct 17 22:46:44 2016.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to RankNodes's documentation!
=====================================

RankNodes is a simple utility based on graph-tool that takes a tsv for a graph and outputs a tsv listing the centralities of each node in that graph. 

Installation
=====================================

First install the dependancies
The utility is written in python 2.7. Type this into the console::

        sudo apt-get install python2.7

to install it.

We can now download the package from github ::
    
    git clone git://github.com/rudolflam/RankNodes.git 
    
and then move into the directory ::

    cd RankNodes
    
Next we want to install the graph-tool package. This python package requires Ubuntu 14.04+.
If you meet the requirement you can use the Makefile to install it. ::
        
        sudo make install_all

This will install both the correct graph-tool package and our ranknodes package. However, you may want to compile and install your own graph-tool package. In that case you can::
    
        sudo make install
        
to only install the ranknodes.

The Makefile also comes with an uninstall command which you can access via.::
    
        sudo make uninstall
        

Usage
=====================================
The tool takes as input an edge list in the format of a tsv. Each edge may be followed by a json object to add additional attributes to the edge. Each each is by default directed, so it can be made undirected by setting "directed" attribute to false. A line in the file looks like this::

        vertex1 vertex0 {"weight": 9, "directed": false}
        
This line indicates that there is an edge from vertex1 to vertex0. This edge is undirected and has a weight of 9.

If no json object is provided default values of weight=1 and directed=True is used.

As an example, we have provided a sample file, test_input.dat, in ranknodes/test/. You can try it using::

        cat ranknodes/test/test_input.dat | ranknodes -c
        
to pipe in the input or ::

        ranknodes ranknodes/test/test_input.dat -c
        
to compute the closeness centrality ranking of the nodes. This returns ::

        23871	0.714285714286
        23778	0.555555555556
        23732	0.555555555556
        58098	0.416666666667
        58009	0.384615384615
        58256	0.333333333333

where the first column is the list of nodes' ids and the second column is the list of corresponding betweenness values.
Notice that there are only 6 out of the 7 nodes found in the example data file. The reason one node is missing is that a node's betweenness value is NaN and is thus removed from the list. Likewise for other rankings any nodes with NaN values found in the ranking criterion will be removed.

The output of the utility is by default stdout. However, it can be overridden ::

        cat ranknodes/test/test_input.dat | ranknodes -c > output.txt
        
or ::
    
        ranknodes ranknodes/test/test_input.dat output.txt -c 
        
to write the output to output.txt.

Core options
=====================================

The tool comes with several options:
    
    1) betweenness centrality
    2) closeness centrality
    3) eigentrust centrality
    4) eigenvector centrality
    5) HITS centrality
    6) Katz centrality
    7) PageRank
    8) vertex degrees
    
    
Betweenness centrality
------------------------
To use vertex degrees ranking :option:`-b`::

        ranknodes -b

This will rank nodes using their betweenness centrality.


Closeness centrality
------------------------
To use vertex degrees ranking :option:`-c`::

        ranknodes -c

This will rank nodes using their closeness centrality.


Eigentrust centrality
------------------------
To use vertex degrees ranking :option:`-et`::

        ranknodes -et

This will rank nodes using their eigentrust centrality.

Eigenvector centrality
------------------------
To use vertex degrees ranking :option:`-ev`::

        ranknodes -ev

This will rank nodes using their eigenvector centrality.


HITS centrality
------------------------
To use vertex degrees ranking :option:`-hc`::

        ranknodes -hc

This will output 2 columns right of the node ids column. The first is the authority value of the nodes and the second is the hub value. This will rank nodes using their HITS authority centrality.

Katz centrality
------------------------
To use vertex degrees ranking :option:`-kc`::

        ranknodes -kc

This will rank nodes using their Katz centrality.

PageRank
------------------------
To use vertex degrees ranking :option:`-pr`::

        ranknodes -pr

This will rank nodes using their PageRank.

Vertex degrees
------------------------
To use vertex degrees ranking :option:`-d`::

        ranknodes -d 

This will output 2 columns right of the node ids column. The first is the in-degree of the nodes and the second is the out-degree. This will rank nodes using their in-degrees.


Combinations
------------
You can use output multiple rankings as well in a single command. As an example, ::

        ranknodes -b -c -ev -hc -kc -pr -d
        
will out the betweenness centrality, closeness centrality, eigenvector, HITS centrality, Katz centrality, PageRank, and vertex degree for each node. The nodes will be ranked using the lexicographically first option, here it is the betweenness centrality.

If you want to override the ranking criterion, then use the :option:`-r` option. ::

        ranknodes -b -c -ev -hc -kc -pr -d -r closeness
        
This will result in a ranking using the closeness centrality instead of the betweenness centrality.

Additional option
------------
Moreover, the json output may not be favorable when outputting to other environments. You may use the :option:`--nojson` option to output tsv ::

        ranknodes -b -c -ev -hc -kc -pr -d -r closeness --nojson

Inline help is available using the :option:`-h`, as usual. ::

        ranknodes -h
   
The output will include all the options for the :option:`-r`  ::
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
          -r {PageRank,betweenness,closeness,eigenvector,katz,HITS authority,HITS hubs,eigentrust}, --rankby {PageRank,betweenness,closeness,eigenvector,katz,HITS authority,HITS hubs,eigentrust}                                Rank nodes by a choice of centrality

Useful commands
=====================================

When the number of nodes is overwhelming, using the head command in conjunction to this utility is very handy ::

        cat ranknodes/test/test_input.dat | ranknodes -b -c -ev --nojson | head -n 3

will get the top 3 nodes, ranked by betweenness, with their betweenness, closeness, and eigenvector centrality values. Likewise, you can do so for the bottom 3 nodes using the tail command::

        cat ranknodes/test/test_input.dat | ranknodes -b -c -ev --nojson | tail -n 3
        
        
.. toctree::
   :maxdepth: 2



