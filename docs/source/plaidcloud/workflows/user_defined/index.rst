.. sectionauthor:: Genova Morel <genova.morel@tartansolutions.com>
.. sectionauthor:: Paul Morel <paul.morel@tartansolutions.com>

Transforms - User Defined
!!!!!!!!!!!!!!!!!!!!!!!!!!!!

.. sidebar:: User Defined Functions

   .. toctree::
      :maxdepth: 1
      :includehidden:
      :glob:

      *

Description
-----------

User Defined Functions allow unlimited flexibility for handling cases where the standard transforms would 
be inefficient or where unique logic must be applied.  User defined functions allow interaction with 
outside services as well as direct interaction with PlaidCloud.

User Defined Functions can be written in the following languages:
 - Python 3
 - Python 2
 - R
 - Julia

All UDF code is stored in Git and PlaidCloud fully supports normal Git development operations.

User Defined Transform steps are run as part of workflows like all other steps.  No special setup or configuration is necessary.
