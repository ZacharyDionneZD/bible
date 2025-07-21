import re
import os
import file_helper
import book_helper
from string import Template

def get_chapiter_name(line):
	match = re.match("^\\t\\t<h1>(.*)</h1>$", line)

	return match.group(1)

def get_chapiter_number(chapiter_name):
	match = re.match(".+ ([0-9]+)", chapiter_name)

	return match.group(1)

def get_chapiter_lines(lines, line):
	chapiter_lines = []

	line_reached = False

	for current_line in lines:
		if line_reached:

			if book_helper.is_new_chapiter_line(current_line):
				break
			else:
				chapiter_lines.append(current_line)
		else:
			if current_line == line:
				line_reached = True

				chapiter_lines.append(line)

	chapiter_lines[-1] = chapiter_lines[-1].replace("\n", "")

	return chapiter_lines

def generate(book_path, output_path_template):
	template = Template("""<!DOCTYPE html>
<html lang="fr">
	<head>
		<meta charset="UTF-8">
		<meta name="viewport" content="width=device-width, initial-scale=1.0">
		<title>$chapiter_name</title>
		<link rel="stylesheet" href="/bible.css">
		<link rel="icon" type="image/png" href="/favicon.png">
	</head>
	<body>
$content
	</body>
</html>""")

	lines = file_helper.read_lines(book_path)

	for line in lines:
		if book_helper.is_new_chapiter_line(line):
			chapiter_name = get_chapiter_name(line)
			chapiter_number = get_chapiter_number(chapiter_name)
			output_path = output_path_template.safe_substitute(chapiter_number=chapiter_number)
			chapiter_lines = get_chapiter_lines(lines, line)
			chapiter_text = "".join(chapiter_lines)
			output_content = template.safe_substitute(chapiter_name=chapiter_name, content=chapiter_text)

			file_helper.write_text_to_file(output_path, output_content)