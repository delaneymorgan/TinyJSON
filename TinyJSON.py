#!/usr/bin/env python
# coding=utf-8

"""
TinyJSON

Used for finer control of producing JSON strings.  You should still use the
standard JSON module for loading JSON strings.

© Delaney & Morgan Computing 2021
www.delaneymorgan.com.au

"""


# =============================================================================


class TinyJSON(object):
    def __init__(self):
        return

    def _dump_level(self, obj, indent, indent_depth, sort, precision, this_level=1):
        out_str = ""
        if isinstance(obj, list):
            out_str += "["
            if indent:
                out_str += "\n"
            for index, item in enumerate(obj):
                if index != 0:
                    out_str += ","
                    if indent:
                        out_str += "\n"
                if indent:
                    out_str += " " * this_level * indent_depth
                out_str += self._dump_level(item, indent, indent_depth, sort, precision, (this_level + 1))
            if indent:
                out_str += "\n"
                out_str += " " * (this_level - 1) * indent_depth
            out_str += "]"
        elif isinstance(obj, dict):
            out_str += "{"
            if indent:
                out_str += "\n"
            if sort:
                keys = sorted(obj.keys())
            else:
                keys = obj.keys()
            for index, key in enumerate(keys):
                if index != 0:
                    out_str += ","
                    if indent:
                        out_str += "\n"
                if indent:
                    out_str += " " * this_level * indent_depth
                    out_str += '"%s": ' % key
                else:
                    out_str += '"%s":' % key
                item = obj[key]
                out_str += self._dump_level(item, indent, indent_depth, sort, precision, (this_level + 1))
            if indent:
                out_str += "\n"
                out_str += " " * (this_level - 1) * indent_depth
            out_str += "}"
        elif isinstance(obj, bool):
            out_str += ("%s" % obj).lower()
        elif isinstance(obj, float):
            out_str += "%0.*f" % (precision, obj)
        elif isinstance(obj, int):
            out_str += "%d" % obj
        else:
            out_str += '"%s"' % obj
        return out_str

    def dumps(self, obj, indent=False, indent_depth=2, sort=False, precision=3):
        json_str = self._dump_level(obj, indent, indent_depth, sort, precision)
        return json_str


# =============================================================================


import json

TEST_DICT = dict(
    a=1.23456789,
    b=12345,
    c=True,
    d=[
        "fred",
        1.23456789,
        12345,
        True
    ],
    e=dict(
        ea="fred",
        eb=1.23456789,
        ec=12345,
        ed=True
    )
)

if __name__ == "__main__":
    print("TinyJSON")
    tj = TinyJSON()
    our_json = tj.dumps(TEST_DICT, indent=True)
    outFile = open("tiny.json", "w")
    outFile.write(our_json)
    outFile.close()
    std_json = json.dumps(TEST_DICT, indent=True)
    outFile = open("std.json", "w")
    outFile.write(std_json)
    outFile.close()

    round_trip = json.loads(our_json)
    if TEST_DICT != round_trip:
        print("Different, as expected - but compare output files for differences")
