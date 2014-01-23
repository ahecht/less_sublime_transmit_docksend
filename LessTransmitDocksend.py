import sublime, sublime_plugin, subprocess
import re

class LessTransmitDocksendCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    # get settings and the file we're dealing with
    settings = sublime.load_settings('LessTransmitDocksend.sublime-settings')
    my_file = self.view.file_name()

    if settings.get("disabled"):
      # just send the file
      self.send_to_transmit(my_file)
    
    else:
      is_less = re.search('\.less$',my_file)
      
      if is_less:
        # if set to send both, send the original
        if settings.get("send_both"):
          self.send_to_transmit(my_file)

        # modify the path according to default or custom path regex
        original_path = settings.get("original_path") if settings.get("original_path") else '/less/(.*?)\\.less$'
        upload_path = settings.get("upload_path") if settings.get("upload_path") else '/css/\\1.css'

        file_to_upload = re.sub(r''+original_path+'', r''+upload_path+'', my_file)

      else:
        # not a LESS file, send the original file
        file_to_upload = my_file

      # send the file
      self.send_to_transmit(file_to_upload)


  def send_to_transmit(self, file):
    print('sending '+file)
    args = ['osascript']
    args.extend(['-e', 'tell app "Transmit" to open POSIX file "' + file + '"'])
    subprocess.Popen(args)