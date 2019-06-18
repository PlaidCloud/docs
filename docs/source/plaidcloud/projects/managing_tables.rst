.. sectionauthor:: Genova Morel <genova.morel@tartansolutions.com>
.. sectionauthor:: Paul Morel <paul.morel@tartansolutions.com>

Managing Tables
===============

.. sidebar:: This Page

   .. contents::
      :local:


PlaidCloud offers the ability to organize and manage tables including labels. Tables are available to all workflows within a project and have many tools and options.

In addition to tables, PlaidCloud also offers Views based on table data.  Using views allows for instant updates when 
underlying table changes occur as well as saving on data storage space.

Options include:

- The same table can exist on multiple paths in the hierarchy (alternate hierarchies)
- Tables are taggable for easier search and inclusion in PlaidCloud processes
- Tables can be versioned
- Tables can be published so they are available for Dashboard Visualizations

PlaidCloud uses a path based system to organize tables, like you would use to navigate a series of folders, 
allowing for a more flexible and logical organization of the tables. Using this system, tables can be moved 
within a hierarchy or multiple references to one table from different locations in the hierarchy 
(alternate hierarchies) can be created. The ability to manage tables using this method allows the structure 
to reflect operational needs, reporting, and control.

Searching
---------

Searching for tables is accomplished by using the filter box in the lower left of the hierarchy.  The search filter
will search table names and labels for matches and show the results in the hierarhcy above.

Move
--------------------------------

To move a table, simply drag it into the folder you wish to place it.


Rename
--------------------------------

Right click on the table and select the rename option.  Type in the new name and save it.  The table will now be renamed but retain it's original unique identifier.

Clear
--------------------------------

You can clear a single table or multiple tables by selecting the tables in the hierarchy then clicking the clear button on the top toolbar.

Delete
--------------------------------

You can delete a single table or multiple tables by selecting the tables in the hierarchy then clicking the delete button on the top toolbar.

The delete operation will check to see if the table is in use by workflow steps or views.  If so, you will be asked to remove those associations.

You can also force delete the table(s).  Force deletion of the table(s) will leave references broken so this should only be used sparingly.

Create New Directory Structure
--------------------------------

Add a new folder to the hierarchy by clicking the New Folder button on the to toolbar.  To add a folder to an existing folder, right-click on the folder and select New Folder.

View Data (Table Explorer)
--------------------------------

Table data is easily viewed using the Data Explorer.  The Data Explorer provides a grid view of the data as well as a column by column summary of 
values and statistics.  Point-and-click filtering is available as well as exporting to familiar file formats.  The filter selections can also 
be saved as an Extract step usable in a workflow.

Publish Table for Reporting
--------------------------------

The Dashboard Visualizations are purposely limited to tables that have been published.  When publishing a table, you can provide a unique name that
may help distinguish the data.  This may be useful when the table may have a more obscure name as part of the workflow that generated it but needs 
a clearer name for those building dashboards.

Published tables do not have paths associated with them.  They will appear as a list of tables for use in the dashboards area.

Mark Table for Viewing Roles
--------------------------------

The viewing of tables by various roles can be controlled by clicking in the Explorer or Manager checkboxes.  If multiple tables need to be updated, select the tables
in the hierarchy and select the desired viewing role from the Actions menu on the top toolbar.

Memos to Describe Table Contents
--------------------------------

Add a memo to a table to help understand the data by editing the table and updating the memo.


View Table Shape, Size, and Last Updated Time
-------------------------------------------------

The number rows, columns, and data size for each table is shown in the table hierarchy.  For very large tables (multi-million rows) the row count may be estimated
and an indicator for approximate row count will be shown.

View Additional Table Attributes
--------------------------------

Additional table attributes are viewable and editable by selecting a table and viewing the table context form on the right.

Duplicate a Table
--------------------------------

Duplicate a table by selecting the table and clicking on the Duplicate button on the top toolbar.

.. |log icon select| image:: ../../_static/img/plaidcloud/projects/common/1_log_icon_select.png
.. |member icon select| image:: ../../_static/img/plaidcloud/projects/common/1_member_icon_select.png
.. |projects action select| image:: ../../_static/img/plaidcloud/projects/common/2_projects_action_select.png
