import json
import argparse
from datetime import datetime
from elasticsearch import Elasticsearch
from elasticsearch.client import SnapshotClient

# --
# CLI

parser = argparse.ArgumentParser()
parser.add_argument('--create', action="store_true")
parser.add_argument('--no-snapshot', action="store_true")
args = parser.parse_args()

# --
# Config

config         = json.load(open('config.json'))
config_private = json.load(open('config-private.json'))

config['REPO_DEF']['settings']['access_key'] = config_private['access_key']
config['REPO_DEF']['settings']['secret_key'] = config_private['secret_key']

# --
# Run

client = Elasticsearch([{'host' : config['ES_HOST'], 'port' : config['ES_PORT']}], timeout = 30)
sc     = SnapshotClient(client)

if args.create:
    print "creating repo: %s" % config['REPO_NAME'] 
    sc.create_repository(config['REPO_NAME'], config['REPO_DEF'])
    
body = {}
if config['INDICES'] != '':
	body['indices'] = config['INDICES']

if not args.no_snapshot:
    snapshot_name = config['CLUSTER_NAME'] + '_' + datetime.strftime(datetime.now(), '%Y%m%d%H%M%S'),
    print "creating snapshot : %s" % snapshot_name
    res = sc.create(
    	repository          = config['REPO_NAME'], 
    	snapshot            = snapshot_name, 
    	body                = body,
    	wait_for_completion = False
    )
else:
    print "skipping snapshot"
