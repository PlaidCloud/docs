.. sectionauthor:: Genova Morel <genova.morel@tartansolutions.com>
.. sectionauthor:: Paul Morel <paul.morel@tartansolutions.com>

Jupyter
!!!!!!!

.. sidebar:: Jupyter Operations

   .. contents::
      :local:

   .. toctree::
      :maxdepth: 1
      :includehidden:
      :glob:

      notebook
      lab
      console
      

|jupyter icon|

Description
-----------

PlaidCloud provides access to Jupyter interactive services, a project aimed at developing software and services for
interactive computing across multiple programming languages. This access allows for data analysis and exploration,
including detailed data processing and visualization, through PlaidCloud.

Jupyter services included in PlaidCloud are JupyterLab, Jupyter Notebooks and Jupyter Console.  Many plugins are 
installed by default and a seemless PlaidCloud experience is built-in.  All notebooks are versioned and saved as part
of the project.  They are available through the PlaidCloud Git service for direct access and use locally if desired.

We also made it easy to move your existing notebooks to PlaidCloud by fully supporting the open standards of the Jupyter project.

JupyterLab and Jupyter Notebooks are common tools used by many data scientists as they provide powerful capabilities
including narrative style data analysis (typically used for qualitative data) and strong ad-hoc
insight generation.

From Jupyter, you have access to all the data you have been granted permission to see. You can also utilize the JSON-RPC
processes to interact with other PlaidCloud services directly from JupyterLab, Jupyter Consoles, and Jupyter Notebooks.  In fact,
since PlaidCloud provides an open JSON-RPC protocol, the same code and notebooks can run from other locations and still
interoperate with PlaidCloud as if it was running within the service.

.. todo:: Screenshots to illustrate the power of Jupyter Notebooks, JupyterLab, and Jupyter Console coming soon

.. |jupyter icon| image:: ../../_static/img/plaidcloud/jupyter/common/250px-Jupyter_logo.png