#!/usr/bin/env python3
"""
    Extensible text editor.
"""

import abc


class Plugin(abc.ABC):
    
    @abc.abstractmethod
    def process(self, text):
        pass

    @property
    @abc.abstractmethod
    def name(self):
        pass


class ToUpper(Plugin):
    def process(self, text):
        return text.upper()

    @property
    def name(self):
        return "ToUpper"


class ToLower(Plugin):
    def process(self, text):
        return text.lower()

    @property
    def name(self):
        return "ToLower"


class Capitalize(Plugin):
    def process(self, text):
        return text.capitalize()

    @property
    def name(self):
        return "Capitalize"


class TextEditor:
    def __init__(self, *plugins):
        super().__init__()
        self.plugins = list(plugins)

    def add_plugin(self, plugin):
        self.plugins.append(plugin)


    @staticmethod
    def usage():
        print('Prints what user writes')
        print('Write ":pluginName --text--" to let the plugin process the text')
        print('Write ":exit" to exit the program')


    def start(self):
        print("Text editor start.")
        TextEditor.usage()
        print(f'List of loaded plugins: {[pl.name for pl in self.plugins]}')

        while True:
            _str = input('>')
            space_in = _str.find(' ') if _str.count(' ') > 0 else len(_str)
            cmd = _str[1:space_in] if _str.startswith(':') else None

            if cmd == 'exit':
                break

            if cmd is None:
                print(_str)
            else:
                try:
                    print(f'Plugin to be used {cmd}')
                    plugin_in = [pl.name for pl in plugins].index(cmd)
                    print(plugins[plugin_in].process(_str[len(cmd)+2:]))
                except ValueError:
                    print(f'Plugin {cmd} not found. Printing without change.')
                    print(_str[len(cmd)+2:])





if __name__ == '__main__':
    plugins = [ToUpper(), ToLower(), Capitalize()]
    tEditor = TextEditor(*plugins)

    tEditor.start()


