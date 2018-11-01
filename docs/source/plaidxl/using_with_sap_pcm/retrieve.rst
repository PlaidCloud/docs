.. sectionauthor:: Genova Morel <genova.morel@tartansolutions.com>
.. sectionauthor:: Paul Morel <paul.morel@tartansolutions.com>

PCM Data Retrieval Methods
============================

.. sidebar:: This Topic

   .. contents::
      :local:


ActivityDriverValue
--------------------

This value is a measure of an appropriate operational quantity such as Number
of Sales or Number of Invoices, which is used to distribute costs across a range
of Cost Objects. It drives costs from Line Items, Services, or Activities through to
Cost Objects in a specific Version, Period, and Responsibility Center, where a
Cost Object can be a combination of up to five distinct Cost Object dimensions.
Each value is associated with a particular Cost Object whose costs are calculated
as the proportion of the value to its total.


+---------------------+-------------------------------+
| Item                | Value                         |
+=====================+===============================+
| **SAP PCM Cube**    | ActivityDriverValue           |
+---------------------+-------------------------------+
| **PlaidXL Method**  | ActivityDriverValue           |
+---------------------+-------------------------------+
| **Arguments**       | - Versions                    |
|                     | - Periods                     |
|                     | - Responsibility Centers      |
|                     | - Activity Driver             |
|                     | - Cost Object 1               |
|                     | - Cost Object 2               |
|                     | - Cost Object 3               |
|                     | - Cost Object 4               |
|                     | - Cost Object 5               |
+---------------------+-------------------------------+


ActivityCostObjectValue
-------------------------

This is the summarized cost of a Cost Object across all Responsibility Centers and Line Items. It identifies the cost by Version, Period, Activity, and Cost Object combination from the five different levels of Cost Object item. It includes all reassigned costs to the specified Activity, from all Responsibility Centers. It also includes all contributions from Service costs and External Cost Object values. Direct costs are also visible because they are held against <Activity Unassigned>.

Note:

This grid value does not have Line Items and Responsibility Centers as key di-
mensions although Cost Object values would normally include these. As a result all items in these dimensions are contributors to its value, including those specified Asnon-consolidation in their dimension hierarchies. <RC Unassigned> costs are also included.


+---------------------+-------------------------------+
| Item                | Value                         |
+=====================+===============================+
| **SAP PCM Cube**    | ActivityCostObjectValue       |
+---------------------+-------------------------------+
| **PlaidXL Method**  | ActivityCostObjectValue       |
+---------------------+-------------------------------+
| **Arguments**       | - Versions                    |
|                     | - Periods                     |
|                     | - Activities                  |
|                     | - Cost Object 1               |
|                     | - Cost Object 2               |
|                     | - Cost Object 3               |
|                     | - Cost Object 4               |
|                     | - Cost Object 5               |
|                     | - Currencies                  |
+---------------------+-------------------------------+


ActivityDriverDataValue
-------------------------

If the Activity Driver has no associated rule, this grid value is the same as ActivityDriverValue Grid Value. If a rule exists, it records a value that can be entered against the Activity Driver in addition to the computed value obtained by the rule. This could be used by the rule to influence its computed value. Note: Data values can be entered against consolidated totals as well as individual line items, so the consolidation feature does not operate for values of this type.


+---------------------+-------------------------------+
| Item                | Value                         |
+=====================+===============================+
| **SAP PCM Cube**    | ActivityDriverDataValue       |
+---------------------+-------------------------------+
| **PlaidXL Method**  | ActivityDriverDataValue       |
+---------------------+-------------------------------+
| **Arguments**       | - Versions                    |
|                     | - Periods                     |
|                     | - Responsibility Centers      |
|                     | - Cost Object 1               |
|                     | - Cost Object 2               |
|                     | - Cost Object 3               |
|                     | - Cost Object 4               |
|                     | - Cost Object 5               |
+---------------------+-------------------------------+


ActivityLineItemValue
-------------------------
In a specific Version, Period, and Responsibility Center, this calculated value represents the component part of an Activity cost that derives from a specific Line Item before any Activity reassignments are applied. It is similar to the grid value ActivityValue where the cost is broken down further by Resource Driver. The Line Item component of the cost is calculated using the proportion of Re sourceDriverSplit to total ResourceDriverValue for the specified Line Item.

+---------------------+-------------------------------+
| Item                | Value                         |
+=====================+===============================+
| **SAP PCM Cube**    | ActivityLineItemValue         |
+---------------------+-------------------------------+
| **PlaidXL Method**  | ActivityLineItemValue         |
+---------------------+-------------------------------+
| **Arguments**       | - Versions                    |
|                     | - Periods                     |
|                     | - Responsibility Centers      |
|                     | - Line Items                  |
|                     | - Activities                  |
|                     | - Currencies                  |
+---------------------+-------------------------------+


ActivityValue
-------------------------

Returns the ActivityValue for the specified parameters


+---------------------+-------------------------------+
| Item                | Value                         |
+=====================+===============================+
| **SAP PCM Cube**    | ActivityValue                 |
+---------------------+-------------------------------+
| **PlaidXL Method**  | ActivityValue                 |
+---------------------+-------------------------------+
| **Arguments**       | - Versions                    |
|                     | - Periods                     |
|                     | - Responsibility Centers      |
|                     | - Line Items                  |
|                     | - Activities                  |
|                     | - Resource Drivers            |
|                     | - Currencies                  |
+---------------------+-------------------------------+


CostObjectValue
-------------------------

This is the component cost of a Cost Object identified by the dimension items listed below, where the Cost Object can be a combination of five different levels of Cost Object item. 

This value includes all costs reassigned to the specified Activities but does not include any contribution from Service costs or direct costs (those that originate from Line Item/Service costs that are transmitted directly to Cost Objects avoiding Activities). 

Note: 
This value identifies the Responsibility Centers where Line Item costs from all Responsibility Centers end up after reassignment. In reassignment terms these are Target Responsibility Centers. To obtain the equivalent Line Item costs that originate from source Responsibility Centers, use SourceCostObjectValue. This a trace value which can only be calculated after CostObjectValues have been fully generated, so will take longer to appear. 

For greater detail you can use TracebackValue, which identifies these costs through both Source and Target dimensions. But be aware of the massive amount of calculated values this may generate, which need careful handling to avoid performance problems.

+---------------------+-------------------------------+
| Item                | Value                         |
+=====================+===============================+
| **SAP PCM Cube**    | CostObjectValue               |
+---------------------+-------------------------------+
| **PlaidXL Method**  | CostObjectValue               |
+---------------------+-------------------------------+
| **Arguments**       | - Versions                    |
|                     | - Periods                     |
|                     | - Responsibility Centers      |
|                     | - Cost Object 1               |
|                     | - Cost Object 2               |
|                     | - Cost Object 3               |
|                     | - Cost Object 4               |
|                     | - Cost Object 5               |
|                     | - Currencies                  |
+---------------------+-------------------------------+


DataRevenue
-------------------------

Returns the Data value for the Revenue of the Cost Object specified by the parameters listed below.

+---------------------+-------------------------------+
| Item                | Value                         |
+=====================+===============================+
| **SAP PCM Cube**    | DataRevenue                   |
+---------------------+-------------------------------+
| **PlaidXL Method**  | DataRevenue                   |
+---------------------+-------------------------------+
| **Arguments**       | - Versions                    |
|                     | - Periods                     |
|                     | - Responsibility Centers      |
|                     | - Revenue Types               |
|                     | - Cost Object 1               |
|                     | - Cost Object 2               |
|                     | - Cost Object 3               |
|                     | - Cost Object 4               |
|                     | - Cost Object 5               |
|                     | - Currencies                  |
+---------------------+-------------------------------+


DataUnitPrice
-------------------------

Returns the Data value for the Unit Price of the Cost Object specified by the parameters listed below.


+---------------------+-------------------------------+
| Item                | Value                         |
+=====================+===============================+
| **SAP PCM Cube**    | DataUnitPrice                 |
+---------------------+-------------------------------+
| **PlaidXL Method**  | DataUnitPrice                 |
+---------------------+-------------------------------+
| **Arguments**       | - Versions                    |
|                     | - Periods                     |
|                     | - Responsibility Centers      |
|                     | - Cost Object 1               |
|                     | - Cost Object 2               |
|                     | - Cost Object 3               |
|                     | - Cost Object 4               |
|                     | - Cost Object 5               |
|                     | - Currencies                  |
+---------------------+-------------------------------+


DataUnitsSold
-------------------------

Returns the Data value for the Units Sold of the Cost Object specified by the parameters listed below.

+---------------------+-------------------------------+
| Item                | Value                         |
+=====================+===============================+
| **SAP PCM Cube**    | DataUnitPrice                 |
+---------------------+-------------------------------+
| **PlaidXL Method**  | DataUnitPrice                 |
+---------------------+-------------------------------+
| **Arguments**       | - Versions                    |
|                     | - Periods                     |
|                     | - Responsibility Centers      |
|                     | - Revenue Types               |
|                     | - Cost Object 1               |
|                     | - Cost Object 2               |
|                     | - Cost Object 3               |
|                     | - Cost Object 4               |
|                     | - Cost Object 5               |
+---------------------+-------------------------------+


DirectCostObjectValue
-------------------------

This is the component cost of a Cost Object that derives from specific Cost Object Type Line Items, where the Cost Object can be a combination of five different levels of Cost Object item. The Line Item must have been defined as Cost Object Type Line Item in the Line Items dimension screen. This means its costs avoid being distributed across Activities and are directly assigned to Cost Objects. 

Note: 
This value does not include any contribution from Service costs or direct Service costs.

+---------------------+-------------------------------+
| Item                | Value                         |
+=====================+===============================+
| **SAP PCM Cube**    | DirectCostObjectValue         |
+---------------------+-------------------------------+
| **PlaidXL Method**  | DirectCostObjectValue         |
+---------------------+-------------------------------+
| **Arguments**       | - Versions                    |
|                     | - Periods                     |
|                     | - Responsibility Centers      |
|                     | - Line Items                  |
|                     | - Cost Object 1               |
|                     | - Cost Object 2               |
|                     | - Cost Object 3               |
|                     | - Cost Object 4               |
|                     | - Cost Object 5               |
|                     | - Currencies                  |
+---------------------+-------------------------------+



ExternalActivityValue
-------------------------

Returns the basic value of the external costs associated with specific Activity LineItemValues.


+---------------------+-------------------------------+
| Item                | Value                         |
+=====================+===============================+
| **SAP PCM Cube**    | ExternalActivityValue         |
+---------------------+-------------------------------+
| **PlaidXL Method**  | ExternalActivityValue         |
+---------------------+-------------------------------+
| **Arguments**       | - Versions                    |
|                     | - Periods                     |
|                     | - Responsibility Centers      |
|                     | - Line Items                  |
|                     | - Activities                  |
|                     | - Resource Drivers            |
|                     | - Currencies                  |
+---------------------+-------------------------------+


ExternalCostObjectValue
-------------------------

Returns the basic value of the external costs associated with specific CostOb jectValues. 

Note: 
CostObjectValues are not calculated On Demand due to the large number of Cost Object combinations in a model. They are either calculated automatically by the Calculation Engine or by command using the CalculateSlice function. As a result when using this function you should consider making use of the function: RestrictCombinationCostObjectValue. 

This allows you to limit the number of combinations to those that have a value within a specific range.


+---------------------+-------------------------------+
| Item                | Value                         |
+=====================+===============================+
| **SAP PCM Cube**    | ExternalCostObjectValue       |
+---------------------+-------------------------------+
| **PlaidXL Method**  | ExternalCostObjectValue       |
+---------------------+-------------------------------+
| **Arguments**       | - Versions                    |
|                     | - Periods                     |
|                     | - Responsibility Centers      |
|                     | - Line Items                  |
|                     | - Activities                  |
|                     | - Cost Object 1               |
|                     | - Cost Object 2               |
|                     | - Cost Object 3               |
|                     | - Cost Object 4               |
|                     | - Cost Object 5               |
|                     | - Currencies                  |
+---------------------+-------------------------------+


LineItemValue
-------------------------

This function is not available for Objectives and Metrics type models. Returns the Line Item value for the specified parameters.


+---------------------+-------------------------------+
| Item                | Value                         |
+=====================+===============================+
| **SAP PCM Cube**    | LineItemValue                 |
+---------------------+-------------------------------+
| **PlaidXL Method**  | LineItemValue                 |
+---------------------+-------------------------------+
| **Arguments**       | - Versions                    |
|                     | - Periods                     |
|                     | - Responsibility Centers      |
|                     | - Line Items                  |
|                     | - Currencies                  |
+---------------------+-------------------------------+


LineItemCostObjectValue
-------------------------

Returns the LineItemCostObjectValue for the specified parameters. 

Note: 
CostObjectValues are not calculated On Demand due to the large number of Cost Object combinations in a model. They are either calculated automatically by the Calculation Engine or by command using the CalculateSlice function. As a result when using this function you should consider making use of the functions: 

• IsCostObjectCalculated 
• RestrictCombinationCostObjectValue 

The first allows you to find out if the value you want has been calculated yet and the other allows you to limit the number of combinations to those that have a non zero value in specific Versions and Periods.

+---------------------+-------------------------------+
| Item                | Value                         |
+=====================+===============================+
| **SAP PCM Cube**    | LineItemCostObjectValue       |
+---------------------+-------------------------------+
| **PlaidXL Method**  | LineItemCostObjectValue       |
+---------------------+-------------------------------+
| **Arguments**       | - Versions                    |
|                     | - Periods                     |
|                     | - Responsibility Centers      |
|                     | - Cost Object 1               |
|                     | - Cost Object 2               |
|                     | - Cost Object 3               |
|                     | - Cost Object 4               |
|                     | - Cost Object 5               | 
|                     | - Currencies                  |
+---------------------+-------------------------------+



LineItemDataValue
-------------------------

This function is not available for Objectives and Metrics type models. Returns the Data value for the Line Item specified by the dimension items listed below.

+---------------------+-------------------------------+
| Item                | Value                         |
+=====================+===============================+
| **SAP PCM Cube**    | LineItemDataValue             |
+---------------------+-------------------------------+
| **PlaidXL Method**  | LineItemDataValue             |
+---------------------+-------------------------------+
| **Arguments**       | - Versions                    |
|                     | - Periods                     |
|                     | - Responsibility Centers      |
|                     | - Line Items                  | 
|                     | - Currencies                  |
+---------------------+-------------------------------+


LineItemDetailDataValue
-------------------------

This function is not available for Objectives and Metrics type models. Returns the Data value for the Line Item Detail item specified by the dimension items listed below. TheLineItem Detail Datavalueisalways referenced through an associated Line Item.

+---------------------+-------------------------------+
| Item                | Value                         |
+=====================+===============================+
| **SAP PCM Cube**    | LineItemDetailDataValue       |
+---------------------+-------------------------------+
| **PlaidXL Method**  | LineItemDetailDataValue       |
+---------------------+-------------------------------+
| **Arguments**       | - Versions                    |
|                     | - Periods                     |
|                     | - Responsibility Centers      |
|                     | - Line Items                  |
|                     | - Line Item Details           | 
|                     | - Currencies                  |
+---------------------+-------------------------------+


LineItemDetailValue
-------------------------

This function is not available for Objectives and Metrics type models. Returns the non-currency Line Item Detail value for the specified dimension items listed below. The Line Item Detail value is always referenced through an associated Line Item.

+---------------------+-------------------------------+
| Item                | Value                         |
+=====================+===============================+
| **SAP PCM Cube**    | LineItemDetailValue           |
+---------------------+-------------------------------+
| **PlaidXL Method**  | LineItemDetailValue           |
+---------------------+-------------------------------+
| **Arguments**       | - Versions                    |
|                     | - Periods                     |
|                     | - Responsibility Centers      |
|                     | - Line Items                  |
|                     | - Line Item Details           | 
|                     | - Currencies                  |
+---------------------+-------------------------------+


ResourceDriverDataValue
-------------------------

Returns the Data value for the Resource Driver specified by the parameters listed below.

+---------------------+-------------------------------+
| Item                | Value                         |
+=====================+===============================+
| **SAP PCM Cube**    | ResourceDriverDataValue       |
+---------------------+-------------------------------+
| **PlaidXL Method**  | ResourceDriverDataValue       |
+---------------------+-------------------------------+
| **Arguments**       | - Versions                    |
|                     | - Periods                     |
|                     | - Responsibility Centers      |
|                     | - Resource Drivers            |
+---------------------+-------------------------------+


ResourceDriverDataSplit
-------------------------

Returns the Data value for the “Resource Driver Split” specified by the parameters listed below.

+---------------------+-------------------------------+
| Item                | Value                         |
+=====================+===============================+
| **SAP PCM Cube**    | ResourceDriverDataSplit       |
+---------------------+-------------------------------+
| **PlaidXL Method**  | ResourceDriverDataSplit       |
+---------------------+-------------------------------+
| **Arguments**       | - Versions                    |
|                     | - Periods                     |
|                     | - Responsibility Centers      |
|                     | - Resource Drivers            |         
|                     | - Activities                  |
+---------------------+-------------------------------+


ResourceDriverPctSplit
-------------------------

Returns the Resource Driver Split by percentage (range 0-100) for the specified parameters.

+---------------------+-------------------------------+
| Item                | Value                         |
+=====================+===============================+
| **SAP PCM Cube**    | ResourceDriverPctSplit        |
+---------------------+-------------------------------+
| **PlaidXL Method**  | ResourceDriverPctSplit        |
+---------------------+-------------------------------+
| **Arguments**       | - Versions                    |
|                     | - Periods                     |
|                     | - Responsibility Centers      |
|                     | - Resource Drivers            |         
|                     | - Activities                  |
+---------------------+-------------------------------+


ResourceDriverSplit
-------------------------

Returns the ResourceDriverSplit value for the specified parameters.

+---------------------+-------------------------------+
| Item                | Value                         |
+=====================+===============================+
| **SAP PCM Cube**    | ResourceDriverSplit           |
+---------------------+-------------------------------+
| **PlaidXL Method**  | ResourceDriverSplit           |
+---------------------+-------------------------------+
| **Arguments**       | - Versions                    |
|                     | - Periods                     |
|                     | - Responsibility Centers      |
|                     | - Resource Drivers            |         
|                     | - Activities                  |
+---------------------+-------------------------------+


ResourceDriverValue
-------------------------

Returns the ResourceDriverValue for the specified parameters.

+---------------------+-------------------------------+
| Item                | Value                         |
+=====================+===============================+
| **SAP PCM Cube**    | ResourceDriverValue           |
+---------------------+-------------------------------+
| **PlaidXL Method**  | ResourceDriverValue           |
+---------------------+-------------------------------+
| **Arguments**       | - Versions                    |
|                     | - Periods                     |
|                     | - Responsibility Centers      |
|                     | - Resource Drivers            |         
+---------------------+-------------------------------+

Revenue
-------------------------

Returns the Revenue for the specified parameters. 

Note: 
CostObjectValues are not calculated On Demand due to the large number of Cost Object combinations in a model. They are either calculated automatically by the Calculation Engine or by command using the CalculateSlice function. As a result when using this function you could consider making use of the function: 

• RestrictCombinationDataRevenue 

This allows you to limit the number of combinations to those that have had a Revenue value entered against them.

+---------------------+-------------------------------+
| Item                | Value                         |
+=====================+===============================+
| **SAP PCM Cube**    | Revenue                       |
+---------------------+-------------------------------+
| **PlaidXL Method**  | Revenue                       |
+---------------------+-------------------------------+
| **Arguments**       | - Versions                    |
|                     | - Periods                     |
|                     | - Responsibility Centers      |
|                     | - Revenue Types               |
|                     | - Cost Object 1               |
|                     | - Cost Object 2               |
|                     | - Cost Object 3               |
|                     | - Cost Object 4               |
|                     | - Cost Object 5               |
|                     | - Currencies                  |         
+---------------------+-------------------------------+


SetPCMModelName
-------------------------

Closes the current open PCM model and open a new one. Notice, you can use one SetPCMModelName per tab. 

This function is primary used for What-If analysis. A user can set multiple tabs connecting to multiple models and check for variances.

This view shows the function opening the “International_Motors” before retrieving data.



SpreadDataValue
-------------------------

This function is not available to Objectives and Metrics models. Returns the Data value for the Spread specified by the dimensions listed below. Although the Spread dimension was designed to contain values that are to be calculated across time, in fact this dimension can contain any calculated or input values that only need to be dimensioned by Version and Period, thus making it ideal for producing fast calculations.

+---------------------+-------------------------------+
| Item                | Value                         |
+=====================+===============================+
| **SAP PCM Cube**    | SpreadDataValue               |
+---------------------+-------------------------------+
| **PlaidXL Method**  | SpreadDataValue               |
+---------------------+-------------------------------+
| **Arguments**       | - Versions                    |
|                     | - Periods                     |
|                     | - Spreads                     |         
+---------------------+-------------------------------+


SummaryActivityValue
-------------------------

Returns the variable part of all Line Items that contribute to the Activities specified by the parameters listed below.

+---------------------+-------------------------------+
| Item                | Value                         |
+=====================+===============================+
| **SAP PCM Cube**    | SummaryActivityValue          |
+---------------------+-------------------------------+
| **PlaidXL Method**  | SummaryActivityValue          |
+---------------------+-------------------------------+
| **Arguments**       | - Versions                    |
|                     | - Periods                     |
|                     | - Responsibility Centers      |
|                     | - Activities                  |
|                     | - Currencies                  | 
+---------------------+-------------------------------+


SummaryCostObjectValue
-------------------------

Returns the SummaryCostObjectValue for the specified parameters. 

Note: 
CostObjectValues are not calculated On Demand due to the large number of Cost Object combinations in a model. They are either calculated automatically by the Calculation Engine or by command using the CalculateSlice function. As a result when using this function you should consider making use of the functions: 

• IsCostObjectCalculated 
• RestrictCombinationCostObjectValue

The first allows you to find out if the value you want has been calculated yet and the other allows you to limit the number of combinations to those that have a nonzero value in specific Versions and Periods.


+---------------------+-------------------------------+
| Item                | Value                         |
+=====================+===============================+
| **SAP PCM Cube**    | SummaryCostObjectValue        |
+---------------------+-------------------------------+
| **PlaidXL Method**  | SummaryCostObjectValue        |
+---------------------+-------------------------------+
| **Arguments**       | - Versions                    |
|                     | - Periods                     |
|                     | - Responsibility Centers      |
|                     | - Cost Object 1               |
|                     | - Cost Object 2               |
|                     | - Cost Object 3               |
|                     | - Cost Object 4               |
|                     | - Cost Object 5               |
|                     | - Currencies                  |         
+---------------------+-------------------------------+


TargetCostObjectValue
-------------------------

Returns the TargetCostObjectValue for the specified parameters. 

Note: 
CostObjectValues are not calculated On Demand due to the large number of Cost Object combinations in a model. They are either calculated automatically by the Calculation Engine or by command using the CalculateSlice function. As a result when using this function you should consider making use of the functions: 

• IsCostObjectCalculated 
• RestrictCombinationCostObjectValue 

The first allows you to find out if the value you want has been calculated yet and the other allows you to limit the number of combinations to those that have a nonzero value in specific Versions and Periods.

+---------------------+-------------------------------+
| Item                | Value                         |
+=====================+===============================+
| **SAP PCM Cube**    | TargetCostObjectValue         |
+---------------------+-------------------------------+
| **PlaidXL Method**  | TargetCostObjectValue         |
+---------------------+-------------------------------+
| **Arguments**       | - Versions                    |
|                     | - Periods                     |
|                     | - Responsibility Centers      |
|                     | - Activity                    |
|                     | - Target Resp Centers         | 
|                     | - Target Activity             |
|                     | - Cost Object 1               |
|                     | - Cost Object 2               |
|                     | - Cost Object 3               |
|                     | - Cost Object 4               |
|                     | - Cost Object 5               |
|                     | - Currencies                  |         
+---------------------+-------------------------------+



UnitPrice
-------------------------

Returns the Unit Price for the specified parameters.

+---------------------+-------------------------------+
| Item                | Value                         |
+=====================+===============================+
| **SAP PCM Cube**    | UnitPrice                     |
+---------------------+-------------------------------+
| **PlaidXL Method**  | UnitPrice                     |
+---------------------+-------------------------------+
| **Arguments**       | - Versions                    |
|                     | - Periods                     |
|                     | - Responsibility Centers      |
|                     | - Revenue Types               |
|                     | - Cost Object 1               |
|                     | - Cost Object 2               |
|                     | - Cost Object 3               |
|                     | - Cost Object 4               |
|                     | - Cost Object 5               |
|                     | - Currencies                  |         
+---------------------+-------------------------------+


UnitsSold
-------------------------

Returns the Units Sold for the specified parameters.

+---------------------+-------------------------------+
| Item                | Value                         |
+=====================+===============================+
| **SAP PCM Cube**    | UnitsSold                     |
+---------------------+-------------------------------+
| **PlaidXL Method**  | UnitsSold                     |
+---------------------+-------------------------------+
| **Arguments**       | - Versions                    |
|                     | - Periods                     |
|                     | - Responsibility Centers      |
|                     | - Revenue Types               |
|                     | - Cost Object 1               |
|                     | - Cost Object 2               |
|                     | - Cost Object 3               |
|                     | - Cost Object 4               |
|                     | - Cost Object 5               |
+---------------------+-------------------------------+


WorksheetDataValue
-------------------------

Returns the Data value of the specified Work Sheet. Work Sheet values are paired due to the inter-relationship between Work Sheets. A Work Sheets 1 value must haveanassociated Work Sheets2valuespecified,and conversely a Work Sheets 2 value must have a Work Sheets 1 value specified.

+---------------------+-------------------------------+
| Item                | Value                         |
+=====================+===============================+
| **SAP PCM Cube**    | WorksheetDataValue            |
+---------------------+-------------------------------+
| **PlaidXL Method**  | WorksheetDataValue            |
+---------------------+-------------------------------+
| **Arguments**       | - Versions                    |
|                     | - Periods                     |
|                     | - Responsibility Centers      |
|                     | - Work Sheets 1               |
|                     | - Work Sheets 2               |
+---------------------+-------------------------------+


WorksheetValue
-------------------------

This function is not available to Objectives and Metrics models. Returns the value of the specified Work Sheet. Worksheet valuesarepairedduetotheinter-relation between Work Sheets. A Work Sheets 1 value must have an associated Work Sheets 2 value specified, and conversely a Work Sheets 2 value must have a Work Sheets 1 value specified.


+---------------------+-------------------------------+
| Item                | Value                         |
+=====================+===============================+
| **SAP PCM Cube**    | WorksheetValue                |
+---------------------+-------------------------------+
| **PlaidXL Method**  | WorksheetValue                |
+---------------------+-------------------------------+
| **Arguments**       | - Versions                    |
|                     | - Periods                     |
|                     | - Responsibility Centers      |
|                     | - Work Sheets 1               |
|                     | - Work Sheets 2               |
+---------------------+-------------------------------+



