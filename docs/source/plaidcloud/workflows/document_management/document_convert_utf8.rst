.. sectionauthor:: Paul Morel <paul.morel@tartansolutions.com>
.. sectionauthor:: Michael Rea <michael.rea@tartansolutions.com>

Convert Document Encoding to UTF-8
==================================

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
| **Operation**       | document\_convert\_utf8       |
+---------------------+-------------------------------+
| **Workflow Icon**   | |Icon|                        |
+---------------------+-------------------------------+
| **Input Type**      |                               |
+---------------------+-------------------------------+
| **Output Type**     |                               |
+---------------------+-------------------------------+


Description
-----------

Updates file encoding and converts all characters to UTF-8. This is
particularly useful if the information source has mixed encodings or
other tools don't support certain encodings.

Workflow Configuration Forms
----------------------------

.. image:: ../../../_static/images/transforms/document_convert_file_ASCII_encoding.png

Examples
--------

Select the input file and browse for the file within that location. Select the desired output
location, and browse to selected the desired location for the file. Save and run. |Document Convert File to UTF-8
Encoding|

.. todo:: Screenshots, description, and update parameters coming soon

.. |Document Convert File to UTF-8 Encoding| image:: ../../../_static/images/transforms/document_convert_ascii_encoding.png

.. |Icon| image:: https://plaidcloud.com/client/resource/fugue/icons/document-globe-blue.png
