""" It is possible to access gzip file and read its content

"""
import gzip
import os
import logging

log = logging.getLogger('Open gzip')

log.info('Open gzip started')

for dirname, dirnames, filenames in os.walk('gzip_test_files'):
	for file_name in filenames:
		print dirname, file_name, '\n'
		if os.path.splitext(file_name)[1] == '.gz':
			f = gzip.open(os.path.join(dirname, file_name), 'r')
			for line in f:
				print line
			f.close()
		else:
			print 'Not a gzip file {}'.format(file_name)
			log.info('Not a gzip file {}'.format(file_name))

log.info('Open gzip ended')