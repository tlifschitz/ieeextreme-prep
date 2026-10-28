# Monokeros

**IEEEXtreme 13.0** · Time limit: 2500 ms · Memory limit: 256 MB

**CS Academy:** <https://csacademy.com/ieeextreme-practice/task/monokeros/>

The true tyrant, mr. W has given Tiranca a new problem: you are given an initially empty binary search tree and a sequence of numbers $(x_1, x_2, ... , x_N)$. A binary search tree is a <Definition term="binary tree"/>, that stores a value in each node and respects the following rules:

- the value stored in its left child is smaller or equal to the value of the node
- the value stored in its right child is strictly greater than the value of the node

Your task is to insert these numbers in the binary search tree (in the given order) and output the depth (edge-distance from the node to the root) of the newly added node after each insertion. An insertion goes like this:

```
insert_value(current_node, new_value):
    if new_value <= value(current_node):
        if the left child of current_node exists:
            insert_value(left_child(current_node), new_value)
        else:
            // create a new node with the new_value and place it as current_node's left child
    else:
        if the right child of current_node exists:
            insert_value(right_child(current_node), new_value)
        else:
            // create a new node with the new_value and place it as current_node's right child
```

## Standard input

The first line will contain $N$, the number of elements in the sequence.

The second line will contain $N$ numbers: $x_1, x_2, ..., x_N$.

## Standard output

The first line will contain $N$ numbers, corresponding to the depths of the added nodes.

## Constraints and notes

- $1 \le N \le 2 \cdot 10^5$
- $-10^9 \le x_i \le 10^9$

## Examples

### Example 1

Input:
```
4
-2 -2 6 -1
```

Output:
```
1 2 2 3
```

Explanation:

<Graph indexType="custom" height="300" width="300" forcePaused="true" nodes={

[

   {

      label:"-2",

      center:{

         x:150,

         y:50,

      }

   },

   {

      label:"-2",

      center:{

         x:100,

         y:150

      }

   },

   {

      label:"6",

      center:{

         x:200,

         y:150

      }

   },

   {

      label:"-1",

      center:{

         x:150,

         y:250

      }

   }

]}

edges={

[

      {

         source:0,

         target:1

      },

      {

         source:0,

         target:2

      },

      {

         source:2,

         target:3

      },

   ]

} />

### Example 2

Input:
```
5
80 10 70 20 60
```

Output:
```
1 2 3 4 5
```

Explanation:

<Graph indexType="custom" height="300" width="300" forcePaused="true" nodes={

[

   {

      label:"80",

      center:{

         x:150,

         y:50,

      }

   },

   {

      label:"10",

      center:{

         x:100,

         y:100

      }

   },

   {

      label:"70",

      center:{

         x:150,

         y:150

      }

   },

   {

      label:"20",

      center:{

         x:100,

         y:200

      }

   },

{

      label:"60",

      center:{

         x:150,

         y:250

      }

   }

]}

edges={

[

      {

         source:0,

         target:1

      },

      {

         source:1,

         target:2

      },

      {

         source:2,

         target:3

      },

{

         source:3,

         target:4

      },

   ]

} />
