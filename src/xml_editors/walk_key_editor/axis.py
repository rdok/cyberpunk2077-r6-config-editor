from abc import ABC


class Axis(ABC):
    y_axis_xpath = './/mapping[@name="LeftY_Axis"]'
    x_axis_xpath = './/mapping[@name="LeftX_Axis"]'
