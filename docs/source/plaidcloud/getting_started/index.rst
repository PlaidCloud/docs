.. sectionauthor:: Genova Morel <genova.morel@tartansolutions.com>
.. sectionauthor:: Paul Morel <paul.morel@tartansolutions.com>

Getting Started
================

.. sidebar:: This Page

   .. contents::
      :local:

Welcome to PlaidCloud!

When you login for the first time, your 
workspace will be empty. Don't worry. As you begin to use the service, 
your activity will be displayed in the "Activity Stream" (on the right hand side).
To get you started, we'll cover some of the primary features.

Creating an Account and Signing In
-------------------------------------

This is step 1! 

If you have not created an account with PlaidCloud, do so by going to:

Sign-up Link (https://plaidcloud.com/signup)

Once you have an account, go ahead and sign into Workspace. You won't have anything in your newly created Workspace
yet but we will go through how to get started using the service.

Personalization
---------------

PlaidCloud offers the abilty to personalize your experience through picking a theme for your browser client and preferred language.
In addition, the dashboard visualizations and JupyterLab area allow personalization with themes and language preferences too.  The themes are
slightly different depending on the area due to each theme being optimized for the particular task.

The Dashboards and JupyterLab areas are mobile friendly.  In addition the dashboards are designed for display from very large displays in public
areas all the way down to mobile phones.

Branding
--------

The PlaidCloud Firewall installation, either on-prem or in a private cloud, allows for customized branding options.  The PlaidCloud SaaS solution
does not offer customized branding options at this time.

For enterprise customers, custom domains are possible for the PlaidCloud SaaS.


Projects, Workflows, and Tables
-------------------------------------

PlaidCloud makes it simple and easy to organize analytic workflows by separating them into two levels within a Workspace: Projects and Workflows.

To access these:

Open the **Analyze** tab on the left of the browser

The **Projects** area displays the projects you have access to and allows you to interact with those projects. Double 
clicking on the project record will open the project in a separate tab where you can view the project details as well as
workflows, tables, data editors, logs, hierarchies, and user defined functions (UDFs) for the project.

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

There is no limit to the number of steps in a workflow, allowing each
step to be as simple or complex as needed to do the job.

Initially, the "Workflows" panel will be emtpy, but the workflow hierarchy 
shows a list of workflows within a project.

As a Workflow runs, its status is updated in real time to allow users to
follow along with its progress. Completed steps are given a green
checkmark to show they have finished executing. 


Building a Workflow
---------------------

Many available transforms are available for use in a workflow.
Click on a transform below to learn more about how it helps fulfill 
your analysis needs.

The output of a workflow step can be a table, view, file, notification, or remote
system action if using PlaidLink. The output is determined by the transform type.

Tables
~~~~~~~~~~~~~~~~~~~

Essentially, a table is where all the data is stored. For those familiar
with Excel or databases, just think of a table as a spreadsheet of tablular data. 
For those coming from R or Pandas, a table is a data frame. 
But Analyze is more than sets of tables like you would find in a database. It's a tool for
preparing data and performing analysis.

Working with Tables
^^^^^^^^^^^^^^^^^^^^^^

As you use Analyze, you'll notice that any operation that creates or
appends to a table will enable the setting of sorts, data types, and
even expressions. It's important to understand how each of your 
selection options operate and the impact they will have on your results.

There are two types of data tables in PlaidCloud.

- **View**: Views are not updateable so they cannot be used for Update, Delete, and
  Append operations but they are highly optimized so steps that use them run extremely fast. These depend on Table
  data so updates to underlying tables automatically update dependent views.  Views in Analyze operate
  very similar to database views if you are familiar with those.
- **Table**: Tables provide independence from their original source which allows for
  updating the data in the table.  Tables can only be updated or modified through workflow operations, 
  Data Editors, UDFs, Notebooks, or remote operations using PlaidTools or PlaidLink.

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

It's also possible to convert from one Dtype to another as well as use many other expressions.  See the section on
Expressions for more information on advanced table mapping processes.
