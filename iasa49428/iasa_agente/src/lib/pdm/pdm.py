from pdm.mec_util import MecUtil


class PDM():

    def __init__(self, modelo, gama, delta_max):
        self.mec_util = MecUtil(modelo, gama, delta_max)
        raise NotImplementedError("Not implemented yet")
    
    def politica(self, U):
        raise NotImplementedError("Not implemented yet")
    
    def resolver(self):
        raise NotImplementedError("Not implemented yet")
    


