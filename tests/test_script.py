import os
import sys
import inspect

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir) 

import example_pf_config

staticmap_file = "../templates/staticmap.csv"
output_file = "test_out.xml"
configuration_file = "../examples/example_pf_config.xml"
target_lan_interface = 'lan'

add_static_map_to_file(configuration_file, staticmap_file, interface = target_lan_interface , output_file = output_file)