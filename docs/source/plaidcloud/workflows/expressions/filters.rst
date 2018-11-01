Filters
=========

.. toctree::
   :maxdepth: 2
   :includehidden:

You may apply filters using column references.

+---------------+--------------------------+-----------------------------------+
| Operator      | Description              | Example                           |
+===============+==========================+===================================+
| and\_()       | Creates an AND SQL       | and\_(table.a > 23, table.b ==    |
|               | condition                | u'blue')                          |
+---------------+--------------------------+-----------------------------------+
| or\_()        | Creates an OR SQL        | or\_(table.a > 23, table.b ==     |
|               | condition                | u'blue')                          |
+---------------+--------------------------+-----------------------------------+
| not\_()       | Inverts the condition    | not\_(and\_(table.a > 23, table.b |
|               |                          | == u'blue'))                      |
+---------------+--------------------------+-----------------------------------+
| in\_()        | Test if values are with  | table.column.in\_((1, 2, 3))      |
|               | a tuple of values        |                                   |
+---------------+--------------------------+-----------------------------------+
| notin         | Inverts the IN condition | table.column.notin((1, 2, 3))     |
+---------------+--------------------------+-----------------------------------+
| any\_()       | Applies the SQL ANY()    | table.column.any(('red', 'blue',  |
|               | condition to a column    | 'yellow'))                        |
+---------------+--------------------------+-----------------------------------+
| between       | Applies the SQL BETWEEN  | table.column.between(23, 46)      |
|               | condition                |                                   |
+---------------+--------------------------+-----------------------------------+
| startswith    | Applies the SQL LIKE '%' | table.column.startswith('abc')    |
+---------------+--------------------------+-----------------------------------+
| contains      | Applies the SQL LIKE     | table.column.contains('mno')      |
|               | '%%'                     |                                   |
+---------------+--------------------------+-----------------------------------+
| endswith      | Applies the SQL LIKE     | table.column.endswith('xyz')      |
|               | '%%'                     |                                   |
+---------------+--------------------------+-----------------------------------+
| is\_          | Applies the SQL is the   | table.column.is\_(None)           |
|               | IS for things like IS    |                                   |
|               | NULL                     |                                   |
+---------------+--------------------------+-----------------------------------+
| isnot         | Applies the SQL is the   | table.column.isnot(None)          |
|               | IS for things like IS    |                                   |
|               | NOT NULL                 |                                   |
+---------------+--------------------------+-----------------------------------+
| like          | Applies the SQL LIKE     | table.column.like('%foobar%'')    |
|               | method                   |                                   |
+---------------+--------------------------+-----------------------------------+
| table.column. |                          |                                   |
| like('%       |                          |                                   |
| /% of         |                          |                                   |
| profit%',     |                          |                                   |
| escape='/')   |                          |                                   |
+---------------+--------------------------+-----------------------------------+
| notlike       | Applies the SQL NOT LIKE | table.column.notlike('%foobar%')  |
|               | method                   |                                   |
+---------------+--------------------------+-----------------------------------+
| table.column. |                          |                                   |
| notlike('%    |                          |                                   |
| /% of         |                          |                                   |
| profit%',     |                          |                                   |
| escape='/')   |                          |                                   |
+---------------+--------------------------+-----------------------------------+
| ilike         | Applies the SQL ILIKE    | table.column.ilike('%foobar%')    |
|               | method                   |                                   |
+---------------+--------------------------+-----------------------------------+
| table.column. |                          |                                   |
| like('%       |                          |                                   |
| /% of         |                          |                                   |
| profit%',     |                          |                                   |
| escape='/')   |                          |                                   |
+---------------+--------------------------+-----------------------------------+
| notilike      | Applies the SQL NOT      | table.column.notilike('%foobar%') |
|               | ILIKE method             |                                   |
+---------------+--------------------------+-----------------------------------+
| table.column. |                          |                                   |
| notilike('%   |                          |                                   |
| /% of         |                          |                                   |
| profit%',     |                          |                                   |
| escape='/')   |                          |                                   |
+---------------+--------------------------+-----------------------------------+
| NULL, Null,   | Alias for Python None    |                                   |
| null          |                          |                                   |
+---------------+--------------------------+-----------------------------------+
| TRUE, true    | Alias for Python True    |                                   |
+---------------+--------------------------+-----------------------------------+
| FALSE, false  | Alias for Python False   |                                   |
+---------------+--------------------------+-----------------------------------+
| >             | Greater Than             | table.column > 23                 |
+---------------+--------------------------+-----------------------------------+
| <             | Less Than                | table.column < 23                 |
+---------------+--------------------------+-----------------------------------+
| >=            | Greater than or equal to | table.column >= 23                |
+---------------+--------------------------+-----------------------------------+
| <=            | Less than or equal to    | table.column <= 23                |
+---------------+--------------------------+-----------------------------------+
| ==            | Equal                    | table.column == 23 table.column   |
|               |                          | == 'blue'                         |
+---------------+--------------------------+-----------------------------------+
| !=            | Not Equal                | table.column != 23 table.column   |
|               |                          | != 'blue'                         |
+---------------+--------------------------+-----------------------------------+

.. todo:: Add screenshots
