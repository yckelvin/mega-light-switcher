def on_button_pressed_a():
    global LGTNum
    MuseOLED.clear()
    MuseOLED.write_string_new_line("Key: " + Key)
    MuseOLED.write_string_new_line("UserID: " + UserID)
    LGTNum += 1
    if LGTNum > 3:
        LGTNum = 1
    basic.show_number(LGTNum)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    global value
    MuseOLED.clear()
    MuseOLED.write_string_new_line("Turn off Light " + convert_to_text(LGTNum))
    value = MuseIoT.HKTIAQ(Key,
        "620a0a72b42bf200180ae085",
        Light_List[LGTNum - 1],
        MuseIoT.deviceDescription.NULL,
        MuseIoT.methodDirection.SWITCH_OFF)
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    global value
    MuseOLED.clear()
    MuseOLED.write_string_new_line("Turn on Light " + convert_to_text(LGTNum))
    value = MuseIoT.HKTIAQ(Key,
        "620a0a72b42bf200180ae085",
        Light_List[LGTNum - 1],
        MuseIoT.deviceDescription.NULL,
        MuseIoT.methodDirection.SWITCH_ON)
input.on_button_pressed(Button.B, on_button_pressed_b)

value = ""
LGTNum = 0
Light_List: List[str] = []
Key = ""
UserID = ""
MuseIoT.initialize_wifi()
basic.pause(5000)
MuseIoT.set_wifi("KLHOME", "127214529")
basic.pause(10000)
UserID = "NAMS" + str(randint(0, 1000))
MuseIoT.connect_muse_data_mqt_tbroker(UserID)
basic.pause(10000)
MuseOLED.clear()
Key = MuseIoT.get_the_security_key("muselabs", "muselabs")
Light_List = ["627395eefad13d5e6826c9d6",
    "627395f7fad13d5e6826cf0d",
    "62739681fad13d5e6827371a"]
LGTNum = 0
MuseOLED.write_string_new_line("Ready!")