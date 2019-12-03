import xml.etree.ElementTree as ET
import os, sys, json, time
from appDiscovery import listDevices, listSoftware
from apkDiscovery import downloadAPK
from resultDiscovery import results

def getBillingID():

    billingID = None
    tree = ET.parse('placeholder/config.xml')
    root = tree.getroot()
    for connection in root:
        placeholderBillingID = connection.text

    os.system('clear')
    print('AutoCOVERT')
    print('\nUNDER DEVELOPMENT\n')
    billingIDInput = input('Enter billing ID: (Leave Blank to use Placeholder)')
    if billingIDInput == '':
        billingID = placeholderBillingID
    else:
        billingID = billingIDInput
    
    return billingID

def printProgramInfo(billingID,deviceList,appList,apkFolderPath):
    os.system('clear')
    print('AutoCOVERT\n\nUNDER DEVELOPMENT\n')
    print('Billing ID:',billingID)
    print('Number of Devices Found:',len(deviceList))
    print('Number of Applications Found:',len(appList))
    print('Path to downloaded APK\'s',apkFolderPath)
    shouldContinue = input('Press ENTER to continue: (Or type c to cancel)\n')
    if shouldContinue == '':
        pass
    else:
        sys.exit('\nProcess Ended by User Input\n')

def main():
    billingID = getBillingID()

    # Get list of all android devices on an institutional account
    deviceList = listDevices(billingID)
    appList = []

    # Create folder for downloaded APKs
    os.system('cd ~/working/covert/app_repo && mkdir testBundle')
    apkFolderPath = '~/working/Covert/app_repo/testBundle'

    # Create list of applications installed company-wide
    for device in deviceList:
        installedSoftware = listSoftware(device)
        for app in installedSoftware:
            appList.append(app)
    
    # Download APK File for every application in the appList
    for app in appList:
        downloadAPK(app,apkFolderPath)

    printProgramInfo(billingID,deviceList,appList,apkFolderPath)

    # Analyze Bundle Created
    os.system('clear')
    print('Analyzing with COVERT...')
    os.system('cd ~/working/covert && ./covert.sh testBundle')

    # Finalize Results
    results()

main()