import java.util
import org.hipparchus.analysis
import org.hipparchus.ode
import org.hipparchus.optim.nonlinear.vector.leastsquares
import org.orekit.attitudes
import org.orekit.data
import org.orekit.estimation.leastsquares
import org.orekit.estimation.measurements
import org.orekit.estimation.sequential
import org.orekit.forces
import org.orekit.forces.gravity.potential
import org.orekit.frames
import org.orekit.orbits
import org.orekit.propagation
import org.orekit.propagation.analytical.tle
import org.orekit.propagation.integration
import org.orekit.propagation.numerical
import org.orekit.propagation.semianalytical.dsst
import org.orekit.propagation.semianalytical.dsst.forces
import org.orekit.time
import org.orekit.utils
import typing



class ODEIntegratorBuilder:
    def buildIntegrator(self, orbit: org.orekit.orbits.Orbit, orbitType: org.orekit.orbits.OrbitType) -> org.hipparchus.ode.AbstractIntegrator: ...

class OsculatingToMeanElementsConverter:
    def __init__(self, spacecraftState: org.orekit.propagation.SpacecraftState, int: int, propagator: org.orekit.propagation.Propagator, double: float): ...
    def convert(self) -> org.orekit.propagation.SpacecraftState: ...

class PropagatorBuilder:
    def buildPropagator(self, doubleArray: typing.List[float]) -> org.orekit.propagation.Propagator: ...
    def getFrame(self) -> org.orekit.frames.Frame: ...
    def getInitialOrbitDate(self) -> org.orekit.time.AbsoluteDate: ...
    def getOrbitType(self) -> org.orekit.orbits.OrbitType: ...
    def getOrbitalParametersDrivers(self) -> org.orekit.utils.ParameterDriversList: ...
    def getPositionAngle(self) -> org.orekit.orbits.PositionAngle: ...
    def getPropagationParametersDrivers(self) -> org.orekit.utils.ParameterDriversList: ...
    def getSelectedNormalizedParameters(self) -> typing.List[float]: ...

class PropagatorConverter:
    @typing.overload
    def convert(self, list: java.util.List[org.orekit.propagation.SpacecraftState], boolean: bool, stringArray: typing.List[str]) -> org.orekit.propagation.Propagator: ...
    @typing.overload
    def convert(self, list: java.util.List[org.orekit.propagation.SpacecraftState], boolean: bool, list2: java.util.List[str]) -> org.orekit.propagation.Propagator: ...
    @typing.overload
    def convert(self, propagator: org.orekit.propagation.Propagator, double: float, int: int, stringArray: typing.List[str]) -> org.orekit.propagation.Propagator: ...
    @typing.overload
    def convert(self, propagator: org.orekit.propagation.Propagator, double: float, int: int, list: java.util.List[str]) -> org.orekit.propagation.Propagator: ...

class AbstractPropagatorBuilder(PropagatorBuilder):
    def addAdditionalEquations(self, additionalEquations: org.orekit.propagation.integration.AdditionalEquations) -> None: ...
    def deselectDynamicParameters(self) -> None: ...
    def getAttitudeProvider(self) -> org.orekit.attitudes.AttitudeProvider: ...
    def getFrame(self) -> org.orekit.frames.Frame: ...
    def getInitialOrbitDate(self) -> org.orekit.time.AbsoluteDate: ...
    def getMu(self) -> float: ...
    def getOrbitType(self) -> org.orekit.orbits.OrbitType: ...
    def getOrbitalParametersDrivers(self) -> org.orekit.utils.ParameterDriversList: ...
    def getPositionAngle(self) -> org.orekit.orbits.PositionAngle: ...
    def getPositionScale(self) -> float: ...
    def getPropagationParametersDrivers(self) -> org.orekit.utils.ParameterDriversList: ...
    def getSelectedNormalizedParameters(self) -> typing.List[float]: ...
    def resetOrbit(self, orbit: org.orekit.orbits.Orbit) -> None: ...
    def setAttitudeProvider(self, attitudeProvider: org.orekit.attitudes.AttitudeProvider) -> None: ...

class AbstractPropagatorConverter(PropagatorConverter):
    @typing.overload
    def convert(self, list: java.util.List[org.orekit.propagation.SpacecraftState], boolean: bool, stringArray: typing.List[str]) -> org.orekit.propagation.Propagator: ...
    @typing.overload
    def convert(self, list: java.util.List[org.orekit.propagation.SpacecraftState], boolean: bool, list2: java.util.List[str]) -> org.orekit.propagation.Propagator: ...
    @typing.overload
    def convert(self, propagator: org.orekit.propagation.Propagator, double: float, int: int, stringArray: typing.List[str]) -> org.orekit.propagation.Propagator: ...
    @typing.overload
    def convert(self, propagator: org.orekit.propagation.Propagator, double: float, int: int, list: java.util.List[str]) -> org.orekit.propagation.Propagator: ...
    def getAdaptedPropagator(self) -> org.orekit.propagation.Propagator: ...
    def getEvaluations(self) -> int: ...
    def getRMS(self) -> float: ...

class AdamsBashforthIntegratorBuilder(ODEIntegratorBuilder):
    def __init__(self, int: int, double: float, double2: float, double3: float): ...
    def buildIntegrator(self, orbit: org.orekit.orbits.Orbit, orbitType: org.orekit.orbits.OrbitType) -> org.hipparchus.ode.AbstractIntegrator: ...

class AdamsMoultonIntegratorBuilder(ODEIntegratorBuilder):
    def __init__(self, int: int, double: float, double2: float, double3: float): ...
    def buildIntegrator(self, orbit: org.orekit.orbits.Orbit, orbitType: org.orekit.orbits.OrbitType) -> org.hipparchus.ode.AbstractIntegrator: ...

class ClassicalRungeKuttaIntegratorBuilder(ODEIntegratorBuilder):
    def __init__(self, double: float): ...
    def buildIntegrator(self, orbit: org.orekit.orbits.Orbit, orbitType: org.orekit.orbits.OrbitType) -> org.hipparchus.ode.AbstractIntegrator: ...

class DormandPrince54IntegratorBuilder(ODEIntegratorBuilder):
    def __init__(self, double: float, double2: float, double3: float): ...
    def buildIntegrator(self, orbit: org.orekit.orbits.Orbit, orbitType: org.orekit.orbits.OrbitType) -> org.hipparchus.ode.AbstractIntegrator: ...

class DormandPrince853IntegratorBuilder(ODEIntegratorBuilder):
    def __init__(self, double: float, double2: float, double3: float): ...
    def buildIntegrator(self, orbit: org.orekit.orbits.Orbit, orbitType: org.orekit.orbits.OrbitType) -> org.hipparchus.ode.AbstractIntegrator: ...

class EulerIntegratorBuilder(ODEIntegratorBuilder):
    def __init__(self, double: float): ...
    def buildIntegrator(self, orbit: org.orekit.orbits.Orbit, orbitType: org.orekit.orbits.OrbitType) -> org.hipparchus.ode.AbstractIntegrator: ...

class GillIntegratorBuilder(ODEIntegratorBuilder):
    def __init__(self, double: float): ...
    def buildIntegrator(self, orbit: org.orekit.orbits.Orbit, orbitType: org.orekit.orbits.OrbitType) -> org.hipparchus.ode.AbstractIntegrator: ...

class GraggBulirschStoerIntegratorBuilder(ODEIntegratorBuilder):
    def __init__(self, double: float, double2: float, double3: float): ...
    def buildIntegrator(self, orbit: org.orekit.orbits.Orbit, orbitType: org.orekit.orbits.OrbitType) -> org.hipparchus.ode.AbstractIntegrator: ...

class HighamHall54IntegratorBuilder(ODEIntegratorBuilder):
    def __init__(self, double: float, double2: float, double3: float): ...
    def buildIntegrator(self, orbit: org.orekit.orbits.Orbit, orbitType: org.orekit.orbits.OrbitType) -> org.hipparchus.ode.AbstractIntegrator: ...

class LutherIntegratorBuilder(ODEIntegratorBuilder):
    def __init__(self, double: float): ...
    def buildIntegrator(self, orbit: org.orekit.orbits.Orbit, orbitType: org.orekit.orbits.OrbitType) -> org.hipparchus.ode.AbstractIntegrator: ...

class MidpointIntegratorBuilder(ODEIntegratorBuilder):
    def __init__(self, double: float): ...
    def buildIntegrator(self, orbit: org.orekit.orbits.Orbit, orbitType: org.orekit.orbits.OrbitType) -> org.hipparchus.ode.AbstractIntegrator: ...

class OrbitDeterminationPropagatorBuilder(PropagatorBuilder):
    def buildKalmanModel(self, list: java.util.List['OrbitDeterminationPropagatorBuilder'], list2: java.util.List[org.orekit.estimation.sequential.CovarianceMatrixProvider], parameterDriversList: org.orekit.utils.ParameterDriversList, covarianceMatrixProvider: org.orekit.estimation.sequential.CovarianceMatrixProvider) -> org.orekit.estimation.sequential.AbstractKalmanModel: ...
    def buildLSModel(self, orbitDeterminationPropagatorBuilderArray: typing.List['OrbitDeterminationPropagatorBuilder'], list: java.util.List[org.orekit.estimation.measurements.ObservedMeasurement[typing.Any]], parameterDriversList: org.orekit.utils.ParameterDriversList, modelObserver: org.orekit.estimation.leastsquares.ModelObserver) -> org.orekit.estimation.leastsquares.AbstractBatchLSModel: ...
    def resetOrbit(self, orbit: org.orekit.orbits.Orbit) -> None: ...

class PythonODEIntegratorBuilder(ODEIntegratorBuilder):
    def __init__(self): ...
    def buildIntegrator(self, orbit: org.orekit.orbits.Orbit, orbitType: org.orekit.orbits.OrbitType) -> org.hipparchus.ode.AbstractIntegrator: ...
    def finalize(self) -> None: ...
    def pythonDecRef(self) -> None: ...
    @typing.overload
    def pythonExtension(self) -> int: ...
    @typing.overload
    def pythonExtension(self, long: int) -> None: ...

class PythonPropagatorBuilder(PropagatorBuilder):
    def __init__(self): ...
    def buildPropagator(self, doubleArray: typing.List[float]) -> org.orekit.propagation.Propagator: ...
    def finalize(self) -> None: ...
    def getFrame(self) -> org.orekit.frames.Frame: ...
    def getInitialOrbitDate(self) -> org.orekit.time.AbsoluteDate: ...
    def getOrbitType(self) -> org.orekit.orbits.OrbitType: ...
    def getOrbitalParametersDrivers(self) -> org.orekit.utils.ParameterDriversList: ...
    def getPositionAngle(self) -> org.orekit.orbits.PositionAngle: ...
    def getPropagationParametersDrivers(self) -> org.orekit.utils.ParameterDriversList: ...
    def getSelectedNormalizedParameters(self) -> typing.List[float]: ...
    def pythonDecRef(self) -> None: ...
    @typing.overload
    def pythonExtension(self) -> int: ...
    @typing.overload
    def pythonExtension(self, long: int) -> None: ...

class PythonPropagatorConverter(PropagatorConverter):
    def __init__(self): ...
    @typing.overload
    def convert(self, propagator: org.orekit.propagation.Propagator, double: float, int: int, list: java.util.List[str]) -> org.orekit.propagation.Propagator: ...
    @typing.overload
    def convert(self, list: java.util.List[org.orekit.propagation.SpacecraftState], boolean: bool, stringArray: typing.List[str]) -> org.orekit.propagation.Propagator: ...
    @typing.overload
    def convert(self, list: java.util.List[org.orekit.propagation.SpacecraftState], boolean: bool, list2: java.util.List[str]) -> org.orekit.propagation.Propagator: ...
    @typing.overload
    def convert(self, propagator: org.orekit.propagation.Propagator, double: float, int: int, stringArray: typing.List[str]) -> org.orekit.propagation.Propagator: ...
    def convert_LbL(self, list: java.util.List[org.orekit.propagation.SpacecraftState], boolean: bool, list2: java.util.List[str]) -> org.orekit.propagation.Propagator: ...
    def convert_LbS(self, list: java.util.List[org.orekit.propagation.SpacecraftState], boolean: bool, stringArray: typing.List[str]) -> org.orekit.propagation.Propagator: ...
    def convert_PdiS(self, propagator: org.orekit.propagation.Propagator, double: float, int: int, stringArray: typing.List[str]) -> org.orekit.propagation.Propagator: ...
    def finalize(self) -> None: ...
    def pythonDecRef(self) -> None: ...
    @typing.overload
    def pythonExtension(self) -> int: ...
    @typing.overload
    def pythonExtension(self, long: int) -> None: ...

class ThreeEighthesIntegratorBuilder(ODEIntegratorBuilder):
    def __init__(self, double: float): ...
    def buildIntegrator(self, orbit: org.orekit.orbits.Orbit, orbitType: org.orekit.orbits.OrbitType) -> org.hipparchus.ode.AbstractIntegrator: ...

class DSSTPropagatorBuilder(AbstractPropagatorBuilder, OrbitDeterminationPropagatorBuilder):
    @typing.overload
    def __init__(self, orbit: org.orekit.orbits.Orbit, oDEIntegratorBuilder: ODEIntegratorBuilder, double: float, propagationType: org.orekit.propagation.PropagationType, propagationType2: org.orekit.propagation.PropagationType): ...
    @typing.overload
    def __init__(self, orbit: org.orekit.orbits.Orbit, oDEIntegratorBuilder: ODEIntegratorBuilder, double: float, propagationType: org.orekit.propagation.PropagationType, propagationType2: org.orekit.propagation.PropagationType, attitudeProvider: org.orekit.attitudes.AttitudeProvider): ...
    def addForceModel(self, dSSTForceModel: org.orekit.propagation.semianalytical.dsst.forces.DSSTForceModel) -> None: ...
    def buildKalmanModel(self, list: java.util.List[OrbitDeterminationPropagatorBuilder], list2: java.util.List[org.orekit.estimation.sequential.CovarianceMatrixProvider], parameterDriversList: org.orekit.utils.ParameterDriversList, covarianceMatrixProvider: org.orekit.estimation.sequential.CovarianceMatrixProvider) -> org.orekit.estimation.sequential.DSSTKalmanModel: ...
    def buildLSModel(self, orbitDeterminationPropagatorBuilderArray: typing.List[OrbitDeterminationPropagatorBuilder], list: java.util.List[org.orekit.estimation.measurements.ObservedMeasurement[typing.Any]], parameterDriversList: org.orekit.utils.ParameterDriversList, modelObserver: org.orekit.estimation.leastsquares.ModelObserver) -> org.orekit.estimation.leastsquares.DSSTBatchLSModel: ...
    def buildPropagator(self, doubleArray: typing.List[float]) -> org.orekit.propagation.semianalytical.dsst.DSSTPropagator: ...
    def copy(self) -> 'DSSTPropagatorBuilder': ...
    def getAllForceModels(self) -> java.util.List[org.orekit.propagation.semianalytical.dsst.forces.DSSTForceModel]: ...
    def getIntegratorBuilder(self) -> ODEIntegratorBuilder: ...
    def getMass(self) -> float: ...
    def setMass(self, double: float) -> None: ...

class EcksteinHechlerPropagatorBuilder(AbstractPropagatorBuilder):
    @typing.overload
    def __init__(self, orbit: org.orekit.orbits.Orbit, double: float, double2: float, tideSystem: org.orekit.forces.gravity.potential.TideSystem, double3: float, double4: float, double5: float, double6: float, double7: float, orbitType: org.orekit.orbits.OrbitType, positionAngle: org.orekit.orbits.PositionAngle, double8: float): ...
    @typing.overload
    def __init__(self, orbit: org.orekit.orbits.Orbit, unnormalizedSphericalHarmonicsProvider: org.orekit.forces.gravity.potential.UnnormalizedSphericalHarmonicsProvider, positionAngle: org.orekit.orbits.PositionAngle, double: float): ...
    @typing.overload
    def __init__(self, orbit: org.orekit.orbits.Orbit, unnormalizedSphericalHarmonicsProvider: org.orekit.forces.gravity.potential.UnnormalizedSphericalHarmonicsProvider, positionAngle: org.orekit.orbits.PositionAngle, double: float, attitudeProvider: org.orekit.attitudes.AttitudeProvider): ...
    def buildPropagator(self, doubleArray: typing.List[float]) -> org.orekit.propagation.Propagator: ...

class FiniteDifferencePropagatorConverter(AbstractPropagatorConverter):
    def __init__(self, propagatorBuilder: PropagatorBuilder, double: float, int: int): ...

class JacobianPropagatorConverter(AbstractPropagatorConverter):
    def __init__(self, numericalPropagatorBuilder: 'NumericalPropagatorBuilder', double: float, int: int): ...

class KeplerianPropagatorBuilder(AbstractPropagatorBuilder):
    @typing.overload
    def __init__(self, orbit: org.orekit.orbits.Orbit, positionAngle: org.orekit.orbits.PositionAngle, double: float): ...
    @typing.overload
    def __init__(self, orbit: org.orekit.orbits.Orbit, positionAngle: org.orekit.orbits.PositionAngle, double: float, attitudeProvider: org.orekit.attitudes.AttitudeProvider): ...
    def buildPropagator(self, doubleArray: typing.List[float]) -> org.orekit.propagation.Propagator: ...

class NumericalPropagatorBuilder(AbstractPropagatorBuilder, OrbitDeterminationPropagatorBuilder):
    @typing.overload
    def __init__(self, orbit: org.orekit.orbits.Orbit, oDEIntegratorBuilder: ODEIntegratorBuilder, positionAngle: org.orekit.orbits.PositionAngle, double: float): ...
    @typing.overload
    def __init__(self, orbit: org.orekit.orbits.Orbit, oDEIntegratorBuilder: ODEIntegratorBuilder, positionAngle: org.orekit.orbits.PositionAngle, double: float, attitudeProvider: org.orekit.attitudes.AttitudeProvider): ...
    def addForceModel(self, forceModel: org.orekit.forces.ForceModel) -> None: ...
    def buildKalmanModel(self, list: java.util.List[OrbitDeterminationPropagatorBuilder], list2: java.util.List[org.orekit.estimation.sequential.CovarianceMatrixProvider], parameterDriversList: org.orekit.utils.ParameterDriversList, covarianceMatrixProvider: org.orekit.estimation.sequential.CovarianceMatrixProvider) -> org.orekit.estimation.sequential.KalmanModel: ...
    def buildLSModel(self, orbitDeterminationPropagatorBuilderArray: typing.List[OrbitDeterminationPropagatorBuilder], list: java.util.List[org.orekit.estimation.measurements.ObservedMeasurement[typing.Any]], parameterDriversList: org.orekit.utils.ParameterDriversList, modelObserver: org.orekit.estimation.leastsquares.ModelObserver) -> org.orekit.estimation.leastsquares.BatchLSModel: ...
    def buildPropagator(self, doubleArray: typing.List[float]) -> org.orekit.propagation.numerical.NumericalPropagator: ...
    def copy(self) -> 'NumericalPropagatorBuilder': ...
    def getAllForceModels(self) -> java.util.List[org.orekit.forces.ForceModel]: ...
    def getIntegratorBuilder(self) -> ODEIntegratorBuilder: ...
    def getMass(self) -> float: ...
    def setMass(self, double: float) -> None: ...

class PythonAbstractPropagatorBuilder(AbstractPropagatorBuilder):
    def __init__(self, orbit: org.orekit.orbits.Orbit, positionAngle: org.orekit.orbits.PositionAngle, double: float, boolean: bool): ...
    def buildPropagator(self, doubleArray: typing.List[float]) -> org.orekit.propagation.Propagator: ...
    def finalize(self) -> None: ...
    def pythonDecRef(self) -> None: ...
    @typing.overload
    def pythonExtension(self) -> int: ...
    @typing.overload
    def pythonExtension(self, long: int) -> None: ...

class PythonAbstractPropagatorConverter(AbstractPropagatorConverter):
    def __init__(self, propagatorBuilder: PropagatorBuilder, double: float, int: int): ...
    def finalize(self) -> None: ...
    def getModel(self) -> org.hipparchus.optim.nonlinear.vector.leastsquares.MultivariateJacobianFunction: ...
    def getObjectiveFunction(self) -> org.hipparchus.analysis.MultivariateVectorFunction: ...
    def pythonDecRef(self) -> None: ...
    @typing.overload
    def pythonExtension(self) -> int: ...
    @typing.overload
    def pythonExtension(self, long: int) -> None: ...

class PythonOrbitDeterminationPropagatorBuilder(OrbitDeterminationPropagatorBuilder):
    def __init__(self): ...
    def buildKalmanModel(self, list: java.util.List[OrbitDeterminationPropagatorBuilder], list2: java.util.List[org.orekit.estimation.sequential.CovarianceMatrixProvider], parameterDriversList: org.orekit.utils.ParameterDriversList, covarianceMatrixProvider: org.orekit.estimation.sequential.CovarianceMatrixProvider) -> org.orekit.estimation.sequential.AbstractKalmanModel: ...
    def buildLSModel(self, orbitDeterminationPropagatorBuilderArray: typing.List[OrbitDeterminationPropagatorBuilder], list: java.util.List[org.orekit.estimation.measurements.ObservedMeasurement[typing.Any]], parameterDriversList: org.orekit.utils.ParameterDriversList, modelObserver: org.orekit.estimation.leastsquares.ModelObserver) -> org.orekit.estimation.leastsquares.AbstractBatchLSModel: ...
    def buildPropagator(self, doubleArray: typing.List[float]) -> org.orekit.propagation.Propagator: ...
    def finalize(self) -> None: ...
    def getFrame(self) -> org.orekit.frames.Frame: ...
    def getInitialOrbitDate(self) -> org.orekit.time.AbsoluteDate: ...
    def getOrbitType(self) -> org.orekit.orbits.OrbitType: ...
    def getOrbitalParametersDrivers(self) -> org.orekit.utils.ParameterDriversList: ...
    def getPositionAngle(self) -> org.orekit.orbits.PositionAngle: ...
    def getPropagationParametersDrivers(self) -> org.orekit.utils.ParameterDriversList: ...
    def getSelectedNormalizedParameters(self) -> typing.List[float]: ...
    def pythonDecRef(self) -> None: ...
    @typing.overload
    def pythonExtension(self) -> int: ...
    @typing.overload
    def pythonExtension(self, long: int) -> None: ...
    def resetOrbit(self, orbit: org.orekit.orbits.Orbit) -> None: ...

class TLEPropagatorBuilder(AbstractPropagatorBuilder, OrbitDeterminationPropagatorBuilder):
    @typing.overload
    def __init__(self, tLE: org.orekit.propagation.analytical.tle.TLE, positionAngle: org.orekit.orbits.PositionAngle, double: float): ...
    @typing.overload
    def __init__(self, tLE: org.orekit.propagation.analytical.tle.TLE, positionAngle: org.orekit.orbits.PositionAngle, double: float, dataContext: org.orekit.data.DataContext): ...
    def buildKalmanModel(self, list: java.util.List[OrbitDeterminationPropagatorBuilder], list2: java.util.List[org.orekit.estimation.sequential.CovarianceMatrixProvider], parameterDriversList: org.orekit.utils.ParameterDriversList, covarianceMatrixProvider: org.orekit.estimation.sequential.CovarianceMatrixProvider) -> org.orekit.estimation.sequential.AbstractKalmanModel: ...
    def buildLSModel(self, orbitDeterminationPropagatorBuilderArray: typing.List[OrbitDeterminationPropagatorBuilder], list: java.util.List[org.orekit.estimation.measurements.ObservedMeasurement[typing.Any]], parameterDriversList: org.orekit.utils.ParameterDriversList, modelObserver: org.orekit.estimation.leastsquares.ModelObserver) -> org.orekit.estimation.leastsquares.AbstractBatchLSModel: ...
    def buildPropagator(self, doubleArray: typing.List[float]) -> org.orekit.propagation.analytical.tle.TLEPropagator: ...
    def getTemplateTLE(self) -> org.orekit.propagation.analytical.tle.TLE: ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.orekit.propagation.conversion")``.

    AbstractPropagatorBuilder: typing.Type[AbstractPropagatorBuilder]
    AbstractPropagatorConverter: typing.Type[AbstractPropagatorConverter]
    AdamsBashforthIntegratorBuilder: typing.Type[AdamsBashforthIntegratorBuilder]
    AdamsMoultonIntegratorBuilder: typing.Type[AdamsMoultonIntegratorBuilder]
    ClassicalRungeKuttaIntegratorBuilder: typing.Type[ClassicalRungeKuttaIntegratorBuilder]
    DSSTPropagatorBuilder: typing.Type[DSSTPropagatorBuilder]
    DormandPrince54IntegratorBuilder: typing.Type[DormandPrince54IntegratorBuilder]
    DormandPrince853IntegratorBuilder: typing.Type[DormandPrince853IntegratorBuilder]
    EcksteinHechlerPropagatorBuilder: typing.Type[EcksteinHechlerPropagatorBuilder]
    EulerIntegratorBuilder: typing.Type[EulerIntegratorBuilder]
    FiniteDifferencePropagatorConverter: typing.Type[FiniteDifferencePropagatorConverter]
    GillIntegratorBuilder: typing.Type[GillIntegratorBuilder]
    GraggBulirschStoerIntegratorBuilder: typing.Type[GraggBulirschStoerIntegratorBuilder]
    HighamHall54IntegratorBuilder: typing.Type[HighamHall54IntegratorBuilder]
    JacobianPropagatorConverter: typing.Type[JacobianPropagatorConverter]
    KeplerianPropagatorBuilder: typing.Type[KeplerianPropagatorBuilder]
    LutherIntegratorBuilder: typing.Type[LutherIntegratorBuilder]
    MidpointIntegratorBuilder: typing.Type[MidpointIntegratorBuilder]
    NumericalPropagatorBuilder: typing.Type[NumericalPropagatorBuilder]
    ODEIntegratorBuilder: typing.Type[ODEIntegratorBuilder]
    OrbitDeterminationPropagatorBuilder: typing.Type[OrbitDeterminationPropagatorBuilder]
    OsculatingToMeanElementsConverter: typing.Type[OsculatingToMeanElementsConverter]
    PropagatorBuilder: typing.Type[PropagatorBuilder]
    PropagatorConverter: typing.Type[PropagatorConverter]
    PythonAbstractPropagatorBuilder: typing.Type[PythonAbstractPropagatorBuilder]
    PythonAbstractPropagatorConverter: typing.Type[PythonAbstractPropagatorConverter]
    PythonODEIntegratorBuilder: typing.Type[PythonODEIntegratorBuilder]
    PythonOrbitDeterminationPropagatorBuilder: typing.Type[PythonOrbitDeterminationPropagatorBuilder]
    PythonPropagatorBuilder: typing.Type[PythonPropagatorBuilder]
    PythonPropagatorConverter: typing.Type[PythonPropagatorConverter]
    TLEPropagatorBuilder: typing.Type[TLEPropagatorBuilder]
    ThreeEighthesIntegratorBuilder: typing.Type[ThreeEighthesIntegratorBuilder]