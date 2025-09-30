# Part 1

Implement a very simple class `Vector2D` and a function `clamp`. I expect you to implement the following:

**Part A** implement methods of the `Vector2D` class, check that vector tests pass.
* `__init__` -- a constructor. You should save two given values (`x` and `y`) to attributes `x` and `y`. I expect these attributes to be accessible later
* `__add__` -- you should implement addition of two vectors -- `self` and `other` (this is the Pythonic way to overload operator "+"; after you implement this function, you will be able to write `w = u + v`, where `w`, `u`, and `v` are all `Vector2D`)
* `__sub__` -- you should implement subtraction of two vectors -- `self` and `other` (this is the Pythonic way to overload operator "-\"; after you implement this function, you will be able to write `w = u - v`, where `w`, `u`, and `v` are all `Vector2D`)
* `__mul__` -- you should implement multiplication of vector `self` by number `num` (this is the Pythonic way to overload operator "*\"; after you implement this function, you will be able to write `u = 2.5 * v` or `u = x * v`, where `w` and `v` are `Vector2D` and `x` is a number)
* `__rmul__` -- implemented for you  (this is the Pythonic way to overload multiplication from the right -- Python makes difference between `w = 2 * v` and `w = v * 2`; I implemented this function for you so that it makes multiplication commutative)
* `__truediv__`  -- implemented for you  (this is the Pythonic way to overload division; I implemented this function for you so that it treats division by $n$ as multiplication by $1/n$)
* `dot` -- you should implement the dot product of two vectors -- `self` and `other`. If you designate this vectors as $\vec{u}$ and $\vec{v}$ the formula is $(\vec{v} \cdot \vec{u}) = v_x u_x + v_y u_y$.
* `perp` -- return a vector perpendicular to the given. I expect you to use a simple formula: let `self` is a vector $\vec{v}$ that has components $\vec{v} = \{v_x;v_y\}$, return a vector $\vec{v}_\perp$ that has components $\vec{v}_\perp = \{-v_y, v_x\}$. You may check that these vectors are indeed perpendicular since $(\vec{v}_\perp \cdot \vec{v}) = -v_y v_x + v_x v_y = 0$
* `lng` -- return the length of the vector; use `math.sqrt` when the square root is needed $\left(|\vec{v}| = \sqrt{v_x^2 + v_y^2}\right)$.
* `decompose` -- return two `Vector2D` objects that are decomposition of the given vector $\vec{v}$ (`self`) along vector $\vec{n}$ (`other`) and $\vec{n}_\perp$. You can use the following algorithm:
    - calculate $\vec{e} = \vec{n} / |\vec{n}|$, use `lng` method of `other` ($\vec{n}$)
    - calculate $\vec{e}_\perp$ -- use `perp` method of the vector $\vec{e}$
    - calculate $\vec{u}_{\|\|} = \vec{e} (\vec{v} \cdot \vec{e})$ and $\vec{u}_\perp = \vec{e}_\perp (\vec{v} \cdot \vec{e}_\perp)$, use `dot` method; notice that $\vec{u}_{||}$ is parallel to $\vec{n}$ and $\vec{u}_\perp$ is perpendicular to $\vec{n}$, $\vec{v} = \vec{u}_{||} + \vec{u}_\perp$
    - return $\vec{u}_{||}$ and $\vec{u}_\perp$ in exactly this order -- parallel component first


**Part B** implement function `clamp`, check that clamp tests pass
function `clamp(x, x_min, x_max)` -- should return `x_min` if `x < x_min`; `x_max` if `x > m_max` and `x` otherwise

  
# Part 2

* Implement missing functions in class `Ball`
   - `__init__(self, radius, pos, velocity, gravity)` -- constructor; it is given a bunch of data that you should save to internal variables:
       + `radius` -- ball radius, integer
       + `pos` -- `Vector2D` that contains current coordinates
       + `velocity` -- `Vector2D`, velocity of the ball
       + `gravity` -- float number, gravity
   - `get_coordinates(self)` -- return a `Vector2D` that contains current coordinates of the ball
   - `get_properties(self)` -- return a float (ball radius)
   - `move` -- imlement ball movement. You may suppose the time is dimensionless. I expect you to update ball's position basing on the current position, say $\vec{p}_{\text{current}}$, and current velocity, say $\vec{v}_{\text{current}}$, as
   $$
   \vec{p}_{\text{updated}} = \vec{p}_{\text{current}} + \vec{v}_{\text{current}},
   $$
   than update the $y$ coordinate of the velocity
   $$
   v_{y,\text{updated}} = v_{y,\text{current}} - g
   $$
   and clamp the updated velocity to prevent it from overgrowing. Make sure that it is always true that
   $$
   \begin{aligned}
   -\frac{r}{2} < v_{x,\text{updated}} < \frac{r}{2},\\
   -\frac{r}{2} < v_{y,\text{updated}} < \frac{r}{2}.
   \end{aligned}
   $$
   Function `clamp` will be helpful.
* Make sure all tests are passing

# Part 3

Now we will endow the ball with the ability to bounce.
* Implement `check_collision_and_bounce(self, A, B)` function. As an input the function takes two parameters `A` and `B` both of the type `Vector2D`. These are the endpoints of certain segment you should bounce the ball off. Your function should return `True` if the ball bounced and `False` otherwise. This is the challenging part, please read carefully the following explanation how to implement the function.

Consider figure 1. The ball has coordinates $\vec{p}$ and we should check whether it hits segment with endpoints $\vec{A}$ and $\vec{B}$.

![image1](https://raw.githubusercontent.com/fbeilstein/python/master/practice_1/image1.png)

We consider the ball to be bouncing if its center $\vec{p}$ is inside the "hitbox" shown in figure 2. The hitbox is rectangular and has width $|\vec{A}-\vec{B}| + r$, where $r$ is the ball's radius. Height of the hitbox is $2r$. Please not how the $AB$ segment is positioned inside the hitbox.
* Calculate the halfwidth and the halfheight of the hitbox: $d_{||} = |\vec{A} - \vec{B}|/2 + r/2$ and $d_\perp = r$

![image2](https://raw.githubusercontent.com/fbeilstein/python/master/practice_1/image2.png)

The easiest way to check that ball's center $\vec{p}$ is (or is not) in the hitbox is to decompose the vector $\vec{p} - \frac{\vec{A}+\vec{B}}{2}$ into components parallel to $\vec{A} - \vec{B}$, say $\vec{w}_{||}$, and perpendicular to it $\vec{w}_\perp$. See figure 3 for details.
* Suppose, current position of the ball is $\vec{p}$. Calculate vector $\vec{w} = \vec{p} - \frac{\vec{A} + \vec{B}}{2}$ that is position of the ball relative to the segment's center
* Use `decompose` method of $\vec{w}$ with argument $\vec{A} - \vec{B}$ to get $\vec{w}_{||}$ and $\vec{w}_\perp$ that are projections of $\vec{w}$ on the segment and its normal; notice that the `decompose` method returns two vectors, $\vec{w}_{||}$ is the first

![image3](https://raw.githubusercontent.com/fbeilstein/python/master/practice_1/image3.png)

We suppose that ball hits the segment, when **both** following conditions are satisfied
* Center of the ball is inside the hitbox, namely $|\vec{w}_{||}| < d_{||}$ **and** $|\vec{w}_\perp| < d_\perp$; use method `lng` when needed
* The ball is moving **toward** the segment, i.e. if it has velocity $\vec{v}$ then $(\vec{v} \cdot \vec{w}_\perp) < 0$; use method `dot` when needed

After you determined if the segment is hit, do the following:
* If the segment is not hit, return `False` and do nothing
* If the segment is hit, decompose ball's velocity $\vec{v}$ into components parallel to $\vec{A} - \vec{B}$, say $\vec{v}_{||}$, and perpendicular $\vec{v}_\perp$, then update $\vec{v}_{\text{updated}} = \vec{v}_{||} - \vec{v}_\perp$ and return `True`; notice that before the update the velocity was $\vec{v} = \vec{v}_{||} + \vec{v}_\perp$

**Note:** you may have noticed that for large velocities ball will tunnel through the wall (how quantum-mechanically, I should say :) ). This is the reason, why I asked you to limit its speed in the previous problem. If you have ignored this part of the instructions, it's time to implement it. Or you may come up with some more robust and cunning algorithm for bouncing -- let me know and I will consider it for the future runs of the course.

# Part 4

* Implement a class `Paddle`. I have already created a draft, you should complete the implementation of few functions here.
   - `__init__(self, pos, size, velocity=0.0, direction=Vector2D(0, 0))` -- constructor; it is given a bunch of data that you should store to internal variables:
       + `pos` -- `Vector2D`, contains current coordinates (corresponds to the lower left corner)
       + `size` -- `Vector2D`, contains width and height of the block
       + `velocity` -- float number, absolute value of the velocity of the ball (not a vector!) velocity of the ball
       + `direction` -- `Vector2D`, unit vector along direction of movement; velocity as a vector should be `v * direction`
   - `get_sizes` -- should return two `Vector2D` -- coordinate of the block (initial is `p`) and its size; use multiple return feature to implement this function
   - `move` -- change position of the block by `v * direction`, clamp coordinates so that the block remains inside the field
* Make sure that tests pass
