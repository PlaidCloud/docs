.. sectionauthor:: Genova Morel <genova.morel@tartansolutions.com>
.. sectionauthor:: Paul Morel <paul.morel@tartansolutions.com>

Using with SAP PCM
====================

.. sidebar:: This Topic

   .. contents::
      :local:

   .. toctree::
      :maxdepth: 1
      :includehidden:
      :glob:

      *


If you already have a SAP PCM client installed on the server or PC with which you are using Excel, the PCM ribbon will
appear automatically allowing you connect to PCM models.

.. note:: You will not see the SAP PCM ribbon if your PC does not have the PCM client installed

In order to ensure model access and rights are consistent across all PCM usage scenarios, PlaidXL leverages the same
PCM security model that is used by all aspects of PCM.

This is a list of all the Model Builder functions divided into two types: Retrieve and WriteBack. Retrieve functions are
updated by the Retrieving data ribbon options while WriteBack function are updated by the Saving data ribbon options.
Notice each Retrieve function has a hashtag code, and the WriteBack has only the #WB. The hashtag code is used when no
value has been retrieved from PCM.


+--------------------------------------------------+------------------------------------+
| Retrieve Functions                               | WriteBack Functions                |
+==================================================+====================================+
| - ActivityDriverValue (#ADV)                     |  - LineItemValue (#LIV)            |
| - ActivityCostObjectValue (#ACOV)                |  - LineItemDetailValue (#LIDV)     |
| - ActivityDriverDataValue (#ADDV)                |  - ResourceDriverValue (#RDV)      |
| - ActivityLineItemValue (#ALIV)                  |  - ResourceDriverSplit (#RDS)      |
| - ActivityValue (#AV)                            |  - ActivityDriverValue (#ADV)      |
| - CostObjectValue (#COV)                         |  - ExternalActivityValue (#EAV)    |
| - DataRevenue (#DR)                              |  - ExternalCostObjectValue (#ECOV) |
| - DataUnitPrice (#DUP)                           |  - Revenue (#REV)                  |
| - DataUnitsSold (#DUS)                           |  - PropertyValue (#PV)             |
| - DirectCostObjectValue (#DCOV)                  |  - Memo(#MEM)                      |
| - ExternalActivityValue (#EAV)                   |                                    |
| - ExternalCostObjectValue (#ECOV)                |                                    |
| - LineItemValue (#LIV)                           |                                    |
| - LineItemCostObjectValue (#LICOV)               |                                    |
| - LineItemDataValue (#LIDV)                      |                                    |
| - LineItemDetailDataValue (#LIDDV)               |                                    |
| - LineItemDetailValue (#LIDV)                    |                                    |
| - ResourceDriverDataValue (#RDDV)                |                                    |
| - ResourceDriverDataSplit (#RDDS)                |                                    |
| - ResourceDriverPctSplit (#RDPS)                 |                                    |
| - ResourceDriverSplit (#RDS)                     |                                    |
| - ResourceDriverValue (#RDV)                     |                                    |
| - Revenue (#REV)                                 |                                    |
| - SetPCMModelName                                |                                    |
| - SpreadDataValue (#SDV)                         |                                    |
| - SummaryActivityValue (#SAV)                    |                                    |
| - SummaryCostObjectValue (#SCOV)                 |                                    |
| - TargetCostObjectValue (#TCOV)                  |                                    |
| - UnitPrice (#UP)                                |                                    |
| - UnitsSold (#US)                                |                                    |
| - WorksheetDataValue (#WDV)                      |                                    |
| - WorksheetValue (#WV)                           |                                    |
+--------------------------------------------------+------------------------------------+

+--------------------------------------------------+------------------------------------+
| Reassignment Value Functions                     | Model Information Functions        |
+==================================================+====================================+
| - ReassignSplitValue (#RSV)                      | - GetAlias                         |
| - ReassignSplitPostValue (#RSPV)                 | - GetPCMModelName                  |
| - ReassignSplitInValue (#RSIV)                   | - GetRetrieveTime                  |
| - ReassignSplitOutValue (#RSOV)                  | - GetParent                        |
| - ReassignActivityLineItemValue (#RALIV)         | - GetParentBelowParent             |
| - SourceActivityLineItemValue (#SALIV)           | - GetMemo                          |
| - SourceActivityLineItemFixedValue (#SALIFV)     | - GetProperty                      |
| - SourceActivityLineItemVariableValue (#SALIVV)  | - GetParentBelowGroup              |
| - ReassignedInValue (#RIV)                       |                                    |
| - ReassignedOutValue (#ROV)                      |                                    |
| - ReassignedFinalValue (#RFV)                    |                                    |
| - ReassignedMoveValue (#RMV)                     |                                    |
| - PostReassignLineItemValue (#PRLIV)             |                                    |
| - PostReassignLineItemFixedValue (#PRLIFV)       |                                    |
| - PostReassignLineItemVariableValue (#PRLIVV)    |                                    |
+--------------------------------------------------+------------------------------------+



