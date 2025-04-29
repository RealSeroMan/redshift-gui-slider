# Redshift GUI Slider

A minimal Python GUI to control screen color temperature using [Redshift](http://jonls.dk/redshift/), with a simple slider interface.

## Features

- Adjust color temperature with a horizontal slider (3000K–6500K)
- Instant effect on slider release
- Optional autostart on system login
- Built with `tkinter`, lightweight and dependency-free

## Requirements

- Python 3
- [Redshift](http://jonls.dk/redshift/)
- Linux (X11-based desktop environment, e.g. GNOME Xorg. This won't work on Wayland based GNOME.)

## Installation

1. **Install Redshift** (if not already installed):

   ```bash
   sudo apt install redshift

2. **Clone this repository**:

    ```bash
    git clone https://github.com/yourusername/redshift-gui-slider.git
    cd redshift-gui-slider
    chmod +x redshift-gui.py


3. **Run the script manually:**

    ```bash
    ./redshift-gui.py

4. **(Optional) Enable autostart on login:**
    ```bash
    mkdir -p ~/.config/autostart
    cp redshift-gui.desktop ~/.config/autostart/

Ensure the Exec= path in redshift-gui.desktop matches your script location.

## How It Works
When the slider is released:

    redshift -x          # Reset Redshift
    redshift -O <temp>   # Apply selected color temperature

- **Default**: 4500K
- **Range**: 3000K to 6500K

## License

MIT License -- free to use, modify, and distribute.
