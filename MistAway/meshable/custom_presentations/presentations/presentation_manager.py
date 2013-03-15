############################################################################
#                                                                          #
# Copyright (c)2008, 2009, Digi International (Digi). All Rights Reserved. #
#                                                                          #
# Permission to use, copy, modify, and distribute this software and its    #
# documentation, without fee and without a signed licensing agreement, is  #
# hereby granted, provided that the software is used on Digi products only #
# and that the software contain this copyright notice,  and the following  #
# two paragraphs appear in all copies, modifications, and distributions as #
# well. Contact Product Management, Digi International, Inc., 11001 Bren   #
# Road East, Minnetonka, MN, +1 952-912-3444, for commercial licensing     #
# opportunities for non-Digi products.                                     #
#                                                                          #
# DIGI SPECIFICALLY DISCLAIMS ANY WARRANTIES, INCLUDING, BUT NOT LIMITED   #
# TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A          #
# PARTICULAR PURPOSE. THE SOFTWARE AND ACCOMPANYING DOCUMENTATION, IF ANY, #
# PROVIDED HEREUNDER IS PROVIDED "AS IS" AND WITHOUT WARRANTY OF ANY KIND. #
# DIGI HAS NO OBLIGATION TO PROVIDE MAINTENANCE, SUPPORT, UPDATES,         #
# ENHANCEMENTS, OR MODIFICATIONS.                                          #
#                                                                          #
# IN NO EVENT SHALL DIGI BE LIABLE TO ANY PARTY FOR DIRECT, INDIRECT,      #
# SPECIAL, INCIDENTAL, OR CONSEQUENTIAL DAMAGES, INCLUDING LOST PROFITS,   #
# ARISING OUT OF THE USE OF THIS SOFTWARE AND ITS DOCUMENTATION, EVEN IF   #
# DIGI HAS BEEN ADVISED OF THE POSSIBILITY OF SUCH DAMAGES.                #
#                                                                          #
############################################################################

"""\
Manages the loading and instances of individual presentations.

The PresentationManager allows for the dynamic loading of presentation
drivers as well as the ability to retrieve an instance of a presentation
by name.

The PresentationManager also provides an interface to start and stop
an instance as well as to query the instance for its configuration
parameters.
"""

# imports
from common.classloader import classloader
from settings.settings_base import SettingsBase, Setting
from copy import copy
from common.abstract_service_manager import AbstractServiceManager

# constants

# exception classes

# interface functions

# classes

class PresentationManager(AbstractServiceManager, SettingsBase):
    def __init__(self, core_services):
        self.__core = core_services
        self.__core.set_service("presentation_manager", self)

        # Initialize our base class:
        AbstractServiceManager.__init__(self, core_services, ('presentations',))

    def driver_load(self, name):
        """\
        Loads a presentation driver class dynamically.

        If the driver has not been loaded previously, an unconfigured
        instance of the driver will be created and managed by the
        PresentationManager.  If the driver has already been loaded
        nothing will be done.  In either case, this function will
        return True.

        If the presentation driver cannot be loaded for any reason, an
        exception will be raised.
        """
	return AbstractServiceManager.service_load(self, name)

    def _instance_exists(self, instancename):
	return AbstractServiceManager._instance_exists(self, instancename)

    def instance_get(self, instancename):
        """Internal method to find a given driver instance."""
	return AbstractServiceManager.instance_get(self, instancename)

    def instance_new(self, classname, instancename):
        """Create a new instance of a loaded driver class."""
	return AbstractServiceManager.instance_new(self,
                                        classname, instancename)

    def instance_list(self):
	return AbstractServiceManager.instance_list(self)

    def instance_settings_get(self, instancename):
        """Get the settings of a given class instance."""
        return AbstractServiceManager.instance_settings_get(self, instancename)

    def instance_setting_set(self, instancename, settingname, settingvalue):
        """\
            Set a setting on a given instance name, the setting will go
            into the instance's pending settings registry.
        """
	return AbstractServiceManager.instance_setting_set(self,
                                        instancename,
                                        settingname,
                                        settingvalue)

    def instance_settings_apply(self, instancename):
        """Apply all pending settings on a given instance."""
	return AbstractServiceManager.instance_settings_apply(self,
                                        instancename)
    
    def instance_start(self, instancename):
	return AbstractServiceManager.instance_start(self, instancename)

    def instance_stop(self, instancename):
	return AbstractServiceManager.instance_stop(self, instancename)

# internal functions & classes

def main():
    pass

if __name__ == '__main__':
    import sys
    status = main()
    sys.exit(status)

