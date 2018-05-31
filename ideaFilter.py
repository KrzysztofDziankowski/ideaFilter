#!/usr/bin/env python3


def parseArguments():
	import argparse
	parser = argparse.ArgumentParser(
description='''Idea filter is a utility tool.
 It is used for filtering out ideas/notes/data gathrered in YAML file.
 Any "schema" can be used in YAML file.
 Filtered out ideas are printed out in nice format based on template file.
''')
	parser.add_argument('-v', '--verbose', action="store_true",
		 help="Increase output verbosity")
	parser.add_argument('-i', '--input', dest='inputFile', required=True,
		 help='Input YAML file.')
	parser.add_argument('-o', '--output', dest='outputFile',
		 help='Output file.')
	parser.add_argument('-q', '--query', default='$',
		 help='Query applied on input file.')
	parser.add_argument('-t', '--template', dest='templateFile',
		 help='Template jinja2 file based on which will be generated output.')
	return parser.parse_args()

def parseYaml(inputFile, query):
	import yaql
	import yaml
	with open(inputFile,'r') as yaml_file:
		data_source = yaml.load(yaml_file)
		engine = yaql.factory.YaqlFactory().create()
		expression = engine(query)
		return expression.evaluate(data=data_source)

def fillTemplate(templateFile, data):
	from jinja2 import Environment, FileSystemLoader, select_autoescape
	env = Environment(
		loader=FileSystemLoader('.'),
		autoescape=select_autoescape(['html', 'xml'])
	)
	template = env.get_template(templateFile)
	return template.render(data=data)

def saveToFile(outputFile, text):
	with open(outputFile, 'w') as output:
		output.write(text)

args = parseArguments()
if args.verbose:
	print("args: ", args)

parsed_data = parseYaml(args.inputFile, args.query)
if args.verbose:
	print("parsed_data: ", parsed_data)

if args.templateFile:
	outputText = fillTemplate(args.templateFile, parsed_data)
else:
	outputText = str(parsed_data)

if args.outputFile:
	saveToFile(args.outputFile, outputText)
else:
	print(outputText)

