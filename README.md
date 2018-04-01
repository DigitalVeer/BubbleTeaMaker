# Boba Tea


The **Boba Tea Dispenser** is a modern, effecient, and cheap machine that dispenses *bubble tea* at any given command. The system is composed of a few key parts:

- 1x Rasbperry Pi - Model 3
- 1x Amazon Echo
- 1x Servo Motors
- 1x Aquariam Fish Pump
- Two tube dispensors

# Alexa, you know the drill!

As mentioned before, the dispensor can be activated at the sound of your voice! Simply  repeat the following magic words and Alexa shall obey:
*Alexa, tell bubble tea maker to make me some tea*

**That's it.**
**The rest is taken care of.**

----

The development of the Boba Tea Dispensor was heavily inspired by the staff over at *std-libs.* The use of their library gave the team a first look on how to interact with Alexa. From there, the task was focused on understanding how to set up a connection between the Rasbperry Pi 3 and Alexa. Through the use of API's such as *Flask*, making the connection was not too difficult and it finished the last piece of the puzzle.

One of the bigger challenges for the team was specifically hardware. Aside from the fact that creating a giant cardboard box with stickers and paper flowers brought back rather unpleasant first grade art project flashbacks, a majority of the difficulty for members of the team came from connecting the relay, pi, and the aquariam fish pump purchased at PetSmart. The team learned the components of what makes a breadboard, relay, and complete circuit, and combined all that knowledge to create the ultimate 

What is Boba Tea?
-----

>Boba is a Taiwanese tea-based drink invented in Tainan and Taichung in the 1980s. Most bubble tea recipes contain a tea base mixed with fruit or milk, to which chewy tapioca balls and fruit jelly are often added.


### Tech

The **Boba Tea Dispensor** uses a number of open source projects to work properly:

* [Flask] - Connection bewteen Pi and Alexa
* [AWS] - Developer Console to control and test Alexa
* [std-lib] - Great API manager and controller


And of course, the code behind the Boba Tea dispesnsor itself is open source with a [public repository][gitplz]
on GitHub.

### Installation

Boba Tea Dispensor requires *Flask* and a *Raspberry Pi* to work.



[//]: # (These are reference links used in the body of this note and get stripped out when the markdown processor does its job. There is no need to format nicely because it shouldn't be seen. Thanks SO - http://stackoverflow.com/questions/4823468/store-comments-in-markdown-syntax)


[gitplz]: <https://github.com/emuvengeance/bubbleteamaker>

