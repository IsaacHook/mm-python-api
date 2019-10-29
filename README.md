# Controlling MachineMotion with Python

<p style="text-align:center;" ><img src="__documentation/_media/CE-CL-105-0003_+python.png" width="60%" height="60%"></p>
<p style="text-align: center;"><span style="color: #808080; font-size: 11pt;"><em>Figure 1: MachineMotion Controller.</em></p>

<p>&nbsp;</p>

The MachineMotion Python API simplifies motion control and provides an intuitive, human-readable way to bring your equipment to life. 

Inexperienced programmers should consider using [MachineLogic's](https://www.vention.io/technical-documents/in-cad-automation-with-machinelogic-24) code-free visual sequence editor to create simple motion programs. 

However, MachineLogic is not suitable for developing complex applications. The Python API is generally required if:
* The application must communicate with custom hardware
* The application requires complex logic
* The application must integrate with third party software and tools

###### For more information on 3D design using Vention, datasheets and more, please visit [Vention.io](https://www.vention.io/technical-documents/machinemotion-controller-datasheet-10)

<div>&nbsp;</div>

## Getting Started

To get started with the MachineMotion Python API:

* Install Python on your computer [(link)](#install-python-on-your-computer)
* Download the MachineMotion API  [(link)](#install-python-on-your-computer)
* Download the required libraries [(link)](#install-python-on-your-computer)
* Connect to MachineMotion [(link)](#install-python-on-your-computer)
* Run your first program [(link)](#install-python-on-your-computer)

<div>&nbsp;</div>

### Install Python On Your Computer

The MachineMotion library supports both Python 2.7 and Python 3.6.

- If installing on Windows, make sure to add Python.exe to the PATH environment variable as shown in *Figure 2* and *Figure 3*.

<p style="text-align:center;" ><img src="__documentation/_media/python_2.7_install_edited.png" width="45%" height="45%" <img style="border:1px solid grey;"></p>

<p style="text-align: center;"><span style="color: #808080; font-size: 11pt;"><em>Figure 2: Make sure to select "Add python.exe to path" if installing on Windows.</em></p>

<p style="text-align:center;" ><img src="__documentation/_media/python_3.6_install_edited.png" width="45%" height="45%" <img style="border:1px solid grey;"></p>

<p style="text-align: center;"><span style="color: #808080; font-size: 11pt;"><em>Figure 3: Make sure to click "Add Python 3.6 to PATH" if installing on Windows.</em></p>

<div>&nbsp;</div>


### Download The API Library

The MachineMotion controller software comes pre-installed on the MachineMotion controller. There are two versions of the Python API, so the correct version of the Python API must be selected. The table below shows which version should be downloaded.

| Controller Software| Python API | Git Clone | Link |
| ------------- |:-------------:| :-----:| ---|
| v1.2.11 and earlier    | Python API v1.6.8 | `git clone https://github.com/VentionCo/mm-python-api/tree/release/v1.6.8` | [v1.6.8](https://github.com/VentionCo/mm-python-api/tree/release/v1.6.8) |
| v1.12.0 and later    | Python API v2.0+     | `git clone https://github.com/VentionCo/mm-python-api/tree/release/v2.0`) | [v1.12.0](https://github.com/VentionCo/mm-python-api/tree/release/v2.0)

<p style="text-align: center;"><span style="color: #808080; font-size: 11pt;"><em>Check your controller software version <a href="">here</a></em></p>

<b>To Download the API library</b>:
<hr>

<div style="text-align: center">
Open the command prompt (for Windows) or the terminal (for Mac or Linux), navigate to your destination folder and paste the suitable 'git clone' command  

<span style="color: #808080; font-size: 11pt;"> or </span>

Follow the download link above and unzip the contents in your directory of choice
</div>
<hr>

###### Need Help? See Github's download guide [here](https://help.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository)

<div>&nbsp;</div>

### Download the required libraries

 Open the command prompt (for Windows) or the terminal (for Mac or Linux) and run the following installations  

  ```console
  pip install -U socketIO-client
  ```  
  
  ```console
  pip install -U pathlib
  ```

  ```console
  pip install -U paho-mqtt
  ```

The MachineMotion Python library is now installed and ready to use! Continue below to start your first custom program. 

## Connecting to MachineMotion

If you require more information about how to setup you controller to communicate with your computer or network, consult the ressource below.

[QuickStart: Connecting to MachineMotion](__documentation/quick_start/machine_motion--quickstart.md)

## API Documentation

[Application Programming Interface: Python v1.6.8](__documentation/api/machine_motion_python_api--v1.6.8.md)

## Release Notes
[Release Notes: Python v1.6.8](release-notes.md)
