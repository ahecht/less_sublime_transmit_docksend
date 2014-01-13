import sublime, sublime_plugin, subprocess
import re

class LessTransmitDocksendCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    my_file = self.view.file_name()
    is_less = re.search('\.less$',my_file)
    if is_less:
      file_to_upload = re.sub(r'/less/(.*?)\.less$', r'/css/\1.css', my_file)
    else:
      file_to_upload = my_file
    
    args = ['osascript']
    args.extend(['-e', 'tell app "Transmit" to open POSIX file "' + file_to_upload + '"'])
    subprocess.Popen(args)

