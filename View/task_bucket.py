from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label

Builder.load_file('kv/task_bucket.kv')


class TaskBucket(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
