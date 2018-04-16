import arcpy
import pythonaddins

class extDDP(object):
    """Implementation for ddp_assistant_addin.ddp_extension (Extension)"""
    def __init__(self):
        # For performance considerations, please remove all unused methods in this class.
        self.enabled = True
    def pageIndexExtentChanged(self, new_id):
        pass