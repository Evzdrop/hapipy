import urllib

from base import BaseClient
import logging_helper

WORKFLOWS_API_VERSION = '3'
ENROLLMENT_API_VERSION = '2'

class WorkflowsClient(BaseClient):
    """
    The hapipy Leads client uses the _make_request method to call the API for data.  It returns a python object translated from the json return
    """

    def __init__(self, *args, **kwargs):
        super(WorkflowsClient, self).__init__(*args, **kwargs)
        self.log = logging_helper.get_log('hapi.workflows')

    def _get_path(self, subpath):
        version = WORKFLOWS_API_VERSION
        if subpath.find('enrollments') != -1:
            version = ENROLLMENT_API_VERSION
        return '/automation/v%s/workflows/%s' % (version, subpath)
  
    def get_workflow(self, id, **options):
        return self._call(id, **options)

    def get_workflows(self, **options):
        workflows = self._call('', **options)
        self.log.info("retrieved %s workflows through API ( options=%s )" % 
                (len(workflows), options))
        return workflows

    def enroll_contact(self, workflow_id, contact_email, **options):
        subpath = "%s/enrollments/contacts/%s" % (workflow_id, contact_email)
        return self._call(subpath, method='POST', **options)

    def unenroll_contact(self, workflow_id, contact_email, **options):
        subpath = "%s/enrollments/contacts/%s" % (workflow_id, contact_email)
        return self._call(subpath, method='DELETE', **options)
