<p align="center"> 
<img src="https://i.imgur.com/Qk4df7C.png">
</p>





<p align="center">
<a href=""><img src="https://img.shields.io/badge/Read_more-at_dev.to-000000?logo=dev.to&logoColor=ffffff"></a>
<a href="https://chat.openai.com/chat"><img src="https://img.shields.io/badge/ChatGPT_Assissted_-Program-412991?logo=OpenAI&logoColor=ffffff"></a>
<img src="https://img.shields.io/badge/Made_With-Python-3776AB?logo=python&logoColor=ffffff">
<a href="https://www.buymeacoffee.com/frostkurti0"><img src="https://img.shields.io/badge/buy_me-a_coffee-FFDD00?logo=buy+me+a+coffee"></a></p>


<br>

---

<br>

# The Concept:
The original concept for this was for me to enter a prompt to the ai to make an RPG styled combat system. In my mind, it was supposed to work like this:

- User would select "Attack", "Defend" or "Run"
- "Attack" would deal damage to the Goblin
- "Defend" would reduce the damage of the next attack by a %
- "Run" would end the loop and print out a "Game Over" message
- The Goblin would only have the "Attack" & "Defend" options and would chose one of them at random.
- Combat would resume until the Knight or Goblin reached 0 HP.
- If the knight reach 0, "Game Over"
- If the Gbolin reaches 0 "YOU WIN"

It didn't work as planned.

<br><br>

# What is it?
This is a little project I made while I was putting the [ChatGPT](https://chat.openai.com/chat) ai through it's paces. I gave the ai 2 different prompts to see what it could handle and these are the results. **If you want to read more about this process, I have documented in over on [dev.to]()**

<br>

**First Prompt:**

> _"use python. Create an RPG combat system where you are a knight that fights a Goblin."_

<br>

**Second Prompt:**
> _use python and make an RPG combat system where you can fight a goblin. The user controls the knight. You have three options: Attack which deals damage. Defend which reduces damage taken by 25%. and Run which has a 50% chance to end the combat. The goblin can only attack or defend and picks at random._

<br>

On the **first prompt** it managed to handle no problem. The results it spit out worked. The only problem was there is no interactivity in the program. It runs through the fight and the Knight attacks the Goblin and the Goblin never attacks back. The prompt will run start to finish and you just sit there as it runs.

For the **second prompt** it never managed to complete the task. It got hunt up on line 67:

```python
knight_health -=
```

After around **15 minutes** of inactivity, I decided to run the prompt again and see if it could do it. _Sadly, I forgot to copy the code before the refresh._ The second attempt of the prompt took around **2 and a half hours** and never completed.

<br><br>

# What I learned:
Your prompts seem to have to be very direct but not overly complicated (or at least in my experiments). If I make the prompt too complicated, the ai gets hung up and doesn't complete the prompt. If I make it too simple, it seems to generate wonky code that either doesn't work or doesn't follow the original prompt.

<br>

---

[![Buy Me - A Coffee](https://img.shields.io/badge/Buy_Me-A_Coffee-FFDD00?style=for-the-badge&logo=buy+me+a+coffee&logoColor=ffffff)](https://www.buymeacoffee.com/frostkurti0)