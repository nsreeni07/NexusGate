Description

NexusGate is a DIY smart lock system designed to replace traditional key-based access with RFID authentication. The system uses an RFID reader to detect authorized cards or fobs and controls a locking mechanism electronically.

The core controller is a arudino that processes RFID input and determines access permissions. When a valid RFID tag is detected, the system actuates a servo motor to unlock the door. Unauthorized scans are ignored, and optional logging can track access attempts.

The system integrates hardware components including an RFID module (MFRC522), an electronic locking mechanism, and a power management system. 

How to Use

Power on the system and ensure the RFID reader and controller are initialized. Authorized RFID cards or fobs must first be registered in the system’s database.

To unlock the door, place a registered RFID card near the reader. If the UID matches an authorized entry, the controller triggers the locking mechanism to open the door. If the card is not recognized, the system denies access.

After use, the lock automatically returns to the locked state after a set delay or manual reset.

Why I Made This Project

I built NexusGate to explore embedded systems, access control, and hardware-software integration. I wanted to gain hands-on experience working with RFID and microcontrollers.
<img width="1524" height="1143" alt="IMG_6876" src="https://github.com/user-attachments/assets/f581318f-02b4-4bd3-bd88-0dfa4d29a03b" />
