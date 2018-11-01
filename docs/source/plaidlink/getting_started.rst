.. sectionauthor:: Paul Morel <paul.morel@tartansolutions.com>
.. sectionauthor:: Michael Rea <michael.rea@tartansolutions.com>
.. sectionauthor:: Andrew Hodgson <andrew.hodgson@tartansolutions.com>


Getting Started
=============================

.. toctree::
   :maxdepth: 2
   :includehidden:

.. sidebar:: This Page

   .. contents::
      :local:    

The PlaidLink Agent works in conjunction with the PlaidCloud service. The PlaidLink Agent enables remote operations for extracting, loading, and sourcing 
data along with interacting with an SAP Profitability and Cost Management (PCM) system if PCM is installed.



Create an Agent on PlaidCloud
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

PlaidLink Agent management takes place within the Analyze tab of PlaidCloud.  The first thing is to create a new PlaidLink Agent instance on PlaidCloud.  
Navigate to the Analyze Tab and select PlaidLink Agents under the Tools menu.

Create a new Agent with an appropriate name for the environment or server it will be installed on for remote operations. To view the Agent public and private
keys, click on the edit icon and view the form.  At the bottom of the form you will find the public and private keys that were randomly generated during the
Agent creation process.  Note these keys as they will be used in the agent configuration on the remote server.

If you want to regenerate new randomly generated keys, click on the Regenerate icon for the Agent record.  Once the keys are regenerated, don't forget to 
update the agent configuration file with the new keys on the remote server.

.. important:: Retain the public and private keys for configuring the remote agent in the next step.

Document Account Access
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
If the agent will need to have access to a Document account for uploading or downloading files, it must be granted permission to access the Document account.

In the Document tab select Manage Accounts.  Once the table of accounts appears, click on the agent icon for the account which the new Agent should have 
upload/download rights.  Drag the new agent into the Assigned Agents column and save the access control form.

.. important:: Agents can only upload and download files if the agent has been granted access to one or more Document accounts.

Data Connection Access
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
If the agent will need to have access to a data connection such as a database, it must be granted permission to access the external data connection information.

In the Analyze tab select External Data Connections from the Tools menu.  Once the table of data connections appears, click on the agent icon for the connection 
which the new Agent should have usage rights.  Drag the new agent into the Assigned Agents column and save the access control form.

.. important:: Agent data connection credentials are manged in the External Data Connections.

Installation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
The PlaidLink Agent handles initiating all contact with PlaidCloud and does not require opening any ports in the firewall for performing operations.  The connection 
occurs over an encrypted communication channel at all times.  Both  standard HTTPS connections or secure websocket connections are used.

Installing Python (Use Web Browser)
-----------------------------------------
Download the Anaconda python [installer](https://www.continuum.io/downloads#all "Anaconda Python Installer") for the latest version of Python 2.7.x. Install it.

Install Git (Use Web Browser)
-----------------------------------------
Download the [Git](http://git-scm.com/download/win "Git") installer and run the installation.

Allowing Git use from both git bash and the Windows command line is recommended, but overwriting Windows CLI tools with Unix tools IS NOT recommended.

Generate SSH Keys (Use Git Bash)
-----------------------------------------
From the Start menu open the newly installed Git Bash application.

At the command prompt type the following (or copy/paste):

`mkdir ~/.ssh/`
`ssh-keygen -t rsa -b 4096 -N ""`

Send Contents to Tartan Solutions (Windows Explorer and Email)
-------------------------------------------------------------------

From the .ssh directory copy the id_rsa.pub file and email to your Tartan Solutions contact for addition to the installer access list.  This key will be registered 
for the specific server being installed.

Installing Packages not in Anaconda (Use Windows Command Line)
-------------------------------------------------------------------

.. important:: If you cannot use a direct or proxy connection to perform conda or pip install operations please scroll to the bottom of the installation guide below for a 
   manual installation process.

From the Start Menu open the Windows Command Line application as Administrator.

You must manually install the pyodbc package using conda:

`conda install pyodbc`
`conda install workerpool`

.. important:: If http connections require passing through an authenticated proxy, you will need to set up the .condarc file in the user's home directory. The file should have 
   the following lines:

`proxy_servers:`
`    http: http://user:pass@corp.com:8080`
`    https: https://user:pass@corp.com:8080`

The following should be installed using pip.

`pip install websocket-client`
`pip install gitpython`

If you need to use a proxy server for the pip installs then they should follow this syntax instead:

`pip install --proxy http://user:pass@corp.com:8080 websocket-client`
`pip install --proxy http://user:pass@corp.com:8080 gitpython`

Installing PlaidLink (Use Git Bash)
-----------------------------------------

Once you receive a confirmation response back from Tartan Solutions that your id_rsa.pub key has been added to the access list you can proceed with this next step.

Change to the root of the user working directory. 

`cd ~`

> Make sure you are in the base user directory before proceeding

`pip install -e git+ssh://git@github.com/PlaidCloud/profitagent.git#egg=profitagent`

.. important:: If http connections require passing through an authenticated proxy, you will need to use the --proxy switch in the pip command.

`pip install --proxy http://user:pass@corp.com:8080 -e git+ssh://git@github.com/PlaidCloud/profitagent.git#egg=profitagent`

This will create a src/profitagent directory with respect to your current working directory.

Update the Config File (Use Windows Explorer and Notepad)
--------------------------------------------------------------

An initial configuration file is included in the package, named config-dist.json. Make a sibling copy to edit:

This will be in the following directory relative to the user base directory:

`src/profitagent/profitagent`
`cp config-dist.json config.json`

Copy the agent settings from PlaidCloud into the configuration file. Also set any proxy information required to make an external connection.

Set Up a Windows Service (Use Windows Command Line)
-----------------------------------------------------

.. code-block:
   cd %userprofile%\src\profitagent\profitagent\

To install the service and start it, type this:

.. code-block:
   python windows_service.py --startup auto install

.. important:: To install a Windows service, one must have administrative privileges.

The new Windows service should now appear in the list of services on the server.  It will be listed as PlaidCloud Agent in the services.  The Windows application logs
will list the reporting application as PlaidCloudAgent.

Manual Install
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
If there are network settings that prevent the use of direct connections or proxied connections to perform Conda and PIP installations, a manual process must be followed.

This process will manually install the following packages:
- pyodbc
- workerpool
- websocket-client
- gitpython
- profitagent

For each of the installations above, the first step is download the package via a web browser and place it in the user directory where the PlaidLink service will operate.

pyodbc download:
https://github.com/mkleehammer/pyodbc/archive/master.zip

workerpool download:
https://github.com/shazow/workerpool/archive/master.zip

websocket-client download:
https://github.com/websocket-client/websocket-client/archive/master.zip

gitpython download:
https://github.com/gitpython-developers/GitPython/archive/master.zip

Once all zip files are downloaded they should be unzipped into the same parent directory.

For example:
`c:\users\agent\python_packages`

PIP Install Supporting Packages
-----------------------------------------
Now that all the packages are present on the server locally, the next step is to PIP install them so they are properly registered with the system Python process.

Navigate to the directory where all the supporting python packages are present:

For example:
`c:\users\agent\python_packages`

Now run each of the following commands in Git Bash:

'pip install ./pyodbc'
'pip install ./workerpool'
'pip install ./websocket-client'
'pip install ./GitPython'

Install the PlaidLink Package Provided
-----------------------------------------
The PlaidLink zip file must be provided by a Tartan Solutions contact since direct access is not authorized except through the automated installation process.  If the 
Tartan Solutions contact has not already provided the installation package please contact them.

Unzip the PlaidLink installation files into the home directory of the user the service will operate under in a directory called src/.

For example:
`c:\users\agent\src`

Now navigate to the directory that contains the PlaidLink package and run the following command in Git Bash:

'pip install -e ./profitagent'

Resume Configuration and Registration
-----------------------------------------
Now follow the instructions for updating the config file and registering the process as a Windows Service as described in the two sections before this Manual Install section

