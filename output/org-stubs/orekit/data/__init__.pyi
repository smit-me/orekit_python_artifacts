import java.io
import java.lang
import java.net
import java.util
import java.util.regex
import jpype.protocol
import org.hipparchus
import org.orekit.bodies
import org.orekit.forces.gravity.potential
import org.orekit.frames
import org.orekit.models.earth
import org.orekit.time
import org.orekit.utils
import typing



class AbstractSelfFeedingLoader:
    def __init__(self, string: str, dataProvidersManager: 'DataProvidersManager'): ...

class DataContext:
    def getCelestialBodies(self) -> org.orekit.bodies.CelestialBodies: ...
    @staticmethod
    def getDefault() -> 'LazyLoadedDataContext': ...
    def getFrames(self) -> org.orekit.frames.Frames: ...
    def getGeoMagneticFields(self) -> org.orekit.models.earth.GeoMagneticFields: ...
    def getGravityFields(self) -> org.orekit.forces.gravity.potential.GravityFields: ...
    def getTimeScales(self) -> org.orekit.time.TimeScales: ...
    @staticmethod
    def setDefault(lazyLoadedDataContext: 'LazyLoadedDataContext') -> None: ...

class DataFilter:
    def filter(self, dataSource: 'DataSource') -> 'DataSource': ...

class DataLoader:
    def loadData(self, inputStream: java.io.InputStream, string: str) -> None: ...
    def stillAcceptsData(self) -> bool: ...

class DataProvider:
    ZIP_ARCHIVE_PATTERN: typing.ClassVar[java.util.regex.Pattern] = ...
    def feed(self, pattern: java.util.regex.Pattern, dataLoader: DataLoader, dataProvidersManager: 'DataProvidersManager') -> bool: ...

class DataProvidersManager:
    OREKIT_DATA_PATH: typing.ClassVar[str] = ...
    def __init__(self): ...
    def addDefaultProviders(self) -> None: ...
    def addProvider(self, dataProvider: DataProvider) -> None: ...
    def clearLoadedDataNames(self) -> None: ...
    def clearProviders(self) -> None: ...
    def feed(self, string: str, dataLoader: DataLoader) -> bool: ...
    def getFiltersManager(self) -> 'FiltersManager': ...
    def getLoadedDataNames(self) -> java.util.Set[str]: ...
    def getProviders(self) -> java.util.List[DataProvider]: ...
    def isSupported(self, dataProvider: DataProvider) -> bool: ...
    def removeProvider(self, dataProvider: DataProvider) -> DataProvider: ...
    def resetFiltersToDefault(self) -> None: ...

class DataSource:
    @typing.overload
    def __init__(self, file: typing.Union[java.io.File, jpype.protocol.SupportsPath]): ...
    @typing.overload
    def __init__(self, string: str): ...
    @typing.overload
    def __init__(self, string: str, readerOpener: 'DataSource.ReaderOpener'): ...
    @typing.overload
    def __init__(self, string: str, streamOpener: 'DataSource.StreamOpener'): ...
    @typing.overload
    def __init__(self, uRI: java.net.URI): ...
    def getName(self) -> str: ...
    def getOpener(self) -> 'DataSource.Opener': ...
    class Opener:
        def openReaderOnce(self) -> java.io.Reader: ...
        def openStreamOnce(self) -> java.io.InputStream: ...
        def rawDataIsBinary(self) -> bool: ...
    class ReaderOpener:
        def openOnce(self) -> java.io.Reader: ...
    class StreamOpener:
        def openOnce(self) -> java.io.InputStream: ...

class DelaunayArguments(org.orekit.time.TimeStamped, java.io.Serializable):
    def __init__(self, absoluteDate: org.orekit.time.AbsoluteDate, double: float, double2: float, double3: float, double4: float, double5: float, double6: float, double7: float, double8: float, double9: float, double10: float, double11: float, double12: float, double13: float): ...
    def getD(self) -> float: ...
    def getDDot(self) -> float: ...
    def getDate(self) -> org.orekit.time.AbsoluteDate: ...
    def getF(self) -> float: ...
    def getFDot(self) -> float: ...
    def getGamma(self) -> float: ...
    def getGammaDot(self) -> float: ...
    def getL(self) -> float: ...
    def getLDot(self) -> float: ...
    def getLPrime(self) -> float: ...
    def getLPrimeDot(self) -> float: ...
    def getOmega(self) -> float: ...
    def getOmegaDot(self) -> float: ...
    def getTC(self) -> float: ...

_FieldDelaunayArguments__T = typing.TypeVar('_FieldDelaunayArguments__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldDelaunayArguments(org.orekit.time.FieldTimeStamped[_FieldDelaunayArguments__T], typing.Generic[_FieldDelaunayArguments__T]):
    def __init__(self, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_FieldDelaunayArguments__T], t: _FieldDelaunayArguments__T, t2: _FieldDelaunayArguments__T, t3: _FieldDelaunayArguments__T, t4: _FieldDelaunayArguments__T, t5: _FieldDelaunayArguments__T, t6: _FieldDelaunayArguments__T, t7: _FieldDelaunayArguments__T, t8: _FieldDelaunayArguments__T, t9: _FieldDelaunayArguments__T, t10: _FieldDelaunayArguments__T, t11: _FieldDelaunayArguments__T, t12: _FieldDelaunayArguments__T, t13: _FieldDelaunayArguments__T): ...
    def getD(self) -> _FieldDelaunayArguments__T: ...
    def getDDot(self) -> _FieldDelaunayArguments__T: ...
    def getDate(self) -> org.orekit.time.FieldAbsoluteDate[_FieldDelaunayArguments__T]: ...
    def getF(self) -> _FieldDelaunayArguments__T: ...
    def getFDot(self) -> _FieldDelaunayArguments__T: ...
    def getGamma(self) -> _FieldDelaunayArguments__T: ...
    def getGammaDot(self) -> _FieldDelaunayArguments__T: ...
    def getL(self) -> _FieldDelaunayArguments__T: ...
    def getLDot(self) -> _FieldDelaunayArguments__T: ...
    def getLPrime(self) -> _FieldDelaunayArguments__T: ...
    def getLPrimeDot(self) -> _FieldDelaunayArguments__T: ...
    def getOmega(self) -> _FieldDelaunayArguments__T: ...
    def getOmegaDot(self) -> _FieldDelaunayArguments__T: ...
    def getTC(self) -> _FieldDelaunayArguments__T: ...

class FiltersManager:
    def __init__(self): ...
    def addFilter(self, dataFilter: DataFilter) -> None: ...
    def applyRelevantFilters(self, dataSource: DataSource) -> DataSource: ...
    def clearFilters(self) -> None: ...

class FundamentalNutationArguments(java.io.Serializable):
    @typing.overload
    def __init__(self, iERSConventions: org.orekit.utils.IERSConventions, timeScale: org.orekit.time.TimeScale, inputStream: java.io.InputStream, string: str): ...
    @typing.overload
    def __init__(self, iERSConventions: org.orekit.utils.IERSConventions, timeScale: org.orekit.time.TimeScale, inputStream: java.io.InputStream, string: str, timeScales: org.orekit.time.TimeScales): ...
    @typing.overload
    def __init__(self, iERSConventions: org.orekit.utils.IERSConventions, timeScale: org.orekit.time.TimeScale, list: java.util.List[typing.List[float]]): ...
    @typing.overload
    def __init__(self, iERSConventions: org.orekit.utils.IERSConventions, timeScale: org.orekit.time.TimeScale, list: java.util.List[typing.List[float]], timeScales: org.orekit.time.TimeScales): ...
    _evaluateAll_1__T = typing.TypeVar('_evaluateAll_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def evaluateAll(self, absoluteDate: org.orekit.time.AbsoluteDate) -> 'BodiesElements': ...
    @typing.overload
    def evaluateAll(self, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_evaluateAll_1__T]) -> 'FieldBodiesElements'[_evaluateAll_1__T]: ...

class PoissonSeries:
    def __init__(self, polynomialNutation: 'PolynomialNutation', map: typing.Union[java.util.Map[int, 'SeriesTerm'], typing.Mapping[int, 'SeriesTerm']]): ...
    @staticmethod
    def compile(poissonSeriesArray: typing.List['PoissonSeries']) -> 'PoissonSeries.CompiledSeries': ...
    def getNonPolynomialSize(self) -> int: ...
    def getPolynomial(self) -> 'PolynomialNutation': ...
    _value_1__T = typing.TypeVar('_value_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def value(self, bodiesElements: 'BodiesElements') -> float: ...
    @typing.overload
    def value(self, fieldBodiesElements: 'FieldBodiesElements'[_value_1__T]) -> _value_1__T: ...
    class CompiledSeries:
        _derivative_1__S = typing.TypeVar('_derivative_1__S', bound=org.hipparchus.CalculusFieldElement)  # <S>
        @typing.overload
        def derivative(self, bodiesElements: 'BodiesElements') -> typing.List[float]: ...
        @typing.overload
        def derivative(self, fieldBodiesElements: 'FieldBodiesElements'[_derivative_1__S]) -> typing.List[_derivative_1__S]: ...
        _value_1__S = typing.TypeVar('_value_1__S', bound=org.hipparchus.CalculusFieldElement)  # <S>
        @typing.overload
        def value(self, bodiesElements: 'BodiesElements') -> typing.List[float]: ...
        @typing.overload
        def value(self, fieldBodiesElements: 'FieldBodiesElements'[_value_1__S]) -> typing.List[_value_1__S]: ...

class PoissonSeriesParser:
    def __init__(self, int: int): ...
    def parse(self, inputStream: java.io.InputStream, string: str) -> PoissonSeries: ...
    def withDoodson(self, int: int, int2: int) -> 'PoissonSeriesParser': ...
    def withFirstDelaunay(self, int: int) -> 'PoissonSeriesParser': ...
    def withFirstPlanetary(self, int: int) -> 'PoissonSeriesParser': ...
    def withGamma(self, int: int) -> 'PoissonSeriesParser': ...
    def withOptionalColumn(self, int: int) -> 'PoissonSeriesParser': ...
    def withPolynomialPart(self, char: str, unit: 'PolynomialParser.Unit') -> 'PoissonSeriesParser': ...
    def withSinCos(self, int: int, int2: int, double: float, int3: int, double2: float) -> 'PoissonSeriesParser': ...

class PolynomialNutation(java.io.Serializable):
    def __init__(self, doubleArray: typing.List[float]): ...
    _derivative_1__T = typing.TypeVar('_derivative_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def derivative(self, double: float) -> float: ...
    @typing.overload
    def derivative(self, t: _derivative_1__T) -> _derivative_1__T: ...
    _value_1__T = typing.TypeVar('_value_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def value(self, double: float) -> float: ...
    @typing.overload
    def value(self, t: _value_1__T) -> _value_1__T: ...

class PolynomialParser:
    def __init__(self, char: str, unit: 'PolynomialParser.Unit'): ...
    def parse(self, string: str) -> typing.List[float]: ...
    class Unit(java.lang.Enum['PolynomialParser.Unit']):
        RADIANS: typing.ClassVar['PolynomialParser.Unit'] = ...
        DEGREES: typing.ClassVar['PolynomialParser.Unit'] = ...
        ARC_SECONDS: typing.ClassVar['PolynomialParser.Unit'] = ...
        MILLI_ARC_SECONDS: typing.ClassVar['PolynomialParser.Unit'] = ...
        MICRO_ARC_SECONDS: typing.ClassVar['PolynomialParser.Unit'] = ...
        NO_UNITS: typing.ClassVar['PolynomialParser.Unit'] = ...
        def toSI(self, double: float) -> float: ...
        _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
        @typing.overload
        @staticmethod
        def valueOf(class_: typing.Type[_valueOf_0__T], string: str) -> _valueOf_0__T: ...
        @typing.overload
        @staticmethod
        def valueOf(string: str) -> 'PolynomialParser.Unit': ...
        @staticmethod
        def values() -> typing.List['PolynomialParser.Unit']: ...

_SimpleTimeStampedTableParser__RowConverter__S = typing.TypeVar('_SimpleTimeStampedTableParser__RowConverter__S', bound=org.orekit.time.TimeStamped)  # <S>
_SimpleTimeStampedTableParser__T = typing.TypeVar('_SimpleTimeStampedTableParser__T', bound=org.orekit.time.TimeStamped)  # <T>
class SimpleTimeStampedTableParser(typing.Generic[_SimpleTimeStampedTableParser__T]):
    def __init__(self, int: int, rowConverter: 'SimpleTimeStampedTableParser.RowConverter'[_SimpleTimeStampedTableParser__T]): ...
    def parse(self, inputStream: java.io.InputStream, string: str) -> java.util.List[_SimpleTimeStampedTableParser__T]: ...
    class RowConverter(typing.Generic[_SimpleTimeStampedTableParser__RowConverter__S]):
        def convert(self, doubleArray: typing.List[float]) -> _SimpleTimeStampedTableParser__RowConverter__S: ...

class SeriesTerm: ...

_AbstractListCrawler__T = typing.TypeVar('_AbstractListCrawler__T')  # <T>
class AbstractListCrawler(DataProvider, typing.Generic[_AbstractListCrawler__T]):
    def addInput(self, t: _AbstractListCrawler__T) -> None: ...
    def feed(self, pattern: java.util.regex.Pattern, dataLoader: DataLoader, dataProvidersManager: DataProvidersManager) -> bool: ...
    def getInputs(self) -> java.util.List[_AbstractListCrawler__T]: ...

class BodiesElements(DelaunayArguments, java.io.Serializable):
    def __init__(self, absoluteDate: org.orekit.time.AbsoluteDate, double: float, double2: float, double3: float, double4: float, double5: float, double6: float, double7: float, double8: float, double9: float, double10: float, double11: float, double12: float, double13: float, double14: float, double15: float, double16: float, double17: float, double18: float, double19: float, double20: float, double21: float, double22: float, double23: float, double24: float, double25: float, double26: float, double27: float, double28: float, double29: float, double30: float, double31: float): ...
    def getLE(self) -> float: ...
    def getLEDot(self) -> float: ...
    def getLJu(self) -> float: ...
    def getLJuDot(self) -> float: ...
    def getLMa(self) -> float: ...
    def getLMaDot(self) -> float: ...
    def getLMe(self) -> float: ...
    def getLMeDot(self) -> float: ...
    def getLNe(self) -> float: ...
    def getLNeDot(self) -> float: ...
    def getLSa(self) -> float: ...
    def getLSaDot(self) -> float: ...
    def getLUr(self) -> float: ...
    def getLUrDot(self) -> float: ...
    def getLVe(self) -> float: ...
    def getLVeDot(self) -> float: ...
    def getPa(self) -> float: ...
    def getPaDot(self) -> float: ...

class ClasspathCrawler(DataProvider):
    @typing.overload
    def __init__(self, classLoader: java.lang.ClassLoader, stringArray: typing.List[str]): ...
    @typing.overload
    def __init__(self, stringArray: typing.List[str]): ...
    def feed(self, pattern: java.util.regex.Pattern, dataLoader: DataLoader, dataProvidersManager: DataProvidersManager) -> bool: ...

class CompositeDataContext(DataContext):
    def __init__(self, timeScales: org.orekit.time.TimeScales, frames: org.orekit.frames.Frames, celestialBodies: org.orekit.bodies.CelestialBodies, gravityFields: org.orekit.forces.gravity.potential.GravityFields, geoMagneticFields: org.orekit.models.earth.GeoMagneticFields): ...
    def getCelestialBodies(self) -> org.orekit.bodies.CelestialBodies: ...
    def getFrames(self) -> org.orekit.frames.Frames: ...
    def getGeoMagneticFields(self) -> org.orekit.models.earth.GeoMagneticFields: ...
    def getGravityFields(self) -> org.orekit.forces.gravity.potential.GravityFields: ...
    def getTimeScales(self) -> org.orekit.time.TimeScales: ...

class DirectoryCrawler(DataProvider):
    def __init__(self, file: typing.Union[java.io.File, jpype.protocol.SupportsPath]): ...
    def feed(self, pattern: java.util.regex.Pattern, dataLoader: DataLoader, dataProvidersManager: DataProvidersManager) -> bool: ...

_FieldBodiesElements__T = typing.TypeVar('_FieldBodiesElements__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldBodiesElements(FieldDelaunayArguments[_FieldBodiesElements__T], typing.Generic[_FieldBodiesElements__T]):
    def __init__(self, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_FieldBodiesElements__T], t: _FieldBodiesElements__T, t2: _FieldBodiesElements__T, t3: _FieldBodiesElements__T, t4: _FieldBodiesElements__T, t5: _FieldBodiesElements__T, t6: _FieldBodiesElements__T, t7: _FieldBodiesElements__T, t8: _FieldBodiesElements__T, t9: _FieldBodiesElements__T, t10: _FieldBodiesElements__T, t11: _FieldBodiesElements__T, t12: _FieldBodiesElements__T, t13: _FieldBodiesElements__T, t14: _FieldBodiesElements__T, t15: _FieldBodiesElements__T, t16: _FieldBodiesElements__T, t17: _FieldBodiesElements__T, t18: _FieldBodiesElements__T, t19: _FieldBodiesElements__T, t20: _FieldBodiesElements__T, t21: _FieldBodiesElements__T, t22: _FieldBodiesElements__T, t23: _FieldBodiesElements__T, t24: _FieldBodiesElements__T, t25: _FieldBodiesElements__T, t26: _FieldBodiesElements__T, t27: _FieldBodiesElements__T, t28: _FieldBodiesElements__T, t29: _FieldBodiesElements__T, t30: _FieldBodiesElements__T, t31: _FieldBodiesElements__T): ...
    def getLE(self) -> _FieldBodiesElements__T: ...
    def getLEDot(self) -> _FieldBodiesElements__T: ...
    def getLJu(self) -> _FieldBodiesElements__T: ...
    def getLJuDot(self) -> _FieldBodiesElements__T: ...
    def getLMa(self) -> _FieldBodiesElements__T: ...
    def getLMaDot(self) -> _FieldBodiesElements__T: ...
    def getLMe(self) -> _FieldBodiesElements__T: ...
    def getLMeDot(self) -> _FieldBodiesElements__T: ...
    def getLNe(self) -> _FieldBodiesElements__T: ...
    def getLNeDot(self) -> _FieldBodiesElements__T: ...
    def getLSa(self) -> _FieldBodiesElements__T: ...
    def getLSaDot(self) -> _FieldBodiesElements__T: ...
    def getLUr(self) -> _FieldBodiesElements__T: ...
    def getLUrDot(self) -> _FieldBodiesElements__T: ...
    def getLVe(self) -> _FieldBodiesElements__T: ...
    def getLVeDot(self) -> _FieldBodiesElements__T: ...
    def getPa(self) -> _FieldBodiesElements__T: ...
    def getPaDot(self) -> _FieldBodiesElements__T: ...

class GzipFilter(DataFilter):
    def __init__(self): ...
    def filter(self, dataSource: DataSource) -> DataSource: ...

class LazyLoadedDataContext(DataContext):
    def __init__(self): ...
    def getCelestialBodies(self) -> org.orekit.bodies.LazyLoadedCelestialBodies: ...
    def getDataProvidersManager(self) -> DataProvidersManager: ...
    def getFrames(self) -> org.orekit.frames.LazyLoadedFrames: ...
    def getGeoMagneticFields(self) -> org.orekit.models.earth.LazyLoadedGeoMagneticFields: ...
    def getGravityFields(self) -> org.orekit.forces.gravity.potential.LazyLoadedGravityFields: ...
    def getTimeScales(self) -> org.orekit.time.LazyLoadedTimeScales: ...

class PythonAbstractSelfFeedingLoader(AbstractSelfFeedingLoader):
    def __init__(self, string: str, dataProvidersManager: DataProvidersManager): ...

class PythonDataContext(DataContext):
    def __init__(self): ...
    def finalize(self) -> None: ...
    def getCelestialBodies(self) -> org.orekit.bodies.CelestialBodies: ...
    def getFrames(self) -> org.orekit.frames.Frames: ...
    def getGeoMagneticFields(self) -> org.orekit.models.earth.GeoMagneticFields: ...
    def getGravityFields(self) -> org.orekit.forces.gravity.potential.GravityFields: ...
    def getTimeScales(self) -> org.orekit.time.TimeScales: ...
    def pythonDecRef(self) -> None: ...
    @typing.overload
    def pythonExtension(self) -> int: ...
    @typing.overload
    def pythonExtension(self, long: int) -> None: ...

class PythonDataFilter(DataFilter):
    def __init__(self): ...
    def filter(self, dataSource: DataSource) -> DataSource: ...
    def finalize(self) -> None: ...
    def pythonDecRef(self) -> None: ...
    @typing.overload
    def pythonExtension(self) -> int: ...
    @typing.overload
    def pythonExtension(self, long: int) -> None: ...

class PythonDataLoader(DataLoader):
    def __init__(self): ...
    def finalize(self) -> None: ...
    def loadData(self, inputStream: java.io.InputStream, string: str) -> None: ...
    def pythonDecRef(self) -> None: ...
    @typing.overload
    def pythonExtension(self) -> int: ...
    @typing.overload
    def pythonExtension(self, long: int) -> None: ...
    def stillAcceptsData(self) -> bool: ...

class PythonDataProvider(DataProvider):
    def __init__(self): ...
    def feed(self, pattern: java.util.regex.Pattern, dataLoader: DataLoader, dataProvidersManager: DataProvidersManager) -> bool: ...
    def finalize(self) -> None: ...
    def pythonDecRef(self) -> None: ...
    @typing.overload
    def pythonExtension(self) -> int: ...
    @typing.overload
    def pythonExtension(self, long: int) -> None: ...

class PythonSeriesTerm(SeriesTerm):
    def __init__(self): ...
    _argument_1__T = typing.TypeVar('_argument_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def argument(self, bodiesElements: BodiesElements) -> float: ...
    @typing.overload
    def argument(self, fieldBodiesElements: FieldBodiesElements[_argument_1__T]) -> _argument_1__T: ...
    _argumentDerivative_1__T = typing.TypeVar('_argumentDerivative_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def argumentDerivative(self, bodiesElements: BodiesElements) -> float: ...
    @typing.overload
    def argumentDerivative(self, fieldBodiesElements: FieldBodiesElements[_argumentDerivative_1__T]) -> _argumentDerivative_1__T: ...
    _argumentDerivative_F__T = typing.TypeVar('_argumentDerivative_F__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    def argumentDerivative_F(self, fieldBodiesElements: FieldBodiesElements[_argumentDerivative_F__T]) -> _argumentDerivative_F__T: ...
    _argument_F__T = typing.TypeVar('_argument_F__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    def argument_F(self, fieldBodiesElements: FieldBodiesElements[_argument_F__T]) -> _argument_F__T: ...
    def finalize(self) -> None: ...
    def pythonDecRef(self) -> None: ...
    @typing.overload
    def pythonExtension(self) -> int: ...
    @typing.overload
    def pythonExtension(self, long: int) -> None: ...

class UnixCompressFilter(DataFilter):
    def __init__(self): ...
    def filter(self, dataSource: DataSource) -> DataSource: ...

class ZipJarCrawler(DataProvider):
    @typing.overload
    def __init__(self, file: typing.Union[java.io.File, jpype.protocol.SupportsPath]): ...
    @typing.overload
    def __init__(self, classLoader: java.lang.ClassLoader, string: str): ...
    @typing.overload
    def __init__(self, string: str): ...
    @typing.overload
    def __init__(self, uRL: java.net.URL): ...
    def feed(self, pattern: java.util.regex.Pattern, dataLoader: DataLoader, dataProvidersManager: DataProvidersManager) -> bool: ...

class ExceptionalDataContext(LazyLoadedDataContext, DataContext):
    def __init__(self): ...
    def getCelestialBodies(self) -> org.orekit.bodies.LazyLoadedCelestialBodies: ...
    def getFrames(self) -> org.orekit.frames.LazyLoadedFrames: ...
    def getGeoMagneticFields(self) -> org.orekit.models.earth.LazyLoadedGeoMagneticFields: ...
    def getGravityFields(self) -> org.orekit.forces.gravity.potential.LazyLoadedGravityFields: ...
    def getTimeScales(self) -> org.orekit.time.LazyLoadedTimeScales: ...

class FilesListCrawler(AbstractListCrawler[java.io.File]):
    def __init__(self, fileArray: typing.List[java.io.File]): ...

class NetworkCrawler(AbstractListCrawler[java.net.URL]):
    def __init__(self, uRLArray: typing.List[java.net.URL]): ...
    def setTimeout(self, int: int) -> None: ...

_PythonAbstractListCrawler__T = typing.TypeVar('_PythonAbstractListCrawler__T')  # <T>
class PythonAbstractListCrawler(AbstractListCrawler[_PythonAbstractListCrawler__T], typing.Generic[_PythonAbstractListCrawler__T]):
    def __init__(self): ...
    def finalize(self) -> None: ...
    def getBaseName(self, t: _PythonAbstractListCrawler__T) -> str: ...
    def getCompleteName(self, t: _PythonAbstractListCrawler__T) -> str: ...
    def getStream(self, t: _PythonAbstractListCrawler__T) -> java.io.InputStream: ...
    def getZipJarCrawler(self, t: _PythonAbstractListCrawler__T) -> ZipJarCrawler: ...
    def pythonDecRef(self) -> None: ...
    @typing.overload
    def pythonExtension(self) -> int: ...
    @typing.overload
    def pythonExtension(self, long: int) -> None: ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.orekit.data")``.

    AbstractListCrawler: typing.Type[AbstractListCrawler]
    AbstractSelfFeedingLoader: typing.Type[AbstractSelfFeedingLoader]
    BodiesElements: typing.Type[BodiesElements]
    ClasspathCrawler: typing.Type[ClasspathCrawler]
    CompositeDataContext: typing.Type[CompositeDataContext]
    DataContext: typing.Type[DataContext]
    DataFilter: typing.Type[DataFilter]
    DataLoader: typing.Type[DataLoader]
    DataProvider: typing.Type[DataProvider]
    DataProvidersManager: typing.Type[DataProvidersManager]
    DataSource: typing.Type[DataSource]
    DelaunayArguments: typing.Type[DelaunayArguments]
    DirectoryCrawler: typing.Type[DirectoryCrawler]
    ExceptionalDataContext: typing.Type[ExceptionalDataContext]
    FieldBodiesElements: typing.Type[FieldBodiesElements]
    FieldDelaunayArguments: typing.Type[FieldDelaunayArguments]
    FilesListCrawler: typing.Type[FilesListCrawler]
    FiltersManager: typing.Type[FiltersManager]
    FundamentalNutationArguments: typing.Type[FundamentalNutationArguments]
    GzipFilter: typing.Type[GzipFilter]
    LazyLoadedDataContext: typing.Type[LazyLoadedDataContext]
    NetworkCrawler: typing.Type[NetworkCrawler]
    PoissonSeries: typing.Type[PoissonSeries]
    PoissonSeriesParser: typing.Type[PoissonSeriesParser]
    PolynomialNutation: typing.Type[PolynomialNutation]
    PolynomialParser: typing.Type[PolynomialParser]
    PythonAbstractListCrawler: typing.Type[PythonAbstractListCrawler]
    PythonAbstractSelfFeedingLoader: typing.Type[PythonAbstractSelfFeedingLoader]
    PythonDataContext: typing.Type[PythonDataContext]
    PythonDataFilter: typing.Type[PythonDataFilter]
    PythonDataLoader: typing.Type[PythonDataLoader]
    PythonDataProvider: typing.Type[PythonDataProvider]
    PythonSeriesTerm: typing.Type[PythonSeriesTerm]
    SeriesTerm: typing.Type[SeriesTerm]
    SimpleTimeStampedTableParser: typing.Type[SimpleTimeStampedTableParser]
    UnixCompressFilter: typing.Type[UnixCompressFilter]
    ZipJarCrawler: typing.Type[ZipJarCrawler]