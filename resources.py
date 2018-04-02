AWSPDF_RESOURCES = {
    'ec2': 'http://awsdocs.s3.amazonaws.com/EC2/2016-09-15/ec2-api-2016-09-15.pdf',
    'elb': 'https://docs.aws.amazon.com/elasticloadbalancing/2012-06-01/APIReference/elb-api.pdf',
    'iam': 'https://docs.aws.amazon.com/IAM/latest/APIReference/iam-api.pdf',
    'dircon': 'https://docs.aws.amazon.com/directconnect/latest/APIReference/dc-api.pdf',
    }

OSCDOC_RESOURCES = {
    'ec2': 'http://docs.outscale.com/api_fcu/index.html',
    'elb': 'http://docs.outscale.com/api_lbu/index.html',
    'iam': 'http://docs.outscale.com/api_eim/index.html',
    'dircon': 'http://docs.outscale.com/api_directlink/index.html'
    }

OSCWIKI_RESOURCES = {key : 'https://wiki.outscale.net/display/DOCU/AWS+Compatibility+Matrix' 
                     for key in OSCDOC_RESOURCES.keys()}

SAVE_TO = '/tmp/compatibility_matrix.xlsx'
