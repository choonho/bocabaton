from pyengine.info import Info
from pyengine.lib.error import *

class ClusterInfo(Info):

    def __init__(self, vo, options):
        super(self.__class__, self).__init__(vo, options)
        self.fetchByID()

    def __repr__(self):
        return '<ClusterInfo: %s>' %self.vo.name 

    def fetchByID(self):
        """
        Fetch needed data from vo
        """
        if self.checkResponseParams():
            try:
                for p in self.options['res_params']:
                    self.output[p] = self.vo.__dict__[p]

            except:
                raise ERROR_INVALID_PARAMETER(key='res_params', value=p)

        else:
            self.output['name']     = self.vo.name
            self.output['cluster_id']     = self.vo.uuid
            self.output['created']  = self.vo.created
            self.output['status']   = self.vo.status
            self.output['zone_id']   = self.vo.zone_uuid
