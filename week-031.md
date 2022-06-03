## [DAY-213] PICO-8 Adventure Game

> Following the guide she made the game, I used the time to specifically talk about tables and she particularly had an issue with if() looking like a function. I tried to give her more space and time to follow the tutorial on her own.

![game-213-a.png](./screenshots/game-213-a.png "game 213 a screenshot")
![game-213-b.png](./screenshots/game-213-b.png "game 213 b screenshot")


## [DAY-214] PICO-8 Follow Platformer Game Tutorial

In the next week follow the [Platformer Tutorial](https://www.youtube.com/playlist?list=PLyhkEEoUjSQtUiSOu-N4BIrHBFtLNjkyE) from [Nerdy Teachers](https://www.youtube.com/channel/UCbMjF_cWciuBUZjILNL1fyA).

Do not code while watching the video, first watch the video once, and then second time to code with the teacher.

## [DAY-215] make a website

Ask your parents to buy a domain name for you, and buy a domain and some VPS hosting, ask your parent to set it up and install a web server there, buy a domain and point it to the hosting (they know what to do.

ssh into the computer and start editing the index.html file:

```
# cd /var
# cd www
# cd html
# nano index.html

```

write `<h1>Hello</h1>` in the editor and then hit CTRL+S to save it, and then open your website through your browser and phone

> FIXME: we actually spent few days on this just talking about IP addressess, DNS, ssh and etc, but I forgot to write it down

## [DAY-216] directories

Imagine we had all the files on our computer in one place. You will have all the things you use, apps, games, documents, pictures, all in one giant blob of files.

![game-216.png](./screenshots/game-216.png "game 216 screenshot")

Even worse, imagine having only one file with all the stuff in it, one picture ends another begins, one app ends another begins, it is quite useless if you think about it like that, so just having different files for different things is already helpful for organizing your information, but adding directories which allow you to group a bunch of files together, changes the game. Having directories which can contain files or other directories allows you to organize everything to a very fine level.

BTW, there are operating systems that actually speciallize in browsing files in a different way e.g. the [Canon Cat computer](https://www.youtube.com/watch?v=jErqdRE5zpQ)

Lets say we have directory named Games, and inside we have two games, Fortnite and Minecraft, and in each of them we have some files (sound files and the game programs themselves)

```
                        Games
                      /       \
                    /           \
            minecraft            Fortnite
            /    |               /  |   \
           /     |              /    \    \
         sound  minecraft.exe  sound      fortnite.exe
          /                     |       
      zombie.mp3             falling.mp3 
      rain.mp3               song.mp3

```

You can imagine there is a path to get to song.mp3, its Games -> Fortnite -> sound -> song.mp3, you can imagine a small gnome starting from the top (the Games diretory) and going down, and on each crossroad it has to pick.

In linux (the operating system which is used by your web server) the directory we use `/` (slash) to be able to say where are we going, e.g. /Games/Fortnite/sound/song.mp3 will be how we can access the file directly, `/` is the beginning of the path or this is the "root" directory, which is a bit confusing because in linux there is also `/root` which is the `home` directory for the `root` user (the system administrator), but we call `/` the root of the file system.

Using the `cd` command allows us to move our gnome to specific part of the tree. so if we say `cd /Games` now our gnome will be in the Games directory, and from here we can access song.mp3 by just doing `Fortnite/sound/song.mp3`.
