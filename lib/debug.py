#!/usr/bin/env python3
import ipdb
from classes.many_to_many import NationalPark, Trip, Visitor

if __name__ == "__main__":
    print("HELLO! :) let's debug :vibing_potato:")

    p_1 = NationalPark("Yosemite")
    p_2 = NationalPark("Yellow Stone")
    vis_1 = Visitor("Tom")
    Trip(vis_1, p_1, "May 5th", "May 9th")
    Trip(vis_1, p_1, "January 5th", "January 20th")
    Trip(vis_1, p_2, "January 25th", "January 30th")

    ipdb.set_trace()
