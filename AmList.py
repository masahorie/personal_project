import bs4 as bs
import urllib.request
import xlwt

# Make workbook
workbook = xlwt.Workbook()

# Add sheet
sheet = workbook.add_sheet("AM Frequency List", cell_overwrite_ok=True)	
	
#def excel_init(list_num):
#Change col width
third_col = sheet.col(0)
third_col.width = 64 * 50
third_col = sheet.col(1)
third_col.width = 64 * 50
third_col = sheet.col(2)
third_col.width = 64 * 50
third_col = sheet.col(3)
third_col.width = 64 * 50
third_col = sheet.col(4)
third_col.width = 64 * 50
third_col = sheet.col(5)
third_col.width = 64 * 50
third_col = sheet.col(6)
third_col.width = 64 * 50
third_col = sheet.col(7)
third_col.width = 64 * 50
third_col = sheet.col(8)
third_col.width = 64 * 50
third_col = sheet.col(9)
third_col.width = 128 * 50
third_col = sheet.col(10)
third_col.width = 64 * 50
third_col = sheet.col(11)
third_col.width = 64 * 50
third_col = sheet.col(12)
third_col.width = 64 * 50
third_col = sheet.col(13)
third_col.width = 64 * 50
third_col = sheet.col(14)
third_col.width = 64 * 50
third_col = sheet.col(15)
third_col.width = 64 * 50
third_col = sheet.col(16)
third_col.width = 64 * 50
third_col = sheet.col(17)
third_col.width = 64 * 50
third_col = sheet.col(18)
third_col.width = 64 * 50
third_col = sheet.col(19)
third_col.width = 64 * 50
third_col = sheet.col(20)
third_col.width = 64 * 50
third_col = sheet.col(21)
third_col.width = 64 * 50
third_col = sheet.col(22)
third_col.width = 64 * 50
third_col = sheet.col(23)
third_col.width = 64 * 50
third_col = sheet.col(24)
third_col.width = 64 * 50
third_col = sheet.col(25)
third_col.width = 64 * 50
third_col = sheet.col(26)
third_col.width = 64 * 50
third_col = sheet.col(27)
third_col.width = 100 * 50
third_col = sheet.col(28)
third_col.width = 100 * 50
third_col = sheet.col(29)
third_col.width = 64 * 50
third_col = sheet.col(30)
third_col.width = 64 * 50

# Write a cell (row, column, value)
style = xlwt.easyxf('font: bold 1; align: wrap on,vert centre, horiz left;')
sheet.write(0,0, 'Call', style)
sheet.write(0,1, 'Frequency', style)
sheet.write(0,2, 'Modulation', style)
sheet.write(0,3, '-', style)
sheet.write(0,4, 'Antenna', style)
sheet.write(0,5, 'Day/Night', style)
sheet.write(0,6, 'Dom Class', style)
sheet.write(0,7, 'Int Class', style)
sheet.write(0,8, 'FM Stat', style)
sheet.write(0,9, 'City', style)
sheet.write(0,10, 'State', style)
sheet.write(0,11, 'Country', style)
sheet.write(0,12, 'File Num', style)
sheet.write(0,13, 'TX Power', style)
sheet.write(0,14, '-', style)
sheet.write(0,15, '-', style)
sheet.write(0,16, '-', style)
sheet.write(0,17, 'Facility ID', style)
sheet.write(0,18, 'N/S Lat', style)
sheet.write(0,19, 'Deg', style)
sheet.write(0,20, 'Min', style)
sheet.write(0,21, 'Sec', style)
sheet.write(0,22, 'W/E Long', style)
sheet.write(0,23, 'Deg', style)
sheet.write(0,24, 'Min', style)
sheet.write(0,25, 'Dec', style)
sheet.write(0,26, 'Lic/Perm', style)
sheet.write(0,27, 'Dis from Lat/Long', style)
sheet.write(0,28, 'Mil from Lat/Long', style)
sheet.write(0,29, 'Azimuth', style)
sheet.write(0,30, 'App ID', style)

#Save excel sheet
workbook.save("AM Frequency List" + ".xls")	

# Input State
in_state = input ("State: ")
# Input City
in_city = input ("City: ")
# Input lower Frequency
in_frequency_l = input ("Lower Frequency: ")
# Input upper Frequency
in_frequency_u = input ("Upper Frequency: ")

print (in_state)
print (in_city)
print (in_frequency_l)
print (in_frequency_u)




# Get Database data from FCC.
theurl = 'https://transition.fcc.gov/fcc-bin/amq?call=&arn=&state="in_state"&city="in_city"&freq="in_frequency_l"&fre2="in_frequency_u"&type=0&facid=&class=&list=4&ThisTab=Results+to+This+Page%2FTab&dist=&dlat2=&mlat2=&slat2=&NS=N&dlon2=&mlon2=&slon2=&EW=W&size=9'
print (theurl)
source = urllib.request.urlopen(theurl).read()
soup = bs.BeautifulSoup(source,'lxml')

# Read station data and generate csv file.

paragraph = soup.find('p')
s = paragraph.text
str1 = str(s)
str2 = str1[1:]
data = str2.split("|")

i=1
j=0
k=0
#for cell in data:
# Set up Excel format.
style_xls = xlwt.easyxf('font: colour black, bold False;')
# Write station data to Excel
data_len = len(data)
for i in range(1, data_len):
	for j in range(0, data_len):
		if data[j] != '\n':
			if data[j] != ',':
				sheet.write(i,k,data[j], style_xls)
				workbook.save("AM Frequency List" + ".xls")
				j=j+1
				k=k+1
			else:
				j=j+1
				k=k+1
		else:
			i=i+1
			k=0
	break



	

#	j = 0
#	for j in range(1, 18):
#		sheet.write(i,j, data[j], style_xls)

# Save station data in Excel
#	workbook.save("AM Frequency List" + ".xls")
#	print (str1)
#	i = i+1
#	break



#i=1
#for paragraph in soup.find_all('p'):
#	s = paragraph.text
#	str1 = str(s)
#	print (str1)
#	data = str1.split("|")
#	print (data)
# Write station data to Excel
#	style_xls = xlwt.easyxf('font: colour black, bold False;')
	
#	j = 0
#	for j in range(1, 18):
#		sheet.write(i,j, data[j], style_xls)

# Save station data in Excel
#	workbook.save("AM Frequency List" + ".xls")
#	print (str1)
#	i = i+1
#	break