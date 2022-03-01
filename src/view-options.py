#!/usr/bin/python3

import sys
import json 

if len(sys.argv) == 1:
	raise ValueError('Missing url argument')

PROJECT_URL = sys.argv[1].strip()

def row(title:str, path:str = '') -> dict:
	full_path = '%s%s' % (PROJECT_URL, path)
	return {
		'title': title,
		'subtitle': full_path,
		'path': full_path,
		'arg': full_path,
		'icon': {
			'path': '/Users/erstaples/Documents/gitlab-icon-1-color-white-rgb.png'
		}
	}

items = [
	row('Project'),
	row('Pipelines', '/-/pipelines'),
	row('Settings / General', '/edit'),
	row('Settings / CICD', '/-/settings/ci_cd'),
	row('Infrastructure / Terraform', '/-/terraform'),
	row('Infrastructure / Registry', '/-/infrastructure_registry'),
	row('Repository / Tags', '/-/tags')
]

print(json.dumps({'items': items}))