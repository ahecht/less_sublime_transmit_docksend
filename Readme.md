# LESS Sublime Transmit DockSend

A [Sublime Text](http://www.sublimetext.com/3) plugin for OS X that uploads the current open file with [Transmit](http://www.panic.com/transmit/). If triggered on a LESS file, it will upload a CSS file at a parallel path instead.

## Installation

Clone this repository into a "Less Transmit Docksend" folder in the ST3 Packages directory.

  git clone git://github.com/ahecht/less_sublime_transmit_docksend.git ~/Library/Application\ Support/Sublime\ Text\ 3/Packages/Less\ Transmit\ Docksend

## Usage

Use `command+shift+u` or invoke `Less Transmit DockSend` in the Command Pallete to upload the current open file. 

If the file doesn't have a .less extension, it's sent to Transmit as is. If it does, it will send the .css file at the parallel path.

## Example
If you're file is at /Users/johnnychimpo/my_site/less/styles.less, it will send /Users/johnnychimpo/my_site/css/styles.css to Transmit instead of the active file.

## License

  Copyright (c) 2014 Anthony Hecht

  Permission is hereby granted, free of charge, to any person obtaining a copy
  of this software and associated documentation files (the "Software"), to deal
  in the Software without restriction, including without limitation the rights
  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
  copies of the Software, and to permit persons to whom the Software is
  furnished to do so, subject to the following conditions:

  The above copyright notice and this permission notice shall be included in
  all copies or substantial portions of the Software.

  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
  THE SOFTWARE.
