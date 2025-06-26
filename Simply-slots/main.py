from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from backend import spin_slot, admin_login, redeem_user, get_redemptions

Builder.load_file('slot.kv')

class LoginScreen(Screen):
    def login(self):
        uname = self.ids.username.text
        pwd = self.ids.password.text
        if admin_login(uname, pwd):
            self.manager.current = 'admin'
        else:
            self.ids.status.text = "Login failed"

    def play(self):
        self.manager.get_screen('slot').username = self.ids.username.text or 'player1'
        self.manager.current = 'slot'

class SlotScreen(Screen):
    username = "player1"

    def on_enter(self):
        self.ids.user.text = f"Player: {self.username}"

    def spin(self):
        result = spin_slot(self.username)
        self.ids.reels.text = ' '.join(result['result'])
        self.ids.win.text = f"Win: ${result['win']}"
        self.ids.balance.text = f"Balance: ${result['balance']}"

class AdminScreen(Screen):
    def on_enter(self):
        self.load_redeems()

    def load_redeems(self):
        redemptions = get_redemptions()
        self.ids.redeem_list.text = '\\n'.join(
            f"{r['username']} - ${r['amount']} [{r['status']}]" for r in redemptions
        )

    def redeem(self):
        uname = self.ids.redeem_user.text
        amt = int(self.ids.redeem_amt.text)
        msg = redeem_user(uname, amt)
        self.load_redeems()
        self.ids.redeem_status.text = msg

class CasinoApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(LoginScreen(name='login'))
        sm.add_widget(SlotScreen(name='slot'))
        sm.add_widget(AdminScreen(name='admin'))
        return sm

if __name__ == '__main__':
    CasinoApp().run()
