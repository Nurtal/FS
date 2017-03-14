


def write_summary():
	"""
	write html page
	summary report on
	features extraction
	"""

	panels_list = ["1", "2", "3", "4", "5", "6"]

	summary_file = open("summary.html", "w")

	# Write header
	summary_file.write("<html>\n")
	summary_file.write("<head>\n")
	summary_file.write("<title>Features Extractions</title>\n")
	summary_file.write("<link rel=\"stylesheet\" type=\"text/css\" href=\"style.css\">\n")
	summary_file.write("</head>\n")

	# Write body
	summary_file.write("<body>\n")
	summary_file.write("<center>\n")

	summary_file.write("<h1>Features Extraction<h1>\n")

	for panel in panels_list:
		summary_file.write("\t<h2>Panel "+str(panel)+"<h2>\n")
		summary_file.write("\t<img src=\"images/feature_selection_panel_"+str(panel)+".png\" alt=\"stuff\" style=\"width:600px;height:450px;\">\n")

		data_filename = "data/feature_selection_panel_"+str(panel)+".txt"
		data = open(data_filename, "r")
		summary_file.write("\t\t<table>\n")

		cmpt_line = 0
		for line in data:
			line = line.split("\n")
			line = line[0]
			line_array = line.split(";")

			color = "#FFFFFF"
			if(line_array[-1] == "\"Confirmed\""):
				color = "#31B404"
			else:
				color = "#B40404"

			if(cmpt_line == 0):
				line_array = ["Variables", "meanImp", "medianImp", "minImp", "maxImp", "normHits", "Decision"]
				color = "#FFFFFF"

			summary_file.write("\t\t\t<tr bgcolor=\""+color+"\">\n")
			for element in line_array:
				element = element.replace("\"", "")
				summary_file.write("\t\t\t\t<th>"+str(element)+"</th>\n")
			summary_file.write("\t\t\t</tr>\n")

			cmpt_line += 1

		summary_file.write("\t\t</table>\n")
		data.close()


	summary_file.write("</center>\n")
	summary_file.write("</body>\n")


	# Write footer
	summary_file.write("</html>\n")
	

	summary_file.close()


def reformat_table():
	"""
	"""
	panels_list = ["1", "2", "3", "4", "5", "6"]

	for panel in panels_list:
		
		file_name = "panel_"+str(panel)+"_filtered.txt"
		file_name_new = "panel_"+str(panel)+"_filtered_processed.txt"

		file_data = open(file_name, "r")
		file_data_new = open(file_name_new, "w")

		cmpt_line = 0
		for line in file_data:
			line = line.split("\n")
			line = line[0]
			line_array = line.split(";")

			line_new = ""

			cmpt_index = 0
			for element in line_array:
				element = element.replace("\"", "")
				element = element.replace("\t", "")
				element = element.replace(" ", "")

				if(cmpt_index > 0 and cmpt_line > 0):
					line_new += str(element)+";"
				elif(cmpt_line == 0):
					line_new += str(element)+";"

				cmpt_index += 1

			line_new = line_new[:-1]

			file_data_new.write(line_new+"\n")

			cmpt_line += 1


		file_data_new.close()
		file_data.close()



### TEST SPACE###
#write_summary()
reformat_table()




