.. sectionauthor:: Genova Morel <genova.morel@tartansolutions.com>
.. sectionauthor:: Paul Morel <paul.morel@tartansolutions.com>

Conditionals
============

.. toctree::
   :maxdepth: 2
   :includehidden:


Conditional statements use the case syntax. This provides the
equivalent of simple if-then-else logic and more complex
conditions with multiple options.

Examples
--------

Simple If-then-else Operation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: postgresql

   [
       (table.first_name != None, func.concat(table.first_name, table.last_name),
   ],
   else_ = table.last_name

Complex Condition with Multiple Options
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: postgresql

   case(
       [
           (order_table.qty > 100, item_table.specialprice),
           (order_table.qty > 10, item_table.bulkprice)
       ], 
       else_=item_table.regularprice
   )

.. code-block:: postgresql

   case(
       [
           (users_table.name == "wendy", "W"),
           (users_table.name == "jack", "J")
       ], 
       else_='E'
   )

The above may also be written in shorthand as:

.. code-block:: postgresql

   case(
       {"wendy": "W", "jack": "J"},
       value=users_table.name,
       else_='E'
   )

Coalesce
~~~~~~~~

When trying to find the first non-null value in a set of columns, the
coalesce method is very helpful. This example finds the price set for
the sale by looking in three possible fields.

.. code-block:: postgresql

   func.coalesce(table_beta.adjusted_price, table_alpha.override_price, table_alpha.price)  
   * table_beta.quantity_sold

Coalesce also works for text values. This example will use the nickname
if it is not null, or it will fall back to the first\_name.
func.coalesce(table.nickname, table.first\_name).
