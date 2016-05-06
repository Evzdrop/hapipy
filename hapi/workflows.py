import urllib

from base import BaseClient
import logging_helper

WORKFLOWS_API_VERSION = '3'

class WorkflowsClient(BaseClient):
    """
    The hapipy Leads client uses the _make_request method to call the API for data.  It returns a python object translated from the json return
    """

    def __init__(self, *args, **kwargs):
        super(WorkflowsClient, self).__init__(*args, **kwargs)
        self.log = logging_helper.get_log('hapi.workflows')

    def _get_path(self, subpath, version=WORKFLOWS_API_VERSION):
        print self.options
        return 'automation/v%s/workflows/%s' % (self.options.get('version') or version, subpath)
  
    def get_workflow(self, id, **options):
        return self._call(id, **options)

    def get_workflows(self, **options):
        workflows = self._call('', **options)
        self.log.info("retrieved %s workflows through API ( options=%s )" % 
                (len(workflows), options))
        return workflows

    def enroll_contact(self, workflow_id, contact_email, **options):
        params = {}
        self._prepare_request_auth('', params, None, None)
        enroll_path = '/' + self._get_path("%s/enrollments/contacts/%s?%s" % (workflow_id, contact_email, urllib.urlencode(params)), version=2)
        return self._call('', url=enroll_path, method='POST', **options)

    def unenroll_contact(self, workflow_id, contact_email, **options):
        params = {}
        self._prepare_request_auth('', params, None, None)
        unenroll_path = '/' + self._get_path("%s/enrollments/contacts/%s?%s" % (workflow_id, contact_email, urllib.urlencode(params)), version=2)
        return self._call('', url=enroll_path, method='DELETE', **options)
