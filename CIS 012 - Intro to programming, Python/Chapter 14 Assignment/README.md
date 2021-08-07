# Chapter 14 Assignment

Build a simplified Tamagotchi using Object-Oriented Programming.  You get 100 points for implementing the basic class with the listed attributes and behaviors for the pet.  You get 20 points extra credit if you use unit testing.  You can get up to 100 points extra credit if you use inheritance and make interesting Tamagotchi "breeds" with different characteristics and behaviors.

Tamagotchi are virtual pets that start out as alien eggs.

Characters can be based on animals, objects, or people. 

All Tamagotchi have a name, gender, and character type.  At birth, the player can name the pet. But the computer will determine the gender and character type.

You should have a class function that will list the Tamagotchi name, gender, and character type.  This should print to the screen when your Tamagotchi is instantiated or "born."

Tamagotchi have a Hunger meter, Happy meter, Sickness meter.  The Hunger meter starts at 10, signifying fullness.  The Happy meter starts at 10, signifying happiness.  The Sickness meter starts at 0, signifying wellness.

On every turn, the Hunger and Happy meter decrease by 1 unit.

On every turn, you can perform one of the following actions:

a) Feed the pet, which fills the Hunger meter by 2 units

b) Play with the pet, which fills the Happy meter by 3 units.  

c) Nothing

At the end of every turn, you should report the state of the Hunger, Happy, and Sickness meters.  You can be creative and represent it as a meter, or you can just specify the number of units out of 10.  For example: Hunger (10/10).

If you overfeed the pet, aka, overfill the Hunger meter, it will increase the Sickness meter by the number of units that you overfilled the Hunger meter.  For example, if the Hunger meter reaches 12, then you should report that Hunger (10/10) and Sickness (2/10) unit.  There is no way to decrease the Sickness meter.

There is no way to exceed the Happy meter.  For example, if the Happy meter is at 10, and you increase happiness by 3 units, the Happy meter remains (10/10).

When the Sickness meter is 10 or the Happy meter is 0 or the Hunger meter is 0, the pet dies, and the game ends.