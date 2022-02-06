import org.hipparchus.geometry.euclidean.threed
import org.orekit.estimation.measurements
import org.orekit.frames
import org.orekit.orbits
import org.orekit.time
import org.orekit.utils
import typing



class IodGibbs:
    def __init__(self, double: float): ...
    @typing.overload
    def estimate(self, frame: org.orekit.frames.Frame, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D, absoluteDate: org.orekit.time.AbsoluteDate, vector3D2: org.hipparchus.geometry.euclidean.threed.Vector3D, absoluteDate2: org.orekit.time.AbsoluteDate, vector3D3: org.hipparchus.geometry.euclidean.threed.Vector3D, absoluteDate3: org.orekit.time.AbsoluteDate) -> org.orekit.orbits.KeplerianOrbit: ...
    @typing.overload
    def estimate(self, frame: org.orekit.frames.Frame, pV: org.orekit.estimation.measurements.PV, pV2: org.orekit.estimation.measurements.PV, pV3: org.orekit.estimation.measurements.PV) -> org.orekit.orbits.KeplerianOrbit: ...
    @typing.overload
    def estimate(self, frame: org.orekit.frames.Frame, position: org.orekit.estimation.measurements.Position, position2: org.orekit.estimation.measurements.Position, position3: org.orekit.estimation.measurements.Position) -> org.orekit.orbits.KeplerianOrbit: ...

class IodGooding:
    def __init__(self, double: float): ...
    @typing.overload
    def estimate(self, frame: org.orekit.frames.Frame, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D, vector3D2: org.hipparchus.geometry.euclidean.threed.Vector3D, vector3D3: org.hipparchus.geometry.euclidean.threed.Vector3D, vector3D4: org.hipparchus.geometry.euclidean.threed.Vector3D, absoluteDate: org.orekit.time.AbsoluteDate, vector3D5: org.hipparchus.geometry.euclidean.threed.Vector3D, absoluteDate2: org.orekit.time.AbsoluteDate, vector3D6: org.hipparchus.geometry.euclidean.threed.Vector3D, absoluteDate3: org.orekit.time.AbsoluteDate, double: float, double2: float) -> org.orekit.orbits.KeplerianOrbit: ...
    @typing.overload
    def estimate(self, frame: org.orekit.frames.Frame, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D, vector3D2: org.hipparchus.geometry.euclidean.threed.Vector3D, vector3D3: org.hipparchus.geometry.euclidean.threed.Vector3D, vector3D4: org.hipparchus.geometry.euclidean.threed.Vector3D, absoluteDate: org.orekit.time.AbsoluteDate, vector3D5: org.hipparchus.geometry.euclidean.threed.Vector3D, absoluteDate2: org.orekit.time.AbsoluteDate, vector3D6: org.hipparchus.geometry.euclidean.threed.Vector3D, absoluteDate3: org.orekit.time.AbsoluteDate, double: float, double2: float, int: int, boolean: bool) -> org.orekit.orbits.KeplerianOrbit: ...
    @typing.overload
    def estimate(self, frame: org.orekit.frames.Frame, angularRaDec: org.orekit.estimation.measurements.AngularRaDec, angularRaDec2: org.orekit.estimation.measurements.AngularRaDec, angularRaDec3: org.orekit.estimation.measurements.AngularRaDec, double: float, double2: float) -> org.orekit.orbits.KeplerianOrbit: ...
    @typing.overload
    def estimate(self, frame: org.orekit.frames.Frame, angularRaDec: org.orekit.estimation.measurements.AngularRaDec, angularRaDec2: org.orekit.estimation.measurements.AngularRaDec, angularRaDec3: org.orekit.estimation.measurements.AngularRaDec, double: float, double2: float, int: int, boolean: bool) -> org.orekit.orbits.KeplerianOrbit: ...
    def getRange1(self) -> float: ...
    def getRange2(self) -> float: ...
    def getRange3(self) -> float: ...
    @typing.overload
    @staticmethod
    def lineOfSight(double: float, double2: float) -> org.hipparchus.geometry.euclidean.threed.Vector3D: ...
    @typing.overload
    @staticmethod
    def lineOfSight(angularRaDec: org.orekit.estimation.measurements.AngularRaDec) -> org.hipparchus.geometry.euclidean.threed.Vector3D: ...

class IodLambert:
    def __init__(self, double: float): ...
    @typing.overload
    def estimate(self, frame: org.orekit.frames.Frame, boolean: bool, int: int, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D, absoluteDate: org.orekit.time.AbsoluteDate, vector3D2: org.hipparchus.geometry.euclidean.threed.Vector3D, absoluteDate2: org.orekit.time.AbsoluteDate) -> org.orekit.orbits.KeplerianOrbit: ...
    @typing.overload
    def estimate(self, frame: org.orekit.frames.Frame, boolean: bool, int: int, position: org.orekit.estimation.measurements.Position, position2: org.orekit.estimation.measurements.Position) -> org.orekit.orbits.KeplerianOrbit: ...

class IodLaplace:
    def __init__(self, double: float): ...
    @typing.overload
    def estimate(self, frame: org.orekit.frames.Frame, pVCoordinates: org.orekit.utils.PVCoordinates, angularRaDec: org.orekit.estimation.measurements.AngularRaDec, angularRaDec2: org.orekit.estimation.measurements.AngularRaDec, angularRaDec3: org.orekit.estimation.measurements.AngularRaDec) -> org.orekit.orbits.CartesianOrbit: ...
    @typing.overload
    def estimate(self, frame: org.orekit.frames.Frame, pVCoordinates: org.orekit.utils.PVCoordinates, absoluteDate: org.orekit.time.AbsoluteDate, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D, absoluteDate2: org.orekit.time.AbsoluteDate, vector3D2: org.hipparchus.geometry.euclidean.threed.Vector3D, absoluteDate3: org.orekit.time.AbsoluteDate, vector3D3: org.hipparchus.geometry.euclidean.threed.Vector3D) -> org.orekit.orbits.CartesianOrbit: ...
    @typing.overload
    @staticmethod
    def lineOfSight(double: float, double2: float) -> org.hipparchus.geometry.euclidean.threed.Vector3D: ...
    @typing.overload
    @staticmethod
    def lineOfSight(angularRaDec: org.orekit.estimation.measurements.AngularRaDec) -> org.hipparchus.geometry.euclidean.threed.Vector3D: ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.orekit.estimation.iod")``.

    IodGibbs: typing.Type[IodGibbs]
    IodGooding: typing.Type[IodGooding]
    IodLambert: typing.Type[IodLambert]
    IodLaplace: typing.Type[IodLaplace]