# Installing plugin:
# bin/plugin install elasticsearch/elasticsearch-cloud-aws/2.6.0

import json
from datetime import datetime
import elasticsearch
from elasticsearch import Elasticsearch
from elasticsearch.client import SnapshotClient

def timestamp():
	return datetime.strftime(datetime.now(), '%Y%m%d%H%M%S')

with open('config-private.json', 'rb') as f:
	config = json.load(f)

client = Elasticsearch([{'host' : config['ES_HOST'], 'port' : config['ES_PORT']}], timeout = 20)
sc     = SnapshotClient(client)

# Can do this repeatedly
# 
# sc.create_repository(config['REPO_NAME'], config['REPO_DEF'])

# Restrict to certain indices, if necessary
body = {}
if config['INDICES'] != '':
	body['indices'] = config['INDICES']

# Kick off backup creation
print 'starting backup...'
res = sc.create(
	repository          = config['REPO_NAME'], 
	snapshot            = config['CLUSTER_NAME'] + '_' + timestamp(), 
	body                = body,
	wait_for_completion = False
)