import pystray
import PIL.Image
import time
import threading
from pypresence import Presence
from quotes import quotes_data
from heroes import top_champions, jungle_champions, mid_champions, bottom_champions, support_champions


current_state = "Just Started!"
current_details = "SilverFang"
current_image = "silverfang"


def hadnle_exit(icon, item):
    icon.stop()
    exit_event.set()

def update_internal_status(new_state, new_details, new_image):
    global current_state, current_details, current_image
    if (new_state != current_state) or (new_details != current_details) or (new_image != current_image):
        current_state = new_state
        current_details = new_details
        current_image = new_image
        print(f"Changed status to: {current_state} - {current_details} - {current_image}")

def update_discord_status():
    client_id = "1324567013804478464"
    RPC = Presence(client_id)
    RPC.connect()

    last_state = None
    last_details = None
    last_image = None

    while not exit_event.is_set():
        if current_state != last_state or current_details != last_details or current_image != last_image:
            # Call RPC Update only if the user changed status
            RPC.update(
                state=current_state,
                details=current_details,
                large_image=current_image,
                buttons=[{"label": "Join my Server!", "url": "https://discord.com/invite/2F7njSJeh7"}]
            )
            print(f"Updated Discord status: {current_state} - {current_details} - {current_image}")
            last_state = current_state
            last_details = current_details
            last_image = current_image

        time.sleep(1) # Checks every second for a status change (Doesn't fire up Discord status update)


def handle_event(icon, item):
    new_details = "League of Legends"
    
    champion_name = str(item)

    if champion_name in quotes_data:
        new_state, new_image = quotes_data[champion_name]
        update_internal_status(new_state, new_details, new_image)
    else:
        print(f"Champion '{champion_name}' not found in data")

def create_champion_menu(champions):
    menu_items = []
    for champion in champions:
        menu_items.append(pystray.MenuItem(champion, handle_event))
    return menu_items

def tray_icon():
    image = PIL.Image.open("SilverFang.png")

    # Create menus for each category
    top_menu = pystray.Menu(*create_champion_menu(top_champions))
    jungle_menu = pystray.Menu(*create_champion_menu(jungle_champions))
    mid_menu = pystray.Menu(*create_champion_menu(mid_champions))
    bottom_menu = pystray.Menu(*create_champion_menu(bottom_champions))
    support_menu = pystray.Menu(*create_champion_menu(support_champions))

    icon = pystray.Icon("SilverFang", image, menu=pystray.Menu(
        pystray.MenuItem("Games", pystray.Menu(
            pystray.MenuItem("League of Legends", pystray.Menu(
                pystray.MenuItem("Top", top_menu),
                pystray.MenuItem("Jungle", jungle_menu),
                pystray.MenuItem("Mid", mid_menu),
                pystray.MenuItem("Bottom", bottom_menu),
                pystray.MenuItem("Support", support_menu)
            ))
        )),
        pystray.Menu.SEPARATOR,
        pystray.MenuItem("Exit", hadnle_exit),
    ))

    icon.run()

# Event to signal when to exit the program
exit_event = threading.Event()

# Start the tray icon in a separate thread
tray_thread = threading.Thread(target=tray_icon, daemon=True)
tray_thread.start()

# Start the Discord RPC update in a separate thread
rpc_thread = threading.Thread(target=update_discord_status, daemon=True)
rpc_thread.start()

# Wait for the exit event to be triggered (the program will keep running until Exit is clicked)
exit_event.wait()
