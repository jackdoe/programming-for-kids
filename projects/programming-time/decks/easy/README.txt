not entirely true things:

* used one number per object type
    + 1 -> integer
    + 2 -> string
    + 3 -> range
    + 4 -> list
    + 5 -> boolean
    which is not entirely true
    and over over simplifies *ob_type

* integers stored as 1 byte.. and etc
  oversimplifyig the memory layout, but there
  is not a lot of space on the cards..
    
* lists not haivng inline objects
  i think describing lists as basically
  array of pointers is handy so beginners
  start to think about how references are followed

* ranges in cython are basically for (i=start;i<stop;i+=step)
  but are differeint in other implementations
  but i describe them as stateful variables, which
  is not entirely correct, but not horribly wrong either



* games:

    + 1 game per player, dec is upside down, pick
    find your output on top of the deck and
    take the top card, this is your active card
    player with most cards win


    + 6 cards facing up, your goal is to
    collect cards until you get the ascii
    for 'hello'

    each turn you can choose to replace
    a card on the table, or take it

    + program a 4 bit computer?
 
    + make a chain of functions to
      build the biggest number

    e.g. mutiply(add(CARD44,CARD55), CARD22)

    each card can be used as a function
    or result


    
    

    
      
    
    
