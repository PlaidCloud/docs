.. sectionauthor:: Paul Morel <paul.morel@tartansolutions.com>
.. sectionauthor:: Michael Rea <michael.rea@tartansolutions.com>

Call SAP Financial Document Attachment
======================================

.. toctree::
   :maxdepth: 2
   :includehidden:

.. sidebar:: This Page

   .. contents::
      :local: 

+---------------------+---------------------+
| Parameter           | Value               |
+=====================+=====================+
| **Category**        | SAP                 |
+---------------------+---------------------+
| **API Key**         | sap\_attach         |
+---------------------+---------------------+
| **Workflow Icon**   | |Icon|              |
+---------------------+---------------------+
| **Input Type**      |                     |
+---------------------+---------------------+
| **Output Type**     |                     |
+---------------------+---------------------+


Description
-----------

Calls an SAP ECC Remote Function Call (RFC) designed to attach a file to specified FI document number.


Workflow Configuration Forms
----------------------------

Examples
--------

RFC Parameters
~~~~~~~~~~~~~~

|SAP Remote Function Call 1| 

Select Agent to Use. Select Target Directory
from the drop down bar, and browse below for the correct child folder destination
for the file. Next appropriately name the "Target File Name".
Under "Function Call Information", enter the Function, the Return Value
Parameter, and select the parameters. 

|SAP Remote Function Call 2| 

You can choose to Insert Row or Append Row under the Parameters section, as well
as name the parameters and give them values. Choose the Max Concurrent
Requests number, and select Wait for RFC to Complete. Save and Run Step.

.. |SAP Remote Function Call 1| image:: ../../../_static/images/transforms/SAP_rfc_1_ex.png
.. |SAP Remote Function Call 2| image:: ../../../_static/images/transforms/SAP_rfc_2_ex.png
.. |Icon| image:: https://plaidcloud.com/client/resource/fugue/icons/paper-clip.png
