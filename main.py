'''
cryptocurrency quotation
============

Version 0.0.1
'''
from kivmob import KivMob, TestIds

from kivy.app import App
from kivy.uix.tabbedpanel import TabbedPanel
from kivy.lang import Builder
from kivy.network.urlrequest import UrlRequest

Builder.load_string("""
<Panel>:
    size_hint: .95, .95
    pos_hint: {'center_x': .5, 'center_y': .5}
    do_default_tab: False
    TabbedPanelItem:
        text: 'Select'
        GridLayout: 
			id: glay
			rows: 4
			cols: 1
            padding: 10
			spacing: 5
            Image:
                source: 'cripto.png'
                size_hint: 0.3, 0.3
            Spinner:
				id: coin
				size_hint: 0.3, 0.3
				text: 'Bitcoin'
				values: 'Bitcoin','Cardano','Ethereum','xrp', 'dogecoin'
            Button:
			    id: bquote 
                size_hint: 0.3, 0.3
		        font_size: 36
                background_color: [0, 0, 1, 1]
                text: 'Quote'
                on_release: root.button_press()
            RstDocument:
			    id: result 
		        font_size: 24
                text: '\\n'.join(("Quotation", "-----------","Select a currency to receive the quote."))
    TabbedPanelItem:
        text: 'Type'
        GridLayout:
            rows: 4
            cols: 1
            padding: 10
            spacing: 5
            Image:
                source: 'cripto.png'
                size_hint: 0.3, 0.3
            TextInput:
                size_hint: 1, 0.2
		        id: coint 
		        font_size: 36
		        multiline: False
            Button:
			    id: bquoteT 
                size_hint: 0.3, 0.3
		        font_size: 36
                background_color: [0, 0, 1, 1]
                text: 'Quote'
                on_release: root.buttont_press()
            RstDocument:
                id: resultT
	            font_size: 24
                text: '\\n'.join(("Quotation", "-----------", "Enter a currency to receive the quote."))
    TabbedPanelItem:
        text: 'Help'
        GridLayout:
            rows: 3
            cols: 1
            padding: 10
            spacing: 5
            Image:
                source: 'cripto.png'
                size_hint: 0.3, 0.3
            Label:
                size_hint: 0.3, 0.3
                background_color: [0, 0, 1, 1]
                text: 'Al2 Software - 2021'
            RstDocument:
                font_size: 24
                text:
                    '\\n'.join(("=====","Help", "=====", "-**Consult the currency quote:**","Enter a currency to receive the quote"))

""")

class Panel(TabbedPanel):
    urlT='https://api.coincap.io/v2/assets/{}'
    ads = KivMob(TestIds.APP) # put your Admob Id 
 
    def __init__(self, **kwargs):
        super(Panel, self).__init__(**kwargs)
        self.ads.new_banner(TestIds.BANNER,False)
        self.ads.new_interstitial(TestIds.INTERSTITIAL)
  
    def button_press(self):
        self.ads.request_banner()
        self.ads.show_banner()

        coin = self.ids.coin.text.lower()
        req = UrlRequest(self.urlT.format(coin), on_success=self.got_json, on_failure=self.got_erro, on_error=self.got_erro)

    def got_json(self, req, result):
        dicio = dict(result['data']) 
        self.ids.result.text = "{}\n-----------\nUS$ {}".format(dicio['name'],dicio['priceUsd'])

    def buttont_press(self):
        self.ads.hide_banner()
        self.ads.request_interstitial()
        self.ads.show_interstitial()

        coin = self.ids.coint.text.lower()
        req = UrlRequest(self.urlT.format(coin), on_success=self.got_jsonT, on_failure=self.got_erro, on_error=self.got_erro)

    def got_jsonT(self, req, result):
        dicio = dict(result['data'])
        self.ids.resultT.text = "{}\n-----------\nUS$ {}".format(dicio['name'],dicio['priceUsd'])

    def got_erro(self, *args):
        print("Failed to get api.", args)

class ConsultaCriptoApp(App):
  
    def build(self):
        return Panel()

if __name__ == '__main__':
    ConsultaCriptoApp().run()

