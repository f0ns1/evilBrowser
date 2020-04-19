from gi.repository import Gtk as gtk
from gi.repository import Gdk as gdk
import sys
import subprocess

import os




class MyWindow(gtk.ApplicationWindow):

    def __init__(self, app):
        
        gtk.Window.__init__(
        self, title="<script> Evil Terminal!</script>:", application=app)
        self.set_default_size(900, 600)
   
        self.scrolled_window = gtk.ScrolledWindow()
        self.scrolled_window.set_border_width(10)
        self.scrolled_window.set_resize_mode(True)
        self.scrolled_window.set_policy(gtk.PolicyType.ALWAYS, gtk.PolicyType.ALWAYS)
        self.virtual_path=os.path.dirname(sys.argv[0])
        path="pwd"
        self.virtual_path=self.execute(path.split())
        self.vbox = gtk.VBox(spacing=50)
        self.hbox_1 = gtk.HBox(spacing=50)
        self.entry = gtk.TextView()
        self.textbuffer = self.entry.get_buffer()
        self.textbuffer.set_text(self.getPromp())
        #self.entry.set_data(out) 
        self.hbox_1.pack_start(self.entry,expand=True,fill=True,padding=10)
        self.vbox.pack_start(self.hbox_1,expand=True,fill=True,padding=10)
        self.scrolled_window.add(self.vbox)
        self.add(self.scrolled_window)
        self.connect_signals()
        #set css
        self.css = b"""* { background-image: url('background.jpg'); color: white; font-size: large; font-weight: bold;}"""
        css_provider = gtk.CssProvider()
        css_provider.load_from_data(self.css)
        context = gtk.StyleContext()
        screen = gdk.Screen.get_default()
        context.add_provider_for_screen(screen, css_provider, gtk.STYLE_PROVIDER_PRIORITY_APPLICATION)
        #scrolling
        
        self.buffer=""
        self.scrolled_window.connect('size-allocate', self.treeview_changed)
    
    
    def treeview_changed(self, widget, event, data=None):
        adj = self.scrolled_window.get_vadjustment()
        adj.set_value( len(self.buffer)+2)
        
    def getPromp(self):
        user=str(self.getUser()).replace('\'','').replace('\\n','').replace('b','')
        path=str(self.getPath()).replace('\'','').replace('\\n','').replace('b','')
        return "\n "+user+"##"+path+"@:"
    def getUser(self):
        execData ="whoami"
        return self.execute(execData.split())
    def getPath(self):
        execData="pwd"
        return self.execute(execData.split())
    def execute(self,data):
        execData=""
        count=0
        for i in data:
            if ( count+1 < len(data)) :
                execData+=i+" "
            else:
                execData+=i 
            count +=1
        
        print("data to execute : ",execData)
       
        try:
        #ps = subprocess.Popen(('', cwd='C:/myproject/betty/'), stdout=subprocess.PIPE)
            out= subprocess.check_output(execData, cwd=(self.virtual_path.replace('\'','').replace('b','',1).replace("\\n",'')))
        #ps.wait()
        except Exception as e:
            print("Exec : ",e)
        print("path: ",self.virtual_path.replace('\'','').replace('b','',1).replace("\\n",''))
        print("output: ",str(out).replace('\'','').replace('b','',1).replace("\\n",''))
        return str(out).replace('\'','').replace('b','',1).replace("\\n",'')
    
    def connect_signals(self):
        #self.button_ok.connect("clicked", self.callback_ok)
        self.entry.connect("key-press-event",self.on_key_press_event)

    def on_key_press_event(self,widget, event):
        # see if we recognise a keypress
        if event.keyval == gdk.KEY_Return:
            print("Key press on widget: ", widget)
            print("          Modifiers: ", event.state)
            print("      Key val, name: ", event.keyval, gdk.keyval_name(event.keyval))
            print ("return .... TYpe : ")
            self.callback_ok(widget, None)
            

    def callback_ok(self, widget, callback_data=None):
        self.entry.reset_cursor_blink()
        self.entry.set_cursor_visible(False)
        self.name= self.entry.get_buffer()
        print(self.name)
        start_iter = self.name.get_start_iter()
        print(start_iter)
        end_iter = self.name.get_end_iter()
        print(end_iter)
        text = self.name.get_text(start_iter, end_iter, True) 
        for arg in text.split("@:"):
            last=arg
        print("Data::::::::::::::::::::::::::::",last)
        print("End Data::::::::::::::::::::::::::::")
        strOutput=text
        if (not "cd " in last ):
            try:
                
                #output = self.execute(last.split())
                print("Exec : "+last)
                try:
                    execData = last.split()
                    out= subprocess.check_output(execData, cwd=(self.virtual_path.replace('\'','').replace('b','',1).replace("\\n",'')))
                except Exception as e:
                    print(e)
                
                print ("Execute user: ",out)
                #out =str(output).replace('\'b','').replace('\'','')
                self.textbuffer = self.entry.get_buffer()
                strOutput=text
                print ("Execute user: ",out)
                for i in str(out).split("\\n"):
                    strOutput+=("\n"+str(i).replace('b','',1).replace('\'',''))
                print("output: ",strOutput) 
            except Exception as e:
                print("Exec exception ",e)
                pass
        else:
            self.virtual_path=last.split()[1]
        
        strOutput+="\n"+self.getPromp()
        self.buffer=strOutput
        self.textbuffer.set_text(strOutput)
        self.entry.set_cursor_visible(True)
    
        
        
    
 
         
class Terminal(gtk.Application):
      
    def __init__(self):
        gtk.Application.__init__(self)

    def do_activate(self):
        win = MyWindow(self)
        win.show_all()

    def do_startup(self):
        gtk.Application.do_startup(self)


app = Terminal()
#exit_status = app.run(sys.argv)
#sys.exit(exit_status)