.. sectionauthor:: Genova Morel <genova.morel@tartansolutions.com>
.. sectionauthor:: Paul Morel <paul.morel@tartansolutions.com>

PCM Reassignment Value Methods
===============================

.. sidebar:: This Topic

   .. contents::
      :local:

ReassignSplitValue
------------------------

Returns the percentage of reassigned Activity costs received by the Target Responsibility Centers and Target Activities before any reiterative reallocations have been performed, that originate from specified Responsibility Centers, Activities, and Line Items.


+---------------------+-------------------------------+
| Item                | Value                         |
+=====================+===============================+
| **SAP PCM Cube**    | ReassignSplitValue            |
+---------------------+-------------------------------+
| **PlaidXL Method**  | ReassignSplitValue            |
+---------------------+-------------------------------+
| **Arguments**       | - Versions                    |
|                     | - Periods                     |
|                     | - Responsibility Centers      |
|                     | - Activities                  |
|                     | - Target Responsibility       |
|                     | - Target Activities           |
+---------------------+-------------------------------+


ReassignSplitPostValue
------------------------

Returns the percentage of reassigned Activity costs in the Target Responsibility Centers and Target Activities after all required reiterative reallocations have been performed, that originate from specified Responsibility Centers, Activities, and Line Items.


+---------------------+-------------------------------+
| Item                | Value                         |
+=====================+===============================+
| **SAP PCM Cube**    | ReassignSplitPostValue        |
+---------------------+-------------------------------+
| **PlaidXL Method**  | ReassignSplitPostValue        |
+---------------------+-------------------------------+
| **Arguments**       | - Versions                    |
|                     | - Periods                     |
|                     | - Responsibility Centers      |
|                     | - Activities                  |
|                     | - Target Responsibility       |
|                     | - Target Activities           |
+---------------------+-------------------------------+



ReassignSplitInValue
------------------------

Returns the percentage of reassigned Activity costs received by the Target Responsibility Centers and Target Activities after all required reiterative reallocations have been performed that originate from specified Responsibility Centers, Activities, and Line Items.

+---------------------+-------------------------------+
| Item                | Value                         |
+=====================+===============================+
| **SAP PCM Cube**    | ReassignSplitInValue          |
+---------------------+-------------------------------+
| **PlaidXL Method**  | ReassignSplitInValue          |
+---------------------+-------------------------------+
| **Arguments**       | - Versions                    |
|                     | - Periods                     |
|                     | - Responsibility Centers      |
|                     | - Activities                  |
|                     | - Target Responsibility       |
|                     | - Target Activities           |
+---------------------+-------------------------------+


ReassignSplitOutValue
------------------------

Returns the percentage of reassigned Activity costs dispatched by the Target Responsibility Centers and Target Activities after all required reiterative reallocations have been performed, that originate from specified Responsibility Centers, Activities, and Line Items.


+---------------------+-------------------------------+
| Item                | Value                         |
+=====================+===============================+
| **SAP PCM Cube**    | ReassignSplitOutValue         |
+---------------------+-------------------------------+
| **PlaidXL Method**  | ReassignSplitOutValue         |
+---------------------+-------------------------------+
| **Arguments**       | - Versions                    |
|                     | - Periods                     |
|                     | - Responsibility Centers      |
|                     | - Activities                  |
|                     | - Target Responsibility       |
|                     | - Target Activities           |
+---------------------+-------------------------------+

ReassignActivityLineItemValue
------------------------------------------------

Returns the value of any reassigned Activity costs that contribute to the target Responsibility Centers and Activities from the specified Responsibility Centers and Line Items.


+---------------------+-------------------------------+
| Item                | Value                         |
+=====================+===============================+
| **SAP PCM Cube**    | ReassignActivityLineItemValue |
+---------------------+-------------------------------+
| **PlaidXL Method**  | ReassignActivityLineItemValue |
+---------------------+-------------------------------+
| **Arguments**       | - Versions                    |
|                     | - Periods                     |
|                     | - Responsibility Centers      |
|                     | - Line Items                  |
|                     | - Target Responsibility       |
|                     | - Target Activities           |
|                     | - Currencies                  |
+---------------------+-------------------------------+


SourceActivityLineItemValue
------------------------------------------------

Returns the Line Item costs that contribute to the Target Responsibility Centers and Target Activities from specific Versions, Periods, and Responsibility Centers.


+---------------------+-------------------------------+
| Item                | Value                         |
+=====================+===============================+
| **SAP PCM Cube**    | SourceActivityLineItemValue   |
+---------------------+-------------------------------+
| **PlaidXL Method**  | SourceActivityLineItemValue   |
+---------------------+-------------------------------+
| **Arguments**       | - Versions                    |
|                     | - Periods                     |
|                     | - Responsibility Centers      |
|                     | - Line Items                  |
|                     | - Target Responsibility       |
|                     | - Target Activities           |
|                     | - Currencies                  |
+---------------------+-------------------------------+


SourceActivityLineItemFixedValue
------------------------------------------------

Returns the fixed part of the Line Item costs that contribute to the Target Responsibility Centers and Target Activities from specific Versions, Periods, and Responsibility Centers.


+---------------------+-------------------------------+
| Item                | Value                         |
+=====================+===============================+
| **SAP PCM Cube**    | SourceActivityLineItemValue   |
+---------------------+-------------------------------+
| **PlaidXL Method**  | SourceActivityLineItemValue   |
+---------------------+-------------------------------+
| **Arguments**       | - Versions                    |
|                     | - Periods                     |
|                     | - Responsibility Centers      |
|                     | - Line Items                  |
|                     | - Target Responsibility       |
|                     | - Target Activities           |
|                     | - Currencies                  |
+---------------------+-------------------------------+

SourceActivityLineItemVariableValue
------------------------------------------------

Returns the variable part of the Line Item costs that contribute to the Target Responsibility Centers and Target Activities from specific Versions, Periods, and Responsibility Centers.


+---------------------+-------------------------------------+
| Item                | Value                               |
+=====================+=====================================+
| **SAP PCM Cube**    | SourceActivityLineItemVariableValue |
+---------------------+-------------------------------------+
| **PlaidXL Method**  | SourceActivityLineItemVariableValue |
+---------------------+-------------------------------------+
| **Arguments**       | - Versions                          |
|                     | - Periods                           |
|                     | - Responsibility Centers            |
|                     | - Line Items                        |
|                     | - Target Responsibility             |
|                     | - Target Activities                 |
|                     | - Currencies                        |
+---------------------+-------------------------------------+


ReassignedInValue
------------------------------------------------

Returns the total value of reassigned Activity costs after all reiterative reallocation has been completed, that have been received by the Target Responsibility Centers and Target Activities from the specified Responsibility Centers, Activities, and Line Items.


+---------------------+-------------------------------+
| Item                | Value                         |
+=====================+===============================+
| **SAP PCM Cube**    | ReassignedInValue             |
+---------------------+-------------------------------+
| **PlaidXL Method**  | ReassignedInValue             |
+---------------------+-------------------------------+
| **Arguments**       | - Versions                    |
|                     | - Periods                     |
|                     | - Responsibility Centers      |
|                     | - Activities                  |
|                     | - Line Items                  |
|                     | - Target Responsibility       |
|                     | - Target Activities           |
|                     | - Currencies                  |
+---------------------+-------------------------------+


ReassignedOutValue
------------------------------------------------

Returns the total value of reassigned Activity costs dispatched by the Target Responsibility Centers and Target Activities after all reiterative reallocation has been completed, that originate from specified Responsibility Centers, Activities, and Line Items.


+---------------------+-------------------------------+
| Item                | Value                         |
+=====================+===============================+
| **SAP PCM Cube**    | ReassignedOutValue            |
+---------------------+-------------------------------+
| **PlaidXL Method**  | ReassignedOutValue            |
+---------------------+-------------------------------+
| **Arguments**       | - Versions                    |
|                     | - Periods                     |
|                     | - Responsibility Centers      |
|                     | - Activities                  |
|                     | - Line Items                  |
|                     | - Target Responsibility       |
|                     | - Target Activities           |
|                     | - Currencies                  |
+---------------------+-------------------------------+


ReassignedFinalValue
------------------------------------------------

Returns the balanced final value of reassigned Activity costs after all reiterative reallocation and movement has been completed, that contribute to the target Responsibility Centers and Activities from specified Responsibility Centers, Activities, and Line Items.

+---------------------+-------------------------------+
| Item                | Value                         |
+=====================+===============================+
| **SAP PCM Cube**    | ReassignedFinalValue          |
+---------------------+-------------------------------+
| **PlaidXL Method**  | ReassignedFinalValue          |
+---------------------+-------------------------------+
| **Arguments**       | - Versions                    |
|                     | - Periods                     |
|                     | - Responsibility Centers      |
|                     | - Activities                  |
|                     | - Line Items                  |
|                     | - Target Responsibility       |
|                     | - Target Activities           |
|                     | - Currencies                  |
+---------------------+-------------------------------+


ReassignedMoveValue
------------------------

Returns the difference between reassigned Activity costs received and dispatched by the Target Responsibility Centers and Target Activities from specified Responsibility Centers, Activities, and Line Items, after all reiterative reallocation has been completed.


+---------------------+-------------------------------+
| Item                | Value                         |
+=====================+===============================+
| **SAP PCM Cube**    | ReassignedMoveValue           |
+---------------------+-------------------------------+
| **PlaidXL Method**  | ReassignedMoveValue           |
+---------------------+-------------------------------+
| **Arguments**       | - Versions                    |
|                     | - Periods                     |
|                     | - Responsibility Centers      |
|                     | - Activities                  |
|                     | - Line Items                  |
|                     | - Target Responsibility       |
|                     | - Target Activities           |
|                     | - Currencies                  |
+---------------------+-------------------------------+


PostReassignLineItemValue
------------------------------------------------

This calculated value represents the summary activity value analyzed by line item after “Activity Reassignments” have been applied.

+---------------------+-------------------------------+
| Item                | Value                         |
+=====================+===============================+
| **SAP PCM Cube**    | PostReassignLineItemValue     |
+---------------------+-------------------------------+
| **PlaidXL Method**  | PostReassignLineItemValue     |
+---------------------+-------------------------------+
| **Arguments**       | - Versions                    |
|                     | - Periods                     |
|                     | - Responsibility Centers      |
|                     | - Line Items                  |
|                     | - Activities                  |
|                     | - Currencies                  |
+---------------------+-------------------------------+


PostReassignLineItemFixedValue
------------------------------------------------

This calculated value represents the fixed part of the summary activity value analyzed by line item after “Activity Reassignments” have been applied.

+---------------------+-------------------------------+
| Item                | Value                         |
+=====================+===============================+
| **SAP PCM Cube**    | PostReassignLineItemFixedValue|
+---------------------+-------------------------------+
| **PlaidXL Method**  | PostReassignLineItemFixedValue|
+---------------------+-------------------------------+
| **Arguments**       | - Versions                    |
|                     | - Periods                     |
|                     | - Responsibility Centers      |
|                     | - Line Items                  |
|                     | - Activities                  |
|                     | - Currencies                  |
+---------------------+-------------------------------+


PostReassignLineItemVariableValue
------------------------------------------------

This calculated value represents the variable part of the summary activity value analyzed by line item after “Activity Reassignments” have been applied.

+---------------------+-----------------------------------+
| Item                | Value                             |
+=====================+===================================+
| **SAP PCM Cube**    | PostReassignLineItemVariableValue |
+---------------------+-----------------------------------+
| **PlaidXL Method**  | PostReassignLineItemVariableValue |
+---------------------+-----------------------------------+
| **Arguments**       | - Versions                        |
|                     | - Periods                         |
|                     | - Responsibility Centers          |
|                     | - Line Items                      |
|                     | - Activities                      |
|                     | - Currencies                      |
+---------------------+-----------------------------------+


