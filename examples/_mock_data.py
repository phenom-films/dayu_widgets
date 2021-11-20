#!/usr/bin/env python
# -*- coding: utf-8 -*-
###################################################################
# Author: Mu yanru
# Date  : 2019.3
# Email : muyanru345@163.com
###################################################################
# Import local modules
from dayu_widgets import dayu_theme


def score_color(score, y):
    if score < 60:
        return dayu_theme.error_color
    elif score < 80:
        return dayu_theme.warning_color
    elif score >= 90:
        return dayu_theme.success_color
    return dayu_theme.info_color


header_list = [
    {
        "label": "Name",
        "key": "name",
        "checkable": True,
        "searchable": True,
        "width": 200,
        "font": lambda x, y: {"underline": True},
        "icon": "user_fill.svg",
    },
    {
        "label": "Sex",
        "key": "sex",
        "searchable": True,
        "selectable": True,
        "icon": lambda x, y: (
            "{}.svg".format(x.lower()),
            getattr(dayu_theme, x.lower() + "_color"),
        ),
    },
    {
        "label": "Age",
        "key": "age",
        "width": 90,
        "searchable": True,
        "editable": True,
        "display": lambda x, y: "{} 岁".format(x),
        "font": lambda x, y: {"bold": True},
    },
    {
        "label": "Address",
        "key": "city",
        "selectable": True,
        "searchable": True,
        "exclusive": False,
        "width": 120,
        "display": lambda x, y: " & ".join(x) if isinstance(x, list) else x,
        "bg_color": lambda x, y: "transparent" if x else dayu_theme.error_color,
    },
    {
        "label": "Score",
        "key": "score",
        "searchable": True,
        "editable": True,
        "bg_color": score_color,
        "color": "#fff",
    },
    {"label": "Score Copy", "key": "score", "searchable": True, "color": score_color},
]

data_list = [
    {
        "name": "John Brown",
        "sex": "Male",
        "sex_list": ["Male", "Female"],
        "age": 18,
        "score": 89,
        "city": "New York",
        "city_list": ["New York", "Ottawa", "London", "Sydney"],
        "date": "2016-10-03",
    },
    {
        "name": "Jim Green",
        "sex": "Male",
        "sex_list": ["Male", "Female"],
        "age": 24,
        "score": 55,
        "city": "London",
        "city_list": ["New York", "Ottawa", "London", "Sydney"],
        "date": "2016-10-01",
    },
    {
        "name": "Zhang Xiaoming",
        "sex": "Male",
        "sex_list": ["Male", "Female"],
        "age": 30,
        "score": 70,
        "city": "",
        "city_list": ["Beijing", "Shanghai", "Shenzhen", "Guangzhou"],
        "date": "2016-10-02",
    },
    {
        "name": "Jon Snow",
        "sex": "Female",
        "sex_list": ["Male", "Female"],
        "age": 26,
        "score": 60,
        "city": "Ottawa",
        "city_list": ["New York", "Ottawa", "London", "Sydney"],
        "date": "2016-10-04",
    },
    {
        "name": "Li Xiaohua",
        "sex": "Female",
        "sex_list": ["Male", "Female"],
        "age": 18,
        "score": 97,
        "city": "Ottawa",
        "city_list": ["New York", "Ottawa", "London", "Sydney"],
        "date": "2016-10-04",
    },
]

tree_data_list = [
    {
        "name": "John Brown",
        "sex": "Male",
        "sex_list": ["Male", "Female"],
        "age": 18,
        "score": 89,
        "city": "New York",
        "city_list": ["New York", "Ottawa", "London", "Sydney"],
        "date": "2016-10-03",
        "children": [
            {
                "name": "Jim Green",
                "sex": "Male",
                "sex_list": ["Male", "Female"],
                "age": 24,
                "score": 55,
                "city": "London",
                "city_list": ["New York", "Ottawa", "London", "Sydney"],
                "date": "2016-10-01",
            },
            {
                "name": "Zhang Xiaoming",
                "sex": "Male",
                "sex_list": ["Male", "Female"],
                "age": 30,
                "score": 70,
                "city": "",
                "city_list": ["Beijing", "Shanghai", "Shenzhen", "Guangzhou"],
                "date": "2016-10-02",
            },
        ],
    },
    {
        "name": "Jon Snow",
        "sex": "Female",
        "sex_list": ["Male", "Female"],
        "age": 26,
        "score": 60,
        "city": "Ottawa",
        "city_list": ["New York", "Ottawa", "London", "Sydney"],
        "date": "2016-10-04",
    },
    {
        "name": "Li Xiaohua",
        "sex": "Female",
        "sex_list": ["Male", "Female"],
        "age": 18,
        "score": 97,
        "city": "Ottawa",
        "city_list": ["New York", "Ottawa", "London", "Sydney"],
        "date": "2016-10-04",
    },
]
