#! python3
# GoogleAdSenseDownload.py - downloads YouTube files from the web
# creates the monthly folders
# grabs Google AdSese files from shared location and throws them into Consignment Sales folder
# puts the YouTube and Google AdSense files in their folders


import time, os, shutil, datetime, calendar, pandas
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

# gets the current username to pull from the downloads folder
path = os.path.abspath('C:\\Users')
pathFolders = os.listdir(path)
for i in pathFolders:
    if i == 'chehem':
        userName = i
    elif i == 'kevqua':
        userName = i
    elif i == 'keleng':
        userName = i
    elif i == 'hugspe':
        username = i
    
print('Getting filepath for Downloads Folder.')

###############################################Razor & Tie YouTube###############################################	
# chooses chrome as the browser
browser = webdriver.Chrome()

# goes to the YouTube website
browser.get('https://www.youtube.com/')
browser.maximize_window()

signInElem = browser.find_element_by_link_text('SIGN IN').click()

print('What is the email?')
emailUser = input()

print('What is the password?')
emailPassword = input()

emailElem = browser.find_element_by_id('identifierId')
emailElem.send_keys(emailUser)
nextButtonElem = browser.find_element_by_id('identifierNext').click()

browser.implicitly_wait(5)
passwordElem = browser.find_element_by_name('password')
passwordElem.send_keys(emailPassword)
time.sleep(2)
passwordNextButton = browser.find_element_by_xpath("//*[@id='passwordNext']").click()
time.sleep(3)
print('You are now signed in!')

# switch accounts
accountElem = browser.find_element_by_id('avatar-btn').click()
time.sleep(1)
switchAccountElem = browser.find_element_by_link_text('Switch account').click()
time.sleep(2)
razorAndTieElem = browser.find_element_by_xpath("//*[@id='contents']/ytd-account-item-renderer[2]/paper-icon-item/paper-item-body/yt-formatted-string[2]").click()
time.sleep(3)
reportsElem = browser.find_element_by_link_text('REPORTS').click()
time.sleep(2)
print('You are now on the Razor & Tie Account.')

# get the files
adsPartnerElem = browser.find_element_by_link_text('Ads Revenue').click()
time.sleep(2)
adsPartnerVideoClaimElem = browser.find_element_by_xpath("//*[@id='download-reports-tbody-0-monthly']/tr[1]/td[5]/a[2]/span").click()
print('Video Claim file downloaded.')
time.sleep(2)
redPartnerElem = browser.find_element_by_link_text('Subscriptions Revenue').click()
time.sleep(2)
rawDataVideoElem = browser.find_element_by_xpath("//*[@id='download-reports-tbody-0-monthly']/tr[1]/td[4]/a[2]/span").click()
print('Red Label RawData file downloaded.')
time.sleep(2)
rawDataVideoSumElem = browser.find_element_by_xpath("//*[@id='download-reports-tbody-0-monthly']/tr[1]/td[4]/a[1]/span").click()
print('Red Label Summary file downloaded.')

# close the browser
print('Waiting for files to fully download from the site.')
time.sleep(30)


# get the dates for the files
today = datetime.date.today()
year = datetime.datetime.today().year
lastYear = year - 1
lastYear = str(lastYear)
year = str(year)
month = today.month
lastMonth = today.month - 1
lastTwoMonths = today.month - 2
lastMonthName = calendar.month_name[lastMonth]
lastMonth = today.month - 1
monthYear = year + '-' + '{:02d}'.format(month)
lastMonthYear = year + '-' + '{:02d}'.format(lastMonth)
print('Getting the dates')



# go to the filepath and see what all years are listed
googleSourcePath = os.path.abspath(r'\\cmgfs\Shared\Accounting\Consignment Sales\Digital\Google Ad Sense')
googleSourceFiles = os.listdir(googleSourcePath)

# find out if the year was there
if year in googleSourceFiles:
    yearGoogleSource = os.path.abspath(r'\\cmgfs\Shared\Accounting\Consignment Sales\Digital\Google Ad Sense\\' + year)
    yearGoogleSourceFiles = os.listdir(yearGoogleSource)
    workingYear = year
elif lastYear in googleSourceFiles:
    yearGoogleSource = os.path.abspath(r'\\cmgfs\Shared\Accounting\Consignment Sales\Digital\Google Ad Sense\\' + lastYear)
    yearGoogleSourceFiles = os.listdir(yearGoogleSource)
    workingYear = lastYear
elif year not in googleSourceFiles and lastYear not in googleSourceFiles:
    os.mkdir(r'\\cmgfs\Shared\Accounting\Consignment Sales\Digital\Google Ad Sense\\' + year)
    sourcePathNew = os.path.abspath(r'\\cmgfs\Shared\Accounting\Consignment Sales\Digital\Google Ad Sense')
    sourcePathNewFiles = os.listdir(sourcePathNew)
    if year in sourcePathNewFiles:
        yearGoogleSource = os.path.abspath(r'\\cmgfs\Shared\Accounting\Consignment Sales\Digital\Google Ad Sense\\' + year)
        yearGoogleSourceFiles = os.listdir(yearGoogleSource)
        workingYear = year

workingMonthYear = workingYear + '-' + '{:02d}'.format(lastMonth)

# check out if the month is there or not
if workingMonthYear not in yearGoogleSourceFiles:
    os.mkdir(yearGoogleSource + '\\' + workingMonthYear)
    newPath = os.path.abspath(yearGoogleSource + '\\' + workingMonthYear)
    print(newPath + ' was created, for this year, ' + workingYear + ' and month: ' + workingMonthYear)
elif workingMonthYear in yearGoogleSourceFiles:
    print('Month already created.')

# create the destination folders

os.mkdir(newPath + '\\' + 'Razor')
os.mkdir(newPath + '\\' + 'Bicycle')
os.mkdir(newPath + '\\' + 'Formatted')
os.mkdir(newPath + '\\' + 'Formatted\Razor')
os.mkdir(newPath + '\\' + 'Formatted\Bicycle')

print('New monthly folders created.')

# move the files
sourcePath = os.path.abspath('C:\\Users\\' + userName + '\Downloads')
sourceFiles = os.listdir(sourcePath)
destinationPath = os.path.abspath(r'\\cmgfs\Shared\Accounting\Consignment Sales\Digital\Google Ad Sense\2019\\' + year + '-' + '{:02d}'.format(lastMonth) + '\Razor')

for file in sourceFiles:
    if file.endswith('.gz'):
        shutil.move(os.path.join(sourcePath, file), os.path.join(destinationPath, file))
print('Files moved to folder.')

###############################################Google AdSense###############################################
# move the bicycle file sover
googleSourcePath = os.path.abspath(r'\\Cmgfs\group\Royalties\Royalty Statements by Label\Google_Adsense')
googleSourceFiles = os.listdir(googleSourcePath)
googleDestinationPath = os.path.abspath(newPath + '\\' + 'Bicycle')
googleFormattedDestinationPath = os.path.abspath(newPath + '\\' + 'Formatted\Bicycle')
googleFileString = 'YouTube_BicycleMusicCompany+vid_M_' + year + '{:02d}'.format(lastTwoMonths) + '01'
csvList = []

for file in googleSourceFiles:
    if file.startswith(googleFileString) and file.endswith('.csv'):
        csvList.append(file)

for file in csvList:
    shutil.copy(os.path.join(googleSourcePath, file), os.path.join(googleDestinationPath, file))

print('Everything has been moved.')
