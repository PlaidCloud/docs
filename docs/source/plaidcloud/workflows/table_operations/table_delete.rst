.. sectionauthor:: Paul Morel <paul.morel@tartansolutions.com>
.. sectionauthor:: Michael Rea <michael.rea@tartansolutions.com>

Table In-Place Delete
=============================

.. toctree::
   :maxdepth: 2
   :includehidden:

.. sidebar:: This Page

   .. contents::
      :local: 

+---------------------+----------------------------+
| Parameter           | Value                      |
+=====================+============================+
| **Category**        | Table                      |
+---------------------+----------------------------+
| **Operation**       | table\_delete              |
+---------------------+----------------------------+
| **Workflow Icon**   | |Icon|                     |
+---------------------+----------------------------+
| **Input Type**      | PlaidCloud Analyze Table   |
+---------------------+----------------------------+
| **Output Type**     |                            |
+---------------------+----------------------------+


Description
-----------

Performs a delete on the table using the specified filter conditions. The operation is performed on the designated table 
directly so no additional tables are created. Only the rows that meet the filter criteria are deleted. This may be an 
effective approach when concerns of data size are encountered.

Table Selection
---------------

Select the **Source** table for deleting from the dropdown list. This
list includes all *Project* and *Workflow* data tables.

Workflow Configuration Forms
----------------------------

Examples
--------

.. todo:: Screenshots, description, and update parameters coming soon

.. |Icon| image:: https://plaidcloud.com/client/resource/fugue/icons/table-delete-row.png
