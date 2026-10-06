# Raspberry Pi Dashboard

A minimal dark-themed Tkinter dashboard for a Raspberry Pi 2 running Raspberry Pi OS (32-bit legacy). It displays the current time and date in a clean, full-screen layout on an LCD monitor.

## Features
- Full-screen dark UI
- Light text for high contrast
- Large time display
- Date shown underneath
- Auto-updating every second
- Escape key exits the app

## Requirements
- Raspberry Pi 2
- Raspberry Pi OS (32-bit legacy)
- Python 3
- Tkinter (usually included with Raspberry Pi OS)
- LCD monitor connected to the Pi

## Install

1. Open a terminal on the Raspberry Pi.
2. Clone the repository:

```bash
git clone https://github.com/leviaspes/pi-dashboard.git
cd pi-dashboard
```

3. Make the script executable:

```bash
chmod +x dashboard.py
```

4. Run the app manually:

```bash
python3 dashboard.py
```

## Auto-start on boot
To launch the dashboard automatically when the Pi boots, create a desktop launcher and add it to the LXDE autostart configuration.

### Option 1: Use LXDE autostart

1. Open the autostart file:

```bash
nano ~/.config/lxsession/LXDE-pi/autostart
```

2. Add this line at the end:

```bash
@python3 /home/pi/pi-dashboard/dashboard.py
```

If your repository is stored in a different folder, replace `/home/pi/pi-dashboard` with the correct path.

3. Save and exit.

4. Reboot the Raspberry Pi:

```bash
sudo reboot
```

## Exit the dashboard
Press the `Esc` key to close the app.

## Troubleshooting
- If Tkinter is missing, install it:

```bash
sudo apt update
sudo apt install python3-tk
```

- If the display is too large or small, adjust the font sizes in `dashboard.py`.

## Files
- `dashboard.py` — the main application
