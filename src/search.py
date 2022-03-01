#!/usr/bin/python3

import os
import gitlab
import sys
import json 

if len(sys.argv) == 1:
	raise ValueError('Missing search keyword')

keyword = sys.argv[1].strip()

if len(keyword) == 0:
	raise ValueError('Keyword must not be an empty string')

private_token = os.environ.get('GITLAB_ACCESS_TOKEN')

if private_token is None or len(private_token) == 0:
	raise EnvironmentError('Missing GITLAB_ACCESS_TOKEN environment variable')

gl = gitlab.Gitlab('https://gitlab.com/', private_token=private_token)
results = gl.projects.list(search=keyword, owned=True, visibility='private')

items = []
for project in results:
	items.append({
		'title': project.name,
		'subtitle': project.name_with_namespace,
		'arg': project.web_url,
		'icon': {
			'path': '/Users/erstaples/Documents/gitlab-icon-1-color-white-rgb.png'
        }
	})

def key(e):
	return e['subtitle']

items.sort(key=key)

print(json.dumps({'items': items}))