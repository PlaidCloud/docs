.. sectionauthor:: Paul Morel <paul.morel@tartansolutions.com>
.. sectionauthor:: Michael Rea <michael.rea@tartansolutions.com>


Delete Document Directory
===========================

.. toctree::
   :maxdepth: 2
   :includehidden:

.. sidebar:: This Page

   .. contents::
      :local:    

+---------------------+-------------------------------+
| Parameter           | Value                         |
+=====================+===============================+
| **Category**        | Document                      |
+---------------------+-------------------------------+
| **Operation**       | document\_delete\_directory   |
+---------------------+-------------------------------+
| **Workflow Icon**   | |Icon|                        |
+---------------------+-------------------------------+
| **Input Type**      |                               |
+---------------------+-------------------------------+
| **Output Type**     |                               |
+---------------------+-------------------------------+


Description
-----------

Delete an existing directory from within PlaidCloud Document.

Folder to Delete
----------------

First, select the appropriate account from the dropdown menu.

Next, press the **Browse** button to select the directory to delete.

.. note:: If the directory doesn't exist (already deleted), no
    action is taken.

Workflow Configuration Forms
----------------------------

.. image:: ../../../_static/images/transforms/document_delete_directory.png
   :alt: Document Delete Directory

Examples
--------

In this example, the Document directory,
*etl\_prototyping/created\_by\_analyze/*, is deleted.

.. image:: ../../../_static/images/transforms/document_delete_directory.png
   :alt: Document Delete Directory

.. |Icon| image:: https://plaidcloud.com/client/resource/fugue/icons/folder--minus.png
