
## [DAY-192] Class; Methods


There are few ways to represent a rectangle, one is with one point plus width and height, e.g. top left point and width and height.


```
(the screen's y grows downwards, top left is 0,0)
    │       x=8                           x
────┼───────┬────────────────────────────────
    │       │
    │       │
 y=3├───────*──────────────────┐
    │       │##################│
    │       │##################│
    │       │##################│ height
    │       │##################│
    │       └──────────────────┘
    │              width
    │
    │
   y│
```

or you can store the position of two diagonal points, top left and bottom right (or top right and bottom left)

```
    │
    │       x=8              x=27         x
────┼───────┬──────────────────┬─────────────
    │       │                  │
    │       │                  │
 y=3├───────*──────────────────┤
    │       │##################│
    │       │##################│
    │       │##################│
    │       │##################│
 y=8├───────┴──────────────────*
    │
    │
   y│

```

In this example I chose the two points appriach as it I can just make a Point class and use it twice, but sometimes the first approach is more suitable. We want to make a Rect class that has a method to expand to include a point.

```
    │
    │       x=8              x=27   x=31    x
────┼───────┬──────────────────┬─────────────
    │       │                  │     .
    │       │                  │     .
 y=3├───────*──────────────────┤     .
    │       │##################│+++++.
    │       │##################│+++++.
    │       │##################│+++++.
    │       │##################│+++++.
 y=8├───────┴──────────────────*+++++.
    │        ++++++++++++++++++++++++.
    │        ++++++++++++++++++++++++.
    │        ++++++++++++++++++++++++.
    │        ++++++++++++++++++++++++.
y=12│................................*
    │
    │
    │
   y│
```

> Pause here to think about how to approach this, use pen and paper to illustrate the approach.

The solutio is simply to move the topleft's x/y more left/up if they are bigger than the requested point, and move the bottomright's x/y if they are smaller than the requested point. This way the rectangle grows just enough to include the point.

```
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Rect:
    def __init__(self, topLeft, bottomRight):
        self.topLeft = topLeft
        self.bottomRight = bottomRight


    def expand(self, point):
        if self.topLeft.x > point.x:
            self.topLeft.x = point.x
        if self.topLeft.y > point.y:
            self.topLeft.y = point.y
        if self.bottomRight.x < point.x:
            self.bottomRight.x = point.x
        if self.bottomRight.y < point.y:
            self.bottomRight.y = point.y

r = Rect(Point(10,10),Point(20,20))
print(r.topLeft.x, r.topLeft.y,r.bottomRight.x, r.bottomRight.y)
r.expand(Point(5,5))
print(r.topLeft.x, r.topLeft.y,r.bottomRight.x, r.bottomRight.y)
r.expand(Point(50,3))
print(r.topLeft.x, r.topLeft.y,r.bottomRight.x, r.bottomRight.y)
r.expand(Point(50,100))
print(r.topLeft.x, r.topLeft.y,r.bottomRight.x, r.bottomRight.y)
```

Sometimes its handy to be able to chain method calls, so if the method returns an instance you can just call a method on the returned value.

```
class Rect:
    def __init__(self, topLeft, bottomRight):
        self.topLeft = topLeft
        self.bottomRight = bottomRight


    def expand(self, point):
        if self.topLeft.x > point.x:
            self.topLeft.x = point.x
        ...
        return self

r = Rect(Point(10,10),Point(20,20))
r.expand(Point(5,5)).expand(Point(50,3)).expand(Point(50,100))
print(r.topLeft.x, r.topLeft.y,r.bottomRight.x, r.bottomRight.y)
```

