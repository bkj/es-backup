# ES-Backup

## Setup


#### Install `cloud-aws` plugin

In Elasticsearch 1.X:

       bin/plugin install elasticsearch/elasticsearch-cloud-aws/2.6.0

In Elasticsearch 2.X:

       sudo bin/plugin install cloud-aws

#### Set up `config-private.json`

Needs to look like

    {
        "secret_key" : "aws private key",
        "access_key" : "aws access key"
    }

#### Set up `config.json`

Make the appropriate changes, i.e. point at S3, point at Elasticsearch, whitelist indices, etc.


## Use

`s3_backup`

        # 1st time   (create snapshot in ES)
        python s3_backup.py --create

        # > 1st time (use existing snapshot in ES) 
        python s3_backup.py

`s3_restore` - Restore from previous backup in `config['REPO_NAME']`

        python s3_restore.py --indices=index1,index2 --snapshot=snapshot_name

`dev` - ignore for now