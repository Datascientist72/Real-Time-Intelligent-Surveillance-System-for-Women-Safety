"""
Distance Calculation Utility Module

This module provides mathematical utility functions
used for calculating spatial relationships between
objects or persons in a video frame.

Purpose:

    - Calculate Euclidean distance between two points.
    - Support behavior analysis algorithms.
    - Measure proximity between tracked persons.

Used in:

    - Following detection
    - Encirclement detection
    - Aggressive approach detection
    - Person interaction analysis



Input:

Two coordinate points:

    p1 = (x1, y1)

    p2 = (x2, y2)



Output:

    Distance between points as a floating-point value.



Formula:

Euclidean Distance:

        __________________

d = √((x2-x1)² + (y2-y1)²)



Example:


Point 1:

    (10,20)


Point 2:

    (30,40)


Distance:

    28.28 pixels



Pipeline:

Object Detection

        ↓

Person Tracking

        ↓

Person Coordinates

        ↓

Distance Calculation

        ↓

Behavior Analysis

"""



import math





def calculate_distance(p1, p2):
    """
    Calculate Euclidean distance between two points.

    This function measures the spatial distance between
    two detected positions in a video frame.

    Args:

        p1 (tuple/list):
            First point coordinates.

            Format:

                (x, y)


        p2 (tuple/list):
            Second point coordinates.

            Format:

                (x, y)



    Returns:

        float:

            Euclidean distance between the two points.


    Example:


        p1 = (100,100)

        p2 = (200,200)


        distance = 141.42



    """



    # Apply Euclidean distance formula
    #
    # sqrt(
    #       (x2-x1)^2 +
    #       (y2-y1)^2
    # )

    return math.sqrt(

        (p1[0] - p2[0]) ** 2 +

        (p1[1] - p2[1]) ** 2

    )