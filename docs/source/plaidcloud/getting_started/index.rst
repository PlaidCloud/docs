.. sectionauthor:: Genova Morel <genova.morel@tartansolutions.com>
.. sectionauthor:: Paul Morel <paul.morel@tartansolutions.com>

Getting Started
================

.. sidebar:: This Page

   .. contents::
      :local:


Welcome to PlaidCloud! When you login for the first time, your 
workspace will be empty. Don't worry. As you begin to use the software, 
your activity will be displayed in the "Activity Stream" (on the right hand side).
To get you started, we'll cover some of the primary features.

Creating an Account and Signing In
-------------------------------------

This is step 1! If you have not created an account with PlaidCloud, do so by going to:

<https://plaidcloud.com/signup>

Once you have an account, go ahead and sign into Workspace. 

Projects, Workflows, and Tables
-------------------------------------

PlaidCloud makes it simple and easy to organize analytic workflows by separating them into two levels: Projects and Workflows.

To access these:

1) Open the **Analyze** tab on the left of the browser
2) Select Projects or Workflows from the top of the screen

The **Projects** tab provide user access security, information on all workflows in the project, 
entity aliases, and data tables that are able to be shared among workflows. 

**Workflows** are contained within projects and hold the specific analytics workflow you need. Workflows are able to
interact with other workflows in the same project giving you the ability to start and stop other workflows, move data
to other workflows, or move data to project level tables.

Projects
~~~~~~~~~~~~~~~~~~~

There are three available Project security types:

-  **Workspace** (Default Setting): This restricts access to only members of 
   your workspace. As new members are added to your workspace, they are 
   automatically given access to all Projects in the workspace.
-  **Specific Members Only** (Member Access Control List): This restricts access to only the members
   you place on the access list. You need to manage access, but 
   this allow you to limit access to sensitive information.
-  **Specific Security Groups Only** (Group Access Control List): This restricts access to only
   groups you place on the access list. You need to manage access, but 
   this allow you to limit access to sensitive information.

When copying a project, keep in mind that the security type of the 
original project is also copied. This is editable, but the initial state 
will be identical to the original project copied.

Workflows
~~~~~~~~~~~~~~~~~~~

Workflows do the work.

There is no limits to the number of steps in a workflow, allowing each
step to be as simple or complex as needed to do the job.

Initially, the "Workflows" panel will be emtpy, but the below table 
shows a list of workflows within a project.

As a Workflow runs, its status is updated in real time to allow users to
follow along with its progress. Completed steps are given a green
checkmark to show they have finished executing. 


Building a Workflow
---------------------

Many available transforms are available for use in a workflow.
Click on a transform below to learn more about how it helps fulfill 
your analysis needs.

The output of a workflow step can be a source dependent table, source independent table, file, notification, or remote
system action if using PlaidLink. The output is determined by the transform type.

Tables
~~~~~~~~~~~~~~~~~~~

Essentially, a table is where all the data is stored. For those familiar
with Excel or databases, just think of a table as a table of data. 
For those coming from R or Pandas, a table is a frame. 
But Analyze is more than sets of tables like you would find in a database. It's a tool for
preparing data and performing analysis.

Working with Tables
^^^^^^^^^^^^^^^^^^^^^^

As you use Analyze, you'll notice that any operation that creates or
appends to a table will enable the setting of sorts, data types, and
even expressions. It's important to understand how each of your 
selections options operate and the impact they will have on your results.

There are two types of tables in PlaidCloud.

- **Source Dependent**: Source dependent tables are not updateable so they cannot be used for Update, Delete, and
  Append operations but they are highly optimized so steps that use them run extremely fast.
- **Source Independent**: Source independent tables provide independence from their original source which allows for
  updating the data in the table.  These are also the suggested table type when publishing tables for reporting.

Data Types (DTypes)
-------------------

Analyze offers a wide variety of standard DTypes to support your
requirements. As datasets become larger, determining smaller size
DTypes for value storage can shrink the size of the table and improve
performance. Available DTypes are as follows:

-  Boolean
-  Text
-  Numbers

   -  Small Integer (16 bit) (-32768 to 32767)
   -  Integer (32 bit) (-2147483648 to 2147483647)
   -  Big Integer (64 bit) (-9223372036854775808 to 9223372036854775807)
   -  Numeric
   -  Serial
   -  BigSerial

-  UUID
-  Dates and Times

   -  Date
   -  Timestamp
   -  Time Interval

It's also possible to convert from one Dtype to another as well as many other expressions.  See the section on
Expressions for more information on advanced table mapping processes.

