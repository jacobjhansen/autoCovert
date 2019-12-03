import xml.etree.ElementTree as ET
import os, sys, json

def listDevices(bilingID):

    deviceList = []

    # In a finished tool, an API call would be made here to list all device ids on a customer account. Then the deviceIDs of all Android devices would be added to a list. For the scope of this project an example API call will be used, and the data will be read directly from the file deviceSearch.json

    with open("placeholder/deviceSearch.json", "r") as json_file: 
        data = json.load(json_file) 
        current = data['devices']['device']['maas360DeviceID']
        deviceList.append(current)

    return deviceList

def listSoftware(deviceID):
    appList = []

    # In a finished tool, an API call would be made here to list all installed software on the device with the given deviceID. For the scope of this project an example API call will be used, and the data will be read directly from the file softwareSearch.xml

    tree = ET.parse('placeholder/softwareSearch.xml')
    root = tree.getroot()

    for item in root.findall('./devicesw/swAttrs/swAttr/value'):
        appList.append(item.text)

    return appList