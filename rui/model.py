from turbogears.database import PackageHub
from sqlobject import *

hub = PackageHub('rui')
__connection__ = hub

# class YourDataClass(SQLObject):
#     pass
 
