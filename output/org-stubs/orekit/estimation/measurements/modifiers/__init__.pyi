import java.util
import org.hipparchus
import org.hipparchus.analysis.differentiation
import org.hipparchus.geometry.euclidean.threed
import org.orekit.attitudes
import org.orekit.estimation.measurements
import org.orekit.estimation.measurements.gnss
import org.orekit.models
import org.orekit.models.earth.ionosphere
import org.orekit.models.earth.troposphere
import org.orekit.propagation
import org.orekit.propagation.integration
import org.orekit.utils
import typing



class AbstractAmbiguityModifier:
    def __init__(self, int: int, double: float): ...

class AbstractRelativisticClockModifier:
    def __init__(self): ...

class AbstractShapiroBaseModifier:
    def __init__(self, double: float): ...

class AngularIonosphericDelayModifier(org.orekit.estimation.measurements.EstimationModifier[org.orekit.estimation.measurements.AngularAzEl]):
    def __init__(self, ionosphericModel: org.orekit.models.earth.ionosphere.IonosphericModel, double: float): ...
    def getParametersDrivers(self) -> java.util.List[org.orekit.utils.ParameterDriver]: ...
    def modify(self, estimatedMeasurement: org.orekit.estimation.measurements.EstimatedMeasurement[org.orekit.estimation.measurements.AngularAzEl]) -> None: ...

class AngularRadioRefractionModifier(org.orekit.estimation.measurements.EstimationModifier[org.orekit.estimation.measurements.AngularAzEl]):
    def __init__(self, atmosphericRefractionModel: org.orekit.models.AtmosphericRefractionModel): ...
    def getParametersDrivers(self) -> java.util.List[org.orekit.utils.ParameterDriver]: ...
    def modify(self, estimatedMeasurement: org.orekit.estimation.measurements.EstimatedMeasurement[org.orekit.estimation.measurements.AngularAzEl]) -> None: ...

class AngularTroposphericDelayModifier(org.orekit.estimation.measurements.EstimationModifier[org.orekit.estimation.measurements.AngularAzEl]):
    def __init__(self, discreteTroposphericModel: org.orekit.models.earth.troposphere.DiscreteTroposphericModel): ...
    def getParametersDrivers(self) -> java.util.List[org.orekit.utils.ParameterDriver]: ...
    def modify(self, estimatedMeasurement: org.orekit.estimation.measurements.EstimatedMeasurement[org.orekit.estimation.measurements.AngularAzEl]) -> None: ...

_Bias__T = typing.TypeVar('_Bias__T', bound=org.orekit.estimation.measurements.ObservedMeasurement)  # <T>
class Bias(org.orekit.estimation.measurements.EstimationModifier[_Bias__T], typing.Generic[_Bias__T]):
    def __init__(self, stringArray: typing.List[str], doubleArray: typing.List[float], doubleArray2: typing.List[float], doubleArray3: typing.List[float], doubleArray4: typing.List[float]): ...
    def getParametersDrivers(self) -> java.util.List[org.orekit.utils.ParameterDriver]: ...
    def modify(self, estimatedMeasurement: org.orekit.estimation.measurements.EstimatedMeasurement[_Bias__T]) -> None: ...

class IonosphericGradientConverter(org.orekit.propagation.integration.AbstractGradientConverter):
    def __init__(self, spacecraftState: org.orekit.propagation.SpacecraftState, int: int, attitudeProvider: org.orekit.attitudes.AttitudeProvider): ...
    def getFreeStateParameters(self) -> int: ...
    def getParameters(self, fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[org.hipparchus.analysis.differentiation.Gradient], ionosphericModel: org.orekit.models.earth.ionosphere.IonosphericModel) -> typing.List[org.hipparchus.analysis.differentiation.Gradient]: ...
    def getState(self, ionosphericModel: org.orekit.models.earth.ionosphere.IonosphericModel) -> org.orekit.propagation.FieldSpacecraftState[org.hipparchus.analysis.differentiation.Gradient]: ...

class OnBoardAntennaInterSatellitesPhaseModifier(org.orekit.estimation.measurements.EstimationModifier[org.orekit.estimation.measurements.gnss.InterSatellitesPhase]):
    def __init__(self, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D, vector3D2: org.hipparchus.geometry.euclidean.threed.Vector3D): ...
    def getParametersDrivers(self) -> java.util.List[org.orekit.utils.ParameterDriver]: ...
    def modify(self, estimatedMeasurement: org.orekit.estimation.measurements.EstimatedMeasurement[org.orekit.estimation.measurements.gnss.InterSatellitesPhase]) -> None: ...

class OnBoardAntennaInterSatellitesRangeModifier(org.orekit.estimation.measurements.EstimationModifier[org.orekit.estimation.measurements.InterSatellitesRange]):
    def __init__(self, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D, vector3D2: org.hipparchus.geometry.euclidean.threed.Vector3D): ...
    def getParametersDrivers(self) -> java.util.List[org.orekit.utils.ParameterDriver]: ...
    def modify(self, estimatedMeasurement: org.orekit.estimation.measurements.EstimatedMeasurement[org.orekit.estimation.measurements.InterSatellitesRange]) -> None: ...

class OnBoardAntennaOneWayGNSSPhaseModifier(org.orekit.estimation.measurements.EstimationModifier[org.orekit.estimation.measurements.gnss.OneWayGNSSPhase]):
    def __init__(self, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D, vector3D2: org.hipparchus.geometry.euclidean.threed.Vector3D, attitudeProvider: org.orekit.attitudes.AttitudeProvider): ...
    def getParametersDrivers(self) -> java.util.List[org.orekit.utils.ParameterDriver]: ...
    def modify(self, estimatedMeasurement: org.orekit.estimation.measurements.EstimatedMeasurement[org.orekit.estimation.measurements.gnss.OneWayGNSSPhase]) -> None: ...

class OnBoardAntennaOneWayGNSSRangeModifier(org.orekit.estimation.measurements.EstimationModifier[org.orekit.estimation.measurements.gnss.OneWayGNSSRange]):
    def __init__(self, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D, vector3D2: org.hipparchus.geometry.euclidean.threed.Vector3D, attitudeProvider: org.orekit.attitudes.AttitudeProvider): ...
    def getParametersDrivers(self) -> java.util.List[org.orekit.utils.ParameterDriver]: ...
    def modify(self, estimatedMeasurement: org.orekit.estimation.measurements.EstimatedMeasurement[org.orekit.estimation.measurements.gnss.OneWayGNSSRange]) -> None: ...

class OnBoardAntennaPhaseModifier(org.orekit.estimation.measurements.EstimationModifier[org.orekit.estimation.measurements.gnss.Phase]):
    def __init__(self, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D): ...
    def getParametersDrivers(self) -> java.util.List[org.orekit.utils.ParameterDriver]: ...
    def modify(self, estimatedMeasurement: org.orekit.estimation.measurements.EstimatedMeasurement[org.orekit.estimation.measurements.gnss.Phase]) -> None: ...

class OnBoardAntennaRangeModifier(org.orekit.estimation.measurements.EstimationModifier[org.orekit.estimation.measurements.Range]):
    def __init__(self, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D): ...
    def getParametersDrivers(self) -> java.util.List[org.orekit.utils.ParameterDriver]: ...
    def modify(self, estimatedMeasurement: org.orekit.estimation.measurements.EstimatedMeasurement[org.orekit.estimation.measurements.Range]) -> None: ...

class OnBoardAntennaTurnAroundRangeModifier(org.orekit.estimation.measurements.EstimationModifier[org.orekit.estimation.measurements.TurnAroundRange]):
    def __init__(self, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D): ...
    def getParametersDrivers(self) -> java.util.List[org.orekit.utils.ParameterDriver]: ...
    def modify(self, estimatedMeasurement: org.orekit.estimation.measurements.EstimatedMeasurement[org.orekit.estimation.measurements.TurnAroundRange]) -> None: ...

_OutlierFilter__T = typing.TypeVar('_OutlierFilter__T', bound=org.orekit.estimation.measurements.ObservedMeasurement)  # <T>
class OutlierFilter(org.orekit.estimation.measurements.EstimationModifier[_OutlierFilter__T], typing.Generic[_OutlierFilter__T]):
    def __init__(self, int: int, double: float): ...
    def getParametersDrivers(self) -> java.util.List[org.orekit.utils.ParameterDriver]: ...
    def modify(self, estimatedMeasurement: org.orekit.estimation.measurements.EstimatedMeasurement[_OutlierFilter__T]) -> None: ...

class PhaseIonosphericDelayModifier(org.orekit.estimation.measurements.EstimationModifier[org.orekit.estimation.measurements.gnss.Phase]):
    def __init__(self, ionosphericModel: org.orekit.models.earth.ionosphere.IonosphericModel, double: float): ...
    def getParametersDrivers(self) -> java.util.List[org.orekit.utils.ParameterDriver]: ...
    def modify(self, estimatedMeasurement: org.orekit.estimation.measurements.EstimatedMeasurement[org.orekit.estimation.measurements.gnss.Phase]) -> None: ...

class PhaseTroposphericDelayModifier(org.orekit.estimation.measurements.EstimationModifier[org.orekit.estimation.measurements.gnss.Phase]):
    def __init__(self, discreteTroposphericModel: org.orekit.models.earth.troposphere.DiscreteTroposphericModel): ...
    def getParametersDrivers(self) -> java.util.List[org.orekit.utils.ParameterDriver]: ...
    def modify(self, estimatedMeasurement: org.orekit.estimation.measurements.EstimatedMeasurement[org.orekit.estimation.measurements.gnss.Phase]) -> None: ...

class RangeIonosphericDelayModifier(org.orekit.estimation.measurements.EstimationModifier[org.orekit.estimation.measurements.Range]):
    def __init__(self, ionosphericModel: org.orekit.models.earth.ionosphere.IonosphericModel, double: float): ...
    def getParametersDrivers(self) -> java.util.List[org.orekit.utils.ParameterDriver]: ...
    def modify(self, estimatedMeasurement: org.orekit.estimation.measurements.EstimatedMeasurement[org.orekit.estimation.measurements.Range]) -> None: ...

class RangeRateIonosphericDelayModifier(org.orekit.estimation.measurements.EstimationModifier[org.orekit.estimation.measurements.RangeRate]):
    def __init__(self, ionosphericModel: org.orekit.models.earth.ionosphere.IonosphericModel, double: float, boolean: bool): ...
    def getParametersDrivers(self) -> java.util.List[org.orekit.utils.ParameterDriver]: ...
    def modify(self, estimatedMeasurement: org.orekit.estimation.measurements.EstimatedMeasurement[org.orekit.estimation.measurements.RangeRate]) -> None: ...

class RangeRateTroposphericDelayModifier(org.orekit.estimation.measurements.EstimationModifier[org.orekit.estimation.measurements.RangeRate]):
    def __init__(self, discreteTroposphericModel: org.orekit.models.earth.troposphere.DiscreteTroposphericModel, boolean: bool): ...
    def getParametersDrivers(self) -> java.util.List[org.orekit.utils.ParameterDriver]: ...
    def modify(self, estimatedMeasurement: org.orekit.estimation.measurements.EstimatedMeasurement[org.orekit.estimation.measurements.RangeRate]) -> None: ...
    _rangeRateErrorTroposphericModel_1__T = typing.TypeVar('_rangeRateErrorTroposphericModel_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def rangeRateErrorTroposphericModel(self, groundStation: org.orekit.estimation.measurements.GroundStation, spacecraftState: org.orekit.propagation.SpacecraftState) -> float: ...
    @typing.overload
    def rangeRateErrorTroposphericModel(self, groundStation: org.orekit.estimation.measurements.GroundStation, fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[_rangeRateErrorTroposphericModel_1__T], tArray: typing.List[_rangeRateErrorTroposphericModel_1__T]) -> _rangeRateErrorTroposphericModel_1__T: ...

class RangeTroposphericDelayModifier(org.orekit.estimation.measurements.EstimationModifier[org.orekit.estimation.measurements.Range]):
    def __init__(self, discreteTroposphericModel: org.orekit.models.earth.troposphere.DiscreteTroposphericModel): ...
    def getParametersDrivers(self) -> java.util.List[org.orekit.utils.ParameterDriver]: ...
    def modify(self, estimatedMeasurement: org.orekit.estimation.measurements.EstimatedMeasurement[org.orekit.estimation.measurements.Range]) -> None: ...

class TroposphericGradientConverter(org.orekit.propagation.integration.AbstractGradientConverter):
    def __init__(self, spacecraftState: org.orekit.propagation.SpacecraftState, int: int, attitudeProvider: org.orekit.attitudes.AttitudeProvider): ...
    def getFreeStateParameters(self) -> int: ...
    def getParameters(self, fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[org.hipparchus.analysis.differentiation.Gradient], discreteTroposphericModel: org.orekit.models.earth.troposphere.DiscreteTroposphericModel) -> typing.List[org.hipparchus.analysis.differentiation.Gradient]: ...
    def getState(self, discreteTroposphericModel: org.orekit.models.earth.troposphere.DiscreteTroposphericModel) -> org.orekit.propagation.FieldSpacecraftState[org.hipparchus.analysis.differentiation.Gradient]: ...

class TurnAroundRangeIonosphericDelayModifier(org.orekit.estimation.measurements.EstimationModifier[org.orekit.estimation.measurements.TurnAroundRange]):
    def __init__(self, ionosphericModel: org.orekit.models.earth.ionosphere.IonosphericModel, double: float): ...
    def getParametersDrivers(self) -> java.util.List[org.orekit.utils.ParameterDriver]: ...
    def modify(self, estimatedMeasurement: org.orekit.estimation.measurements.EstimatedMeasurement[org.orekit.estimation.measurements.TurnAroundRange]) -> None: ...

class TurnAroundRangeTroposphericDelayModifier(org.orekit.estimation.measurements.EstimationModifier[org.orekit.estimation.measurements.TurnAroundRange]):
    def __init__(self, discreteTroposphericModel: org.orekit.models.earth.troposphere.DiscreteTroposphericModel): ...
    def getParametersDrivers(self) -> java.util.List[org.orekit.utils.ParameterDriver]: ...
    def modify(self, estimatedMeasurement: org.orekit.estimation.measurements.EstimatedMeasurement[org.orekit.estimation.measurements.TurnAroundRange]) -> None: ...

_DynamicOutlierFilter__T = typing.TypeVar('_DynamicOutlierFilter__T', bound=org.orekit.estimation.measurements.ObservedMeasurement)  # <T>
class DynamicOutlierFilter(OutlierFilter[_DynamicOutlierFilter__T], typing.Generic[_DynamicOutlierFilter__T]):
    def __init__(self, int: int, double: float): ...
    def getSigma(self) -> typing.List[float]: ...
    def modify(self, estimatedMeasurement: org.orekit.estimation.measurements.EstimatedMeasurement[_DynamicOutlierFilter__T]) -> None: ...
    def setSigma(self, doubleArray: typing.List[float]) -> None: ...

class InterSatellitesPhaseAmbiguityModifier(AbstractAmbiguityModifier, org.orekit.estimation.measurements.EstimationModifier[org.orekit.estimation.measurements.gnss.InterSatellitesPhase]):
    def __init__(self, int: int, double: float): ...
    def getParametersDrivers(self) -> java.util.List[org.orekit.utils.ParameterDriver]: ...
    def modify(self, estimatedMeasurement: org.orekit.estimation.measurements.EstimatedMeasurement[org.orekit.estimation.measurements.gnss.InterSatellitesPhase]) -> None: ...

class OneWayGNSSPhaseAmbiguityModifier(AbstractAmbiguityModifier, org.orekit.estimation.measurements.EstimationModifier[org.orekit.estimation.measurements.gnss.OneWayGNSSPhase]):
    def __init__(self, int: int, double: float): ...
    def getParametersDrivers(self) -> java.util.List[org.orekit.utils.ParameterDriver]: ...
    def modify(self, estimatedMeasurement: org.orekit.estimation.measurements.EstimatedMeasurement[org.orekit.estimation.measurements.gnss.OneWayGNSSPhase]) -> None: ...

class PhaseAmbiguityModifier(AbstractAmbiguityModifier, org.orekit.estimation.measurements.EstimationModifier[org.orekit.estimation.measurements.gnss.Phase]):
    def __init__(self, int: int, double: float): ...
    def getParametersDrivers(self) -> java.util.List[org.orekit.utils.ParameterDriver]: ...
    def modify(self, estimatedMeasurement: org.orekit.estimation.measurements.EstimatedMeasurement[org.orekit.estimation.measurements.gnss.Phase]) -> None: ...

class RelativisticClockInterSatellitesPhaseModifier(AbstractRelativisticClockModifier, org.orekit.estimation.measurements.EstimationModifier[org.orekit.estimation.measurements.gnss.InterSatellitesPhase]):
    def __init__(self): ...
    def getParametersDrivers(self) -> java.util.List[org.orekit.utils.ParameterDriver]: ...
    def modify(self, estimatedMeasurement: org.orekit.estimation.measurements.EstimatedMeasurement[org.orekit.estimation.measurements.gnss.InterSatellitesPhase]) -> None: ...

class RelativisticClockInterSatellitesRangeModifier(AbstractRelativisticClockModifier, org.orekit.estimation.measurements.EstimationModifier[org.orekit.estimation.measurements.InterSatellitesRange]):
    def __init__(self): ...
    def getParametersDrivers(self) -> java.util.List[org.orekit.utils.ParameterDriver]: ...
    def modify(self, estimatedMeasurement: org.orekit.estimation.measurements.EstimatedMeasurement[org.orekit.estimation.measurements.InterSatellitesRange]) -> None: ...

class RelativisticClockOneWayGNSSPhaseModifier(AbstractRelativisticClockModifier, org.orekit.estimation.measurements.EstimationModifier[org.orekit.estimation.measurements.gnss.OneWayGNSSPhase]):
    def __init__(self): ...
    def getParametersDrivers(self) -> java.util.List[org.orekit.utils.ParameterDriver]: ...
    def modify(self, estimatedMeasurement: org.orekit.estimation.measurements.EstimatedMeasurement[org.orekit.estimation.measurements.gnss.OneWayGNSSPhase]) -> None: ...

class RelativisticClockOneWayGNSSRangeModifier(AbstractRelativisticClockModifier, org.orekit.estimation.measurements.EstimationModifier[org.orekit.estimation.measurements.gnss.OneWayGNSSRange]):
    def __init__(self): ...
    def getParametersDrivers(self) -> java.util.List[org.orekit.utils.ParameterDriver]: ...
    def modify(self, estimatedMeasurement: org.orekit.estimation.measurements.EstimatedMeasurement[org.orekit.estimation.measurements.gnss.OneWayGNSSRange]) -> None: ...

class RelativisticClockPhaseModifier(AbstractRelativisticClockModifier, org.orekit.estimation.measurements.EstimationModifier[org.orekit.estimation.measurements.gnss.Phase]):
    def __init__(self): ...
    def getParametersDrivers(self) -> java.util.List[org.orekit.utils.ParameterDriver]: ...
    def modify(self, estimatedMeasurement: org.orekit.estimation.measurements.EstimatedMeasurement[org.orekit.estimation.measurements.gnss.Phase]) -> None: ...

class RelativisticClockRangeModifier(AbstractRelativisticClockModifier, org.orekit.estimation.measurements.EstimationModifier[org.orekit.estimation.measurements.Range]):
    def __init__(self): ...
    def getParametersDrivers(self) -> java.util.List[org.orekit.utils.ParameterDriver]: ...
    def modify(self, estimatedMeasurement: org.orekit.estimation.measurements.EstimatedMeasurement[org.orekit.estimation.measurements.Range]) -> None: ...

class RelativisticClockRangeRateModifier(AbstractRelativisticClockModifier, org.orekit.estimation.measurements.EstimationModifier[org.orekit.estimation.measurements.RangeRate]):
    def __init__(self, double: float): ...
    def getParametersDrivers(self) -> java.util.List[org.orekit.utils.ParameterDriver]: ...
    def modify(self, estimatedMeasurement: org.orekit.estimation.measurements.EstimatedMeasurement[org.orekit.estimation.measurements.RangeRate]) -> None: ...

class ShapiroInterSatellitePhaseModifier(AbstractShapiroBaseModifier, org.orekit.estimation.measurements.EstimationModifier[org.orekit.estimation.measurements.gnss.InterSatellitesPhase]):
    def __init__(self, double: float): ...
    def getParametersDrivers(self) -> java.util.List[org.orekit.utils.ParameterDriver]: ...
    def modify(self, estimatedMeasurement: org.orekit.estimation.measurements.EstimatedMeasurement[org.orekit.estimation.measurements.gnss.InterSatellitesPhase]) -> None: ...

class ShapiroInterSatelliteRangeModifier(AbstractShapiroBaseModifier, org.orekit.estimation.measurements.EstimationModifier[org.orekit.estimation.measurements.InterSatellitesRange]):
    def __init__(self, double: float): ...
    def getParametersDrivers(self) -> java.util.List[org.orekit.utils.ParameterDriver]: ...
    def modify(self, estimatedMeasurement: org.orekit.estimation.measurements.EstimatedMeasurement[org.orekit.estimation.measurements.InterSatellitesRange]) -> None: ...

class ShapiroOneWayGNSSPhaseModifier(AbstractShapiroBaseModifier, org.orekit.estimation.measurements.EstimationModifier[org.orekit.estimation.measurements.gnss.OneWayGNSSPhase]):
    def __init__(self, double: float): ...
    def getParametersDrivers(self) -> java.util.List[org.orekit.utils.ParameterDriver]: ...
    def modify(self, estimatedMeasurement: org.orekit.estimation.measurements.EstimatedMeasurement[org.orekit.estimation.measurements.gnss.OneWayGNSSPhase]) -> None: ...

class ShapiroOneWayGNSSRangeModifier(AbstractShapiroBaseModifier, org.orekit.estimation.measurements.EstimationModifier[org.orekit.estimation.measurements.gnss.OneWayGNSSRange]):
    def __init__(self, double: float): ...
    def getParametersDrivers(self) -> java.util.List[org.orekit.utils.ParameterDriver]: ...
    def modify(self, estimatedMeasurement: org.orekit.estimation.measurements.EstimatedMeasurement[org.orekit.estimation.measurements.gnss.OneWayGNSSRange]) -> None: ...

class ShapiroPhaseModifier(AbstractShapiroBaseModifier, org.orekit.estimation.measurements.EstimationModifier[org.orekit.estimation.measurements.gnss.Phase]):
    def __init__(self, double: float): ...
    def getParametersDrivers(self) -> java.util.List[org.orekit.utils.ParameterDriver]: ...
    def modify(self, estimatedMeasurement: org.orekit.estimation.measurements.EstimatedMeasurement[org.orekit.estimation.measurements.gnss.Phase]) -> None: ...

class ShapiroRangeModifier(AbstractShapiroBaseModifier, org.orekit.estimation.measurements.EstimationModifier[org.orekit.estimation.measurements.Range]):
    def __init__(self, double: float): ...
    def getParametersDrivers(self) -> java.util.List[org.orekit.utils.ParameterDriver]: ...
    def modify(self, estimatedMeasurement: org.orekit.estimation.measurements.EstimatedMeasurement[org.orekit.estimation.measurements.Range]) -> None: ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.orekit.estimation.measurements.modifiers")``.

    AbstractAmbiguityModifier: typing.Type[AbstractAmbiguityModifier]
    AbstractRelativisticClockModifier: typing.Type[AbstractRelativisticClockModifier]
    AbstractShapiroBaseModifier: typing.Type[AbstractShapiroBaseModifier]
    AngularIonosphericDelayModifier: typing.Type[AngularIonosphericDelayModifier]
    AngularRadioRefractionModifier: typing.Type[AngularRadioRefractionModifier]
    AngularTroposphericDelayModifier: typing.Type[AngularTroposphericDelayModifier]
    Bias: typing.Type[Bias]
    DynamicOutlierFilter: typing.Type[DynamicOutlierFilter]
    InterSatellitesPhaseAmbiguityModifier: typing.Type[InterSatellitesPhaseAmbiguityModifier]
    IonosphericGradientConverter: typing.Type[IonosphericGradientConverter]
    OnBoardAntennaInterSatellitesPhaseModifier: typing.Type[OnBoardAntennaInterSatellitesPhaseModifier]
    OnBoardAntennaInterSatellitesRangeModifier: typing.Type[OnBoardAntennaInterSatellitesRangeModifier]
    OnBoardAntennaOneWayGNSSPhaseModifier: typing.Type[OnBoardAntennaOneWayGNSSPhaseModifier]
    OnBoardAntennaOneWayGNSSRangeModifier: typing.Type[OnBoardAntennaOneWayGNSSRangeModifier]
    OnBoardAntennaPhaseModifier: typing.Type[OnBoardAntennaPhaseModifier]
    OnBoardAntennaRangeModifier: typing.Type[OnBoardAntennaRangeModifier]
    OnBoardAntennaTurnAroundRangeModifier: typing.Type[OnBoardAntennaTurnAroundRangeModifier]
    OneWayGNSSPhaseAmbiguityModifier: typing.Type[OneWayGNSSPhaseAmbiguityModifier]
    OutlierFilter: typing.Type[OutlierFilter]
    PhaseAmbiguityModifier: typing.Type[PhaseAmbiguityModifier]
    PhaseIonosphericDelayModifier: typing.Type[PhaseIonosphericDelayModifier]
    PhaseTroposphericDelayModifier: typing.Type[PhaseTroposphericDelayModifier]
    RangeIonosphericDelayModifier: typing.Type[RangeIonosphericDelayModifier]
    RangeRateIonosphericDelayModifier: typing.Type[RangeRateIonosphericDelayModifier]
    RangeRateTroposphericDelayModifier: typing.Type[RangeRateTroposphericDelayModifier]
    RangeTroposphericDelayModifier: typing.Type[RangeTroposphericDelayModifier]
    RelativisticClockInterSatellitesPhaseModifier: typing.Type[RelativisticClockInterSatellitesPhaseModifier]
    RelativisticClockInterSatellitesRangeModifier: typing.Type[RelativisticClockInterSatellitesRangeModifier]
    RelativisticClockOneWayGNSSPhaseModifier: typing.Type[RelativisticClockOneWayGNSSPhaseModifier]
    RelativisticClockOneWayGNSSRangeModifier: typing.Type[RelativisticClockOneWayGNSSRangeModifier]
    RelativisticClockPhaseModifier: typing.Type[RelativisticClockPhaseModifier]
    RelativisticClockRangeModifier: typing.Type[RelativisticClockRangeModifier]
    RelativisticClockRangeRateModifier: typing.Type[RelativisticClockRangeRateModifier]
    ShapiroInterSatellitePhaseModifier: typing.Type[ShapiroInterSatellitePhaseModifier]
    ShapiroInterSatelliteRangeModifier: typing.Type[ShapiroInterSatelliteRangeModifier]
    ShapiroOneWayGNSSPhaseModifier: typing.Type[ShapiroOneWayGNSSPhaseModifier]
    ShapiroOneWayGNSSRangeModifier: typing.Type[ShapiroOneWayGNSSRangeModifier]
    ShapiroPhaseModifier: typing.Type[ShapiroPhaseModifier]
    ShapiroRangeModifier: typing.Type[ShapiroRangeModifier]
    TroposphericGradientConverter: typing.Type[TroposphericGradientConverter]
    TurnAroundRangeIonosphericDelayModifier: typing.Type[TurnAroundRangeIonosphericDelayModifier]
    TurnAroundRangeTroposphericDelayModifier: typing.Type[TurnAroundRangeTroposphericDelayModifier]