# Demo Description
Simulation file for DC motor follower with tunable PID, built for MZ_APO target board. 

Control one DC motor position by changing position of the other motor with your hand. PID tuning of the controlled motor is possible in real-time by movement of the Encoder Knobs of the MZ_APO board.


# Requirements

  -Host computer

  -pysimCoder installed on host

  -1x MZ_APO educational kit

  -2x DC motor for MZ_APO educational kit

# Hardware Setup 
  
  1 - Connect data cable of DC motors to MZ_APO peripheral port for PWMs. Make sure to remember which DC motor has which connection. 
  
  2 - Connect LAN cable to Ethernet port on MZ_APO.
  
  3 - Connect the DC charger to one DC motor, that DC motor to the other with a cable, and lastly one cable from last DC motor to the MZ_APO power input. In other words connect the three devices in a daisy chain, starting from a DC motor. 

# User Manual

  1 - Open pysimCoder application

  2 - Press File->Open (CTRL+O) or press appropriate toolbar shortcut, and open "DC_PID_follower.dgm" file.

  3 - Go to Simulation->Generate C-code (CTRL+B) or press appropriate toolbar shortcut. Make sure there are no errors during build on pysimCoder terminal.
  
  4 - Open new terminal in pysimCoder/BlockEditor location, and run RTScope.py script. 
  ```
  $ ./RTScope.py
  ```
  
  5 - Go to TCP tab, change port to value '5000', change signals to value '3', and history to '10000'. Then press 'Start Server'. Repeat for UDP tab.
  
  6 - Open "DC_PID_follower-run.sh" in text-editor, replace HOST value with the computer IPv4 address, and replace TARGET value with the MZ_APO board IPv4 address. Save and exit.
  
  7 - Run shell file.
  ```
  $ ./DC_PID_follower-run.sh
  ```
  
  8 - Use Red knob to change value of Proportional part of controller, Green knob to change Integral part, and Blue knob for the Derivative part. 
      Change position of 1st motor to see the reaction in the 2nd motor. The 2nd motor should follow the position of the 1st one. 
      
      
  
