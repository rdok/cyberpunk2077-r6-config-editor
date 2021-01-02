# import tkinter as tk
#
# from src.widgets.button import Button
# from src.widgets.button_frame import ButtonFrame
# from src.widgets.frame import Frame
# from src.widgets.label import Label
# from src.widgets.scale import Scale
# from src.xml_editors.hold_actions.HoldActionEditor import HoldActionEditor
#
#
# class HoldActionTimeoutFrame:
#     hold_action_editor: HoldActionEditor
#     crafting_speed_scale: Scale
#     initial_scale_value = None
#
#     def __init__(self, hold_action_editor: HoldActionEditor):
#         self.hold_action_editor = hold_action_editor
#
#     def render(
#         self,
#         master: tk,
#         label_text: str,
#         from_: float,
#         to_: float,
#         resolution: float,
#         row: int
#     ):
#         self.row = row
#
#         label_frame = Frame(master=master)
#         label_frame.grid(row=self.row, column=0)
#         label = Label(master=label_frame, text=label_text)
#         label.pack()
#
#         crafting_speed_frame = Frame(master=master)
#         crafting_speed_frame.grid(row=self.row, column=1)
#         crafting_speed_scale = Scale(
#             master=crafting_speed_frame,
#             from_=from_,
#             to_=to_,
#             resolution=resolution
#         )
#         initial_scale_value = self.hold_action_editor.get_timeout()
#         crafting_speed_scale.set(initial_scale_value)
#         crafting_speed_scale.pack()
#         self.crafting_speed_scale = crafting_speed_scale
#
#         apply_button_frame = ButtonFrame(master=master)
#         apply_button_frame.grid(row=self.row, column=2)
#         apply_button = Button(master=apply_button_frame, text="APPLY")
#         apply_button.bind('<Button-1>', self.handle_apply_event)
#         apply_button.pack()
#
#     def handle_apply_event(self, event):
#         scale_value = self.crafting_speed_scale.get()
#         self.hold_action_editor.set_timeout(scale_value)
