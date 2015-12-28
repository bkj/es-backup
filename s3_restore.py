
import argparse
import json
from elasticsearch import Elasticsearch
from elasticsearch.client import SnapshotClient

# --
# CLI

parser = argparse.ArgumentParser()
parser.add_argument('--indices',  dest = 'indices', action = 'store', required = True)
parser.add_argument('--snapshot', dest = 'snapshot', action = 'store', required = True)
args = parser.parse_args()

# --
# Config

config         = json.load(open('config.json'))
config_private = json.load(open('config-private.json'))

# --
# Run

client = Elasticsearch([{'host' : config['ES_HOST'], 'port' : config['ES_PORT']}], timeout = 20)
sc     = SnapshotClient(client)

sc.restore(
    repository          = config['REPO_NAME'],
    snapshot            = args.snapshot,
    body                = {"indices" : args.indices},
    wait_for_completion = False    
)