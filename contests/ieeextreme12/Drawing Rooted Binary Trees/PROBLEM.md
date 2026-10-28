**CS Academy:** <https://csacademy.com/ieeextreme-practice/task/drawing-rooted-binary-trees/>

# Drawing Rooted Binary Trees

**IEEEXtreme 12.0** · Time limit: 1000 ms · Memory limit: 256 MB

Binary trees are a common data structure and understanding some basic operations is important.  For this problem, you will play with traversals and tree drawing strategies.

## An ASCII Representation of a Tree

When you are debugging something that uses a <Definition term="binary tree"> is often valuable to be able to get a quick description of the tree to the console (in characters) so you can check its structure.  The basic strategy is to use spaces to position the nodes so that you can infer the tree’s connectivity.  For example, a tree that is just a root with two children can be “drawn” as:

```
 a
b c
```
These types of drawings follow these rules:

- all nodes in a left subtree must be to the left of the root
- all nodes in a right subtree much be to the right of the root
- the root must be between the two subtrees
- no other node will be in the same column as the root
- every node must be as far left as possible without breaking the other rules

## Standard input

For this problem, all node labels are single characters and every tree will contain at least one node.  Each instance of the problem requires two lines of input:

- the first line will be the infix traversal of the tree
- the second line will be the prefix traversal of the tree

One run of the problem may contain many instances of the problem.

## Standard output

For each instance of the problem, you must output the ASCII representation of the tree (trailing characters in a line will be ignored).  Multiple instance of the problem should follow immediately (no blank lines between them).

## Constraints and notes

- All nodes are represented by lowercase English letters

## Examples

### Example 1

Input:
```
bac
abc
```

Output:
```
 a
b c
```

Explanation:

<Graph

    indexType="custom"

    height="120"

    width="160"

    directed={true}

    style={{margin: "0", display: "block"}}

    forcePaused={true}

    nodeOptions={{circleAttr: {radius: 10}

    }}

    nodes={[

        {label:"a", center:{x:60,y:20 }, options:{"color":"black"}},

        {label:"b", center:{x:20,y:60 }, options:{"color":"black"}},

        {label:"c", center:{x:100,y:60}, options:{"color":"black"}},

    ]}

    edges={[

        {label:"", source:0, target:1, color:"black"},

        {label:"", source:0, target:2, color:"black"},

    ]}

/>

### Example 2

Input:
```
ba
ab
```

Output:
```
 a
b
```

Explanation:

<Graph

    indexType="custom"

    height="120"

    width="160"

    directed={true}

    style={{margin: "0", display: "block"}}

    forcePaused={true}

    nodeOptions={{circleAttr: {radius: 10}

    }}

    nodes={[

        {label:"a", center:{x:60,y:20 }, options:{"color":"black"}},

        {label:"b", center:{x:20,y:60 }, options:{"color":"black"}},

    ]}

    edges={[

        {label:"", source:0, target:1, color:"black"},

    ]}

/>

### Example 3

Input:
```
acb
abc
```

Output:
```
a
  b
 c
 
```

Explanation:

<Graph

    indexType="custom"

    height="120"

    width="160"

    directed={true}

    style={{margin: "0", display: "block"}}

    forcePaused={true}

    nodeOptions={{circleAttr: {radius: 10}

    }}

    nodes={[

        {label:"a", center:{x:20,y:20 }, options:{"color":"black"}},

        {label:"b", center:{x:100,y:60 }, options:{"color":"black"}},

        {label:"c", center:{x:60,y:100 }, options:{"color":"black"}},

    ]}

    edges={[

        {label:"", source:0, target:1, color:"black"},

        {label:"", source:1, target:2, color:"black"},

    ]}

/>

### Example 4

Input:
```
acbd
abcd
cba
abc
```

Output:
```
a
  b
 c d
  a
 b
c
```

Explanation:

<Graph

    indexType="custom"

    height="120"

    width="160"

    directed={true}

    style={{margin: "0", display: "block"}}

    forcePaused={true}

    nodeOptions={{circleAttr: {radius: 10}

    }}

    nodes={[

        {label:"a", center:{x:20,y:20 }, options:{"color":"black"}},

        {label:"b", center:{x:100,y:60 }, options:{"color":"black"}},

        {label:"c", center:{x:60,y:100 }, options:{"color":"black"}},

        {label:"d", center:{x:140,y:100 }, options:{"color":"black"}},

    ]}

    edges={[

        {label:"", source:0, target:1, color:"black"},

        {label:"", source:1, target:2, color:"black"},

        {label:"", source:1, target:3, color:"black"},

    ]}

/>

<Graph

    indexType="custom"

    height="120"

    width="120"

    directed={true}

    style={{margin: "0", display: "block"}}

    forcePaused={true}

    nodeOptions={{circleAttr: {radius: 10}

    }}

    nodes={[

        {label:"a", center:{x:100,y:20 }, options:{"color":"black"}},

        {label:"b", center:{x:60,y:60 }, options:{"color":"black"}},

        {label:"c", center:{x:20,y:100 }, options:{"color":"black"}},

    ]}

    edges={[

        {label:"", source:0, target:1, color:"black"},

        {label:"", source:1, target:2, color:"black"},

    ]}

/>

### Example 5

Input:
```
dbeafcg
abdecfg
```

Output:
```
   a
 b   c
d e f g
```

Explanation:

<Graph

    indexType="custom"

    height="120"

    width="300"

    directed={true}

    style={{margin: "0", display: "block"}}

    forcePaused={true}

    nodeOptions={{circleAttr: {radius: 10}

    }}

    nodes={[

        {label:"a", center:{x:140,y:20 }, options:{"color":"black"}},

        {label:"b", center:{x:60,y:60 }, options:{"color":"black"}},

        {label:"c", center:{x:220,y:60}, options:{"color":"black"}},

        {label:"d", center:{x:20,y:100 }, options:{"color":"black"}},

        {label:"e", center:{x:100,y:100 }, options:{"color":"black"}},

        {label:"f", center:{x:180,y:100 }, options:{"color":"black"}},

        {label:"g", center:{x:260,y:100 }, options:{"color":"black"}},

    ]}

    edges={[

        {label:"", source:0, target:1, color:"black"},

        {label:"", source:0, target:2, color:"black"},

        {label:"", source:1, target:3, color:"black"},

        {label:"", source:1, target:4, color:"black"},

        {label:"", source:2, target:5, color:"black"},

        {label:"", source:2, target:6, color:"black"},

    ]}

/>
