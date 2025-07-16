import os

def write_text_to_file(output_path, output_content):
	os.makedirs(os.path.dirname(output_path), exist_ok=True)

	with open(output_path, "w", encoding="utf-8") as output_file:
		output_file.write(output_content)

def read_lines(file_path):
	lines = None

	with open(file_path, "r", encoding="utf-8") as file:
		lines = file.readlines()

	return lines
