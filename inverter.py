#!/usr/bin/env python
#-*- coding: utf-8 -*-

""" Programa criado como exemplo por Rafael Santos
    contato rafael@sourcecode.net.br
    mais informações em http://sourcecode.net.br """

import pygtk
pygtk.require("2.0")
import gtk


class InverterApp(object):
    def __init__(self):
        builder = gtk.Builder()
        builder.add_from_file("inverter.glade")
        self.window = builder.get_object("window1")
        self.text_area = builder.get_object("text_entry")
        self.about = builder.get_object("about_dialog")
        self.window.show()
        builder.connect_signals({"gtk_main_quit": gtk.main_quit,
                            "on_button_invert_clicked": self.invert_url,
                            "on_text_entry_activate": self.invert_url,
                            "on_copy_activate": self.copy_text,
                            "on_paste_activate": self.paste_text,
                            "on_delete_activate": self.delete_text,
                            "on_about_activate": self.about_window,
                                })
                            
    def invert_url(self, widget):
        """Função Principal do programa, irá armazenar a URL que o usuário
        digitar na área de texto e inverte-la"""
        url = self.text_area.get_text()
        url = url[::-1]
        self.text_area.set_text(url)
        
    def copy_text(self, widget):
        """Função para copiar o valor digitado na área de texto para o
        clipboard do sistema"""
        clipboard = gtk.clipboard_get()
        url = self.text_area.get_text()
        clipboard.set_text(url)
        clipboard.store()
        
    def paste_text(self, widget):
        """Função para colar o texto armazenado no clipboard na área de texto
        do programa"""
        clipboard = gtk.clipboard_get()
        url = clipboard.wait_for_text()
        self.text_area.set_text(url)
        
    def delete_text(self, widget):
        """Função para apagar qualquer texto que esteja inserido na
        área de texto"""
        self.text_area.set_text("")
        
    def about_window(self, widget):
        """Função para exibir a Janela Sobre do programa"""
        self.about.run()
        self.about.hide()
        
if __name__ == "__main__":
    app = InverterApp()
    gtk.main()
         
        
