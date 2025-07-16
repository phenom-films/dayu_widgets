# Import built-in modules
from functools import partial
import os
import re

# Import third-party modules
from qtpy import QtCore
from qtpy import QtGui
from qtpy import QtWidgets

# Import local modules
from dayu_widgets.mixin import property_mixin
from dayu_widgets.popup import MPopup
from dayu_widgets.line_edit import MLineEdit
import dayu_widgets.utils as utils


PYSIDE6 = os.environ.get("QT_API") == "pyside6"


class CompatStyle(QtWidgets.QProxyStyle):
    """PySide2 PySide6"""

    def __init__(self, style=None):
        super(CompatStyle, self).__init__(style)
        self.style = style

    @property
    def State_None(self):
        if PYSIDE6:
            return QtWidgets.QStyle.State()
        return QtWidgets.QStyle.State_None

    @property
    def State_Active(self):
        if PYSIDE6:
            return QtWidgets.QStyle.State.State_Active
        return QtWidgets.QStyle.State_Active

    @property
    def State_Enabled(self):
        if PYSIDE6:
            return QtWidgets.QStyle.State.State_Enabled
        return QtWidgets.QStyle.State_Enabled

    @property
    def State_DownArrow(self):
        if PYSIDE6:
            return QtWidgets.QStyle.State.State_DownArrow
        return QtWidgets.QStyle.State_DownArrow

    @property
    def State_UpArrow(self):
        if PYSIDE6:
            return QtWidgets.QStyle.State.State_UpArrow
        return QtWidgets.QStyle.State_UpArrow

    @property
    def PE_PanelMenu(self):
        if PYSIDE6:
            # 在PySide6中使用PE_PanelButtonCommand替代PE_Frame
            # PE_PanelButtonCommand通常会填充背景
            return QtWidgets.QStyle.PE_PanelButtonCommand
        return QtWidgets.QStyle.PE_PanelMenu

    @property
    def PE_FrameMenu(self):
        if PYSIDE6:
            return QtWidgets.QStyle.PE_Frame
        return QtWidgets.QStyle.PE_FrameMenu

    @property
    def CE_MenuEmptyArea(self):
        if PYSIDE6:
            return QtWidgets.QStyle.CE_ShapedFrame
        return QtWidgets.QStyle.CE_MenuEmptyArea

    @property
    def CE_MenuItem(self):
        return QtWidgets.QStyle.CE_MenuItem

    @property
    def CE_MenuScroller(self):
        return QtWidgets.QStyle.CE_MenuScroller

    @property
    def PM_MenuPanelWidth(self):
        return QtWidgets.QStyle.PM_MenuPanelWidth

    @property
    def PM_MenuHMargin(self):
        return QtWidgets.QStyle.PM_MenuHMargin

    @property
    def PM_MenuVMargin(self):
        return QtWidgets.QStyle.PM_MenuVMargin

    @property
    def MenuItemType_EmptyArea(self):
        if PYSIDE6:
            return QtWidgets.QStyleOptionMenuItem.MenuItemType.EmptyArea
        return QtWidgets.QStyleOptionMenuItem.EmptyArea

    @property
    def CheckType_NotCheckable(self):
        if PYSIDE6:
            return QtWidgets.QStyleOptionMenuItem.CheckType.NotCheckable
        return QtWidgets.QStyleOptionMenuItem.NotCheckable

    @property
    def MenuItemType_Scroller(self):
        if PYSIDE6:
            return QtWidgets.QStyleOptionMenuItem.MenuItemType.Scroller
        return QtWidgets.QStyleOptionMenuItem.Scroller

    def combine_states(self, *states):
        if PYSIDE6:
            result = QtWidgets.QStyle.State()
            for state in states:
                result |= state
            return result
        else:
            result = 0
            for state in states:
                result |= state
            return result


@property_mixin
class ScrollableMenuBase(QtWidgets.QMenu):
    """
    https://www.pythonfixing.com/2021/10/fixed-how-to-have-scrollable-context.html
    """

    deltaY = 0
    dirty = True
    ignoreAutoScroll = False

    def __init__(self, *args, **kwargs):
        super(ScrollableMenuBase, self).__init__(*args, **kwargs)
        self._maximumHeight = self.maximumHeight()
        self._actionRects = []
        self._compat_style = CompatStyle(self.style())

        self.scrollTimer = QtCore.QTimer(parent=self, interval=50, singleShot=True)
        self.scrollTimer.timeout.connect(self.checkScroll)

        self.scrollTimer.setProperty("defaultInterval", 50)
        self.delayTimer = QtCore.QTimer(self, interval=100, singleShot=True)

        self.setMaxItemCount(0)

    def _set_max_scroll_count(self, value):
        self.setMaxItemCount(value * 2.2)

    @property
    def actionRects(self):
        if self.dirty or not self._actionRects:
            del self._actionRects[:]
            offset = self.offset()
            for action in self.actions():
                geo = super(ScrollableMenuBase, self).actionGeometry(action)
                if offset:
                    geo.moveTop(geo.y() - offset)
                self._actionRects.append(geo)
            self.dirty = False
        return self._actionRects

    def iterActionRects(self):
        for action, rect in zip(self.actions(), self.actionRects):
            yield action, rect

    def setMaxItemCount(self, count):
        style = self.style()
        opt = QtWidgets.QStyleOptionMenuItem()
        opt.initFrom(self)

        a = QtWidgets.QAction("fake action", self)
        self.initStyleOption(opt, a)
        size = QtCore.QSize()
        fm = self.fontMetrics()
        qfm = opt.fontMetrics
        size.setWidth(fm.boundingRect(QtCore.QRect(), QtCore.Qt.TextSingleLine, a.text()).width())
        size.setHeight(max(fm.height(), qfm.height()))
        self.defaultItemHeight = style.sizeFromContents(QtWidgets.QStyle.CT_MenuItem, opt, size, self).height()

        if not count:
            self.setMaximumHeight(self._maximumHeight)
        else:
            pm_menu_panel_width = self._compat_style.PM_MenuPanelWidth
            fw = style.pixelMetric(pm_menu_panel_width, None, self)
            vmargin = style.pixelMetric(self._compat_style.PM_MenuVMargin, opt, self)
            scrollHeight = self.scrollHeight(style)
            max_height = (
                self.defaultItemHeight * count +
                (fw + vmargin + scrollHeight) * 2
            )
            self.setMaximumHeight(max_height)
        self.dirty = True

    def scrollHeight(self, style):
        height = style.pixelMetric(QtWidgets.QStyle.PixelMetric.PM_MenuScrollerHeight, None, self)
        return height * 2

    def isScrollable(self):
        is_scrollable = self.property("scrollable")
        size_hint = super(ScrollableMenuBase, self).sizeHint()
        return is_scrollable and self.height() < size_hint.height()

    def checkScroll(self):
        pos = self.mapFromGlobal(QtGui.QCursor.pos())
        delta = max(2, int(self.defaultItemHeight * 0.25))
        if self.scrollUpRect.contains(pos):
            delta *= -1
        elif not self.scrollDownRect.contains(pos):
            return
        if self.scrollBy(delta):
            self.scrollTimer.start(self.scrollTimer.property("defaultInterval"))

    def offset(self):
        if self.isScrollable():
            return self.deltaY - self.scrollHeight(self.style())
        return 0

    def translatedActionGeometry(self, action):
        return self.actionRects[self.actions().index(action)]

    def ensureVisible(self, action):
        style = self.style()
        pm_menu_panel_width = self._compat_style.PM_MenuPanelWidth
        fw = style.pixelMetric(pm_menu_panel_width, None, self)
        h_margin = style.pixelMetric(self._compat_style.PM_MenuHMargin, None, self)
        v_margin = style.pixelMetric(self._compat_style.PM_MenuVMargin, None, self)
        scrollHeight = self.scrollHeight(style)
        extent = fw + h_margin + v_margin + scrollHeight
        r = self.rect().adjusted(0, extent, 0, -extent)
        geo = self.translatedActionGeometry(action)
        if geo.top() < r.top():
            self.scrollBy(-(r.top() - geo.top()))
        elif geo.bottom() > r.bottom():
            self.scrollBy(geo.bottom() - r.bottom())

    def scrollBy(self, step):
        if step < 0:
            newDelta = max(0, self.deltaY + step)
            if newDelta == self.deltaY:
                return False
        elif step > 0:
            newDelta = self.deltaY + step
            style = self.style()
            scrollHeight = self.scrollHeight(style)
            bottom = self.height() - scrollHeight

            for lastAction in reversed(self.actions()):
                if lastAction.isVisible():
                    break
            lastBottom = self.actionGeometry(lastAction).bottom() - newDelta + scrollHeight
            if lastBottom < bottom:
                newDelta -= bottom - lastBottom
            if newDelta == self.deltaY:
                return False

        self.deltaY = newDelta
        self.dirty = True
        self.update()
        return True

    def actionAt(self, pos):
        for action, rect in self.iterActionRects():
            if rect.contains(pos):
                return action

    # class methods reimplementation

    def sizeHint(self):
        hint = super(ScrollableMenuBase, self).sizeHint()
        if hint.height() > self.maximumHeight():
            hint.setHeight(self.maximumHeight())
        return hint

    def eventFilter(self, source, event):
        if event.type() == QtCore.QEvent.Show:
            if self.isScrollable() and self.deltaY:
                action = source.menuAction()
                self.ensureVisible(action)
                rect = self.translatedActionGeometry(action)
                delta = rect.topLeft() - self.actionGeometry(action).topLeft()
                source.move(source.pos() + delta)
            return False
        return super(ScrollableMenuBase, self).eventFilter(source, event)

    def event(self, event):
        if not self.isScrollable():
            return super(ScrollableMenuBase, self).event(event)
        if event.type() == event.KeyPress and event.key() in (
            QtCore.Qt.Key_Up,
            QtCore.Qt.Key_Down,
        ):
            res = super(ScrollableMenuBase, self).event(event)
            action = self.activeAction()
            if action:
                self.ensureVisible(action)
                self.update()
            return res
        elif event.type() in (event.MouseButtonPress, event.MouseButtonDblClick):
            pos = event.pos()
            if self.scrollUpRect.contains(pos) or self.scrollDownRect.contains(pos):
                if event.button() == QtCore.Qt.LeftButton:
                    step = max(2, int(self.defaultItemHeight * 0.25))
                    if self.scrollUpRect.contains(pos):
                        step *= -1
                    self.scrollBy(step)
                    self.scrollTimer.start(200)
                    self.ignoreAutoScroll = True
                return True
        elif event.type() == event.MouseButtonRelease:
            pos = event.pos()
            self.scrollTimer.stop()
            if not (self.scrollUpRect.contains(pos) or self.scrollDownRect.contains(pos)):
                action = self.actionAt(pos)
                if action:
                    action.trigger()
                    self.close()
            return True
        return super(ScrollableMenuBase, self).event(event)

    def timerEvent(self, event):
        if not self.isScrollable():
            # ignore internal timer event for reopening popups
            super(ScrollableMenuBase, self).timerEvent(event)

    def mouseMoveEvent(self, event):
        if not self.isScrollable():
            super(ScrollableMenuBase, self).mouseMoveEvent(event)
            return

        pos = event.pos()
        if pos.y() < self.scrollUpRect.bottom() or pos.y() > self.scrollDownRect.top():
            if not self.ignoreAutoScroll and not self.scrollTimer.isActive():
                self.scrollTimer.start(200)
            return
        self.ignoreAutoScroll = False

        oldAction = self.activeAction()
        if not self.rect().contains(pos):
            action = None
        else:
            y = event.y()
            for action, rect in self.iterActionRects():
                if rect.y() <= y <= rect.y() + rect.height():
                    break
            else:
                action = None

        self.setActiveAction(action)
        if action and not action.isSeparator():

            def ensureVisible():
                self.delayTimer.timeout.disconnect()
                self.ensureVisible(action)

            try:
                self.delayTimer.disconnect()
            except:
                pass
            self.delayTimer.timeout.connect(ensureVisible)
            self.delayTimer.start(150)
        elif oldAction and oldAction.menu() and oldAction.menu().isVisible():

            def closeMenu():
                self.delayTimer.timeout.disconnect()
                oldAction.menu().hide()

            self.delayTimer.timeout.connect(closeMenu)
            self.delayTimer.start(50)
        self.update()

    def wheelEvent(self, event):
        if not self.isScrollable():
            return
        self.delayTimer.stop()
        if event.angleDelta().y() < 0:
            self.scrollBy(self.defaultItemHeight)
        else:
            self.scrollBy(-self.defaultItemHeight)

    def showEvent(self, event):
        if self.isScrollable():
            self.deltaY = 0
            self.dirty = True
            for action in self.actions():
                if action.menu():
                    action.menu().installEventFilter(self)
            self.ignoreAutoScroll = False
        super(ScrollableMenuBase, self).showEvent(event)

    def hideEvent(self, event):
        for action in self.actions():
            if action.menu():
                action.menu().removeEventFilter(self)
        super(ScrollableMenuBase, self).hideEvent(event)

    def resizeEvent(self, event):
        super(ScrollableMenuBase, self).resizeEvent(event)

        margins = self.contentsMargins()
        l, t, r, b = margins.left(), margins.top(), margins.right(), margins.bottom()

        style = self.style()
        pm_menu_panel_width = self._compat_style.PM_MenuPanelWidth
        pm_menu_v_margin = self._compat_style.PM_MenuVMargin
        fw = style.pixelMetric(pm_menu_panel_width, None, self)
        h_margin = style.pixelMetric(self._compat_style.PM_MenuHMargin, None, self)
        v_margin = style.pixelMetric(pm_menu_v_margin, None, self)

        left_margin = fw + h_margin + l
        top_margin = fw + v_margin + t
        bottom_margin = fw + v_margin + b
        content_width = self.width() - (fw + v_margin) * 2 - l - r
        scroll_height = self.scrollHeight(style)

        self.scrollUpRect = QtCore.QRect(left_margin, top_margin, content_width, scroll_height)
        self.scrollDownRect = QtCore.QRect(
            left_margin,
            self.height() - scroll_height - bottom_margin,
            content_width,
            scroll_height,
        )

    def paintEvent(self, event):
        if not self.isScrollable():
            super(ScrollableMenuBase, self).paintEvent(event)
            return

        style = self.style()
        qp = QtGui.QPainter(self)
        rect = self.rect()
        emptyArea = QtGui.QRegion(rect)

        menuOpt = QtWidgets.QStyleOptionMenuItem()
        menuOpt.initFrom(self)
        menuOpt.state = self._compat_style.State_None
        menuOpt.maxIconWidth = 0
        menuOpt.tabWidth = 0
        style.drawPrimitive(self._compat_style.PE_PanelMenu, menuOpt, qp, self)

        fw = style.pixelMetric(self._compat_style.PM_MenuPanelWidth, None, self)
        topEdge = self.scrollUpRect.bottom()
        bottomEdge = self.scrollDownRect.top()
        offset = self.offset()
        qp.save()
        qp.translate(0, -offset)
        # offset translation is required in order to allow correct fade animations
        for action, actionRect in self.iterActionRects():
            actionRect = self.translatedActionGeometry(action)
            if actionRect.bottom() < topEdge:
                continue
            if actionRect.top() > bottomEdge:
                continue

            visible = QtCore.QRect(actionRect)
            if actionRect.bottom() > bottomEdge:
                visible.setBottom(bottomEdge)
            elif actionRect.top() < topEdge:
                visible.setTop(topEdge)
            visible = QtGui.QRegion(visible.translated(0, offset))
            qp.setClipRegion(visible)
            emptyArea -= visible.translated(0, -offset)

            opt = QtWidgets.QStyleOptionMenuItem()
            self.initStyleOption(opt, action)
            opt.rect = actionRect.translated(0, offset)
            style.drawControl(self._compat_style.CE_MenuItem, opt, qp, self)
        qp.restore()

        cursor = self.mapFromGlobal(QtGui.QCursor.pos())
        upData = (False, self.deltaY > 0, self.scrollUpRect)
        downData = (True, actionRect.bottom() - 2 > bottomEdge, self.scrollDownRect)

        for isDown, enabled, scrollRect in upData, downData:
            qp.setClipRect(scrollRect)

            scrollOpt = QtWidgets.QStyleOptionMenuItem()
            scrollOpt.initFrom(self)
            scrollOpt.state = self._compat_style.State_None
            scrollOpt.state |= self._compat_style.State_DownArrow if isDown else self._compat_style.State_UpArrow
            scrollOpt.checkType = self._compat_style.CheckType_NotCheckable
            scrollOpt.maxIconWidth = scrollOpt.tabWidth = 0
            scrollOpt.rect = scrollRect
            scrollOpt.menuItemType = self._compat_style.MenuItemType_Scroller
            if enabled:
                frame = QtWidgets.QStyleOptionMenuItem()
                frame.initFrom(self)
                frame.rect = scrollRect
                frame.state = self._compat_style.combine_states(self._compat_style.State_Active,
                                                                self._compat_style.State_Enabled)
                style.drawControl(self._compat_style.CE_MenuItem, frame, qp, self)

                scrollOpt.state = self._compat_style.combine_states(scrollOpt.state, self._compat_style.State_Enabled)
                scrollOpt.palette.setCurrentColorGroup(QtGui.QPalette.Active)
            else:
                scrollOpt.palette.setCurrentColorGroup(QtGui.QPalette.Disabled)
            style.drawControl(self._compat_style.CE_MenuScroller, scrollOpt, qp, self)

        if fw:
            borderReg = QtGui.QRegion()
            borderReg |= QtGui.QRegion(QtCore.QRect(0, 0, fw, self.height()))
            borderReg |= QtGui.QRegion(QtCore.QRect(self.width() - fw, 0, fw, self.height()))
            borderReg |= QtGui.QRegion(QtCore.QRect(0, 0, self.width(), fw))
            borderReg |= QtGui.QRegion(QtCore.QRect(0, self.height() - fw, self.width(), fw))
            qp.setClipRegion(borderReg)
            emptyArea -= borderReg
            frame = QtWidgets.QStyleOptionFrame()
            frame.rect = rect
            frame.palette = self.palette()
            frame.state = self._compat_style.combine_states(self._compat_style.State_None,
                                                            self._compat_style.State_Active,
                                                            self._compat_style.State_Enabled)
            frame.lineWidth = style.pixelMetric(self._compat_style.PM_MenuPanelWidth, None, self)
            frame.midLineWidth = 0
            style.drawPrimitive(self._compat_style.PE_FrameMenu, frame, qp, self)

        qp.setClipRegion(emptyArea)
        menuOpt.state = self._compat_style.combine_states(self._compat_style.State_None,
                                                          self._compat_style.State_Enabled)
        menuOpt.menuItemType = self._compat_style.MenuItemType_EmptyArea
        menuOpt.checkType = self._compat_style.CheckType_NotCheckable
        menuOpt.rect = menuOpt.menuRect = rect
        style.drawControl(self._compat_style.CE_MenuEmptyArea, menuOpt, qp, self)


@property_mixin
class SearchableMenuBase(ScrollableMenuBase):
    def __init__(self, *args, **kwargs):
        super(SearchableMenuBase, self).__init__(*args, **kwargs)
        self.search_popup = MPopup(self)
        self.search_popup.setVisible(False)
        self.search_bar = MLineEdit(parent=self)
        self.search_label = QtWidgets.QLabel()

        self.search_bar.textChanged.connect(self.slot_search_change)
        search_key_event_partial = partial(self.search_key_event,
                                           self.search_bar.keyPressEvent)
        self.search_bar.keyPressEvent = search_key_event_partial
        self.aboutToHide.connect(lambda: self.search_bar.setText(""))

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.search_label)
        layout.addWidget(self.search_bar)
        self.search_popup.setLayout(layout)

        self.setProperty("search_placeholder", self.tr("Search Action..."))
        self.setProperty("search_label", self.tr("Search Action..."))

        self.setProperty("searchable", True)
        self.setProperty("search_re", "I")

    def search_key_event(self, call, event):
        key = event.key()
        # NOTES: support menu original key event on search bar
        if key in (
                QtCore.Qt.Key_Up,
                QtCore.Qt.Key_Down,
                QtCore.Qt.Key_Return,
                QtCore.Qt.Key_Enter,
        ):
            super(SearchableMenuBase, self).keyPressEvent(event)
        elif key == QtCore.Qt.Key_Tab:
            self.search_bar.setFocus()
        return call(event)

    def _set_search_label(self, value):
        self.search_label.setText(value)

    def _set_search_placeholder(self, value):
        self.search_bar.setPlaceholderText(value)

    def _set_search_re(self, value):
        if not isinstance(value, str):
            raise TypeError("`search_re` property should be a string type")

    def slot_search_change(self, text):
        flags = 0
        for m in self.property("search_re") or "":
            flags |= getattr(re, m.upper(), 0)
        search_reg = re.compile(r".*%s.*" % text, flags)
        self._update_search(search_reg)

    def _update_search(self, search_reg, parent_menu=None):
        actions = parent_menu.actions() if parent_menu else self.actions()
        vis_list = []
        for action in actions:
            menu = action.menu()
            if not menu:
                is_match = bool(re.match(search_reg, action.text()))
                action.setVisible(is_match)
                is_match and vis_list.append(action)
            else:
                is_match = bool(re.match(search_reg, menu.title()))
                self._update_search("" if is_match else search_reg, menu)

        if parent_menu:
            parent_menu.menuAction().setVisible(bool(vis_list) or not search_reg)

    def keyPressEvent(self, event):
        key = event.key()
        if self.property("searchable"):
            # NOTES(timmyliang): 26 character trigger search bar
            if 65 <= key <= 90:
                char = chr(key)
                self.search_bar.setText(char)
                self.search_bar.setFocus()
                self.search_bar.selectAll()
                width = self.sizeHint().width()
                width = width if width >= 50 else 50
                offset = QtCore.QPoint(width, 0)
                self.search_popup.move(self.pos() + offset)
                self.search_popup.show()
            elif key == QtCore.Qt.Key_Escape:
                self.search_bar.setText("")
                self.search_popup.hide()
        return super(SearchableMenuBase, self).keyPressEvent(event)


@property_mixin
class MMenu(SearchableMenuBase):
    sig_value_changed = QtCore.Signal(object)

    def __init__(self, exclusive=True, cascader=False, title="", parent=None):
        super(MMenu, self).__init__(title=title, parent=parent)
        self.setProperty("cascader", cascader)
        self.setCursor(QtCore.Qt.PointingHandCursor)
        self._action_group = QtWidgets.QActionGroup(self)
        self._action_group.setExclusive(exclusive)
        self._action_group.triggered.connect(self.slot_on_action_triggered)
        self._load_data_func = None
        self.set_value("")
        self.set_data([])
        self.set_separator("/")

    def set_separator(self, chr):
        self.setProperty("separator", chr)

    def set_load_callback(self, func):
        assert callable(func)
        self._load_data_func = func
        self.aboutToShow.connect(self.slot_fetch_data)

    def slot_fetch_data(self):
        data_list = self._load_data_func()
        self.set_data(data_list)

    def set_value(self, data):
        assert isinstance(data, (list, str, int, float))
        # if isinstance(data, int):
        #     action = self._action_group.actions()[data]
        #     data = action.property('value')
        if self.property("cascader") and isinstance(data, str):
            data = data.split(self.property("separator"))
        self.setProperty("value", data)

    def _set_value(self, value):
        data_list = value if isinstance(value, list) else [value]
        flag = False
        for act in self._action_group.actions():
            checked = act.property("value") in data_list
            if act.isChecked() != checked:  # 更新来自代码
                act.setChecked(checked)
                flag = True
        if flag:
            self.sig_value_changed.emit(value)

    def _add_menu(self, parent_menu, data_dict):
        if "children" in data_dict:
            menu = MMenu(title=data_dict.get("label"), parent=self)
            menu.setProperty("value", data_dict.get("value"))
            parent_menu.addMenu(menu)
            if parent_menu is not self:
                # 用来将来获取父层级数据
                menu.setProperty("parent_menu", parent_menu)
            for i in data_dict.get("children"):
                self._add_menu(menu, i)
        else:
            action = self._action_group.addAction(utils.display_formatter(data_dict.get("label")))
            action.setProperty("value", data_dict.get("value"))
            action.setCheckable(True)
            # 用来将来获取父层级数据
            action.setProperty("parent_menu", parent_menu)
            parent_menu.addAction(action)

    def set_data(self, option_list):
        assert isinstance(option_list, list)
        if option_list:
            if all(isinstance(i, str) for i in option_list):
                option_list = utils.from_list_to_nested_dict(option_list, sep=self.property("separator"))
            if all(isinstance(i, (int, float)) for i in option_list):
                option_list = [{"value": i, "label": str(i)} for i in option_list]
        # 全部转换成 dict 类型的 list
        self.setProperty("data", option_list)

    def _set_data(self, option_list):
        self.clear()
        for act in self._action_group.actions():
            self._action_group.removeAction(act)

        for data_dict in option_list:
            self._add_menu(self, data_dict)

    def _get_parent(self, result, obj):
        if obj.property("parent_menu"):
            parent_menu = obj.property("parent_menu")
            result.insert(0, parent_menu.property("value"))
            self._get_parent(result, parent_menu)

    def slot_on_action_triggered(self, action):
        current_data = action.property("value")
        if self.property("cascader"):
            selected_data = [current_data]
            self._get_parent(selected_data, action)
        else:
            if self._action_group.isExclusive():
                selected_data = current_data
            else:
                selected_data = [act.property("value") for act in self._action_group.actions() if act.isChecked()]
        self.set_value(selected_data)
        self.sig_value_changed.emit(selected_data)

    def set_loader(self, func):
        self._load_data_func = func
