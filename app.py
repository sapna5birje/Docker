import sys
def handler(event, context):
    return 'Hello from AWS Lambda using Python' + sys.version + '!'        
def printing():
	for i in range(10):
		print("hello")
printing()
