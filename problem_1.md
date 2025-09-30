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
    - calculate \\(\vec{u}_{||} = \vec{e} (\vec{v} \cdot \vec{e})\\) and \\(\vec{u}_\perp = \vec{e}_\perp (\vec{v} \cdot \vec{e}_\perp)\\), use `dot` method; notice that \\(\vec{u}_{||}\\) is parallel to \\(\vec{n}\\) and \\(\vec{u}_\perp\\) is perpendicular to \\(\vec{n}\\), \\(\vec{v} = \vec{u}_{||} + \vec{u}_\perp\\)
    - return $\vec{u}_{||}$ and $\vec{u}_\perp$ in exactly this order -- parallel component first


**Part B** implement function `clamp`, check that clamp tests pass
* function `clamp(x, x_min, x_max)` -- should return `x_min` if `x < x_min`; `x_max` if `x > m_max` and `x` otherwise
