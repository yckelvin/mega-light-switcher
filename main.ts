input.onButtonPressed(Button.A, function () {
    MuseOLED.clear()
    MuseOLED.writeStringNewLine("Key: " + Key)
    MuseOLED.writeStringNewLine("UserID: " + UserID)
    LGTNum += 1
    if (LGTNum > 3) {
        LGTNum = 1
    }
    basic.showNumber(LGTNum)
})
input.onButtonPressed(Button.AB, function () {
    MuseOLED.clear()
    MuseOLED.writeStringNewLine("Turn off Light " + convertToText(LGTNum))
    value = MuseIoT.HKTIAQ(
    Key,
    "620a0a72b42bf200180ae085",
    Light_List[LGTNum - 1],
    MuseIoT.deviceDescription.NULL,
    MuseIoT.methodDirection.switch_OFF
    )
})
input.onButtonPressed(Button.B, function () {
    MuseOLED.clear()
    MuseOLED.writeStringNewLine("Turn on Light " + convertToText(LGTNum))
    value = MuseIoT.HKTIAQ(
    Key,
    "620a0a72b42bf200180ae085",
    Light_List[LGTNum - 1],
    MuseIoT.deviceDescription.NULL,
    MuseIoT.methodDirection.switch_ON
    )
})
let value = ""
let LGTNum = 0
let Light_List: string[] = []
let Key = ""
let UserID = ""
MuseIoT.initializeWifi()
basic.pause(5000)
MuseIoT.setWifi("izowifi", "izo1234@")
basic.pause(10000)
UserID = "NAMS" + ("" + randint(0, 1000))
MuseIoT.ConnectMuseDataMQTTbroker(UserID)
basic.pause(10000)
MuseOLED.clear()
Key = MuseIoT.GetTheSecurityKey("muselabs", "muselabs")
Light_List = ["627395eefad13d5e6826c9d6", "627395f7fad13d5e6826cf0d", "62739681fad13d5e6827371a"]
LGTNum = 0
MuseOLED.writeStringNewLine("Ready!")
