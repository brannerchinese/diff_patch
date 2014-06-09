## Make a Differ-Patcher

[General information about Iron Forger](https://hackpad.com/Iron-Forger-kEmauANGcV5)

Build a tool to compare two text files and generate a diff — a file that concisely specifies the differences between the two other files.

 1. A diff file has the following structure:

   2. A **header** of two lines, giving the names of the two original text files and indicating which is considered the "original" file from which the other is being derived. The original file is called the "from-file" and is marked with minus signs; the "to-file" is marked with plus-signs:

        ```
--- from-file
+++ to-file
        ```

   2. A series of **hunks** of differences between the files. Each hunk has two parts:
     3. It begins with a line beginning and ending with a pair of at-signs (`@@`), between which are listed the numbers of the lines in each file described by the hunk and the number of consecutive changes. 
     3. After that there is a list of whole lines, each of which prefaced with a plus or a minus to indicate whether it is being added to the to-file or removed from it. Here is an example of a hunk:

        ```
@@ -3 +3 @@
-some text
+other words
        ```

       This hunk says: The single line at line 3 of the from-file is being removed and a single new line is being added to the to-file. The line being removed is "some text" and the line being added is "other words".
     3. Hunks can also include lines of **context**, for the benefit of human readers. Context lines always begin with a space. They are found in both the from-file and the to-file, and strictly speaking they are not part of the diff. 

     In this hunk

        ```
@@ -2,0 +3 @@
+some words
        ```

     the expression `-2,0 +3` means that line 2 in the from-file corresponds to line 3 in the to-file, and nothing is removed from the from-file at the position specified, but one line is added in the to-file at the position specified. The default change is one line — to be removed, if specified for the from-file; added, if specified for the to-file. 

     If the change is of something other than the default, it is specified after the number, with a comma before it. so `-2,0` above means "We are dealing with position line 2 in the from-file, but there are zero changes". 

       But a hunk like this:

        ```
@@ -24,3 +25 @@
-Extra line to be removed.
-Extra line to be removed.
-Extra line to be removed.
+The flavor of limited-release Japanese soda Pepsi Baobab was described as "liberating" by PepsiCo. (https://en.wikipedia.org/wiki/Adansonia#Food_uses, accessed 20140608)
        ```

       means "At line 24 of the from-file, remove three lines so that they do not appear at line 25 of the to-file; instead, at line 25 of the to-file, add one line." And the three lines to be removed are specified, as is the one line to be added.
       
### Other ideas

 1. If diff functionality is already available in your programming language of choice (look for "unified diff" or words to that effect), build another tool to "patch" a text file using a diff — to generate the other of the two files that was used in producing the original diff. First try generating only the to-file, given a from-file and a diff. If that goes smoothly, next try generating the from-file, given the to-file and the diff-file. Note that only one of the sets of explicitly listed lines are actually needed in the patching process, depending on which direction you are going.
 1. Add diff functionality to your [version control](https://hackpad.com/Week-3-Make-a-Local-Version-Control-System-NZ1n98nFktQ) project from last week.

### Resources
 1. The GNU man page for [`diffutils`](http://www.gnu.org/software/diffutils/manual/html_node/Detailed-Unified.html).
 1. The [`git-diff`](http://git-scm.com/docs/git-diff) man page.
 1. The Python documentation for [`difflib`](https://docs.python.org/3/library/difflib.html).
 1. Google [`diff-match-patch`](https://code.google.com/p/google-diff-match-patch/), available in a number of languages.
 1. The C++ diff templating library [`dtl-cpp`](https://code.google.com/p/dtl-cpp/); [tutorial](https://code.google.com/p/dtl-cpp/wiki/Tutorial) also available.
 1. 

[end]

