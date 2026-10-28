# Xplore

**IEEEXtreme 12.0** · Time limit: 2000 ms · Memory limit: 256 MB

**CS Academy:** <https://csacademy.com/ieeextreme-practice/task/xplore/>

![](images/1539897382-1355206737.png)

[Click here to learn more about Xplore API](http://developer.ieee.org/)

---

The IEEE Xplore Application Programming Interface (API) is an efficient data delivery vehicle for content indexing/discovery as well as text and data mining of IEEE metadata content of academic publications. Loading a database/repository using the content delivered by the IEEE API can be subsequently used to draw domain/subject relationships, data analytics, and various other use cases for researchers. To learn more about the IEEE Xplore API please visit https://developer.ieee.org and register for an API key. All participants of the IEEEXtreme 12.0 competition will have access to the IEEE API during and after the competition, for a limited period of time, to discover its research utility potential.

A useful metric commonly associated with academic publishing is the [h-index](https://en.wikipedia.org/wiki/H-index). /An author with an index of/ $h$ /has published/ $h$ /papers each of which has been cited in other papers at least/ $h$ /times./

For this challenge, write a program that reads a set of $N$ entries from the Xplore database, in a JSON format, and prints ALL author names followed by the their **h-index**. The authors should be raked by **h-index** and by alphabetical order in case of an **h-index** tie.

## Standard input

The input will consist of an integer $N$, followed by $N$ lines with a single article entry in each line in a JSON format.

Each entry will follow a format described in the Xplore API website: https://developer.ieee.org/docs/read/Metadata_API_responses

## Standard output

Print the authors ranked by their **h-index** followed by a space and by the **h-index** itself. The authors should be ranked alphabetically if there are ties.

## Constraints and notes

- $2 \leq N \leq 10000$

<RawHTML innerHTML="

<hr style='margin-bottom: 10px; margin-top: 10px'>

<div style='

    font-size: 14px;

    font-family: Lato, 'Segoe UI', 'Lucida Sans Unicode', 'Helvetica Neue', Helvetica, Arial, sans-serif;'>

<b>Input</b>

</div>

<hr style='margin-bottom: 5px; margin-top: 10px'>

<pre style='

    overflow: auto;

    display: block;

    padding: 0.2rem;

    margin: 0 0 5px;

    font-size: 13px;

    line-height: 1.42857143;

    color: #333;

    word-break: break-all;

    word-wrap: break-word;

    background-color: #f5f5f5;

    border: 1px solid #ccc;'>

10

{&quot;authors&quot;: {&quot;authors&quot;: [{&quot;author_order&quot;: 1,&quot;affiliation&quot;: &quot;&quot;,&quot;full_name&quot;: &quot;Echo&quot;}, {&quot;author_order&quot;: 2,&quot;affiliation&quot;: &quot;&quot;,&quot;full_name&quot;: &quot;Bravo&quot;}, {&quot;author_order&quot;: 3,&quot;affiliation&quot;: &quot;&quot;,&quot;full_name&quot;: &quot;Alfa&quot;}]},&quot;title&quot;: &quot;Article Title 1&quot;,&quot;article_number&quot;: &quot;1&quot;,&quot;publication_title&quot;: &quot;Publication Title 1&quot;,&quot;publication_number&quot;: &quot;7&quot;,&quot;citing_paper_count&quot;: 9,&quot;publisher&quot;: &quot;IEEE&quot;}

{&quot;authors&quot;: {&quot;authors&quot;: [{&quot;author_order&quot;: 1,&quot;affiliation&quot;: &quot;&quot;,&quot;full_name&quot;: &quot;Charlie&quot;}, {&quot;author_order&quot;: 2,&quot;affiliation&quot;: &quot;&quot;,&quot;full_name&quot;: &quot;Bravo&quot;}]},&quot;title&quot;: &quot;Article Title 2&quot;,&quot;article_number&quot;: &quot;2&quot;,&quot;publication_title&quot;: &quot;Publication Title 1&quot;,&quot;publication_number&quot;: &quot;7&quot;,&quot;citing_paper_count&quot;: 9,&quot;publisher&quot;: &quot;IEEE&quot;}

{&quot;authors&quot;: {&quot;authors&quot;: [{&quot;author_order&quot;: 1,&quot;affiliation&quot;: &quot;&quot;,&quot;full_name&quot;: &quot;Echo&quot;}, {&quot;author_order&quot;: 2,&quot;affiliation&quot;: &quot;&quot;,&quot;full_name&quot;: &quot;Delta&quot;}, {&quot;author_order&quot;: 3,&quot;affiliation&quot;: &quot;&quot;,&quot;full_name&quot;: &quot;Alfa&quot;}, {&quot;author_order&quot;: 4,&quot;affiliation&quot;: &quot;&quot;,&quot;full_name&quot;: &quot;Charlie&quot;}]},&quot;title&quot;: &quot;Article Title 3&quot;,&quot;article_number&quot;: &quot;3&quot;,&quot;publication_title&quot;: &quot;Publication Title 1&quot;,&quot;publication_number&quot;: &quot;7&quot;,&quot;citing_paper_count&quot;: 4,&quot;publisher&quot;: &quot;IEEE&quot;}

{&quot;authors&quot;: {&quot;authors&quot;: [{&quot;author_order&quot;: 1,&quot;affiliation&quot;: &quot;&quot;,&quot;full_name&quot;: &quot;Charlie&quot;}]},&quot;title&quot;: &quot;Article Title 4&quot;,&quot;article_number&quot;: &quot;4&quot;,&quot;publication_title&quot;: &quot;Publication Title 1&quot;,&quot;publication_number&quot;: &quot;7&quot;,&quot;citing_paper_count&quot;: 9,&quot;publisher&quot;: &quot;IEEE&quot;}

{&quot;authors&quot;: {&quot;authors&quot;: [{&quot;author_order&quot;: 1,&quot;affiliation&quot;: &quot;&quot;,&quot;full_name&quot;: &quot;Charlie&quot;}, {&quot;author_order&quot;: 2,&quot;affiliation&quot;: &quot;&quot;,&quot;full_name&quot;: &quot;Echo&quot;}, {&quot;author_order&quot;: 3,&quot;affiliation&quot;: &quot;&quot;,&quot;full_name&quot;: &quot;Alfa&quot;}]},&quot;title&quot;: &quot;Article Title 5&quot;,&quot;article_number&quot;: &quot;5&quot;,&quot;publication_title&quot;: &quot;Publication Title 1&quot;,&quot;publication_number&quot;: &quot;7&quot;,&quot;citing_paper_count&quot;: 5,&quot;publisher&quot;: &quot;IEEE&quot;}

{&quot;authors&quot;: {&quot;authors&quot;: [{&quot;author_order&quot;: 1,&quot;affiliation&quot;: &quot;&quot;,&quot;full_name&quot;: &quot;Charlie&quot;}, {&quot;author_order&quot;: 2,&quot;affiliation&quot;: &quot;&quot;,&quot;full_name&quot;: &quot;Echo&quot;}]},&quot;title&quot;: &quot;Article Title 6&quot;,&quot;article_number&quot;: &quot;6&quot;,&quot;publication_title&quot;: &quot;Publication Title 1&quot;,&quot;publication_number&quot;: &quot;7&quot;,&quot;citing_paper_count&quot;: 6,&quot;publisher&quot;: &quot;IEEE&quot;}

{&quot;authors&quot;: {&quot;authors&quot;: [{&quot;author_order&quot;: 1,&quot;affiliation&quot;: &quot;&quot;,&quot;full_name&quot;: &quot;Delta&quot;}]},&quot;title&quot;: &quot;Article Title 7&quot;,&quot;article_number&quot;: &quot;7&quot;,&quot;publication_title&quot;: &quot;Publication Title 1&quot;,&quot;publication_number&quot;: &quot;7&quot;,&quot;citing_paper_count&quot;: 4,&quot;publisher&quot;: &quot;IEEE&quot;}

{&quot;authors&quot;: {&quot;authors&quot;: [{&quot;author_order&quot;: 1,&quot;affiliation&quot;: &quot;&quot;,&quot;full_name&quot;: &quot;Charlie&quot;}]},&quot;title&quot;: &quot;Article Title 8&quot;,&quot;article_number&quot;: &quot;8&quot;,&quot;publication_title&quot;: &quot;Publication Title 1&quot;,&quot;publication_number&quot;: &quot;7&quot;,&quot;citing_paper_count&quot;: 9,&quot;publisher&quot;: &quot;IEEE&quot;}

{&quot;authors&quot;: {&quot;authors&quot;: [{&quot;author_order&quot;: 1,&quot;affiliation&quot;: &quot;&quot;,&quot;full_name&quot;: &quot;Delta&quot;}, {&quot;author_order&quot;: 2,&quot;affiliation&quot;: &quot;&quot;,&quot;full_name&quot;: &quot;Charlie&quot;}]},&quot;title&quot;: &quot;Article Title 9&quot;,&quot;article_number&quot;: &quot;9&quot;,&quot;publication_title&quot;: &quot;Publication Title 1&quot;,&quot;publication_number&quot;: &quot;7&quot;,&quot;citing_paper_count&quot;: 4,&quot;publisher&quot;: &quot;IEEE&quot;}

{&quot;authors&quot;: {&quot;authors&quot;: [{&quot;author_order&quot;: 1,&quot;affiliation&quot;: &quot;&quot;,&quot;full_name&quot;: &quot;Bravo&quot;}, {&quot;author_order&quot;: 2,&quot;affiliation&quot;: &quot;&quot;,&quot;full_name&quot;: &quot;Echo&quot;}]},&quot;title&quot;: &quot;Article Title 10&quot;,&quot;article_number&quot;: &quot;10&quot;,&quot;publication_title&quot;: &quot;Publication Title 1&quot;,&quot;publication_number&quot;: &quot;7&quot;,&quot;citing_paper_count&quot;: 6,&quot;publisher&quot;: &quot;IEEE&quot;}

</pre>

<hr style='margin-bottom: 10px; margin-top: 0px'>

<div style='

    font-size: 14px;

    font-family: Lato, 'Segoe UI', 'Lucida Sans Unicode', 'Helvetica Neue', Helvetica, Arial, sans-serif;'>

<b>Output</b>

</div>

<hr style='margin-bottom: 5px; margin-top: 10px'>

<pre style='

    overflow: auto;

    display: block;

    padding: 0.2rem;

    margin: 0 0 5px;

    font-size: 13px;

    line-height: 1.42857143;

    color: #333;

    word-break: break-all;

    word-wrap: break-word;

    background-color: #f5f5f5;

    border: 1px solid #ccc;'>

Charlie 5

Echo 4

Alfa 3

Bravo 3

Delta 3

</pre>

<hr style='margin-bottom: 10px; margin-top: 5px'>

<div style='

    font-size: 14px;

    font-family: Lato, 'Segoe UI', 'Lucida Sans Unicode', 'Helvetica Neue', Helvetica, Arial, sans-serif;'>

<b> Explanation </b>

</div>

<hr style='margin-bottom: 10px; margin-top: 10px'>

"/>

In this list, Charlie is the author of 7 papers: with `article_number` 2, 3, 4, 5, 6, 8, and 9. His papers have citation counts of 9, 4, 9, 5, 6, 9, and 4 respectively.

If we order his papers by citation count it will be: 9, 9, 9, 6, 5, 4, 4. Charlie's **h-index** is `5` Because he has `5` papers with at least `5` citations.

The same method is applied for Echo, Alfa, Bravo, and Delta. Because Alfa, Bravo, and Delta all have the same **h-index** they are listed alphabetically.

## Examples

### Example 1

Input:
```
10
{"authors": {"authors": [{"author_order": 1,"affiliation": "","full_name": "Echo"}, {"author_order": 2,"affiliation": "","full_name": "Bravo"}, {"author_order": 3,"affiliation": "","full_name": "Alfa"}]},"title": "Article Title 1","article_number": "1","publication_title": "Publication Title 1","publication_number": "7","citing_paper_count": 9,"publisher": "IEEE"}
{"authors": {"authors": [{"author_order": 1,"affiliation": "","full_name": "Charlie"}, {"author_order": 2,"affiliation": "","full_name": "Bravo"}]},"title": "Article Title 2","article_number": "2","publication_title": "Publication Title 1","publication_number": "7","citing_paper_count": 9,"publisher": "IEEE"}
{"authors": {"authors": [{"author_order": 1,"affiliation": "","full_name": "Echo"}, {"author_order": 2,"affiliation": "","full_name": "Delta"}, {"author_order": 3,"affiliation": "","full_name": "Alfa"}, {"author_order": 4,"affiliation": "","full_name": "Charlie"}]},"title": "Article Title 3","article_number": "3","publication_title": "Publication Title 1","publication_number": "7","citing_paper_count": 4,"publisher": "IEEE"}
{"authors": {"authors": [{"author_order": 1,"affiliation": "","full_name": "Charlie"}]},"title": "Article Title 4","article_number": "4","publication_title": "Publication Title 1","publication_number": "7","citing_paper_count": 9,"publisher": "IEEE"}
{"authors": {"authors": [{"author_order": 1,"affiliation": "","full_name": "Charlie"}, {"author_order": 2,"affiliation": "","full_name": "Echo"}, {"author_order": 3,"affiliation": "","full_name": "Alfa"}]},"title": "Article Title 5","article_number": "5","publication_title": "Publication Title 1","publication_number": "7","citing_paper_count": 5,"publisher": "IEEE"}
{"authors": {"authors": [{"author_order": 1,"affiliation": "","full_name": "Charlie"}, {"author_order": 2,"affiliation": "","full_name": "Echo"}]},"title": "Article Title 6","article_number": "6","publication_title": "Publication Title 1","publication_number": "7","citing_paper_count": 6,"publisher": "IEEE"}
{"authors": {"authors": [{"author_order": 1,"affiliation": "","full_name": "Delta"}]},"title": "Article Title 7","article_number": "7","publication_title": "Publication Title 1","publication_number": "7","citing_paper_count": 4,"publisher": "IEEE"}
{"authors": {"authors": [{"author_order": 1,"affiliation": "","full_name": "Charlie"}]},"title": "Article Title 8","article_number": "8","publication_title": "Publication Title 1","publication_number": "7","citing_paper_count": 9,"publisher": "IEEE"}
{"authors": {"authors": [{"author_order": 1,"affiliation": "","full_name": "Delta"}, {"author_order": 2,"affiliation": "","full_name": "Charlie"}]},"title": "Article Title 9","article_number": "9","publication_title": "Publication Title 1","publication_number": "7","citing_paper_count": 4,"publisher": "IEEE"}
{"authors": {"authors": [{"author_order": 1,"affiliation": "","full_name": "Bravo"}, {"author_order": 2,"affiliation": "","full_name": "Echo"}]},"title": "Article Title 10","article_number": "10","publication_title": "Publication Title 1","publication_number": "7","citing_paper_count": 6,"publisher": "IEEE"}
```

Output:
```
Charlie 5
Echo 4
Alfa 3
Bravo 3
Delta 3
```

Explanation:

In this list, Charlie is the author of 7 papers: with `article_number` 2, 3, 4, 5, 6, 8, and 9. His papers have citation counts of 9, 4, 9, 5, 6, 9, and 4 respectively.

If we order his papers by citation count it will be: 9, 9, 9, 6, 5, 4, 4. Charlie's **h-index** is `5` Because he has `5` papers with at least `5` citations.

The same method is applied for Echo, Alfa, Bravo, and Delta. Because Alfa, Bravo, and Delta all have the same **h-index** they are listed alphabetically.

