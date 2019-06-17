.. sectionauthor:: Paul Morel <paul.morel@tartansolutions.com>
.. sectionauthor:: Michael Rea <michael.rea@tartansolutions.com>

Document - Remote Delete File
===============================

.. toctree::
   :maxdepth: 2
   :includehidden:

.. sidebar:: This Page

   .. contents::
      :local:    

+---------------------+----------------------------------+
| Parameter           | Value                            |
+=====================+==================================+
| **Category**        | Document                         |
+---------------------+----------------------------------+
| **Operation**       | document\_remote\_delete\_file   |
+---------------------+----------------------------------+
| **Workflow Icon**   | |Icon|                           |
+---------------------+----------------------------------+
| **Input Type**      |                                  |
+---------------------+----------------------------------+
| **Output Type**     |                                  |
+---------------------+----------------------------------+


Description
-----------

Deletes a remote file system file using a PlaidLink agent installed
within the firewall.

Workflow Configuration Forms
----------------------------

.. image:: ../../../_static/images/transforms/document_delete_remote_file.png
   :alt: Document Remote Delete File

Examples
--------

First, make a selection from the "Agent to Use" dropdown. Next, enter the file or folder path under "File or Folder Path for Delete". Finally, select "Save and Run Step". |Document Remote Delete|

.. |Document Remote Delete| image:: ../../../_static/images/transforms/document_remote_delete_ex.png

.. |Icon| image:: https://plaidcloud.com/client/resource/fugue/icons/blue-document--minus.png
