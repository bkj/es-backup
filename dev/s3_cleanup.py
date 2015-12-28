import datetime, json
from boto.s3.connection import S3Connection

with open('config.json', 'rb') as f:
	config = json.load(f)

STRF = '%Y-%m-%dT%H:%M:%S.000Z'
delete_before = datetime.datetime.now() - datetime.timedelta(days = N_DAYS)

con = S3Connection(
	config['REPO_DEF']['settings']['access_key'], 
	config['REPO_DEF']['settings']['secret_key']
)
bucket  = con.get_bucket(config['settings']['bucket'])
keys    = bucket.get_all_keys(delimiter = '/')

for k in keys:
	try:
		lm = datetime.datetime.strptime(k.last_modified, STRF)
		if lm < delete_before:
			print 'deleting'
			k.delete()
	except:
		print 'error @'
		print k
