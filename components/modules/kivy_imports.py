import os
import json
from kivy.clock import Clock
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import ScreenManager, FadeTransition
from kivy.properties import StringProperty, NumericProperty, ObjectProperty
from kivy.utils import get_color_from_hex
from kivy.factory import Factory

from kivymd.uix.card import MDCard
from kivymd.uix.screen import MDScreen
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
from kivymd.uix.fitimage import FitImage
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.relativelayout import MDRelativeLayout
from kivymd.uix.bottomsheet import MDGridBottomSheet
from kivymd.uix.button import MDRectangleFlatIconButton
from kivymd.uix.bottomsheet import MDCustomBottomSheet
from kivymd.uix.list import OneLineAvatarListItem, OneLineListItem
from kivymd.uix.list import ImageLeftWidget,ImageRightWidget, TwoLineAvatarListItem
from kivymd.uix.list import TwoLineAvatarIconListItem, IRightBodyTouch, ILeftBodyTouch

# Tabs
from kivymd.uix.tab import MDTabsBase
from kivymd.uix.floatlayout import MDFloatLayout


# import module
from components.modules import utils


