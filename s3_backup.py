# Installing plugin:
# bin/plugin install elasticsearch/elasticsearch-cloud-aws/2.6.0

import argparse
import json
from datetime import datetime
import elasticsearch
from elasticsearch import Elasticsearch
from elasticsearch.client import SnapshotClient

# --
# CLI

parser = argparse.ArgumentParser()
parser.add_argument('--create', dest = 'create', action="store_true")
args = parser.parse_args()

# --

def timestamp():
	return datetime.strftime(datetime.now(), '%Y%m%d%H%M%S')

# --
# Config

config         = json.load(open('config.json'))
config_private = json.load(open('config-private.json'))

config['REPO_DEF']['settings']['access_key'] = config_private['access_key']
config['REPO_DEF']['settings']['secret_key'] = config_private['secret_key']

# --
# Run

client = Elasticsearch([{'host' : config['ES_HOST'], 'port' : config['ES_PORT']}], timeout = 20)
sc     = SnapshotClient(client)

if args.create:
    sc.create_repository(config['REPO_NAME'], config['REPO_DEF'])

body = {}
if config['INDICES'] != '':
	body['indices'] = config['INDICES']


print 'starting backup...'
res = sc.create(
	repository          = config['REPO_NAME'], 
	snapshot            = config['CLUSTER_NAME'] + '_' + timestamp(), 
	body                = body,
	wait_for_completion = False
)