import java.awt
import java.awt.font
import java.lang
import java.text
import java.util
import typing



class AWTEventListener(java.util.EventListener):
    def eventDispatched(self, aWTEvent: java.awt.AWTEvent) -> None: ...

class ActionEvent(java.awt.AWTEvent):
    SHIFT_MASK: typing.ClassVar[int] = ...
    CTRL_MASK: typing.ClassVar[int] = ...
    META_MASK: typing.ClassVar[int] = ...
    ALT_MASK: typing.ClassVar[int] = ...
    ACTION_FIRST: typing.ClassVar[int] = ...
    ACTION_LAST: typing.ClassVar[int] = ...
    ACTION_PERFORMED: typing.ClassVar[int] = ...
    @typing.overload
    def __init__(self, object: typing.Any, int: int, string: str): ...
    @typing.overload
    def __init__(self, object: typing.Any, int: int, string: str, int2: int): ...
    @typing.overload
    def __init__(self, object: typing.Any, int: int, string: str, long: int, int2: int): ...
    def getActionCommand(self) -> str: ...
    def getModifiers(self) -> int: ...
    def getWhen(self) -> int: ...
    def paramString(self) -> str: ...

class ActionListener(java.util.EventListener):
    def actionPerformed(self, actionEvent: ActionEvent) -> None: ...

class AdjustmentEvent(java.awt.AWTEvent):
    ADJUSTMENT_FIRST: typing.ClassVar[int] = ...
    ADJUSTMENT_LAST: typing.ClassVar[int] = ...
    ADJUSTMENT_VALUE_CHANGED: typing.ClassVar[int] = ...
    UNIT_INCREMENT: typing.ClassVar[int] = ...
    UNIT_DECREMENT: typing.ClassVar[int] = ...
    BLOCK_DECREMENT: typing.ClassVar[int] = ...
    BLOCK_INCREMENT: typing.ClassVar[int] = ...
    TRACK: typing.ClassVar[int] = ...
    @typing.overload
    def __init__(self, adjustable: java.awt.Adjustable, int: int, int2: int, int3: int): ...
    @typing.overload
    def __init__(self, adjustable: java.awt.Adjustable, int: int, int2: int, int3: int, boolean: bool): ...
    def getAdjustable(self) -> java.awt.Adjustable: ...
    def getAdjustmentType(self) -> int: ...
    def getValue(self) -> int: ...
    def getValueIsAdjusting(self) -> bool: ...
    def paramString(self) -> str: ...

class AdjustmentListener(java.util.EventListener):
    def adjustmentValueChanged(self, adjustmentEvent: AdjustmentEvent) -> None: ...

class ComponentEvent(java.awt.AWTEvent):
    COMPONENT_FIRST: typing.ClassVar[int] = ...
    COMPONENT_LAST: typing.ClassVar[int] = ...
    COMPONENT_MOVED: typing.ClassVar[int] = ...
    COMPONENT_RESIZED: typing.ClassVar[int] = ...
    COMPONENT_SHOWN: typing.ClassVar[int] = ...
    COMPONENT_HIDDEN: typing.ClassVar[int] = ...
    def __init__(self, component: java.awt.Component, int: int): ...
    def getComponent(self) -> java.awt.Component: ...
    def paramString(self) -> str: ...

class ComponentListener(java.util.EventListener):
    def componentHidden(self, componentEvent: ComponentEvent) -> None: ...
    def componentMoved(self, componentEvent: ComponentEvent) -> None: ...
    def componentResized(self, componentEvent: ComponentEvent) -> None: ...
    def componentShown(self, componentEvent: ComponentEvent) -> None: ...

class ContainerListener(java.util.EventListener):
    def componentAdded(self, containerEvent: 'ContainerEvent') -> None: ...
    def componentRemoved(self, containerEvent: 'ContainerEvent') -> None: ...

class FocusListener(java.util.EventListener):
    def focusGained(self, focusEvent: 'FocusEvent') -> None: ...
    def focusLost(self, focusEvent: 'FocusEvent') -> None: ...

class HierarchyBoundsListener(java.util.EventListener):
    def ancestorMoved(self, hierarchyEvent: 'HierarchyEvent') -> None: ...
    def ancestorResized(self, hierarchyEvent: 'HierarchyEvent') -> None: ...

class HierarchyEvent(java.awt.AWTEvent):
    HIERARCHY_FIRST: typing.ClassVar[int] = ...
    HIERARCHY_CHANGED: typing.ClassVar[int] = ...
    ANCESTOR_MOVED: typing.ClassVar[int] = ...
    ANCESTOR_RESIZED: typing.ClassVar[int] = ...
    HIERARCHY_LAST: typing.ClassVar[int] = ...
    PARENT_CHANGED: typing.ClassVar[int] = ...
    DISPLAYABILITY_CHANGED: typing.ClassVar[int] = ...
    SHOWING_CHANGED: typing.ClassVar[int] = ...
    @typing.overload
    def __init__(self, component: java.awt.Component, int: int, component2: java.awt.Component, container: java.awt.Container): ...
    @typing.overload
    def __init__(self, component: java.awt.Component, int: int, component2: java.awt.Component, container: java.awt.Container, long: int): ...
    def getChangeFlags(self) -> int: ...
    def getChanged(self) -> java.awt.Component: ...
    def getChangedParent(self) -> java.awt.Container: ...
    def getComponent(self) -> java.awt.Component: ...
    def paramString(self) -> str: ...

class HierarchyListener(java.util.EventListener):
    def hierarchyChanged(self, hierarchyEvent: HierarchyEvent) -> None: ...

class InputMethodEvent(java.awt.AWTEvent):
    INPUT_METHOD_FIRST: typing.ClassVar[int] = ...
    INPUT_METHOD_TEXT_CHANGED: typing.ClassVar[int] = ...
    CARET_POSITION_CHANGED: typing.ClassVar[int] = ...
    INPUT_METHOD_LAST: typing.ClassVar[int] = ...
    @typing.overload
    def __init__(self, component: java.awt.Component, int: int, textHitInfo: java.awt.font.TextHitInfo, textHitInfo2: java.awt.font.TextHitInfo): ...
    @typing.overload
    def __init__(self, component: java.awt.Component, int: int, attributedCharacterIterator: java.text.AttributedCharacterIterator, int2: int, textHitInfo: java.awt.font.TextHitInfo, textHitInfo2: java.awt.font.TextHitInfo): ...
    @typing.overload
    def __init__(self, component: java.awt.Component, int: int, long: int, attributedCharacterIterator: java.text.AttributedCharacterIterator, int2: int, textHitInfo: java.awt.font.TextHitInfo, textHitInfo2: java.awt.font.TextHitInfo): ...
    def consume(self) -> None: ...
    def getCaret(self) -> java.awt.font.TextHitInfo: ...
    def getCommittedCharacterCount(self) -> int: ...
    def getText(self) -> java.text.AttributedCharacterIterator: ...
    def getVisiblePosition(self) -> java.awt.font.TextHitInfo: ...
    def getWhen(self) -> int: ...
    def isConsumed(self) -> bool: ...
    def paramString(self) -> str: ...

class InputMethodListener(java.util.EventListener):
    def caretPositionChanged(self, inputMethodEvent: InputMethodEvent) -> None: ...
    def inputMethodTextChanged(self, inputMethodEvent: InputMethodEvent) -> None: ...

class InvocationEvent(java.awt.AWTEvent, java.awt.ActiveEvent):
    INVOCATION_FIRST: typing.ClassVar[int] = ...
    INVOCATION_DEFAULT: typing.ClassVar[int] = ...
    INVOCATION_LAST: typing.ClassVar[int] = ...
    @typing.overload
    def __init__(self, object: typing.Any, runnable: typing.Union[java.lang.Runnable, typing.Callable]): ...
    @typing.overload
    def __init__(self, object: typing.Any, runnable: typing.Union[java.lang.Runnable, typing.Callable], object2: typing.Any, boolean: bool): ...
    @typing.overload
    def __init__(self, object: typing.Any, runnable: typing.Union[java.lang.Runnable, typing.Callable], runnable2: typing.Union[java.lang.Runnable, typing.Callable], boolean: bool): ...
    def dispatch(self) -> None: ...
    def getException(self) -> java.lang.Exception: ...
    def getThrowable(self) -> java.lang.Throwable: ...
    def getWhen(self) -> int: ...
    def isDispatched(self) -> bool: ...
    def paramString(self) -> str: ...

class ItemEvent(java.awt.AWTEvent):
    ITEM_FIRST: typing.ClassVar[int] = ...
    ITEM_LAST: typing.ClassVar[int] = ...
    ITEM_STATE_CHANGED: typing.ClassVar[int] = ...
    SELECTED: typing.ClassVar[int] = ...
    DESELECTED: typing.ClassVar[int] = ...
    def __init__(self, itemSelectable: java.awt.ItemSelectable, int: int, object: typing.Any, int2: int): ...
    def getItem(self) -> typing.Any: ...
    def getItemSelectable(self) -> java.awt.ItemSelectable: ...
    def getStateChange(self) -> int: ...
    def paramString(self) -> str: ...

class ItemListener(java.util.EventListener):
    def itemStateChanged(self, itemEvent: ItemEvent) -> None: ...

class KeyListener(java.util.EventListener):
    def keyPressed(self, keyEvent: 'KeyEvent') -> None: ...
    def keyReleased(self, keyEvent: 'KeyEvent') -> None: ...
    def keyTyped(self, keyEvent: 'KeyEvent') -> None: ...

class MouseListener(java.util.EventListener):
    def mouseClicked(self, mouseEvent: 'MouseEvent') -> None: ...
    def mouseEntered(self, mouseEvent: 'MouseEvent') -> None: ...
    def mouseExited(self, mouseEvent: 'MouseEvent') -> None: ...
    def mousePressed(self, mouseEvent: 'MouseEvent') -> None: ...
    def mouseReleased(self, mouseEvent: 'MouseEvent') -> None: ...

class MouseMotionListener(java.util.EventListener):
    def mouseDragged(self, mouseEvent: 'MouseEvent') -> None: ...
    def mouseMoved(self, mouseEvent: 'MouseEvent') -> None: ...

class MouseWheelListener(java.util.EventListener):
    def mouseWheelMoved(self, mouseWheelEvent: 'MouseWheelEvent') -> None: ...

class TextEvent(java.awt.AWTEvent):
    TEXT_FIRST: typing.ClassVar[int] = ...
    TEXT_LAST: typing.ClassVar[int] = ...
    TEXT_VALUE_CHANGED: typing.ClassVar[int] = ...
    def __init__(self, object: typing.Any, int: int): ...
    def paramString(self) -> str: ...

class TextListener(java.util.EventListener):
    def textValueChanged(self, textEvent: TextEvent) -> None: ...

class WindowFocusListener(java.util.EventListener):
    def windowGainedFocus(self, windowEvent: 'WindowEvent') -> None: ...
    def windowLostFocus(self, windowEvent: 'WindowEvent') -> None: ...

class WindowListener(java.util.EventListener):
    def windowActivated(self, windowEvent: 'WindowEvent') -> None: ...
    def windowClosed(self, windowEvent: 'WindowEvent') -> None: ...
    def windowClosing(self, windowEvent: 'WindowEvent') -> None: ...
    def windowDeactivated(self, windowEvent: 'WindowEvent') -> None: ...
    def windowDeiconified(self, windowEvent: 'WindowEvent') -> None: ...
    def windowIconified(self, windowEvent: 'WindowEvent') -> None: ...
    def windowOpened(self, windowEvent: 'WindowEvent') -> None: ...

class WindowStateListener(java.util.EventListener):
    def windowStateChanged(self, windowEvent: 'WindowEvent') -> None: ...

class AWTEventListenerProxy(java.util.EventListenerProxy[AWTEventListener], AWTEventListener):
    def __init__(self, long: int, aWTEventListener: AWTEventListener): ...
    def eventDispatched(self, aWTEvent: java.awt.AWTEvent) -> None: ...
    def getEventMask(self) -> int: ...

class ComponentAdapter(ComponentListener):
    def componentHidden(self, componentEvent: ComponentEvent) -> None: ...
    def componentMoved(self, componentEvent: ComponentEvent) -> None: ...
    def componentResized(self, componentEvent: ComponentEvent) -> None: ...
    def componentShown(self, componentEvent: ComponentEvent) -> None: ...

class ContainerAdapter(ContainerListener):
    def componentAdded(self, containerEvent: 'ContainerEvent') -> None: ...
    def componentRemoved(self, containerEvent: 'ContainerEvent') -> None: ...

class ContainerEvent(ComponentEvent):
    CONTAINER_FIRST: typing.ClassVar[int] = ...
    CONTAINER_LAST: typing.ClassVar[int] = ...
    COMPONENT_ADDED: typing.ClassVar[int] = ...
    COMPONENT_REMOVED: typing.ClassVar[int] = ...
    def __init__(self, component: java.awt.Component, int: int, component2: java.awt.Component): ...
    def getChild(self) -> java.awt.Component: ...
    def getContainer(self) -> java.awt.Container: ...
    def paramString(self) -> str: ...

class FocusAdapter(FocusListener):
    def focusGained(self, focusEvent: 'FocusEvent') -> None: ...
    def focusLost(self, focusEvent: 'FocusEvent') -> None: ...

class FocusEvent(ComponentEvent):
    FOCUS_FIRST: typing.ClassVar[int] = ...
    FOCUS_LAST: typing.ClassVar[int] = ...
    FOCUS_GAINED: typing.ClassVar[int] = ...
    FOCUS_LOST: typing.ClassVar[int] = ...
    @typing.overload
    def __init__(self, component: java.awt.Component, int: int): ...
    @typing.overload
    def __init__(self, component: java.awt.Component, int: int, boolean: bool): ...
    @typing.overload
    def __init__(self, component: java.awt.Component, int: int, boolean: bool, component2: java.awt.Component): ...
    @typing.overload
    def __init__(self, component: java.awt.Component, int: int, boolean: bool, component2: java.awt.Component, cause: 'FocusEvent.Cause'): ...
    def getCause(self) -> 'FocusEvent.Cause': ...
    def getOppositeComponent(self) -> java.awt.Component: ...
    def isTemporary(self) -> bool: ...
    def paramString(self) -> str: ...
    class Cause(java.lang.Enum['FocusEvent.Cause']):
        UNKNOWN: typing.ClassVar['FocusEvent.Cause'] = ...
        MOUSE_EVENT: typing.ClassVar['FocusEvent.Cause'] = ...
        TRAVERSAL: typing.ClassVar['FocusEvent.Cause'] = ...
        TRAVERSAL_UP: typing.ClassVar['FocusEvent.Cause'] = ...
        TRAVERSAL_DOWN: typing.ClassVar['FocusEvent.Cause'] = ...
        TRAVERSAL_FORWARD: typing.ClassVar['FocusEvent.Cause'] = ...
        TRAVERSAL_BACKWARD: typing.ClassVar['FocusEvent.Cause'] = ...
        ROLLBACK: typing.ClassVar['FocusEvent.Cause'] = ...
        UNEXPECTED: typing.ClassVar['FocusEvent.Cause'] = ...
        ACTIVATION: typing.ClassVar['FocusEvent.Cause'] = ...
        CLEAR_GLOBAL_FOCUS_OWNER: typing.ClassVar['FocusEvent.Cause'] = ...
        _valueOf_1__T = typing.TypeVar('_valueOf_1__T', bound=java.lang.Enum)  # <T>
        @typing.overload
        @staticmethod
        def valueOf(string: str) -> 'FocusEvent.Cause': ...
        @typing.overload
        @staticmethod
        def valueOf(class_: typing.Type[_valueOf_1__T], string: str) -> _valueOf_1__T: ...
        @staticmethod
        def values() -> typing.List['FocusEvent.Cause']: ...

class HierarchyBoundsAdapter(HierarchyBoundsListener):
    def ancestorMoved(self, hierarchyEvent: HierarchyEvent) -> None: ...
    def ancestorResized(self, hierarchyEvent: HierarchyEvent) -> None: ...

class InputEvent(ComponentEvent):
    SHIFT_MASK: typing.ClassVar[int] = ...
    CTRL_MASK: typing.ClassVar[int] = ...
    META_MASK: typing.ClassVar[int] = ...
    ALT_MASK: typing.ClassVar[int] = ...
    ALT_GRAPH_MASK: typing.ClassVar[int] = ...
    BUTTON1_MASK: typing.ClassVar[int] = ...
    BUTTON2_MASK: typing.ClassVar[int] = ...
    BUTTON3_MASK: typing.ClassVar[int] = ...
    SHIFT_DOWN_MASK: typing.ClassVar[int] = ...
    CTRL_DOWN_MASK: typing.ClassVar[int] = ...
    META_DOWN_MASK: typing.ClassVar[int] = ...
    ALT_DOWN_MASK: typing.ClassVar[int] = ...
    BUTTON1_DOWN_MASK: typing.ClassVar[int] = ...
    BUTTON2_DOWN_MASK: typing.ClassVar[int] = ...
    BUTTON3_DOWN_MASK: typing.ClassVar[int] = ...
    ALT_GRAPH_DOWN_MASK: typing.ClassVar[int] = ...
    def consume(self) -> None: ...
    @staticmethod
    def getMaskForButton(int: int) -> int: ...
    def getModifiers(self) -> int: ...
    def getModifiersEx(self) -> int: ...
    @staticmethod
    def getModifiersExText(int: int) -> str: ...
    def getWhen(self) -> int: ...
    def isAltDown(self) -> bool: ...
    def isAltGraphDown(self) -> bool: ...
    def isConsumed(self) -> bool: ...
    def isControlDown(self) -> bool: ...
    def isMetaDown(self) -> bool: ...
    def isShiftDown(self) -> bool: ...

class KeyAdapter(KeyListener):
    def keyPressed(self, keyEvent: 'KeyEvent') -> None: ...
    def keyReleased(self, keyEvent: 'KeyEvent') -> None: ...
    def keyTyped(self, keyEvent: 'KeyEvent') -> None: ...

class MouseAdapter(MouseListener, MouseWheelListener, MouseMotionListener):
    def mouseClicked(self, mouseEvent: 'MouseEvent') -> None: ...
    def mouseDragged(self, mouseEvent: 'MouseEvent') -> None: ...
    def mouseEntered(self, mouseEvent: 'MouseEvent') -> None: ...
    def mouseExited(self, mouseEvent: 'MouseEvent') -> None: ...
    def mouseMoved(self, mouseEvent: 'MouseEvent') -> None: ...
    def mousePressed(self, mouseEvent: 'MouseEvent') -> None: ...
    def mouseReleased(self, mouseEvent: 'MouseEvent') -> None: ...
    def mouseWheelMoved(self, mouseWheelEvent: 'MouseWheelEvent') -> None: ...

class MouseMotionAdapter(MouseMotionListener):
    def mouseDragged(self, mouseEvent: 'MouseEvent') -> None: ...
    def mouseMoved(self, mouseEvent: 'MouseEvent') -> None: ...

class PaintEvent(ComponentEvent):
    PAINT_FIRST: typing.ClassVar[int] = ...
    PAINT_LAST: typing.ClassVar[int] = ...
    PAINT: typing.ClassVar[int] = ...
    UPDATE: typing.ClassVar[int] = ...
    def __init__(self, component: java.awt.Component, int: int, rectangle: java.awt.Rectangle): ...
    def getUpdateRect(self) -> java.awt.Rectangle: ...
    def paramString(self) -> str: ...
    def setUpdateRect(self, rectangle: java.awt.Rectangle) -> None: ...

class WindowAdapter(WindowListener, WindowStateListener, WindowFocusListener):
    def windowActivated(self, windowEvent: 'WindowEvent') -> None: ...
    def windowClosed(self, windowEvent: 'WindowEvent') -> None: ...
    def windowClosing(self, windowEvent: 'WindowEvent') -> None: ...
    def windowDeactivated(self, windowEvent: 'WindowEvent') -> None: ...
    def windowDeiconified(self, windowEvent: 'WindowEvent') -> None: ...
    def windowGainedFocus(self, windowEvent: 'WindowEvent') -> None: ...
    def windowIconified(self, windowEvent: 'WindowEvent') -> None: ...
    def windowLostFocus(self, windowEvent: 'WindowEvent') -> None: ...
    def windowOpened(self, windowEvent: 'WindowEvent') -> None: ...
    def windowStateChanged(self, windowEvent: 'WindowEvent') -> None: ...

class WindowEvent(ComponentEvent):
    WINDOW_FIRST: typing.ClassVar[int] = ...
    WINDOW_OPENED: typing.ClassVar[int] = ...
    WINDOW_CLOSING: typing.ClassVar[int] = ...
    WINDOW_CLOSED: typing.ClassVar[int] = ...
    WINDOW_ICONIFIED: typing.ClassVar[int] = ...
    WINDOW_DEICONIFIED: typing.ClassVar[int] = ...
    WINDOW_ACTIVATED: typing.ClassVar[int] = ...
    WINDOW_DEACTIVATED: typing.ClassVar[int] = ...
    WINDOW_GAINED_FOCUS: typing.ClassVar[int] = ...
    WINDOW_LOST_FOCUS: typing.ClassVar[int] = ...
    WINDOW_STATE_CHANGED: typing.ClassVar[int] = ...
    WINDOW_LAST: typing.ClassVar[int] = ...
    @typing.overload
    def __init__(self, window: java.awt.Window, int: int): ...
    @typing.overload
    def __init__(self, window: java.awt.Window, int: int, int2: int, int3: int): ...
    @typing.overload
    def __init__(self, window: java.awt.Window, int: int, window2: java.awt.Window): ...
    @typing.overload
    def __init__(self, window: java.awt.Window, int: int, window2: java.awt.Window, int2: int, int3: int): ...
    def getNewState(self) -> int: ...
    def getOldState(self) -> int: ...
    def getOppositeWindow(self) -> java.awt.Window: ...
    def getWindow(self) -> java.awt.Window: ...
    def paramString(self) -> str: ...

class KeyEvent(InputEvent):
    KEY_FIRST: typing.ClassVar[int] = ...
    KEY_LAST: typing.ClassVar[int] = ...
    KEY_TYPED: typing.ClassVar[int] = ...
    KEY_PRESSED: typing.ClassVar[int] = ...
    KEY_RELEASED: typing.ClassVar[int] = ...
    VK_ENTER: typing.ClassVar[int] = ...
    VK_BACK_SPACE: typing.ClassVar[int] = ...
    VK_TAB: typing.ClassVar[int] = ...
    VK_CANCEL: typing.ClassVar[int] = ...
    VK_CLEAR: typing.ClassVar[int] = ...
    VK_SHIFT: typing.ClassVar[int] = ...
    VK_CONTROL: typing.ClassVar[int] = ...
    VK_ALT: typing.ClassVar[int] = ...
    VK_PAUSE: typing.ClassVar[int] = ...
    VK_CAPS_LOCK: typing.ClassVar[int] = ...
    VK_ESCAPE: typing.ClassVar[int] = ...
    VK_SPACE: typing.ClassVar[int] = ...
    VK_PAGE_UP: typing.ClassVar[int] = ...
    VK_PAGE_DOWN: typing.ClassVar[int] = ...
    VK_END: typing.ClassVar[int] = ...
    VK_HOME: typing.ClassVar[int] = ...
    VK_LEFT: typing.ClassVar[int] = ...
    VK_UP: typing.ClassVar[int] = ...
    VK_RIGHT: typing.ClassVar[int] = ...
    VK_DOWN: typing.ClassVar[int] = ...
    VK_COMMA: typing.ClassVar[int] = ...
    VK_MINUS: typing.ClassVar[int] = ...
    VK_PERIOD: typing.ClassVar[int] = ...
    VK_SLASH: typing.ClassVar[int] = ...
    VK_0: typing.ClassVar[int] = ...
    VK_1: typing.ClassVar[int] = ...
    VK_2: typing.ClassVar[int] = ...
    VK_3: typing.ClassVar[int] = ...
    VK_4: typing.ClassVar[int] = ...
    VK_5: typing.ClassVar[int] = ...
    VK_6: typing.ClassVar[int] = ...
    VK_7: typing.ClassVar[int] = ...
    VK_8: typing.ClassVar[int] = ...
    VK_9: typing.ClassVar[int] = ...
    VK_SEMICOLON: typing.ClassVar[int] = ...
    VK_EQUALS: typing.ClassVar[int] = ...
    VK_A: typing.ClassVar[int] = ...
    VK_B: typing.ClassVar[int] = ...
    VK_C: typing.ClassVar[int] = ...
    VK_D: typing.ClassVar[int] = ...
    VK_E: typing.ClassVar[int] = ...
    VK_F: typing.ClassVar[int] = ...
    VK_G: typing.ClassVar[int] = ...
    VK_H: typing.ClassVar[int] = ...
    VK_I: typing.ClassVar[int] = ...
    VK_J: typing.ClassVar[int] = ...
    VK_K: typing.ClassVar[int] = ...
    VK_L: typing.ClassVar[int] = ...
    VK_M: typing.ClassVar[int] = ...
    VK_N: typing.ClassVar[int] = ...
    VK_O: typing.ClassVar[int] = ...
    VK_P: typing.ClassVar[int] = ...
    VK_Q: typing.ClassVar[int] = ...
    VK_R: typing.ClassVar[int] = ...
    VK_S: typing.ClassVar[int] = ...
    VK_T: typing.ClassVar[int] = ...
    VK_U: typing.ClassVar[int] = ...
    VK_V: typing.ClassVar[int] = ...
    VK_W: typing.ClassVar[int] = ...
    VK_X: typing.ClassVar[int] = ...
    VK_Y: typing.ClassVar[int] = ...
    VK_Z: typing.ClassVar[int] = ...
    VK_OPEN_BRACKET: typing.ClassVar[int] = ...
    VK_BACK_SLASH: typing.ClassVar[int] = ...
    VK_CLOSE_BRACKET: typing.ClassVar[int] = ...
    VK_NUMPAD0: typing.ClassVar[int] = ...
    VK_NUMPAD1: typing.ClassVar[int] = ...
    VK_NUMPAD2: typing.ClassVar[int] = ...
    VK_NUMPAD3: typing.ClassVar[int] = ...
    VK_NUMPAD4: typing.ClassVar[int] = ...
    VK_NUMPAD5: typing.ClassVar[int] = ...
    VK_NUMPAD6: typing.ClassVar[int] = ...
    VK_NUMPAD7: typing.ClassVar[int] = ...
    VK_NUMPAD8: typing.ClassVar[int] = ...
    VK_NUMPAD9: typing.ClassVar[int] = ...
    VK_MULTIPLY: typing.ClassVar[int] = ...
    VK_ADD: typing.ClassVar[int] = ...
    VK_SEPARATER: typing.ClassVar[int] = ...
    VK_SEPARATOR: typing.ClassVar[int] = ...
    VK_SUBTRACT: typing.ClassVar[int] = ...
    VK_DECIMAL: typing.ClassVar[int] = ...
    VK_DIVIDE: typing.ClassVar[int] = ...
    VK_DELETE: typing.ClassVar[int] = ...
    VK_NUM_LOCK: typing.ClassVar[int] = ...
    VK_SCROLL_LOCK: typing.ClassVar[int] = ...
    VK_F1: typing.ClassVar[int] = ...
    VK_F2: typing.ClassVar[int] = ...
    VK_F3: typing.ClassVar[int] = ...
    VK_F4: typing.ClassVar[int] = ...
    VK_F5: typing.ClassVar[int] = ...
    VK_F6: typing.ClassVar[int] = ...
    VK_F7: typing.ClassVar[int] = ...
    VK_F8: typing.ClassVar[int] = ...
    VK_F9: typing.ClassVar[int] = ...
    VK_F10: typing.ClassVar[int] = ...
    VK_F11: typing.ClassVar[int] = ...
    VK_F12: typing.ClassVar[int] = ...
    VK_F13: typing.ClassVar[int] = ...
    VK_F14: typing.ClassVar[int] = ...
    VK_F15: typing.ClassVar[int] = ...
    VK_F16: typing.ClassVar[int] = ...
    VK_F17: typing.ClassVar[int] = ...
    VK_F18: typing.ClassVar[int] = ...
    VK_F19: typing.ClassVar[int] = ...
    VK_F20: typing.ClassVar[int] = ...
    VK_F21: typing.ClassVar[int] = ...
    VK_F22: typing.ClassVar[int] = ...
    VK_F23: typing.ClassVar[int] = ...
    VK_F24: typing.ClassVar[int] = ...
    VK_PRINTSCREEN: typing.ClassVar[int] = ...
    VK_INSERT: typing.ClassVar[int] = ...
    VK_HELP: typing.ClassVar[int] = ...
    VK_META: typing.ClassVar[int] = ...
    VK_BACK_QUOTE: typing.ClassVar[int] = ...
    VK_QUOTE: typing.ClassVar[int] = ...
    VK_KP_UP: typing.ClassVar[int] = ...
    VK_KP_DOWN: typing.ClassVar[int] = ...
    VK_KP_LEFT: typing.ClassVar[int] = ...
    VK_KP_RIGHT: typing.ClassVar[int] = ...
    VK_DEAD_GRAVE: typing.ClassVar[int] = ...
    VK_DEAD_ACUTE: typing.ClassVar[int] = ...
    VK_DEAD_CIRCUMFLEX: typing.ClassVar[int] = ...
    VK_DEAD_TILDE: typing.ClassVar[int] = ...
    VK_DEAD_MACRON: typing.ClassVar[int] = ...
    VK_DEAD_BREVE: typing.ClassVar[int] = ...
    VK_DEAD_ABOVEDOT: typing.ClassVar[int] = ...
    VK_DEAD_DIAERESIS: typing.ClassVar[int] = ...
    VK_DEAD_ABOVERING: typing.ClassVar[int] = ...
    VK_DEAD_DOUBLEACUTE: typing.ClassVar[int] = ...
    VK_DEAD_CARON: typing.ClassVar[int] = ...
    VK_DEAD_CEDILLA: typing.ClassVar[int] = ...
    VK_DEAD_OGONEK: typing.ClassVar[int] = ...
    VK_DEAD_IOTA: typing.ClassVar[int] = ...
    VK_DEAD_VOICED_SOUND: typing.ClassVar[int] = ...
    VK_DEAD_SEMIVOICED_SOUND: typing.ClassVar[int] = ...
    VK_AMPERSAND: typing.ClassVar[int] = ...
    VK_ASTERISK: typing.ClassVar[int] = ...
    VK_QUOTEDBL: typing.ClassVar[int] = ...
    VK_LESS: typing.ClassVar[int] = ...
    VK_GREATER: typing.ClassVar[int] = ...
    VK_BRACELEFT: typing.ClassVar[int] = ...
    VK_BRACERIGHT: typing.ClassVar[int] = ...
    VK_AT: typing.ClassVar[int] = ...
    VK_COLON: typing.ClassVar[int] = ...
    VK_CIRCUMFLEX: typing.ClassVar[int] = ...
    VK_DOLLAR: typing.ClassVar[int] = ...
    VK_EURO_SIGN: typing.ClassVar[int] = ...
    VK_EXCLAMATION_MARK: typing.ClassVar[int] = ...
    VK_INVERTED_EXCLAMATION_MARK: typing.ClassVar[int] = ...
    VK_LEFT_PARENTHESIS: typing.ClassVar[int] = ...
    VK_NUMBER_SIGN: typing.ClassVar[int] = ...
    VK_PLUS: typing.ClassVar[int] = ...
    VK_RIGHT_PARENTHESIS: typing.ClassVar[int] = ...
    VK_UNDERSCORE: typing.ClassVar[int] = ...
    VK_WINDOWS: typing.ClassVar[int] = ...
    VK_CONTEXT_MENU: typing.ClassVar[int] = ...
    VK_FINAL: typing.ClassVar[int] = ...
    VK_CONVERT: typing.ClassVar[int] = ...
    VK_NONCONVERT: typing.ClassVar[int] = ...
    VK_ACCEPT: typing.ClassVar[int] = ...
    VK_MODECHANGE: typing.ClassVar[int] = ...
    VK_KANA: typing.ClassVar[int] = ...
    VK_KANJI: typing.ClassVar[int] = ...
    VK_ALPHANUMERIC: typing.ClassVar[int] = ...
    VK_KATAKANA: typing.ClassVar[int] = ...
    VK_HIRAGANA: typing.ClassVar[int] = ...
    VK_FULL_WIDTH: typing.ClassVar[int] = ...
    VK_HALF_WIDTH: typing.ClassVar[int] = ...
    VK_ROMAN_CHARACTERS: typing.ClassVar[int] = ...
    VK_ALL_CANDIDATES: typing.ClassVar[int] = ...
    VK_PREVIOUS_CANDIDATE: typing.ClassVar[int] = ...
    VK_CODE_INPUT: typing.ClassVar[int] = ...
    VK_JAPANESE_KATAKANA: typing.ClassVar[int] = ...
    VK_JAPANESE_HIRAGANA: typing.ClassVar[int] = ...
    VK_JAPANESE_ROMAN: typing.ClassVar[int] = ...
    VK_KANA_LOCK: typing.ClassVar[int] = ...
    VK_INPUT_METHOD_ON_OFF: typing.ClassVar[int] = ...
    VK_CUT: typing.ClassVar[int] = ...
    VK_COPY: typing.ClassVar[int] = ...
    VK_PASTE: typing.ClassVar[int] = ...
    VK_UNDO: typing.ClassVar[int] = ...
    VK_AGAIN: typing.ClassVar[int] = ...
    VK_FIND: typing.ClassVar[int] = ...
    VK_PROPS: typing.ClassVar[int] = ...
    VK_STOP: typing.ClassVar[int] = ...
    VK_COMPOSE: typing.ClassVar[int] = ...
    VK_ALT_GRAPH: typing.ClassVar[int] = ...
    VK_BEGIN: typing.ClassVar[int] = ...
    VK_UNDEFINED: typing.ClassVar[int] = ...
    CHAR_UNDEFINED: typing.ClassVar[str] = ...
    KEY_LOCATION_UNKNOWN: typing.ClassVar[int] = ...
    KEY_LOCATION_STANDARD: typing.ClassVar[int] = ...
    KEY_LOCATION_LEFT: typing.ClassVar[int] = ...
    KEY_LOCATION_RIGHT: typing.ClassVar[int] = ...
    KEY_LOCATION_NUMPAD: typing.ClassVar[int] = ...
    @typing.overload
    def __init__(self, component: java.awt.Component, int: int, long: int, int2: int, int3: int): ...
    @typing.overload
    def __init__(self, component: java.awt.Component, int: int, long: int, int2: int, int3: int, char: str): ...
    @typing.overload
    def __init__(self, component: java.awt.Component, int: int, long: int, int2: int, int3: int, char: str, int4: int): ...
    def getExtendedKeyCode(self) -> int: ...
    @staticmethod
    def getExtendedKeyCodeForChar(int: int) -> int: ...
    def getKeyChar(self) -> str: ...
    def getKeyCode(self) -> int: ...
    def getKeyLocation(self) -> int: ...
    @staticmethod
    def getKeyModifiersText(int: int) -> str: ...
    @staticmethod
    def getKeyText(int: int) -> str: ...
    def isActionKey(self) -> bool: ...
    def paramString(self) -> str: ...
    def setKeyChar(self, char: str) -> None: ...
    def setKeyCode(self, int: int) -> None: ...
    def setModifiers(self, int: int) -> None: ...

class MouseEvent(InputEvent):
    MOUSE_FIRST: typing.ClassVar[int] = ...
    MOUSE_LAST: typing.ClassVar[int] = ...
    MOUSE_CLICKED: typing.ClassVar[int] = ...
    MOUSE_PRESSED: typing.ClassVar[int] = ...
    MOUSE_RELEASED: typing.ClassVar[int] = ...
    MOUSE_MOVED: typing.ClassVar[int] = ...
    MOUSE_ENTERED: typing.ClassVar[int] = ...
    MOUSE_EXITED: typing.ClassVar[int] = ...
    MOUSE_DRAGGED: typing.ClassVar[int] = ...
    MOUSE_WHEEL: typing.ClassVar[int] = ...
    NOBUTTON: typing.ClassVar[int] = ...
    BUTTON1: typing.ClassVar[int] = ...
    BUTTON2: typing.ClassVar[int] = ...
    BUTTON3: typing.ClassVar[int] = ...
    @typing.overload
    def __init__(self, component: java.awt.Component, int: int, long: int, int2: int, int3: int, int4: int, int5: int, boolean: bool): ...
    @typing.overload
    def __init__(self, component: java.awt.Component, int: int, long: int, int2: int, int3: int, int4: int, int5: int, boolean: bool, int6: int): ...
    @typing.overload
    def __init__(self, component: java.awt.Component, int: int, long: int, int2: int, int3: int, int4: int, int5: int, int6: int, int7: int, boolean: bool, int8: int): ...
    def getButton(self) -> int: ...
    def getClickCount(self) -> int: ...
    def getLocationOnScreen(self) -> java.awt.Point: ...
    def getModifiersEx(self) -> int: ...
    @staticmethod
    def getMouseModifiersText(int: int) -> str: ...
    def getPoint(self) -> java.awt.Point: ...
    def getX(self) -> int: ...
    def getXOnScreen(self) -> int: ...
    def getY(self) -> int: ...
    def getYOnScreen(self) -> int: ...
    def isPopupTrigger(self) -> bool: ...
    def paramString(self) -> str: ...
    def translatePoint(self, int: int, int2: int) -> None: ...

class MouseWheelEvent(MouseEvent):
    WHEEL_UNIT_SCROLL: typing.ClassVar[int] = ...
    WHEEL_BLOCK_SCROLL: typing.ClassVar[int] = ...
    @typing.overload
    def __init__(self, component: java.awt.Component, int: int, long: int, int2: int, int3: int, int4: int, int5: int, boolean: bool, int6: int, int7: int, int8: int): ...
    @typing.overload
    def __init__(self, component: java.awt.Component, int: int, long: int, int2: int, int3: int, int4: int, int5: int, int6: int, int7: int, boolean: bool, int8: int, int9: int, int10: int): ...
    @typing.overload
    def __init__(self, component: java.awt.Component, int: int, long: int, int2: int, int3: int, int4: int, int5: int, int6: int, int7: int, boolean: bool, int8: int, int9: int, int10: int, double: float): ...
    def getPreciseWheelRotation(self) -> float: ...
    def getScrollAmount(self) -> int: ...
    def getScrollType(self) -> int: ...
    def getUnitsToScroll(self) -> int: ...
    def getWheelRotation(self) -> int: ...
    def paramString(self) -> str: ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("java.awt.event")``.

    AWTEventListener: typing.Type[AWTEventListener]
    AWTEventListenerProxy: typing.Type[AWTEventListenerProxy]
    ActionEvent: typing.Type[ActionEvent]
    ActionListener: typing.Type[ActionListener]
    AdjustmentEvent: typing.Type[AdjustmentEvent]
    AdjustmentListener: typing.Type[AdjustmentListener]
    ComponentAdapter: typing.Type[ComponentAdapter]
    ComponentEvent: typing.Type[ComponentEvent]
    ComponentListener: typing.Type[ComponentListener]
    ContainerAdapter: typing.Type[ContainerAdapter]
    ContainerEvent: typing.Type[ContainerEvent]
    ContainerListener: typing.Type[ContainerListener]
    FocusAdapter: typing.Type[FocusAdapter]
    FocusEvent: typing.Type[FocusEvent]
    FocusListener: typing.Type[FocusListener]
    HierarchyBoundsAdapter: typing.Type[HierarchyBoundsAdapter]
    HierarchyBoundsListener: typing.Type[HierarchyBoundsListener]
    HierarchyEvent: typing.Type[HierarchyEvent]
    HierarchyListener: typing.Type[HierarchyListener]
    InputEvent: typing.Type[InputEvent]
    InputMethodEvent: typing.Type[InputMethodEvent]
    InputMethodListener: typing.Type[InputMethodListener]
    InvocationEvent: typing.Type[InvocationEvent]
    ItemEvent: typing.Type[ItemEvent]
    ItemListener: typing.Type[ItemListener]
    KeyAdapter: typing.Type[KeyAdapter]
    KeyEvent: typing.Type[KeyEvent]
    KeyListener: typing.Type[KeyListener]
    MouseAdapter: typing.Type[MouseAdapter]
    MouseEvent: typing.Type[MouseEvent]
    MouseListener: typing.Type[MouseListener]
    MouseMotionAdapter: typing.Type[MouseMotionAdapter]
    MouseMotionListener: typing.Type[MouseMotionListener]
    MouseWheelEvent: typing.Type[MouseWheelEvent]
    MouseWheelListener: typing.Type[MouseWheelListener]
    PaintEvent: typing.Type[PaintEvent]
    TextEvent: typing.Type[TextEvent]
    TextListener: typing.Type[TextListener]
    WindowAdapter: typing.Type[WindowAdapter]
    WindowEvent: typing.Type[WindowEvent]
    WindowFocusListener: typing.Type[WindowFocusListener]
    WindowListener: typing.Type[WindowListener]
    WindowStateListener: typing.Type[WindowStateListener]
