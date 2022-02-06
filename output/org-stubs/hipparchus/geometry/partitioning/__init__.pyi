import java.lang
import java.util
import org.hipparchus.geometry
import typing



_BSPTree__LeafMerger__S = typing.TypeVar('_BSPTree__LeafMerger__S', bound=org.hipparchus.geometry.Space)  # <S>
_BSPTree__VanishingCutHandler__S = typing.TypeVar('_BSPTree__VanishingCutHandler__S', bound=org.hipparchus.geometry.Space)  # <S>
_BSPTree__S = typing.TypeVar('_BSPTree__S', bound=org.hipparchus.geometry.Space)  # <S>
class BSPTree(typing.Generic[_BSPTree__S]):
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, object: typing.Any): ...
    @typing.overload
    def __init__(self, subHyperplane: 'SubHyperplane'[_BSPTree__S], bSPTree: 'BSPTree'[_BSPTree__S], bSPTree2: 'BSPTree'[_BSPTree__S], object: typing.Any): ...
    def copySelf(self) -> 'BSPTree'[_BSPTree__S]: ...
    def getAttribute(self) -> typing.Any: ...
    def getCell(self, point: org.hipparchus.geometry.Point[_BSPTree__S], double: float) -> 'BSPTree'[_BSPTree__S]: ...
    def getCloseCuts(self, point: org.hipparchus.geometry.Point[_BSPTree__S], double: float) -> java.util.List['BSPTree'[_BSPTree__S]]: ...
    def getCut(self) -> 'SubHyperplane'[_BSPTree__S]: ...
    def getMinus(self) -> 'BSPTree'[_BSPTree__S]: ...
    def getParent(self) -> 'BSPTree'[_BSPTree__S]: ...
    def getPlus(self) -> 'BSPTree'[_BSPTree__S]: ...
    def insertCut(self, hyperplane: 'Hyperplane'[_BSPTree__S]) -> bool: ...
    def insertInTree(self, bSPTree: 'BSPTree'[_BSPTree__S], boolean: bool, vanishingCutHandler: 'BSPTree.VanishingCutHandler'[_BSPTree__S]) -> None: ...
    def merge(self, bSPTree: 'BSPTree'[_BSPTree__S], leafMerger: 'BSPTree.LeafMerger'[_BSPTree__S]) -> 'BSPTree'[_BSPTree__S]: ...
    def pruneAroundConvexCell(self, object: typing.Any, object2: typing.Any, object3: typing.Any) -> 'BSPTree'[_BSPTree__S]: ...
    def setAttribute(self, object: typing.Any) -> None: ...
    def split(self, subHyperplane: 'SubHyperplane'[_BSPTree__S]) -> 'BSPTree'[_BSPTree__S]: ...
    def visit(self, bSPTreeVisitor: 'BSPTreeVisitor'[_BSPTree__S]) -> None: ...
    class LeafMerger(typing.Generic[_BSPTree__LeafMerger__S]):
        def merge(self, bSPTree: 'BSPTree'[_BSPTree__LeafMerger__S], bSPTree2: 'BSPTree'[_BSPTree__LeafMerger__S], bSPTree3: 'BSPTree'[_BSPTree__LeafMerger__S], boolean: bool, boolean2: bool) -> 'BSPTree'[_BSPTree__LeafMerger__S]: ...
    class VanishingCutHandler(typing.Generic[_BSPTree__VanishingCutHandler__S]):
        def fixNode(self, bSPTree: 'BSPTree'[_BSPTree__VanishingCutHandler__S]) -> 'BSPTree'[_BSPTree__VanishingCutHandler__S]: ...

_BSPTreeVisitor__S = typing.TypeVar('_BSPTreeVisitor__S', bound=org.hipparchus.geometry.Space)  # <S>
class BSPTreeVisitor(typing.Generic[_BSPTreeVisitor__S]):
    def visitInternalNode(self, bSPTree: BSPTree[_BSPTreeVisitor__S]) -> None: ...
    def visitLeafNode(self, bSPTree: BSPTree[_BSPTreeVisitor__S]) -> None: ...
    def visitOrder(self, bSPTree: BSPTree[_BSPTreeVisitor__S]) -> 'BSPTreeVisitor.Order': ...
    class Order(java.lang.Enum['BSPTreeVisitor.Order']):
        PLUS_MINUS_SUB: typing.ClassVar['BSPTreeVisitor.Order'] = ...
        PLUS_SUB_MINUS: typing.ClassVar['BSPTreeVisitor.Order'] = ...
        MINUS_PLUS_SUB: typing.ClassVar['BSPTreeVisitor.Order'] = ...
        MINUS_SUB_PLUS: typing.ClassVar['BSPTreeVisitor.Order'] = ...
        SUB_PLUS_MINUS: typing.ClassVar['BSPTreeVisitor.Order'] = ...
        SUB_MINUS_PLUS: typing.ClassVar['BSPTreeVisitor.Order'] = ...
        _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
        @typing.overload
        @staticmethod
        def valueOf(class_: typing.Type[_valueOf_0__T], string: str) -> _valueOf_0__T: ...
        @typing.overload
        @staticmethod
        def valueOf(string: str) -> 'BSPTreeVisitor.Order': ...
        @staticmethod
        def values() -> typing.List['BSPTreeVisitor.Order']: ...

_BoundaryAttribute__S = typing.TypeVar('_BoundaryAttribute__S', bound=org.hipparchus.geometry.Space)  # <S>
class BoundaryAttribute(typing.Generic[_BoundaryAttribute__S]):
    def getPlusInside(self) -> 'SubHyperplane'[_BoundaryAttribute__S]: ...
    def getPlusOutside(self) -> 'SubHyperplane'[_BoundaryAttribute__S]: ...
    def getSplitters(self) -> 'NodesSet'[_BoundaryAttribute__S]: ...

_BoundaryProjection__S = typing.TypeVar('_BoundaryProjection__S', bound=org.hipparchus.geometry.Space)  # <S>
class BoundaryProjection(typing.Generic[_BoundaryProjection__S]):
    def __init__(self, point: org.hipparchus.geometry.Point[_BoundaryProjection__S], point2: org.hipparchus.geometry.Point[_BoundaryProjection__S], double: float): ...
    def getOffset(self) -> float: ...
    def getOriginal(self) -> org.hipparchus.geometry.Point[_BoundaryProjection__S]: ...
    def getProjected(self) -> org.hipparchus.geometry.Point[_BoundaryProjection__S]: ...

_Embedding__S = typing.TypeVar('_Embedding__S', bound=org.hipparchus.geometry.Space)  # <S>
_Embedding__T = typing.TypeVar('_Embedding__T', bound=org.hipparchus.geometry.Space)  # <T>
class Embedding(typing.Generic[_Embedding__S, _Embedding__T]):
    def toSpace(self, point: org.hipparchus.geometry.Point[_Embedding__T]) -> org.hipparchus.geometry.Point[_Embedding__S]: ...
    def toSubSpace(self, point: org.hipparchus.geometry.Point[_Embedding__S]) -> org.hipparchus.geometry.Point[_Embedding__T]: ...

_Hyperplane__S = typing.TypeVar('_Hyperplane__S', bound=org.hipparchus.geometry.Space)  # <S>
class Hyperplane(typing.Generic[_Hyperplane__S]):
    def copySelf(self) -> 'Hyperplane'[_Hyperplane__S]: ...
    def emptyHyperplane(self) -> 'SubHyperplane'[_Hyperplane__S]: ...
    def getOffset(self, point: org.hipparchus.geometry.Point[_Hyperplane__S]) -> float: ...
    def getTolerance(self) -> float: ...
    def project(self, point: org.hipparchus.geometry.Point[_Hyperplane__S]) -> org.hipparchus.geometry.Point[_Hyperplane__S]: ...
    def sameOrientationAs(self, hyperplane: 'Hyperplane'[_Hyperplane__S]) -> bool: ...
    def wholeHyperplane(self) -> 'SubHyperplane'[_Hyperplane__S]: ...
    def wholeSpace(self) -> 'Region'[_Hyperplane__S]: ...

_NodesSet__S = typing.TypeVar('_NodesSet__S', bound=org.hipparchus.geometry.Space)  # <S>
class NodesSet(java.lang.Iterable[BSPTree[_NodesSet__S]], typing.Generic[_NodesSet__S]):
    def __init__(self): ...
    def add(self, bSPTree: BSPTree[_NodesSet__S]) -> None: ...
    def addAll(self, iterable: typing.Union[java.lang.Iterable[BSPTree[_NodesSet__S]], typing.Sequence[BSPTree[_NodesSet__S]], typing.Set[BSPTree[_NodesSet__S]]]) -> None: ...
    def iterator(self) -> java.util.Iterator[BSPTree[_NodesSet__S]]: ...

_Region__S = typing.TypeVar('_Region__S', bound=org.hipparchus.geometry.Space)  # <S>
class Region(typing.Generic[_Region__S]):
    def buildNew(self, bSPTree: BSPTree[_Region__S]) -> 'Region'[_Region__S]: ...
    def checkPoint(self, point: org.hipparchus.geometry.Point[_Region__S]) -> 'Region.Location': ...
    def contains(self, region: 'Region'[_Region__S]) -> bool: ...
    def copySelf(self) -> 'Region'[_Region__S]: ...
    def getBarycenter(self) -> org.hipparchus.geometry.Point[_Region__S]: ...
    def getBoundarySize(self) -> float: ...
    def getSize(self) -> float: ...
    def getTree(self, boolean: bool) -> BSPTree[_Region__S]: ...
    def intersection(self, subHyperplane: 'SubHyperplane'[_Region__S]) -> 'SubHyperplane'[_Region__S]: ...
    @typing.overload
    def isEmpty(self) -> bool: ...
    @typing.overload
    def isEmpty(self, bSPTree: BSPTree[_Region__S]) -> bool: ...
    @typing.overload
    def isFull(self) -> bool: ...
    @typing.overload
    def isFull(self, bSPTree: BSPTree[_Region__S]) -> bool: ...
    def projectToBoundary(self, point: org.hipparchus.geometry.Point[_Region__S]) -> BoundaryProjection[_Region__S]: ...
    class Location(java.lang.Enum['Region.Location']):
        INSIDE: typing.ClassVar['Region.Location'] = ...
        OUTSIDE: typing.ClassVar['Region.Location'] = ...
        BOUNDARY: typing.ClassVar['Region.Location'] = ...
        _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
        @typing.overload
        @staticmethod
        def valueOf(class_: typing.Type[_valueOf_0__T], string: str) -> _valueOf_0__T: ...
        @typing.overload
        @staticmethod
        def valueOf(string: str) -> 'Region.Location': ...
        @staticmethod
        def values() -> typing.List['Region.Location']: ...

_RegionFactory__S = typing.TypeVar('_RegionFactory__S', bound=org.hipparchus.geometry.Space)  # <S>
class RegionFactory(typing.Generic[_RegionFactory__S]):
    def __init__(self): ...
    def buildConvex(self, hyperplaneArray: typing.List[Hyperplane[_RegionFactory__S]]) -> Region[_RegionFactory__S]: ...
    def difference(self, region: Region[_RegionFactory__S], region2: Region[_RegionFactory__S]) -> Region[_RegionFactory__S]: ...
    def getComplement(self, region: Region[_RegionFactory__S]) -> Region[_RegionFactory__S]: ...
    def intersection(self, region: Region[_RegionFactory__S], region2: Region[_RegionFactory__S]) -> Region[_RegionFactory__S]: ...
    def union(self, region: Region[_RegionFactory__S], region2: Region[_RegionFactory__S]) -> Region[_RegionFactory__S]: ...
    def xor(self, region: Region[_RegionFactory__S], region2: Region[_RegionFactory__S]) -> Region[_RegionFactory__S]: ...

class Side(java.lang.Enum['Side']):
    PLUS: typing.ClassVar['Side'] = ...
    MINUS: typing.ClassVar['Side'] = ...
    BOTH: typing.ClassVar['Side'] = ...
    HYPER: typing.ClassVar['Side'] = ...
    _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(class_: typing.Type[_valueOf_0__T], string: str) -> _valueOf_0__T: ...
    @typing.overload
    @staticmethod
    def valueOf(string: str) -> 'Side': ...
    @staticmethod
    def values() -> typing.List['Side']: ...

_SubHyperplane__SplitSubHyperplane__U = typing.TypeVar('_SubHyperplane__SplitSubHyperplane__U', bound=org.hipparchus.geometry.Space)  # <U>
_SubHyperplane__S = typing.TypeVar('_SubHyperplane__S', bound=org.hipparchus.geometry.Space)  # <S>
class SubHyperplane(typing.Generic[_SubHyperplane__S]):
    def copySelf(self) -> 'SubHyperplane'[_SubHyperplane__S]: ...
    def getHyperplane(self) -> Hyperplane[_SubHyperplane__S]: ...
    def getSize(self) -> float: ...
    def isEmpty(self) -> bool: ...
    def reunite(self, subHyperplane: 'SubHyperplane'[_SubHyperplane__S]) -> 'SubHyperplane'[_SubHyperplane__S]: ...
    def split(self, hyperplane: Hyperplane[_SubHyperplane__S]) -> 'SubHyperplane.SplitSubHyperplane'[_SubHyperplane__S]: ...
    class SplitSubHyperplane(typing.Generic[_SubHyperplane__SplitSubHyperplane__U]):
        def __init__(self, subHyperplane: 'SubHyperplane'[_SubHyperplane__SplitSubHyperplane__U], subHyperplane2: 'SubHyperplane'[_SubHyperplane__SplitSubHyperplane__U]): ...
        def getMinus(self) -> 'SubHyperplane'[_SubHyperplane__SplitSubHyperplane__U]: ...
        def getPlus(self) -> 'SubHyperplane'[_SubHyperplane__SplitSubHyperplane__U]: ...
        def getSide(self) -> Side: ...

_Transform__S = typing.TypeVar('_Transform__S', bound=org.hipparchus.geometry.Space)  # <S>
_Transform__T = typing.TypeVar('_Transform__T', bound=org.hipparchus.geometry.Space)  # <T>
class Transform(typing.Generic[_Transform__S, _Transform__T]):
    @typing.overload
    def apply(self, point: org.hipparchus.geometry.Point[_Transform__S]) -> org.hipparchus.geometry.Point[_Transform__S]: ...
    @typing.overload
    def apply(self, hyperplane: Hyperplane[_Transform__S]) -> Hyperplane[_Transform__S]: ...
    @typing.overload
    def apply(self, subHyperplane: SubHyperplane[_Transform__T], hyperplane: Hyperplane[_Transform__S], hyperplane2: Hyperplane[_Transform__S]) -> SubHyperplane[_Transform__T]: ...

_AbstractRegion__S = typing.TypeVar('_AbstractRegion__S', bound=org.hipparchus.geometry.Space)  # <S>
_AbstractRegion__T = typing.TypeVar('_AbstractRegion__T', bound=org.hipparchus.geometry.Space)  # <T>
class AbstractRegion(Region[_AbstractRegion__S], typing.Generic[_AbstractRegion__S, _AbstractRegion__T]):
    def __init__(self, hyperplaneArray: typing.List[Hyperplane[_AbstractRegion__S]], double: float): ...
    def applyTransform(self, transform: Transform[_AbstractRegion__S, _AbstractRegion__T]) -> 'AbstractRegion'[_AbstractRegion__S, _AbstractRegion__T]: ...
    def buildNew(self, bSPTree: BSPTree[_AbstractRegion__S]) -> 'AbstractRegion'[_AbstractRegion__S, _AbstractRegion__T]: ...
    @typing.overload
    def checkPoint(self, point: org.hipparchus.geometry.Point[_AbstractRegion__S]) -> Region.Location: ...
    @typing.overload
    def checkPoint(self, vector: org.hipparchus.geometry.Vector[_AbstractRegion__S]) -> Region.Location: ...
    def contains(self, region: Region[_AbstractRegion__S]) -> bool: ...
    def copySelf(self) -> 'AbstractRegion'[_AbstractRegion__S, _AbstractRegion__T]: ...
    def getBarycenter(self) -> org.hipparchus.geometry.Point[_AbstractRegion__S]: ...
    def getBoundarySize(self) -> float: ...
    def getSize(self) -> float: ...
    def getTolerance(self) -> float: ...
    def getTree(self, boolean: bool) -> BSPTree[_AbstractRegion__S]: ...
    def intersection(self, subHyperplane: SubHyperplane[_AbstractRegion__S]) -> SubHyperplane[_AbstractRegion__S]: ...
    @typing.overload
    def isEmpty(self) -> bool: ...
    @typing.overload
    def isEmpty(self, bSPTree: BSPTree[_AbstractRegion__S]) -> bool: ...
    @typing.overload
    def isFull(self) -> bool: ...
    @typing.overload
    def isFull(self, bSPTree: BSPTree[_AbstractRegion__S]) -> bool: ...
    def projectToBoundary(self, point: org.hipparchus.geometry.Point[_AbstractRegion__S]) -> BoundaryProjection[_AbstractRegion__S]: ...

_AbstractSubHyperplane__S = typing.TypeVar('_AbstractSubHyperplane__S', bound=org.hipparchus.geometry.Space)  # <S>
_AbstractSubHyperplane__T = typing.TypeVar('_AbstractSubHyperplane__T', bound=org.hipparchus.geometry.Space)  # <T>
class AbstractSubHyperplane(SubHyperplane[_AbstractSubHyperplane__S], typing.Generic[_AbstractSubHyperplane__S, _AbstractSubHyperplane__T]):
    def applyTransform(self, transform: Transform[_AbstractSubHyperplane__S, _AbstractSubHyperplane__T]) -> 'AbstractSubHyperplane'[_AbstractSubHyperplane__S, _AbstractSubHyperplane__T]: ...
    def copySelf(self) -> 'AbstractSubHyperplane'[_AbstractSubHyperplane__S, _AbstractSubHyperplane__T]: ...
    def getHyperplane(self) -> Hyperplane[_AbstractSubHyperplane__S]: ...
    def getRemainingRegion(self) -> Region[_AbstractSubHyperplane__T]: ...
    def getSize(self) -> float: ...
    def isEmpty(self) -> bool: ...
    def reunite(self, subHyperplane: SubHyperplane[_AbstractSubHyperplane__S]) -> 'AbstractSubHyperplane'[_AbstractSubHyperplane__S, _AbstractSubHyperplane__T]: ...
    def split(self, hyperplane: Hyperplane[_AbstractSubHyperplane__S]) -> SubHyperplane.SplitSubHyperplane[_AbstractSubHyperplane__S]: ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.hipparchus.geometry.partitioning")``.

    AbstractRegion: typing.Type[AbstractRegion]
    AbstractSubHyperplane: typing.Type[AbstractSubHyperplane]
    BSPTree: typing.Type[BSPTree]
    BSPTreeVisitor: typing.Type[BSPTreeVisitor]
    BoundaryAttribute: typing.Type[BoundaryAttribute]
    BoundaryProjection: typing.Type[BoundaryProjection]
    Embedding: typing.Type[Embedding]
    Hyperplane: typing.Type[Hyperplane]
    NodesSet: typing.Type[NodesSet]
    Region: typing.Type[Region]
    RegionFactory: typing.Type[RegionFactory]
    Side: typing.Type[Side]
    SubHyperplane: typing.Type[SubHyperplane]
    Transform: typing.Type[Transform]