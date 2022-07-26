# Question 4
To make sure the results we are giving the client are true,
we can test the calculator with different inputs and compare the outputs to our manual calculation
or use a similar calculator found online (if exists and assuming the calculator is correct),
and compare the output to their output.

## Edge cases
### Invalid input type
If the calculator is given an empty or non-number input, it will raise a `ValueError`
indicating that the input is invalid.
### Special input values
In case the calculator encounters some combination of values that are physically irrational,
for instance, `initial height = 0` and `initial velocity = 0`, then it will raise an `Exception` that
indicates that there are no solutions.
### Large input values
In case the calculator is given a highly large number that causes an overflow, an `Exception` 
will be raised that indicates the number is too large.

# Question 5
### Air resistance
Currently, the physical model does not take into account `Air Resistance` which significantly
affects projectile motion in real life.

It is possible to calculate the air resistance given additional values, such as `Air drag`, 
`Air density`, `Cross sectional area` (The area of the object from a forward, 2D perspective)
and the `Drag coefficient` of the object.
Most of these values can be easily calculated and will dramatically increase the accuracy of 
the calculator.
### Sloped ground and hills
Currently, the calculator assumes that the object will land on a flat ground, 
this will not be the case most of the time.

Sloped land and hills will decrease the accuracy of the landing position, 
landing velocity and landing angle, because the object will land sooner (or later) and 
not necessarily on `y = 0` (flat ground level), therefore, all the calculations will be off, depending
on the slope of the land or the hill.

Additionally, objects mid-air could also disrupt the motion of the object, which will again decrease
the accuracy.