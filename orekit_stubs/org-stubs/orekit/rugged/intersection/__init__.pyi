import org.hipparchus.geometry.euclidean.threed
import org.orekit.rugged.api
import org.orekit.rugged.intersection.duvenhage
import org.orekit.rugged.raster
import org.orekit.rugged.utils
import typing



class IntersectionAlgorithm:
    def getAlgorithmId(self) -> org.orekit.rugged.api.AlgorithmId: ...
    def getElevation(self, double: float, double2: float) -> float: ...
    def intersection(self, extendedEllipsoid: org.orekit.rugged.utils.ExtendedEllipsoid, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D, vector3D2: org.hipparchus.geometry.euclidean.threed.Vector3D) -> org.orekit.rugged.utils.NormalizedGeodeticPoint: ...
    def refineIntersection(self, extendedEllipsoid: org.orekit.rugged.utils.ExtendedEllipsoid, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D, vector3D2: org.hipparchus.geometry.euclidean.threed.Vector3D, normalizedGeodeticPoint: org.orekit.rugged.utils.NormalizedGeodeticPoint) -> org.orekit.rugged.utils.NormalizedGeodeticPoint: ...

class BasicScanAlgorithm(IntersectionAlgorithm):
    def __init__(self, tileUpdater: org.orekit.rugged.raster.TileUpdater, int: int): ...
    def getAlgorithmId(self) -> org.orekit.rugged.api.AlgorithmId: ...
    def getElevation(self, double: float, double2: float) -> float: ...
    def intersection(self, extendedEllipsoid: org.orekit.rugged.utils.ExtendedEllipsoid, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D, vector3D2: org.hipparchus.geometry.euclidean.threed.Vector3D) -> org.orekit.rugged.utils.NormalizedGeodeticPoint: ...
    def refineIntersection(self, extendedEllipsoid: org.orekit.rugged.utils.ExtendedEllipsoid, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D, vector3D2: org.hipparchus.geometry.euclidean.threed.Vector3D, normalizedGeodeticPoint: org.orekit.rugged.utils.NormalizedGeodeticPoint) -> org.orekit.rugged.utils.NormalizedGeodeticPoint: ...

class ConstantElevationAlgorithm(IntersectionAlgorithm):
    def __init__(self, double: float): ...
    def getAlgorithmId(self) -> org.orekit.rugged.api.AlgorithmId: ...
    def getElevation(self, double: float, double2: float) -> float: ...
    def intersection(self, extendedEllipsoid: org.orekit.rugged.utils.ExtendedEllipsoid, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D, vector3D2: org.hipparchus.geometry.euclidean.threed.Vector3D) -> org.orekit.rugged.utils.NormalizedGeodeticPoint: ...
    def refineIntersection(self, extendedEllipsoid: org.orekit.rugged.utils.ExtendedEllipsoid, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D, vector3D2: org.hipparchus.geometry.euclidean.threed.Vector3D, normalizedGeodeticPoint: org.orekit.rugged.utils.NormalizedGeodeticPoint) -> org.orekit.rugged.utils.NormalizedGeodeticPoint: ...

class IgnoreDEMAlgorithm(IntersectionAlgorithm):
    def __init__(self): ...
    def getAlgorithmId(self) -> org.orekit.rugged.api.AlgorithmId: ...
    def getElevation(self, double: float, double2: float) -> float: ...
    def intersection(self, extendedEllipsoid: org.orekit.rugged.utils.ExtendedEllipsoid, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D, vector3D2: org.hipparchus.geometry.euclidean.threed.Vector3D) -> org.orekit.rugged.utils.NormalizedGeodeticPoint: ...
    def refineIntersection(self, extendedEllipsoid: org.orekit.rugged.utils.ExtendedEllipsoid, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D, vector3D2: org.hipparchus.geometry.euclidean.threed.Vector3D, normalizedGeodeticPoint: org.orekit.rugged.utils.NormalizedGeodeticPoint) -> org.orekit.rugged.utils.NormalizedGeodeticPoint: ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.orekit.rugged.intersection")``.

    BasicScanAlgorithm: typing.Type[BasicScanAlgorithm]
    ConstantElevationAlgorithm: typing.Type[ConstantElevationAlgorithm]
    IgnoreDEMAlgorithm: typing.Type[IgnoreDEMAlgorithm]
    IntersectionAlgorithm: typing.Type[IntersectionAlgorithm]
    duvenhage: org.orekit.rugged.intersection.duvenhage.__module_protocol__
