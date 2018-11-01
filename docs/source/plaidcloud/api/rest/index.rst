REST
!!!!!!!!!!!!!!!!!!!!!!!!!!!!


.. sidebar:: REST

   .. contents::
      :local:

   .. toctree::
      :maxdepth: 1
      :includehidden:
      :glob:

      *
      

Description
-----------

PlaidCloud supports POST-only RESTful interfaces.  The RESTful interfaces are actually implemented as JSON-RPC methods behind the scenes and then provided as RESTful interfaces for those services that are more easily configured using REST.  There is no benefit to using REST over JSON-RPC from a performance perspective on the PlaidCloud side, but, if you are indifferent to either protocol, we suggest using the JSON-RPC protocol.
