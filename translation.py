class Translation(object):
    START_TEXT = """Hi! 𝐍𝐄𝐍𝐔 𝐀𝐏𝐈_𝐈𝐝, 𝐀𝐏𝐈_𝐇𝐀𝐒𝐇 𝐆𝐄𝐍𝐄𝐑𝐀𝐓𝐄𝐑 𝐍𝐈 😁
https://te.legra.ph/file/e719f19bbeeb7f55e6202.jpg
𝐍𝐚𝐧𝐮 𝐝𝐞𝐩𝐥𝐨𝐲 𝐜𝐡𝐞𝐧𝐝𝐡𝐢:@santhu_music_bot
𝐍𝐄𝐓𝐖𝐎𝐑𝐊: @santhuvc
𝐂𝐡𝐚𝐧𝐧𝐞𝐥: @santhubotupadates

    # Rest Buttons
    buttons = [
        [InlineKeyboardButton("𝐎𝐖𝐍𝐄𝐑", url="https://t.me/santhu_music_bot"),
        [InlineKeyboardButton("𝐍𝐄𝐓𝐖𝐎𝐑𝐊", url="https://t.me/santhuvc"),
        [
            InlineKeyboardButton("𝐆𝐄𝐍𝐄𝐑𝐀𝐓𝐄 𝐘𝐎𝐔𝐑 𝐒𝐓𝐑𝐈𝐍𝐆 𝐇𝐄𝐑𝐄", url="https://t.me/Santhustringbot"),
            InlineKeyboardButton("ᴀʙᴏᴜᴛ​", callback_data="about"), 
        ],
        [InlineKeyboardButton("𝐉𝐎𝐈𝐍 𝐆𝐑𝐎𝐔𝐏​", url="https://t.me/santhuvc"),
    ]


Enter your Telegram Phone Number, to get the APP-ID from my.telegram.org

/start at any stage to re-enter your details"""
    AFTER_RECVD_CODE_TEXT = """I see!
𝐀𝐫𝐞𝐲 𝐧𝐢𝐛𝐛𝐚 𝐧𝐞𝐤𝐮 𝐨𝐤𝐚 𝐜𝐨𝐝𝐞 𝐯𝐚𝐜𝐡𝐢𝐧𝐝𝐡𝐢 𝐞𝐧𝐭𝐞𝐫 𝐜𝐡𝐞𝐲𝐢 𝐫𝐚 𝐧𝐢𝐛𝐛𝐚 😆!

this code is only used for the purpose of getting the APP ID from my.telegram.org
if you do not trust this bot dev, please host this bot yourself
by opening https://t.me/santhuvc and clicking on the Pink Button

/start at any stage to re-enter your details"""
    BEFORE_SUCC_LOGIN = "recieved code. Scarpping web page ..."
    ERRED_PAGE = "something wrongings. failed to get app id. \n\n@santhuvc"
    CANCELLED_MESG = "Bye! Please re /start the bot conversation"
    IN_VALID_CODE_PVDED = "sorry, but the input does not seem to be a valid Telegram Web-Login code"
    IN_VALID_PHNO_PVDED = "sorry, but the input does not seem to be a valid phone number"
