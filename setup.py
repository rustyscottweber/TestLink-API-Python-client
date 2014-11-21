#! /usr/bin/python
# -*- coding: UTF-8 -*-

#  Copyright 2012-2014 Luiko Czub, TestLink-API-Python-client developers
#
#  Licensed under Apache 2.0 
#  

from os.path import join, dirname
from distutils.core import setup

with open(join(dirname(__file__), 'src', 'testlink', 'version.py')) as fpv:
    version_code = compile(fpv.read(), 'version.py', 'exec')
    exec(version_code)

CLASSIFIERS = [
  'Development Status :: 5 - Production/Stable',
  'License :: OSI Approved :: Apache Software License',
  'Operating System :: OS Independent',
  'Programming Language :: Python :: 2.6',
  'Programming Language :: Python :: 2.7',
  'Programming Language :: Python :: 3.4',
  'Topic :: Software Development :: Testing',
  'Topic :: Software Development :: Libraries :: Python Modules'
]

DESCRIPTION = """
TestLink-API-Python-client is a Python XML-RPC client for TestLink_.

Initially based on James Stock testlink-api-python-client R7 and  Olivier 
Renault JinFeng_ idea - an interaction of TestLink_, `Robot Framework`_ and Jenkins_.

TestLink-API-Python-client delivers two main classes

- TestlinkAPIGeneric - Implements the TestLink API methods as generic PY methods
  with error handling
- TestlinkAPIClient - Inherits from TestlinkAPIGeneric and defines service 
  methods like "copyTCnewVersion".

and the helper class

- TestLinkHelper - search connection parameter from environment variables and 
  command line arguments
  
How to talk with TestLink in a python shell and copy a test case: ::

 set TESTLINK_API_PYTHON_SERVER_URL=http://[YOURSERVER]/testlink/lib/api/xmlrpc/v1/xmlrpc.php
 set TESTLINK_API_PYTHON_DEVKEY=[Users devKey generated by TestLink]
 python
 >>> import testlink
 >>> tls = testlink.TestLinkHelper().connect(testlink.TestlinkAPIClient)
 >>> tls.countProjects()
 3
 >>> tc_info = tls.getTestCase(None, testcaseexternalid='NPROAPI-3')
 [{'full_tc_external_id': 'NPROAPI-3', ..., 'id': '5440',  'version': '2',  
   'testsuite_id': '5415', 'tc_external_id': '3','testcase_id': '5425', ...}]
 >>> tls.copyTCnewTestCase(tc_info[0]['testcase_id'], testsuiteid=newSuiteID, 
                                          testcasename='a new test case name')
 >>> print tls.whatArgs('createTestPlan')
 createTestPlan(<testplanname>, <testprojectname>, [note=<note>], [active=<active>], 
                [public=<public>], [devKey=<devKey>])
   create a test plan 

More information about this library can be found on the Wiki_ 

.. _TestLink: http://testlink.org
.. _JinFeng: http://www.sqaopen.net/blog/en/?p=63
.. _Robot Framework: http://code.google.com/p/robotframework
.. _Jenkins: http://jenkins-ci.org
.. _Wiki: https://github.com/lczub/TestLink-API-Python-client/wiki

"""[1:-1]

setup(name='TestLink-API-Python-client',
      version=VERSION,
      description='Python XML-RPC client for TestLink %s' % TL_RELEASE,
      long_description = DESCRIPTION,
      author='James Stock, Olivier Renault, Luiko Czub, TestLink-API-Python-client developers',
      author_email='orenault@gmail.com, Luiko.Czub@Liegkat-Archiv.de',
      url='https://github.com/lczub/TestLink-API-Python-client',
      license      = 'Apache 2.0',
      package_dir  = {'': 'src'},
      packages     = ['testlink'],
      classifiers  = CLASSIFIERS,
      platforms    = 'any',
      keywords     = ['testing', 'testlink', 'xml-rpc', 'testautomation']
      
     )

