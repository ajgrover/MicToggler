import rumps
import os

icon_on = "mic-on.png"
icon_off = "mic-off.png"

class AwesomeStatusBarApp(rumps.App):
    def __init__(self):
        super(AwesomeStatusBarApp, self).__init__("Mic Mute Toggler")
        self.microphone_active = True
        self.icon = icon_on
        self.quit_button = None
        os.system("SwitchAudioSource -s MacBook\ Air\ Microphone -t input")
        # os.system("SwitchAudioSource -m unmute -t input")

    @rumps.clicked("Toggle Microphone")
    def onoff(self, _):
        if self.microphone_active:
            #switch to off
            self.microphone_active = False
            self.icon = icon_off
            os.system("SwitchAudioSource -s Background\ Music -t input")
            # os.system("SwitchAudioSource -m mute -t input")
        else:
            #switch to on
            self.microphone_active = True
            self.icon = icon_on
            os.system("SwitchAudioSource -s MacBook\ Air\ Microphone -t input")
            # os.system("SwitchAudioSource -m unmute -t input")

if __name__ == "__main__":
    AwesomeStatusBarApp().run()

