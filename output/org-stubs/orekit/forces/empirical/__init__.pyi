import java.util
import java.util.stream
import org.hipparchus
import org.hipparchus.geometry.euclidean.threed
import org.orekit.attitudes
import org.orekit.forces
import org.orekit.propagation
import org.orekit.propagation.events
import org.orekit.time
import org.orekit.utils
import typing



class AccelerationModel:
    def getParametersDrivers(self) -> java.util.List[org.orekit.utils.ParameterDriver]: ...
    def init(self, spacecraftState: org.orekit.propagation.SpacecraftState, absoluteDate: org.orekit.time.AbsoluteDate) -> None: ...
    _signedAmplitude_1__T = typing.TypeVar('_signedAmplitude_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def signedAmplitude(self, spacecraftState: org.orekit.propagation.SpacecraftState, doubleArray: typing.List[float]) -> float: ...
    @typing.overload
    def signedAmplitude(self, fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[_signedAmplitude_1__T], tArray: typing.List[_signedAmplitude_1__T]) -> _signedAmplitude_1__T: ...

class ParametricAcceleration(org.orekit.forces.AbstractForceModel):
    @typing.overload
    def __init__(self, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D, boolean: bool, accelerationModel: AccelerationModel): ...
    @typing.overload
    def __init__(self, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D, attitudeProvider: org.orekit.attitudes.AttitudeProvider, accelerationModel: AccelerationModel): ...
    _acceleration_0__T = typing.TypeVar('_acceleration_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def acceleration(self, fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[_acceleration_0__T], tArray: typing.List[_acceleration_0__T]) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[_acceleration_0__T]: ...
    @typing.overload
    def acceleration(self, spacecraftState: org.orekit.propagation.SpacecraftState, doubleArray: typing.List[float]) -> org.hipparchus.geometry.euclidean.threed.Vector3D: ...
    def dependsOnPositionOnly(self) -> bool: ...
    def getEventsDetectors(self) -> java.util.stream.Stream[org.orekit.propagation.events.EventDetector]: ...
    _getFieldEventsDetectors__T = typing.TypeVar('_getFieldEventsDetectors__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    def getFieldEventsDetectors(self, field: org.hipparchus.Field[_getFieldEventsDetectors__T]) -> java.util.stream.Stream[org.orekit.propagation.events.FieldEventDetector[_getFieldEventsDetectors__T]]: ...
    def getParametersDrivers(self) -> java.util.List[org.orekit.utils.ParameterDriver]: ...
    def init(self, spacecraftState: org.orekit.propagation.SpacecraftState, absoluteDate: org.orekit.time.AbsoluteDate) -> None: ...

class TimeSpanParametricAcceleration(org.orekit.forces.AbstractForceModel):
    DATE_BEFORE: typing.ClassVar[str] = ...
    DATE_AFTER: typing.ClassVar[str] = ...
    @typing.overload
    def __init__(self, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D, boolean: bool, accelerationModel: AccelerationModel): ...
    @typing.overload
    def __init__(self, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D, attitudeProvider: org.orekit.attitudes.AttitudeProvider, accelerationModel: AccelerationModel): ...
    _acceleration_0__T = typing.TypeVar('_acceleration_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def acceleration(self, fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[_acceleration_0__T], tArray: typing.List[_acceleration_0__T]) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[_acceleration_0__T]: ...
    @typing.overload
    def acceleration(self, spacecraftState: org.orekit.propagation.SpacecraftState, doubleArray: typing.List[float]) -> org.hipparchus.geometry.euclidean.threed.Vector3D: ...
    def addAccelerationModelValidAfter(self, accelerationModel: AccelerationModel, absoluteDate: org.orekit.time.AbsoluteDate) -> None: ...
    def addAccelerationModelValidBefore(self, accelerationModel: AccelerationModel, absoluteDate: org.orekit.time.AbsoluteDate) -> None: ...
    def dependsOnPositionOnly(self) -> bool: ...
    def extractAccelerationModelRange(self, absoluteDate: org.orekit.time.AbsoluteDate, absoluteDate2: org.orekit.time.AbsoluteDate) -> org.orekit.utils.TimeSpanMap[AccelerationModel]: ...
    _extractParameters_1__T = typing.TypeVar('_extractParameters_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def extractParameters(self, doubleArray: typing.List[float], absoluteDate: org.orekit.time.AbsoluteDate) -> typing.List[float]: ...
    @typing.overload
    def extractParameters(self, tArray: typing.List[_extractParameters_1__T], fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_extractParameters_1__T]) -> typing.List[_extractParameters_1__T]: ...
    def getAccelerationModel(self, absoluteDate: org.orekit.time.AbsoluteDate) -> AccelerationModel: ...
    def getAccelerationModelSpan(self, absoluteDate: org.orekit.time.AbsoluteDate) -> org.orekit.utils.TimeSpanMap.Span[AccelerationModel]: ...
    def getEventsDetectors(self) -> java.util.stream.Stream[org.orekit.propagation.events.EventDetector]: ...
    _getFieldEventsDetectors__T = typing.TypeVar('_getFieldEventsDetectors__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    def getFieldEventsDetectors(self, field: org.hipparchus.Field[_getFieldEventsDetectors__T]) -> java.util.stream.Stream[org.orekit.propagation.events.FieldEventDetector[_getFieldEventsDetectors__T]]: ...
    def getParametersDrivers(self) -> java.util.List[org.orekit.utils.ParameterDriver]: ...
    def getTransitions(self) -> java.util.NavigableSet[org.orekit.utils.TimeSpanMap.Transition[AccelerationModel]]: ...
    def init(self, spacecraftState: org.orekit.propagation.SpacecraftState, absoluteDate: org.orekit.time.AbsoluteDate) -> None: ...

class HarmonicAccelerationModel(AccelerationModel):
    def __init__(self, string: str, absoluteDate: org.orekit.time.AbsoluteDate, double: float, int: int): ...
    def getParametersDrivers(self) -> java.util.List[org.orekit.utils.ParameterDriver]: ...
    def init(self, spacecraftState: org.orekit.propagation.SpacecraftState, absoluteDate: org.orekit.time.AbsoluteDate) -> None: ...
    _signedAmplitude_1__T = typing.TypeVar('_signedAmplitude_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def signedAmplitude(self, spacecraftState: org.orekit.propagation.SpacecraftState, doubleArray: typing.List[float]) -> float: ...
    @typing.overload
    def signedAmplitude(self, fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[_signedAmplitude_1__T], tArray: typing.List[_signedAmplitude_1__T]) -> _signedAmplitude_1__T: ...

class PolynomialAccelerationModel(AccelerationModel):
    def __init__(self, string: str, absoluteDate: org.orekit.time.AbsoluteDate, int: int): ...
    def getParametersDrivers(self) -> java.util.List[org.orekit.utils.ParameterDriver]: ...
    def init(self, spacecraftState: org.orekit.propagation.SpacecraftState, absoluteDate: org.orekit.time.AbsoluteDate) -> None: ...
    _signedAmplitude_1__T = typing.TypeVar('_signedAmplitude_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def signedAmplitude(self, spacecraftState: org.orekit.propagation.SpacecraftState, doubleArray: typing.List[float]) -> float: ...
    @typing.overload
    def signedAmplitude(self, fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[_signedAmplitude_1__T], tArray: typing.List[_signedAmplitude_1__T]) -> _signedAmplitude_1__T: ...

class PythonAccelerationModel(AccelerationModel):
    def __init__(self): ...
    def finalize(self) -> None: ...
    def getParametersDrivers(self) -> java.util.List[org.orekit.utils.ParameterDriver]: ...
    def pythonDecRef(self) -> None: ...
    @typing.overload
    def pythonExtension(self) -> int: ...
    @typing.overload
    def pythonExtension(self, long: int) -> None: ...
    _signedAmplitude_1__T = typing.TypeVar('_signedAmplitude_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def signedAmplitude(self, spacecraftState: org.orekit.propagation.SpacecraftState, doubleArray: typing.List[float]) -> float: ...
    @typing.overload
    def signedAmplitude(self, fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[_signedAmplitude_1__T], tArray: typing.List[_signedAmplitude_1__T]) -> _signedAmplitude_1__T: ...
    _signedAmplitude_FT__T = typing.TypeVar('_signedAmplitude_FT__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    def signedAmplitude_FT(self, fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[_signedAmplitude_FT__T], tArray: typing.List[_signedAmplitude_FT__T]) -> _signedAmplitude_FT__T: ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.orekit.forces.empirical")``.

    AccelerationModel: typing.Type[AccelerationModel]
    HarmonicAccelerationModel: typing.Type[HarmonicAccelerationModel]
    ParametricAcceleration: typing.Type[ParametricAcceleration]
    PolynomialAccelerationModel: typing.Type[PolynomialAccelerationModel]
    PythonAccelerationModel: typing.Type[PythonAccelerationModel]
    TimeSpanParametricAcceleration: typing.Type[TimeSpanParametricAcceleration]