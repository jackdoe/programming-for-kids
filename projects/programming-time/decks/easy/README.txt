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
