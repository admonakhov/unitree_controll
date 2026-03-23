# Controlling Unitree G1 Robot with Dualshock Controller

This project allows controlling the Unitree G1 robot using a wireless Dualshock (PlayStation) controller via Bluetooth.

## Description

The project provides a real-time interface for controlling the G1 robot using a gamepad. 

## Requirements

- Python >= 3.8
- Ubuntu/Linux with Bluetooth support
- Dualshock controller (PS4 or PS5) or other
- Access to Unitree G1 robot

## Installation

1. Install Unitree SDK python:
   ```bash
   pip3 install -e ./sdk
   ```

2. Install Pygame library for controller support:
   ```bash
   pip3 install pygame
   ```

## Controller Setup

1. Install necessary Bluetooth packages:
   ```bash
   sudo apt install bluetooth bluez bluez-tools
   ```

2. Start Bluetooth service:
   ```bash
   sudo systemctl start bluetooth
   ```

3. Enter Bluetooth setup mode:
   ```bash
   bluetoothctl
   ```

4. Inside bluetoothctl, run the following commands:
   ```bash
   power on
   agent on
   default-agent
   scan on
   ```

5. Find your controller's address (usually named "Wireless Controller"):
   ```
   Wireless Controller XX:XX:XX:XX:XX:XX
   ```

6. Pair the controller:
   ```bash
   pair XX:XX:XX:XX:XX:XX
   connect XX:XX:XX:XX:XX:XX
   trust XX:XX:XX:XX:XX:XX
   ```

7. Add user to input group (replace `unitree` with your username):
   ```bash
   sudo usermod -aG input unitree
   ```

   Reboot the system or log out and back in for changes to take effect.

## Running

Run the control script, specifying the robot connection interface:

```bash
python g1_controller.py <interface>
```

Replace `<interface>` with the appropriate network interface or robot IP address.

## Controls

Use the following button combinations on the controller:

- **L2 + Circle**: Damping mode
- **L2 + Up**: Stand mode
- **L2 + Square**: Walk mode

### Additional Commands

- Other buttons and sticks on the controller can be used to control robot movement in respective modes.

## Troubleshooting

- **Controller not connecting**: Ensure Bluetooth is enabled and the controller is charged. Try resetting the controller (hold PS + Share for 10 seconds).
- **Input access error**: Ensure the user is added to the `input` group and reboot.
- **SDK issues**: Check SDK installation and dependencies.

## Project Structure

- `g1_controller.py`: Main control script
- `gamepad_control.py`: Gamepad handling module
- `sdk/`: Unitree SDK

## License

This project uses the Unitree SDK. Check the license in the `sdk/` folder.

## Contacts

For questions and support, refer to Unitree documentation or developer community.