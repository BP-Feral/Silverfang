![SilverFang Logo](utils/silverfang.png)

SilverFang is a desktop application that allows users to set custom Discord activities with interactive tray menus to spice up their profile. It provides an easy way to update your Discord status with a cool video game persona, as well as custom images and buttons, all directly from a system tray menu.

Currently, **SilverFang** supports **League of Legends** champions and plans to add more games/activities in the future.

## Features

- **Interactive System Tray Menu**: Easily manage and switch between your custom Discord activities directly from the system tray.
- **Custom Discord Status**: Update your Discord status to reflect your in-game activity, with detailed states and images.
- **Custom Buttons**: Include custom buttons in your Discord activity (e.g., "Join my Server").
- **League of Legends Support**: Select champions from different roles in League of Legends to set your Discord activity automatically.
- **More Customization**: Allow users to trim the buttons they don't want to use to achieve a clearer menu, or add to **Favorite Activities**.

> **Note:** This tool was originally created for personal use, which is why a lot of the content is hardcoded. However, I plan to make it more user-friendly and adaptable for the public in future versions. You can still download and modify it, or contact me over Discord (`rioterneeko`) if you have some good suggestions.

- Python 3.7 or newer
- Required libraries:
  - `pystray`: For creating the system tray menu
  - `Pillow`: For working with images in the tray icon
  - `pypresence`: For interacting with Discord's Rich Presence API

## Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/your-username/SilverFang.git
   cd SilverFang
   ```

2. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Ensure you have a valid Discord Client ID (you can obtain it from the Discord Developer Portal).

4. Add your Discord Client ID in the code or configuration.

## How to Use

1. Run Silverfang

    Once the dependencies are installed and configured, you can run the program by executing:

    ```bash
    python silverfang.py
    ```

    This will launch SilverFang, which will run in your system tray.

    >_if you don't want to run from script you can [download the default app](https://github.com/BP-Feral/Silverfang/releases/download/v1.1pre/silverfang.rar) from Releases, or build the executable yourself using `pyinstaller`._
    use this command and copy the icon next to the .exe
    ```bash
    pyinstaller --windowed --icon=silverfang.png  silverfang.py --name "silverfang"
    ```

2. Select Your Activity

    Right-click the SilverFang icon in the system tray to bring up the menu. You can select a game from the "Games" section, and then choose a champion. Your Discord activity will automatically update to reflect the game and champion you selected.

    For example, choosing a champion like Aatrox will set your Discord status to reflect "League of Legends - Playing as Aatrox" with the relevant image.

3. Custom Discord Buttons

    You can also include custom buttons, such as a "Join my Server" button, directly within your Discord status.

4. Exiting SilverFang

    To exit the application, right-click the tray icon and select Exit. This will stop the SilverFang process and remove the icon from the system tray.

## Future Features

- Additional Games: Plans to add support for more games.

- More Detailed Status Options: Support for additional Discord status options, such as "Watching" or "Listening to".

- Custom Image Support: Allow users to upload their own images for Discord status updates.

- Custom Buttons: Allow users to write their own buttons and links for example
    YouTube, Twitch, or advertising their work.

## Contributing

Contributions are welcome! If you'd like to contribute, feel free to fork the repository, create a feature branch, and submit a pull request.

You can also [join my discord server](https://discord.com/invite/2F7njSJeh7) or write me a direct message on Discord at: `rioterneeko`