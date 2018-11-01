Select Subset of Source Data
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Any valid Python expression is acceptable to subset the data.  Please see `Expressions <../index#expressions>`__ for more details and examples.

.. todo:: Add screenshots, description, and update filter to use SQLAlchemy style instead of Pandas style

.. image:: ../../../_static/images/transforms/common_data_filters_subset_source_data.png

.. Note:: Compound filters **must** have individual elements wrapped in parentheses. For example, if filtering for Temperature and Humidity, a valid filter would look like this: 

   .. code-block:: postgresql
