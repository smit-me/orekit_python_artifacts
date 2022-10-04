import java.awt
import java.beans
import java.io
import java.net
import java.util
import typing



class BeanContextChild:
    def addPropertyChangeListener(self, string: str, propertyChangeListener: java.beans.PropertyChangeListener) -> None: ...
    def addVetoableChangeListener(self, string: str, vetoableChangeListener: java.beans.VetoableChangeListener) -> None: ...
    def getBeanContext(self) -> 'BeanContext': ...
    def removePropertyChangeListener(self, string: str, propertyChangeListener: java.beans.PropertyChangeListener) -> None: ...
    def removeVetoableChangeListener(self, string: str, vetoableChangeListener: java.beans.VetoableChangeListener) -> None: ...
    def setBeanContext(self, beanContext: 'BeanContext') -> None: ...

class BeanContextChildComponentProxy:
    def getComponent(self) -> java.awt.Component: ...

class BeanContextContainerProxy:
    def getContainer(self) -> java.awt.Container: ...

class BeanContextEvent(java.util.EventObject):
    def getBeanContext(self) -> 'BeanContext': ...
    def getPropagatedFrom(self) -> 'BeanContext': ...
    def isPropagated(self) -> bool: ...
    def setPropagatedFrom(self, beanContext: 'BeanContext') -> None: ...

class BeanContextMembershipListener(java.util.EventListener):
    def childrenAdded(self, beanContextMembershipEvent: 'BeanContextMembershipEvent') -> None: ...
    def childrenRemoved(self, beanContextMembershipEvent: 'BeanContextMembershipEvent') -> None: ...

class BeanContextProxy:
    def getBeanContextProxy(self) -> BeanContextChild: ...

class BeanContextServiceProvider:
    def getCurrentServiceSelectors(self, beanContextServices: 'BeanContextServices', class_: typing.Type) -> java.util.Iterator: ...
    def getService(self, beanContextServices: 'BeanContextServices', object: typing.Any, class_: typing.Type, object2: typing.Any) -> typing.Any: ...
    def releaseService(self, beanContextServices: 'BeanContextServices', object: typing.Any, object2: typing.Any) -> None: ...

class BeanContextServiceProviderBeanInfo(java.beans.BeanInfo):
    def getServicesBeanInfo(self) -> typing.List[java.beans.BeanInfo]: ...

class BeanContextServiceRevokedListener(java.util.EventListener):
    def serviceRevoked(self, beanContextServiceRevokedEvent: 'BeanContextServiceRevokedEvent') -> None: ...

class BeanContext(BeanContextChild, java.util.Collection, java.beans.DesignMode, java.beans.Visibility):
    globalHierarchyLock: typing.ClassVar[typing.Any] = ...
    def addBeanContextMembershipListener(self, beanContextMembershipListener: BeanContextMembershipListener) -> None: ...
    def equals(self, object: typing.Any) -> bool: ...
    def getResource(self, string: str, beanContextChild: BeanContextChild) -> java.net.URL: ...
    def getResourceAsStream(self, string: str, beanContextChild: BeanContextChild) -> java.io.InputStream: ...
    def hashCode(self) -> int: ...
    def instantiateChild(self, string: str) -> typing.Any: ...
    def removeBeanContextMembershipListener(self, beanContextMembershipListener: BeanContextMembershipListener) -> None: ...

class BeanContextMembershipEvent(BeanContextEvent):
    @typing.overload
    def __init__(self, beanContext: BeanContext, objectArray: typing.List[typing.Any]): ...
    @typing.overload
    def __init__(self, beanContext: BeanContext, collection: typing.Union[java.util.Collection, typing.Sequence, typing.Set]): ...
    def contains(self, object: typing.Any) -> bool: ...
    def iterator(self) -> java.util.Iterator: ...
    def size(self) -> int: ...
    def toArray(self) -> typing.List[typing.Any]: ...

class BeanContextServiceAvailableEvent(BeanContextEvent):
    def __init__(self, beanContextServices: 'BeanContextServices', class_: typing.Type): ...
    def getCurrentServiceSelectors(self) -> java.util.Iterator: ...
    def getServiceClass(self) -> typing.Type: ...
    def getSourceAsBeanContextServices(self) -> 'BeanContextServices': ...

class BeanContextServiceRevokedEvent(BeanContextEvent):
    def __init__(self, beanContextServices: 'BeanContextServices', class_: typing.Type, boolean: bool): ...
    def getServiceClass(self) -> typing.Type: ...
    def getSourceAsBeanContextServices(self) -> 'BeanContextServices': ...
    def isCurrentServiceInvalidNow(self) -> bool: ...
    def isServiceClass(self, class_: typing.Type) -> bool: ...

class BeanContextServicesListener(BeanContextServiceRevokedListener):
    def serviceAvailable(self, beanContextServiceAvailableEvent: BeanContextServiceAvailableEvent) -> None: ...

class BeanContextChildSupport(BeanContextChild, BeanContextServicesListener, java.io.Serializable):
    beanContextChildPeer: BeanContextChild = ...
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, beanContextChild: BeanContextChild): ...
    def addPropertyChangeListener(self, string: str, propertyChangeListener: java.beans.PropertyChangeListener) -> None: ...
    def addVetoableChangeListener(self, string: str, vetoableChangeListener: java.beans.VetoableChangeListener) -> None: ...
    def firePropertyChange(self, string: str, object: typing.Any, object2: typing.Any) -> None: ...
    def fireVetoableChange(self, string: str, object: typing.Any, object2: typing.Any) -> None: ...
    def getBeanContext(self) -> BeanContext: ...
    def getBeanContextChildPeer(self) -> BeanContextChild: ...
    def isDelegated(self) -> bool: ...
    def removePropertyChangeListener(self, string: str, propertyChangeListener: java.beans.PropertyChangeListener) -> None: ...
    def removeVetoableChangeListener(self, string: str, vetoableChangeListener: java.beans.VetoableChangeListener) -> None: ...
    def serviceAvailable(self, beanContextServiceAvailableEvent: BeanContextServiceAvailableEvent) -> None: ...
    def serviceRevoked(self, beanContextServiceRevokedEvent: BeanContextServiceRevokedEvent) -> None: ...
    def setBeanContext(self, beanContext: BeanContext) -> None: ...
    def validatePendingSetBeanContext(self, beanContext: BeanContext) -> bool: ...

class BeanContextServices(BeanContext, BeanContextServicesListener):
    def addBeanContextServicesListener(self, beanContextServicesListener: BeanContextServicesListener) -> None: ...
    def addService(self, class_: typing.Type, beanContextServiceProvider: BeanContextServiceProvider) -> bool: ...
    def equals(self, object: typing.Any) -> bool: ...
    def getCurrentServiceClasses(self) -> java.util.Iterator: ...
    def getCurrentServiceSelectors(self, class_: typing.Type) -> java.util.Iterator: ...
    def getService(self, beanContextChild: BeanContextChild, object: typing.Any, class_: typing.Type, object2: typing.Any, beanContextServiceRevokedListener: BeanContextServiceRevokedListener) -> typing.Any: ...
    def hasService(self, class_: typing.Type) -> bool: ...
    def hashCode(self) -> int: ...
    def releaseService(self, beanContextChild: BeanContextChild, object: typing.Any, object2: typing.Any) -> None: ...
    def removeBeanContextServicesListener(self, beanContextServicesListener: BeanContextServicesListener) -> None: ...
    def revokeService(self, class_: typing.Type, beanContextServiceProvider: BeanContextServiceProvider, boolean: bool) -> None: ...

class BeanContextSupport(BeanContextChildSupport, BeanContext, java.io.Serializable, java.beans.PropertyChangeListener, java.beans.VetoableChangeListener):
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, beanContext: BeanContext): ...
    @typing.overload
    def __init__(self, beanContext: BeanContext, locale: java.util.Locale): ...
    @typing.overload
    def __init__(self, beanContext: BeanContext, locale: java.util.Locale, boolean: bool): ...
    @typing.overload
    def __init__(self, beanContext: BeanContext, locale: java.util.Locale, boolean: bool, boolean2: bool): ...
    def add(self, object: typing.Any) -> bool: ...
    def addAll(self, collection: typing.Union[java.util.Collection, typing.Sequence, typing.Set]) -> bool: ...
    def addBeanContextMembershipListener(self, beanContextMembershipListener: BeanContextMembershipListener) -> None: ...
    def avoidingGui(self) -> bool: ...
    def clear(self) -> None: ...
    def contains(self, object: typing.Any) -> bool: ...
    def containsAll(self, collection: typing.Union[java.util.Collection, typing.Sequence, typing.Set]) -> bool: ...
    def containsKey(self, object: typing.Any) -> bool: ...
    def dontUseGui(self) -> None: ...
    def getBeanContextPeer(self) -> BeanContext: ...
    def getLocale(self) -> java.util.Locale: ...
    def getResource(self, string: str, beanContextChild: BeanContextChild) -> java.net.URL: ...
    def getResourceAsStream(self, string: str, beanContextChild: BeanContextChild) -> java.io.InputStream: ...
    def instantiateChild(self, string: str) -> typing.Any: ...
    def isDesignTime(self) -> bool: ...
    def isEmpty(self) -> bool: ...
    def isSerializing(self) -> bool: ...
    def iterator(self) -> java.util.Iterator: ...
    def needsGui(self) -> bool: ...
    def okToUseGui(self) -> None: ...
    def propertyChange(self, propertyChangeEvent: java.beans.PropertyChangeEvent) -> None: ...
    def readChildren(self, objectInputStream: java.io.ObjectInputStream) -> None: ...
    def remove(self, object: typing.Any) -> bool: ...
    def removeAll(self, collection: typing.Union[java.util.Collection, typing.Sequence, typing.Set]) -> bool: ...
    def removeBeanContextMembershipListener(self, beanContextMembershipListener: BeanContextMembershipListener) -> None: ...
    def retainAll(self, collection: typing.Union[java.util.Collection, typing.Sequence, typing.Set]) -> bool: ...
    def setDesignTime(self, boolean: bool) -> None: ...
    def setLocale(self, locale: java.util.Locale) -> None: ...
    def size(self) -> int: ...
    @typing.overload
    def toArray(self) -> typing.List[typing.Any]: ...
    @typing.overload
    def toArray(self, objectArray: typing.List[typing.Any]) -> typing.List[typing.Any]: ...
    def vetoableChange(self, propertyChangeEvent: java.beans.PropertyChangeEvent) -> None: ...
    def writeChildren(self, objectOutputStream: java.io.ObjectOutputStream) -> None: ...

class BeanContextServicesSupport(BeanContextSupport, BeanContextServices):
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, beanContextServices: BeanContextServices): ...
    @typing.overload
    def __init__(self, beanContextServices: BeanContextServices, locale: java.util.Locale): ...
    @typing.overload
    def __init__(self, beanContextServices: BeanContextServices, locale: java.util.Locale, boolean: bool): ...
    @typing.overload
    def __init__(self, beanContextServices: BeanContextServices, locale: java.util.Locale, boolean: bool, boolean2: bool): ...
    def addBeanContextServicesListener(self, beanContextServicesListener: BeanContextServicesListener) -> None: ...
    def addService(self, class_: typing.Type, beanContextServiceProvider: BeanContextServiceProvider) -> bool: ...
    def getBeanContextServicesPeer(self) -> BeanContextServices: ...
    def getCurrentServiceClasses(self) -> java.util.Iterator: ...
    def getCurrentServiceSelectors(self, class_: typing.Type) -> java.util.Iterator: ...
    def getService(self, beanContextChild: BeanContextChild, object: typing.Any, class_: typing.Type, object2: typing.Any, beanContextServiceRevokedListener: BeanContextServiceRevokedListener) -> typing.Any: ...
    def hasService(self, class_: typing.Type) -> bool: ...
    def initialize(self) -> None: ...
    def releaseService(self, beanContextChild: BeanContextChild, object: typing.Any, object2: typing.Any) -> None: ...
    def removeBeanContextServicesListener(self, beanContextServicesListener: BeanContextServicesListener) -> None: ...
    def revokeService(self, class_: typing.Type, beanContextServiceProvider: BeanContextServiceProvider, boolean: bool) -> None: ...
    def serviceAvailable(self, beanContextServiceAvailableEvent: BeanContextServiceAvailableEvent) -> None: ...
    def serviceRevoked(self, beanContextServiceRevokedEvent: BeanContextServiceRevokedEvent) -> None: ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("java.beans.beancontext")``.

    BeanContext: typing.Type[BeanContext]
    BeanContextChild: typing.Type[BeanContextChild]
    BeanContextChildComponentProxy: typing.Type[BeanContextChildComponentProxy]
    BeanContextChildSupport: typing.Type[BeanContextChildSupport]
    BeanContextContainerProxy: typing.Type[BeanContextContainerProxy]
    BeanContextEvent: typing.Type[BeanContextEvent]
    BeanContextMembershipEvent: typing.Type[BeanContextMembershipEvent]
    BeanContextMembershipListener: typing.Type[BeanContextMembershipListener]
    BeanContextProxy: typing.Type[BeanContextProxy]
    BeanContextServiceAvailableEvent: typing.Type[BeanContextServiceAvailableEvent]
    BeanContextServiceProvider: typing.Type[BeanContextServiceProvider]
    BeanContextServiceProviderBeanInfo: typing.Type[BeanContextServiceProviderBeanInfo]
    BeanContextServiceRevokedEvent: typing.Type[BeanContextServiceRevokedEvent]
    BeanContextServiceRevokedListener: typing.Type[BeanContextServiceRevokedListener]
    BeanContextServices: typing.Type[BeanContextServices]
    BeanContextServicesListener: typing.Type[BeanContextServicesListener]
    BeanContextServicesSupport: typing.Type[BeanContextServicesSupport]
    BeanContextSupport: typing.Type[BeanContextSupport]
