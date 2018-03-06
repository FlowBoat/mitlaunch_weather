# Input data format

The input format should be an array with shape `(3, 9, 5)`. Each `(9, 5)`-subarray represents an individual timeframe, with the first array being the current data, the second array being the data from one timeframe ago, and the third array being the data from two timeframes ago. Timeframes can be arbitrarily defined.

The `(9, 5)`-arrays are row (east-west)-major data vectors for weighted average data points at the position and in a 3x3 lattice around it with 1 distance unit of a gap. The distance unit can be arbitrarily defined.

Each `5`-vector represented the following data:

1. Temperature (Celcius)
2. Humidity
3. Barometric Pressure (Inches of Mercury)
4. x-component of the 2D wind vector (north-south)
5. y-component of the 2D wind vector (east-west)

The wind vector is the vector with the appropriate wind angle and with magnitude equal to the wind speed in km/h.
