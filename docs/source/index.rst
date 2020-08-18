.. sectionauthor:: Genova Morel <genova.morel@tartansolutions.com>
.. sectionauthor:: Paul Morel <paul.morel@tartansolutions.com>

PlaidCloud APIs
!!!!!!!!!!!!!!!

.. sidebar:: API Operations

   .. contents::
      :local:
      
   .. toctree::
      :maxdepth: 1
      :includehidden:
      :glob:

      api/*
      

Description
-----------

PlaidCloud provides interaction API capabilities through JSON-RPC.  This
section describes the API parameter requirements and method names. PlaidCloud supports the JSON-RPC 2.0 Protocol.

For those that wish to use XML-RPC or RESTful interactions, PlaidCloud also provides an emulation endpoints that communicate
in those protocols but utilize the JSON-RPC methods behind the scenes.  RESTful requests are POST-only.

Authentication is performed through oAuth and all traffic is https only.

Please see documentation to set up remote access for using the PlaidCloud APIs at https://plaidcloud.com/documentation
