from kivymd.app import MDApp

class mainapp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = ("teak")


app = mainapp()

app.run()