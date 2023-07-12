# Monte_Carlo_Pi
 Monte Carlo Pi Approximation code uses random points in a square to estimate pi. It demonstrates the Monte Carlo method and provides a scatter plot visualization.


## Monte Carlo Pi Approximation
This code calculates an approximation of the mathematical constant pi (π) using the Monte Carlo method. It generates random points within a square and determines the ratio of points that fall within a unit circle to the total number of points. This ratio is then used to estimate the value of pi.

## Installation
To use this code, you need to have Python installed on your system. You can download Python from the official website: https://www.python.org/downloads/

Additionally, you will need the following libraries:

numpy
matplotlib
You can install these libraries using the pip package manager by running the following command:

```
pip install numpy matplotlib
```

## Usage
The main function of the code is simulate(), which performs the Monte Carlo simulation to approximate pi. It iteratively increases the number of points used in the calculation and returns a list of the pi approximations at each iteration.

To run the code and visualize the results, execute the following command:

## Copy code
python monte_carlo_pi.py
The code will output the approximation of pi with the corresponding number of points used in each iteration. It will also display a scatter plot of the absolute difference between the approximations and the actual value of pi, along with a line of best fit.

## Contributing
Contributions are welcome! If you find any issues with the code or have suggestions for improvements, feel free to open an issue or submit a pull request.

## License
This code is provided under the MIT License.

## Acknowledgments
This code is inspired by the Monte Carlo method and its application to approximating pi. It is intended for educational purposes and to demonstrate the principles of Monte Carlo simulation.

## References
[- Monte Carlo method](https://en.wikipedia.org/wiki/Monte_Carlo_method)
[- Approximations of π](https://en.wikipedia.org/wiki/Approximations_of_%CF%80)
Feel free to modify and customize this README according to your specific needs.
