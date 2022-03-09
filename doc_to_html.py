import importlib
import sys
from inspect import *

#python doc_to_html.py mymodule.py mydoc.html

def q1(module_name, html_name):
    out_file = open(html_name, 'w')
    module = importlib.import_module(module_name.replace('.py', ''))
    html_content = f'<html>'
    html_content += f'<head><h1>{"Homeworkmodule:"}{module.__doc__}</h1><br> </head>'
  #  html_content += 
    for func in getmembers(module, isfunction):
       
        html_content += f'<h2>{"name:"}{module.__getattribute__(func[0]).__name__}</h2>'
        html_content += f'<h3>{"documentation:"}{module.__getattribute__(func[0]).__doc__}</h3>'
      #  html_content += f'<p>{"arguments:"}{module.__getattribute__(func[0]).__annotations__}</p>'
        html_content += f'<p>{"annotations:"}{module.__getattribute__(func[0]).__annotations__}</p>'
        
        html_content += '<br>'
    html_content += '</body>'
    html_content += '</html>'
        
 
    
    out_file.write(html_content)
    out_file.close()
    

args = sys.argv[1:]
q1(args[0],args[1])