Simple wrapper for elasticsearch-aws-cloud

- s3_backup (should work)
	
	creates of a backup of an index (possibly with a comma separated list of document types) and saves to specified bucket on s3

- s3_cleanup (totally untested)

    deletes backups that are more than a certain age (apparently this is a good thing to do, but I haven't tested.  If the backups are really saving diffs it seems like this might break them, so use with caution)


