 /
/(_____________            ____
\              /______)\  |    |        
:\      |     /         \:|    |:::::::::: : .. . : ..  . .  :.    .
  \_____|    /      |    \|    |______  
___ /               ________          \...     .     .      .
\______________     \       |  |      /.. . .   .   .             .
               \            |__|     /
--x--x-----x----\______     |-/_____/-x--x-xx--x-- - -x -- - -   --  - - - 
. . . . . . . . . . . .\____|. . . . . .
-------------------------------------------------------------------------------
>> perfect dos vga 437 - general information  >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
-------------------------------------------------------------------------------

 "Perfect DOS VGA 437" and "Perfect DOS VGA 437 Win" are truetype fonts
 designed to emulate the MS-DOS/Text mode standard font, used on VGA monitors,
 with the 437 Codepage (standard US/International). This is a "bitmap" font,
 meaning it emulates a bitmap font and can only be used at a given size (8 or
 multiples of it like 16, 24, 32, etc). It's optimized for Flash too, so it
 won't produce antialias if used at round positions.
 
 There are two fonts available. "Perfect DOS VGA 437" uses the original DOS
 codepage 437. It should be used, for example, if you're opening DOS ASCII
 files on notepad or another windows-based editor. Since it's faithful to the
 original DOS codes, it won't accent correctly in windows ("é" would produce
 something different, not an "e" with an acute).
 
 There's also "Perfect DOS VGA 437 Win" which is the exactly same font adapted
 to a windows codepage. This should use accented characters correctly but won't
 work if you're opening a DOS-based text file.
 
 UPDATE: this is a new version, updated in august/2008. It has fixed leading
 metrics for Mac systems.

-------------------------------------------------------------------------------
>> perfect dos vga 437 - creation process >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
-------------------------------------------------------------------------------
 
 This font was created to be used on a Flash-based ANSi viewer I'm working. To
 create it, I created a small Quick Basic program to write all characters on
 screen,
 
  CLS
  FOR l = 0 TO 255
    charWrite 1 + (l MOD 20), 1 + (l \ 20) * 6 + (l MOD 2), LTRIM$(RTRIM$(STR$(l))) + CHR$(l)
  NEXT
  SUB charWrite (lin, col, char$)
    DEF SEG = &HB800
    FOR i = 1 TO LEN(char$)
      POKE ((lin - 1) * 160) + ((col - 2 + i) * 2), ASC(MID$(char$, i, 1))
      IF (i = LEN(char$)) THEN POKE ((lin - 1) * 160) + ((col - 2 + i) * 2) + 1, 113
    NEXT
  END SUB
  
 Then captured the text screen using SCREEN THIEF (a very, very old screen
 capture TSR program which converts text screens to images accurately). I then
 recreated the font polygon by polygon on Fontlab, while looking at the image
 on Photoshop. No conversion took place.

-------------------------------------------------------------------------------
>> copyright and stuff >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
-------------------------------------------------------------------------------

 This is a free font/file, distribute as you wish to who you wish. You are free
 to use it on a movie, a videogame, a video, a broadcast, without having to ask
 my permission.

 Please do not send me emails asking me to sign release forms if it require
 any sort of scanning or digital compositing. It's a big chore. This license
 file and a simple confirmation email should suffice as proof that you are
 allowed to use it.

 Of course I don't mind emails letting me know where something has been used.
 Those are always gratifying!

 Do NOT sell this font. It's not yours and you can't make money of it.

-------------------------------------------------------------------------------
>> author >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
-------------------------------------------------------------------------------

 Zeh Fernando
 zeh@zehfernando.com
 www.zehfernando.com

 rorshack ^ maiden brazil

-------------------------------------------------------------------------------
>> other notes >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
-------------------------------------------------------------------------------

 The year is now 2021. I would be remiss not to mention these more modern font
 packages:

 https://int10h.org/oldschool-pc-fonts/fontlist/

 They include VGA-like fonts and a bunch of other systems, easily supplanting
 the need for "Perfect DOS VGA" and then some.

 They use a Creative Commons license.

-------------------------------------------------------------------------------
^zehPULLSdahTRICK^kudosOUTtoWHOkeepsITreal^smashDAHfuckingENTAH!!!^lowres4ever^
-------------------------------------------------------------------------------
