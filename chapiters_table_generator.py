import re
import os
import file_helper
import book_helper
from string import Template

def get_chapiters_count(lines):
	chapiters_count = 0

	for line in lines:
		if book_helper.is_new_chapiter_line(line):
			chapiters_count += 1

	return chapiters_count

def get_li_tags(chapiters_count):
	li_tags = []

	for chapiter_number in range(1, chapiters_count + 1):
		chapiter_number_text = str(chapiter_number)

		li_tags.append("\t\t\t<li><a href=\"./" + chapiter_number_text + "/\">" + chapiter_number_text +"</a></li>")

	return li_tags

def generate(book_path, book_name, output_path):
	template = Template("""<!DOCTYPE html>
<html lang="fr">
	<head>
		<meta charset="UTF-8">
		<meta name="viewport" content="width=device-width, initial-scale=1.0">
		<title>$book_name</title>
		<link rel="stylesheet" href="/bible.css">
		<link rel="icon" type="image/png" href="/favicon.png">
	</head>
	<body>
		<h1>$book_name</h1>
		<h2>Chapitres</h2>
		<ul>
$content
		</ul>
	</body>
</html>""")

	lines = file_helper.read_lines(book_path)
	chapiters_count = get_chapiters_count(lines)
	li_tags = get_li_tags(chapiters_count)
	content = "\n".join(li_tags)
	output_content = template.safe_substitute(book_name=book_name, content=content)

	file_helper.write_text_to_file(output_path, output_content)