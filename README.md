#LuckyStrike
Orbital Gemini
Problem motivation:
We realised that a lot of people who wanted to play with claw machines were unable to do so at a given moment, be it lack of transportation, COVID-19 or simply too lazy to leave their house. As a result, we devised an application that was tailored to cater to the spontaneous need to play a claw machine at anytime.

User Stories:
User 1: I really want to play the claw machine to win that cute teddy bear I saw the other day, too bad it's almost 11pm and the arcade would've likely been closed by now.
User 2: Such a shame that there's a pandemic and a mini-lockdown is in effect. Were it not for COVID-19, I would be at the arcade giving the claw machine a go right now.
User 3: After a long day, I sometimes think of heading down to the arcade to try my luck at the claw machine. However, most of the time, I'm far too exhausted to leave home and make my way down to the arcade.

Project Idea:
To provide users a way to play an arcade game remotely on their own computer/laptop.
Features
Physical features
•	Player’s computer which allows player to wirelessly connect to a separate computer running the game. 
•	The separate computer is connected to the Ev3 brick via Bluetooth to play the arcade game. 
•	The arcade game is a simple car game that sends a video back to the player’s computer. 
•	The player would only have one control: to stop the claw at the desired spot.
Software features
•	Game contains a log in and registration page.
•	 A top up credits page used to play the physical claw game (no real monetary top up would be used).
•	 A record of the prizes won: big and small prize the former being of harder difficulty.
•	 A button to play the game itself.
•	 A button to connect to the claw laptop.
•	 Only one user can be connected at any one time.
Design your System: images uploaded as a preview for the design.
Necessary Technologies: Python Command Socket Functions Video streaming (Flask/OpenCV) SQL to create the database for the app.
Technical Proof of concept: See the file.
To run the file:
1. Download the schema ORBITAL Database.sql
2. Open Orbit.py and change the username and password below the first function defined to your individual one
3. Connect to SQL
4. Close all files and run interface.py

