import numpy as np
import math
from matplotlib import pyplot as plt
from matplotlib.patches import Polygon
from matplotlib import animation


def draw_triangle(filled, p1, p2, p3):
    # create triangle using Polygon shape
    # filling it only if last level
    pts = np.array([p1, p2, p3])
    p = Polygon(pts, closed=True, fill=filled)

    # return Polygon
    return p


def calc_mid(p1, p2):
    # calculate the mid point between 2 points
    return ((p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2)


def set_triangle(max_level, current_level, p1, p2, p3):
    # create & draw the Polygon (triangle)

    # create Polygon (triangle)
    p = draw_triangle((current_level <= 1), p1, p2, p3)

    # get axes object
    ax = plt.gca()

    # add Polygon (triangle)
    ax.add_patch(p)

    # first triangle?
    if max_level == current_level:
        # yes

        # therefore set axes (since first triangle will have largest x & y co-ords
        # plt.gca().set_aspect('equal', adjustable='box')
        # fig = plt.figure(figsize=(25,50))
        ax.set_xlim(p2[0] * 0.95, p3[0] * 1.05)
        ax.set_ylim(p2[1] * 0.95, p1[1] * 1.05)

    if current_level > 1:
        # not the last level

        # therefore, calculate the mid points of each of the triangle's sides
        # to be used to help define the points of the triangle of the next level
        m1 = calc_mid(p1, p2)
        m2 = calc_mid(p2, p3)
        m3 = calc_mid(p3, p1)

        # bottom left triangle
        set_triangle(max_level, current_level - 1, m1, p2, m2)
        # top triangle
        set_triangle(max_level, current_level - 1, p1, m1, m3)
        # bottom right triangle
        set_triangle(max_level, current_level - 1, m3, m2, p3)


def main():
    # set side lengths of triangle
    initial_side_length = 100

    # set angle between points (needed in radians)
    # (60 degrees = equilateral triangle, else isosceles triangle)
    angle_degs = 80
    angle_rads = math.radians(angle_degs)
    # note the apex angle (180 - 2 * angle_degs)
    angle_apex_degs = 180 - (2 * angle_degs)
    angle_apex_rads = math.radians(angle_apex_degs)

    # calc height of triangle
    height = initial_side_length * math.sin(angle_rads)
    # calc base width
    width = 2 * initial_side_length * math.cos(angle_rads)
    # print ("height = " + str(height) + " , width = " + str(width))

    # left (bottom left point of initial triangle) - use as anchor
    p2 = [0, 0]

    # top (top point of initial triangle)
    p1 = [p2[0] + width / 2, p2[1] + height]

    # right (bottom right point of initial triangle)
    p3 = [p2[0] + width, p2[1]]

    # set the number of levels
    num_levels = 9

    # create the first triangle
    # which will recursively create all the other triangles for the different levels
    set_triangle(num_levels, num_levels, p1, p2, p3)

    # show the final drawing
    plt.show()


main()

