.. sectionauthor:: Genova Morel <genova.morel@tartansolutions.com>
.. sectionauthor:: Paul Morel <paul.morel@tartansolutions.com>

Workflows
!!!!!!!!!!

.. sidebar:: Workflow Operations

   .. contents::
      :local:

   .. toctree::
      :maxdepth: 1
      :includehidden:
      :glob:

      allocations/index
      document_management/index
      export/index
      import/index
      notifications/index
      other/index
      remote/index
      report/index
      sap_integration/index
      sap_pcm_integration/index
      table_operations/index
      user_defined/index
      workflow_control/index
      common/index
      expressions/index

Building a Workflow
=========================

Many available transform steps are available for use in a PlaidCloud workflow. The output of a workflow step can be 
a table, view, file, notification, or remote system action if using PlaidLink. The output is determined by the 
tranform step type.


Viewing Workflows
-----------------

Workflows exist within a **Project** and are organized in a hierarchy. To access workflows:

1) Select **Analyze** from the left menu 
2) Double click on the project you want
3) Click the **Workflows** tab at the top

The list of projects is determined by your access security for each of the projects and your Viewing Role within the
project (i.e. Architect, Manager, or Explorer).  If you are expecting to see a project and it is not present then it
could be that you have not been granted access to the project by one of the project owners.  If you are expecting to
see certain workflows within the project and you are not an Architect on the project, then they might be hidden to your
viewing role.

The status of the workflow will be displayed if it is running, has a warning or error, or completed normally.  The
creation and update dates are also shown along with who created or updated the workflow.

Because workflows are organized in a hierarchy, the same workflow is able to exist in multiple projects simultaneously.

Creating
-----------

To create and add a new workflow to a project:

1) Select **Analyze** from the left menu 
2) Double click on the project you want
3) Click the **Workflows** tab at the top
4) Select the "New Workflow" button
5) Fill in the information
6) Click "Create" or "Create and Open Config"

The "Create and Open Config" option brings you directly to the workflow configuration page whereas the "create button will bring you to the main wokrflow page. 

Managing Errors
-----------------

If a workflow experiences an error during processing, an error indicator is displayed on both the workflow and the step
that had the error.  PlaidCloud provides an ability to retry a failed step multiple times.  This is often useful if the
step is accessing remote systems or data that may not be highly available or intermittently fail for unknown reasons.
The retry capability can be set to retry many times as well as add a delay between retries from seconds to hours.

If no retry is selected or the maximum number of retries is exceeded, then the step will be marked as an error.
PlaidCloud provides three levels of error handling in that case:

  - Stop the workflow when an error occurs
  - Mark the step as an error but keep processing the workflow
  - Mark the step as an error and trigger a remediation workflow process instead of continuing the current workflow

Stop the Workflow
~~~~~~~~~~~~~~~~~

Stopping the workflow when a step errors is the most common approach since workflows generally should run without
errors.  This will stop the workflow and present the error indicator on both the step and the workflow.  The error will
also be displayed in the activity monitor but no further action is taken.

Keep Processing
~~~~~~~~~~~~~~~

Each step can be set to continue on error in the step form.  If this checkbox is enabled then any errors will be marked
for the step, but the workflow will treat the error as a completion of the step and continue on.  This is often useful if
there are steps that perform tasks that can error when there is missing data but are harmless to the overall processes.

Since the workflow is continuing on error under this scenario, the workflow will not display an error indicator but instead
continue to show a running indicator.

Trigger Remediation Workflow
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

With the ability to set a remediation workflow as part of the workflow setup, a workflow error will immediately stop
the processing of the current workflow and start processing the remediation workflow. Note that, if a step is marked to
continue on error, a failure will not trigger the remediation workflow.  Only steps that fail resulting in the entire workflow to stop will trigger the remediation process.

A remediation workflow may be useful for simply notifying people that a failure has occurred. It can also attempt an automatic correction of any underlying reasons 
the original workflow failed.

Viewing the Workflow Log
------------------------

As things happen within a workflow, such as steps running or warnings occurring, those events are logged to the workflow
log.  To view this log:

1) Select Analyze
2) Double click on the project you want
3) Select the **log** tab from the top 

The log viewer allows for sorting and filtering the log as well as viewing the details of a particular log entry.

The workflow log is also present in the project log in case you would like to see a more comprehensive view of logs across multiple workflows.

Clearing the Workflow Log
-------------------------

Clearing the workflow log may be desirable from time to time.  To clear the workflow log:

1) Select Analyze
2) Double click on the project you want
3) Select the **log** tab from the top
4) Select the **Clear Log** button

This will clear the log based on the workflow selected which will also remove the log entries from the project level log too.

Viewing the Workflow Report
---------------------------

Maintaining detailed documentation to support both statutory and management requirements is challenging when the
projects and workflows may be dynamic.  To help solve this problem, PlaidCloud provides a Workflow level report that
provides detailed documentation of workflows, workflow steps, user defined functions, and variables.

The report is generated on-demand and reflects the current state of the workflow.  To download the report:

1) Select Analyze
2) Double click on the project you want
3) Select the **workflows** tab from the top
4) Click the **Report** icon 

Managing Workflow Variables
---------------------------

PlaidCloud allows variables at both the project and workflow scope. This allows for setting project wide
variables or being able to pass information easily between workflows.  The variables and values are viewed by clicking
on the variables icon in the **Workflows** hierarchy.

From the variables table you can view the variables, the current values, and edit the values.  You can also add new
variables or delete existing ones.

Duplicating a Workflow
----------------------

It may be useful to copy a workflow when planning to make major changes or to replicate the process with different
options.  Duplicating an entire workflow is very easy in PlaidCloud.  To do so:

1) Select Analyze
2) Double click on the project you want
3) Select the workflows tab from the top
4) Select the workflows you would like to duplicate 
5) Click the **Duplicate Selected Workflows** button at the top 

This will copy the workflows and append the word *Copy* to the name.

Once the duplication process is complete, the workflow is fully functional.  Copied workflows are completely separate
from the original and can be modified without impacting the original workflow.

Setting Parallelism
--------------------

Workflows in PlaidCloud can be executed as a combination of serial steps and parallel operations.  To set a group of
steps to run in parallel:

1) Select Analyze
2) Double click on the project you want
3) Select the **steps** tab from the top 
4) Click the new folder button
5) Select the new folder
6) Click "add steps" from the top
7) Place all the desired steps into the folder
8) Right click on the group folder
9) Select the **Execute in Parallel** option

This will allow all the steps in the group to trigger simultaneously
and execute in parallel.  Once all steps in the group complete, the next step or group in the workflow after the group will activate.

Running One Step
----------------------

During initial workflow development, testing, or troubleshooting it is often quite useful to run steps individually.
To run a single step in isolation:

1) Select Analyze
2) Double click on the project you want
3) Select the **workflows** tab from the top
4) Double click on the workflow you want
5) Right click on the step you want to run
6) Select **Run Step** from the context menu.

Running Multiple Steps
------------------------------------

While running individual steps is useful, it also may be useful to run subsets of an entire workflow for development,
testing, or troubleshooting.  

To run a subset of steps:

1) Select Analyze
2) Double click on the project you want
3) Select the **workflows** tab from the top
4) Double click on the workflow you want
5) Select all the steps you would like to run 
6) Click **Actions** from the top bar
7) Select **Run Selected** 

This will trigger a normal workflow processing but start the workflow at the beginning of the selected steps and stop once the last selected
step is complete.

Running an Entire Workflow
---------------------------

To run the entire workflow:

Select **start** from the top bar or click the "run" icon

Setting the Workflow to Skip Steps
----------------------------------

Steps in the workflow can be set to skip during the workflow run.  This may be useful if there are debugging steps or
old steps that you are not prepared to completely remove from the workflow yet.

To set this option, you have two options:
 - Edit the step form
 - Uncheck the enabled checkbox in the workflow hierarchy
 
To edit the step form:

1) Select Analyze
2) Double click on the project you want
3) Select the **workflows** tab from the top
4) Double click on the workflow you want
5) Uncheck the **enable** box of the step you wish to skip

Or: 

5) Select the step(s) you wish to skip
6) Open the **actions** tab from the top bar
7) Click **disable step**


.. note:: Steps that have been set to disabled will have a disabled indicator in the workflow steps hierarchy table.

Changing the Order of Steps
---------------------------------------

There are two ways to update the order of steps in the workflow.  

For small changes:

1) Select Analyze
2) Double click on the project you want
3) Select the **workflows** tab from the top
4) Double click on the workflow you want
5) Use the up and down arrows next to each step 

For larger changes:

5) Select the step you want to move
6) Either right click on the step and select the **move this step** option or click the step placement icon
7) Edit the position 
8) Click "update position"

Setting Steps to Continue on Error
----------------------------------

Workflow steps can be set to continue processing even when there is an error.  This might be useful in workflow start-up
conditions or where data may be available intermittently.  If the step errors, it will be recorded as an error but the
workflow will continue to process.

To set this option:

1) Select Analyze
2) Double click on the project you want
3) Select the **workflows** tab from the top
4) Double click on the workflow you want
5) Click on the edit icon
6) Check the checkbox for **Continue On Error**
7) Save changes

Now any errors with the step will not cause the workflow to stop.

Steps that have been set to continue on error will have a special indicator in the workflow steps hierarchy table.

Copy Steps
----------------------

It is often very useful to copy steps instead of starting from scratch each time.  PlaidCloud allows copying steps
within workflows as well as between workflows, even in other projects.  You can select multiple steps to copy at once. To do so:

1) Select Analyze
2) Double click on the project you want
3) Select the **workflows** tab from the top
4) Double click on the workflow you want
5) Select the steps you want to copy
6) Click the **Copy Selected Steps** button at the top 

This will place the selected steps in the clipboard and allow pasting within the current workflow or another one.

Copying a step will make a duplicate step within the project.  If you want to place the same step in more than one
location in a workflow, use the **Add Step** menu option to add a reference to the same step rather than a clone of
the original step.

Paste Steps
----------------------

After selecting steps to copy and placing them on the clipboard, you can paste those steps into the same workflow or
another workflow, even in another project.  There are two options when pasting the steps into the workflow:

  - Append to the end of the workflow
  - Insert after last selected row

The append option will simply append the steps to the end of the selected workflow.  The insert option will insert the
copied steps after the selected row.  Note, that if multiple steps have been copied to the clipboard from multiple areas
in a workflow, that pasting them will paste them in order but will not have any nested hierarchy information from when
they were copied.  The pasting will be a flat list of steps to insert only.  This might be unexpected but it is safer
than creating all of the directory structure in the target workflow that existed in the source workflow.

Run Dependency Audit
----------------------

The **Workflow Dependency Audit** is a very helpful tool to understand data and workflow dependencies in complex
interconnected workflows.  Over time, as workflow processes become more complex, it may become challenging to ensure
all dependencies are in the correct order.  When data already exists in tables, steps will run and appear correct in
many cases but may actually have a dependency issue if the data is populated out of order.

This tool will provide a dependency audit and identify issues with data dependency relationships.

Workflow conditions
--------------------

Setting conditions for a workflow will control whether the workflow will rin or not. In order for the workflow to run, all of the conditions that were set must be met.
If not all set conditions are met, the workflow will not run. To set conditions:

1) Select Analyze
2) Double click on the project you want
3) Select the **workflows** tab from the top
4) Double click on the workflow you want
5) Click the edit icon of the step you want to set a condition for
6) Select the **conditions** tab from the top of the window
7) Fill out the form
8) Click "update" or "update and open config"
