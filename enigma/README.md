### How Enigma Works

The Enigma machine works by taking an input key, running it through a complicated wiring that jumbles the character input into a completely different one.

When a key is pressed, the electrical signal is sent into the plugboard. This essentially ties two letters together, such that if one is pressed it acts as if the other is. From the plugboard, this is sent to the rotors. Each rotor maps each character to a different character, seemingly randomly. Each time a key is pressed the first rotor turns, when the first rotor makes a full rotation the second rotor will turn, and when the second makes a full rotation the third rotor will turn. The signal passes through three of these rotors, before hitting the reflector. This is similar to the rotors in that it maps each character to a different character, but it differs in two aspects:

  - It does not rotate.
  - It is symmetrical (i.e. if A becomes H, H would become A).
  
From the reflector, the signal is sent back through the rotors in reverse order, and then from there it gets sent back through the plugboard, and finally it will light up the relevant lamp to character that is encoded.



### How to use the Enigma implementation

In the enigma repository there are 3 files:

  - *enigma.py*: This is the main file, and when run directly functions as an enigma shell. You can run this as a module.
  - *rotor_gen.py*: This file generates rotor data in JSON format given a rotor map.
  - *rotors.json*: This file is required for *enigma.py* to run, and must be in the same directory as it. It contains all data on each rotor.
