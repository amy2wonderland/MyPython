Python 2.7.8 (default, Jun 30 2014, 16:03:49) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import boto3
>>> s3=boto3.resource('s3')
>>> print s3
s3.ServiceResource()
>>> for bucket in s3.buckets.all():
	print bucket.name

	

Warning (from warnings module):
  File "C:\Python27\lib\site-packages\urllib3\util\ssl_.py", line 369
    SNIMissingWarning
SNIMissingWarning: An HTTPS request has been made, but the SNI (Server Name Indication) extension to TLS is not available on this platform. This may cause the server to present an incorrect TLS certificate, which can cause validation failures. You can upgrade to a newer version of Python to solve this. For more information, see https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings
ansible-citrix-automation
aws-athena-query-results-604349774081-ap-southeast-2
callumtest101
cf-templates-1bt6xvauamhq1-ap-southeast-2
chu-detailed-billing
cloud-data-solutions.access.logs
cloud-data-solutions.alb.logs
config-bucket-604349774081
connect-0055a0275859
connect-8c019d14bac0
ctdindsg
dsg-aws-msp
dsg-central-cloudtrail
dsg-citrix-pakage
dsg-client-logs-for-athena
dsg-cylance-linux
dsg-cylance-msi
dsg-data-lake
dsg-flowlogs
dsg-insight
dsg-managed-services-logs
dsg-ms-reporting
dsg-pipe-allied-mills-prod
dsg-pipe-allied-pinnacle-dev
dsg-pipe-allied-pinnacle-prod
dsg-pipe-helloworld-tourplan-prod
dsg-pipe-william-buck-prod
dsg-profileunity
dsg-puppet
dsg-test-vpc-s3-bucket
dsg-web-assets
dsgcloudforum.com
dsgtest0123
dsgtest01234
elasticbeanstalk-ap-southeast-2-604349774081
icarus-ams-bucket
icarus-cloud-bucket
insightbackup
liwei-firehorse-testing
matt-edb-transfer
me-chrome
old.collaborate.backup
www.dsgcloudforum.com
>>> 
