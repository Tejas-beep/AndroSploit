from modules import color

version = "v1.0.0"

menu1 = f"""

    {color.WHITE}1. {color.GREEN}Connect a Device             {color.WHITE}6. {color.GREEN}Get Screenshot                       {color.WHITE}11. {color.GREEN}Install an APK  
    {color.WHITE}2. {color.GREEN}List Connected Devices       {color.WHITE}7. {color.GREEN}Screen Record                        {color.WHITE}12. {color.GREEN}Uninstall an App
    {color.WHITE}3. {color.GREEN}Disconnect All Devices       {color.WHITE}8. {color.GREEN}Download File/Folder from Device     {color.WHITE}13. {color.GREEN}List Installed Apps 
    {color.WHITE}4. {color.GREEN}Scan Network for Devices     {color.WHITE}9. {color.GREEN}Send File/Folder to Device           {color.WHITE}14. {color.GREEN}Access Device Shell
    {color.WHITE}5. {color.GREEN}Mirror & Control Device     {color.WHITE}10. {color.GREEN}Run an App                           {color.WHITE}15. {color.GREEN}Hack Device {color.RED}(Using Metasploit)


   {color.YELLOW} 
  N : Next Page                                      (Page : 1 / 3)"""

menu2 = f"""

    {color.WHITE}16. {color.GREEN}List All Folders/Files      {color.WHITE}21. {color.GREEN}Anonymous Screenshot                {color.WHITE}26. {color.GREEN}Play a Video on Device
    {color.WHITE}17. {color.GREEN}Send SMS                    {color.WHITE}22. {color.GREEN}Anonymous Screen Record             {color.WHITE}27. {color.GREEN}Get Device Information
    {color.WHITE}18. {color.GREEN}Copy WhatsApp Data          {color.WHITE}23. {color.GREEN}Open a Link on Device               {color.WHITE}28. {color.GREEN}Get Battery Information
    {color.WHITE}19. {color.GREEN}Copy All Screenshots        {color.WHITE}24. {color.GREEN}Display a Photo on Device           {color.WHITE}29. {color.GREEN}Restart Device
    {color.WHITE}20. {color.GREEN}Copy All Camera Photos      {color.WHITE}25. {color.GREEN}Play an Audio on Device             {color.WHITE}30. {color.GREEN}Advanced Reboot Options


   {color.YELLOW} 
  P : Previous Page         N : Next Page            (Page : 2 / 3)"""

menu3 = f"""

    {color.WHITE}31. {color.GREEN}Unlock Device               {color.WHITE}36. {color.GREEN}Extract APK from Installed App      {color.WHITE}41. {color.GREEN}Record Mic Audio
    {color.WHITE}32. {color.GREEN}Lock Device                 {color.WHITE}37. {color.GREEN}Stop ADB Server                     {color.WHITE}42. {color.GREEN}Listen Device Audio
    {color.WHITE}33. {color.GREEN}Dump All SMS                {color.WHITE}38. {color.GREEN}Power Off Device                    {color.WHITE}43. {color.GREEN}Record Device Audio
    {color.WHITE}34. {color.GREEN}Dump All Contacts           {color.WHITE}39. {color.GREEN}Use Keycodes (Control Device)       
    {color.WHITE}35. {color.GREEN}Dump Call Logs              {color.WHITE}40. {color.GREEN}Listen Mic Audio                    


   {color.YELLOW} 
  P : Previous Page                                  (Page : 3 / 3)"""

menu = [menu1, menu2, menu3]

instruction = f"""

This attack will launch Metasploit-Framework    (msfconsole)

Use 'Ctrl + C' to stop at any point

1. Wait until you see:
    
    {color.GREEN}meterpreter >      {color.WHITE}

2. Then use 'help' command to see all meterpreter commands:

    {color.GREEN}meterpreter > {color.YELLOW}help       {color.WHITE}

3. To exit meterpreter enter 'exit' or To exit Metasploit enter 'exit -y':

    {color.GREEN}meterpreter > {color.YELLOW}exit       {color.WHITE}

    {color.GREEN}msf6 > {color.YELLOW}exit -y       {color.WHITE}
     
{color.RED}[PhoneSploit Pro]   {color.WHITE}Press 'Enter' to continue attack / '0' to Go Back to Main Menu
    """

banner2 = f"""
                    _           _____       _       _ _   
    /\             | |         / ____|     | |     (_) |  
   /  \   _ __   __| |_ __ ___| (___  _ __ | | ___  _| |_ 
  / /\ \ | '_ \ / _` | '__/ _ \\___ \| '_ \| |/ _ \| | __|
 / ____ \| | | | (_| | | | (_) |___) | |_) | | (_) | | |_ 
/_/    \_\_| |_|\__,_|_|  \___/_____/| .__/|_|\___/|_|\__|
                                     | |                  
                                     |_|                  

            {color.RED}{version}{color.WHITE}         By https://github.com/Tejas-Beep
"""

banner3 = f"""
 .d8b.  d8b   db d8888b. d8888b.  .d88b.  .d8888. d8888b. db       .d88b.  d888888b d888888b 
d8' `8b 888o  88 88  `8D 88  `8D .8P  Y8. 88'  YP 88  `8D 88      .8P  Y8.   `88'   `~~88~~' 
88ooo88 88V8o 88 88   88 88oobY' 88    88 `8bo.   88oodD' 88      88    88    88       88    
88~~~88 88 V8o88 88   88 88`8b   88    88   `Y8b. 88~~~   88      88    88    88       88    
88   88 88  V888 88  .8D 88 `88. `8b  d8' db   8D 88      88booo. `8b  d8'   .88.      88    
YP   YP VP   V8P Y8888D' 88   YD  `Y88P'  `8888Y' 88      Y88888P  `Y88P'  Y888888P    YP    
                                                                                             

            {color.RED}{version}{color.WHITE}            By https://github.com/Tejas-Beep
"""

banner4 = f"""
 _______           __              _______         __         __ __   
|   _   |.-----.--|  |.----.-----.|     __|.-----.|  |.-----.|__|  |_ 
|       ||     |  _  ||   _|  _  ||__     ||  _  ||  ||  _  ||  |   _|
|___|___||__|__|_____||__| |_____||_______||   __||__||_____||__|____|
                                           |__|                       

            {color.RED}{version}{color.WHITE}            By https://github.com/Tejas-Beep
"""

banner5 = f"""
  ___            _           _____       _       _ _   
 / _ \          | |         /  ___|     | |     (_) |  
/ /_\ \_ __   __| |_ __ ___ \ `--. _ __ | | ___  _| |_ 
|  _  | '_ \ / _` | '__/ _ \ `--. \ '_ \| |/ _ \| | __|
| | | | | | | (_| | | | (_) /\__/ / |_) | | (_) | | |_ 
\_| |_/_| |_|\__,_|_|  \___/\____/| .__/|_|\___/|_|\__|
                                  | |                  
                                  |_|                  

            {color.RED}{version}{color.WHITE}            By https://github.com/Tejas-Beep
"""

banner6 = f"""
  __           _          ___        _       _  _  
 (  )         ( )        /  _)      ( )     (_)( ) 
 /o \  ____  _| | __  ___\_"-.  ___ | | ___  _ | | 
( __ )( __ )/ o )( _)( o )__) )( o \( )( o )( )( _)
/_\/_\/_\/_\\___\/_\  \_//___/ / __//_\ \_/ /_\/_\ 
                               |_|                 

            {color.RED}{version}{color.WHITE}            By https://github.com/Tejas-Beep
"""

banner10 = f"""
 _______  _        ______   _______  _______  _______  _______  _        _______ __________________
(  ___  )( (    /|(  __  \ (  ____ )(  ___  )(  ____ \(  ____ )( \      (  ___  )\__   __/\__   __/
| (   ) ||  \  ( || (  \  )| (    )|| (   ) || (    \/| (    )|| (      | (   ) |   ) (      ) (   
| (___) ||   \ | || |   ) || (____)|| |   | || (_____ | (____)|| |      | |   | |   | |      | |   
|  ___  || (\ \) || |   | ||     __)| |   | |(_____  )|  _____)| |      | |   | |   | |      | |   
| (   ) || | \   || |   ) || (\ (   | |   | |      ) || (      | |      | |   | |   | |      | |   
| )   ( || )  \  || (__/  )| ) \ \__| (___) |/\____) || )      | (____/\| (___) |___) (___   | |   
|/     \||/    )_)(______/ |/   \__/(_______)\_______)|/       (_______/(_______)\_______/   )_(   
                                                                                                   

            {color.RED}{version}{color.WHITE}            By https://github.com/Tejas-Beep
"""

banner11 = f"""
/.\                   ||`               .|'''|          '||`               ||    
    // \\                  ||                ||               ||          ''    ||    
   //...\\    `||''|,  .|''||  '||''| .|''|, `|'''|, '||''|,  ||  .|''|,  ||  ''||''  
  //     \\    ||  ||  ||  ||   ||    ||  ||  .   ||  ||  ||  ||  ||  ||  ||    ||    
.//       \\. .||  ||. `|..||. .||.   `|..|'  |...|'  ||..|' .||. `|..|' .||.   `|..' 
                                                      ||                              
                                                     .||                              

            {color.RED}{version}{color.WHITE}            By https://github.com/Tejas-Beep
"""

banner12 = f"""
    |                   '||                   .|'''.|           '||           ||    .   
   |||    .. ...      .. ||  ... ..    ...    ||..  '  ... ...   ||    ...   ...  .||.  
  |  ||    ||  ||   .'  '||   ||' '' .|  '|.   ''|||.   ||'  ||  ||  .|  '|.  ||   ||   
 .''''|.   ||  ||   |.   ||   ||     ||   || .     '||  ||    |  ||  ||   ||  ||   ||   
.|.  .||. .||. ||.  '|..'||. .||.     '|..|' |'....|'   ||...'  .||.  '|..|' .||.  '|.' 
                                                        ||                              

            {color.RED}{version}{color.WHITE}            By https://github.com/Tejas-Beep
"""

banner_list = [
    banner2,
    banner3,
    banner4,
    banner5,
    banner6,
    banner10,
    banner11,
    banner12,
]

instructions_banner = f"""{color.CYAN}
        ____           __                  __  _                 
       /  _/___  _____/ /________  _______/ /_(_)___  ____  _____
       / // __ \/ ___/ __/ ___/ / / / ___/ __/ / __ \/ __ \/ ___/
     _/ // / / (__  ) /_/ /  / /_/ / /__/ /_/ / /_/ / / / (__  ) 
    /___/_/ /_/____/\__/_/   \__,_/\___/\__/_/\____/_/ /_/____/  
        {color.WHITE}                                                        
"""

hacking_banner = f"""{color.GREEN}
    
    █░█ ▄▀█ █▀▀ █▄▀ █ █▄░█ █▀▀ ░ ░ ░
    █▀█ █▀█ █▄▄ █░█ █ █░▀█ █▄█ ▄ ▄ ▄
    {color.WHITE}
"""

keycode_menu = f"""
    {color.WHITE}1. {color.GREEN}Keyboard Text Input                {color.WHITE}11. {color.GREEN}Enter
    {color.WHITE}2. {color.GREEN}Home                               {color.WHITE}12. {color.GREEN}Volume Up
    {color.WHITE}3. {color.GREEN}Back                               {color.WHITE}13. {color.GREEN}Volume Down          
    {color.WHITE}4. {color.GREEN}Recent Apps                        {color.WHITE}14. {color.GREEN}Media Play           
    {color.WHITE}5. {color.GREEN}Power Button                       {color.WHITE}15. {color.GREEN}Media Pause
    {color.WHITE}6. {color.GREEN}DPAD Up                            {color.WHITE}16. {color.GREEN}Tab 
    {color.WHITE}7. {color.GREEN}DPAD Down                          {color.WHITE}17. {color.GREEN}Esc
    {color.WHITE}8. {color.GREEN}DPAD Left           
    {color.WHITE}9. {color.GREEN}DPAD Right
   {color.WHITE}10. {color.GREEN}Delete/Backspace
"""
