import java.io
import java.lang
import java.util
import org.orekit.data
import org.orekit.time
import typing



class AstronomicalAmplitudeReader(org.orekit.data.DataLoader):
    def __init__(self, string: str, int: int, int2: int, int3: int, double: float): ...
    def getAstronomicalAmplitudesMap(self) -> java.util.Map[int, float]: ...
    def getSupportedNames(self) -> str: ...
    def loadData(self, inputStream: java.io.InputStream, string: str) -> None: ...
    def stillAcceptsData(self) -> bool: ...

class GravityFieldFactory:
    ICGEM_FILENAME: typing.ClassVar[str] = ...
    SHM_FILENAME: typing.ClassVar[str] = ...
    EGM_FILENAME: typing.ClassVar[str] = ...
    GRGS_FILENAME: typing.ClassVar[str] = ...
    FES_CNM_SNM_FILENAME: typing.ClassVar[str] = ...
    FES_CHAT_EPSILON_FILENAME: typing.ClassVar[str] = ...
    FES_HF_FILENAME: typing.ClassVar[str] = ...
    @staticmethod
    def addDefaultOceanTidesReaders() -> None: ...
    @staticmethod
    def addDefaultPotentialCoefficientsReaders() -> None: ...
    @staticmethod
    def addOceanTidesReader(oceanTidesReader: 'OceanTidesReader') -> None: ...
    @staticmethod
    def addPotentialCoefficientsReader(potentialCoefficientsReader: 'PotentialCoefficientsReader') -> None: ...
    @staticmethod
    def clearOceanTidesReaders() -> None: ...
    @staticmethod
    def clearPotentialCoefficientsReaders() -> None: ...
    @staticmethod
    def configureOceanLoadDeformationCoefficients(oceanLoadDeformationCoefficients: 'OceanLoadDeformationCoefficients') -> None: ...
    @staticmethod
    def getConstantNormalizedProvider(int: int, int2: int) -> 'NormalizedSphericalHarmonicsProvider': ...
    @staticmethod
    def getConstantUnnormalizedProvider(int: int, int2: int) -> 'UnnormalizedSphericalHarmonicsProvider': ...
    @staticmethod
    def getGravityFields() -> 'LazyLoadedGravityFields': ...
    @typing.overload
    @staticmethod
    def getNormalizedProvider(double: float, double2: float, tideSystem: 'TideSystem', doubleArray: typing.List[typing.List[float]], doubleArray2: typing.List[typing.List[float]]) -> 'NormalizedSphericalHarmonicsProvider': ...
    @typing.overload
    @staticmethod
    def getNormalizedProvider(int: int, int2: int) -> 'NormalizedSphericalHarmonicsProvider': ...
    @typing.overload
    @staticmethod
    def getNormalizedProvider(unnormalizedSphericalHarmonicsProvider: 'UnnormalizedSphericalHarmonicsProvider') -> 'NormalizedSphericalHarmonicsProvider': ...
    @staticmethod
    def getOceanLoadDeformationCoefficients() -> 'OceanLoadDeformationCoefficients': ...
    @staticmethod
    def getOceanTidesWaves(int: int, int2: int) -> java.util.List['OceanTidesWave']: ...
    @staticmethod
    def getUnnormalizationFactors(int: int, int2: int) -> typing.List[typing.List[float]]: ...
    @typing.overload
    @staticmethod
    def getUnnormalizedProvider(double: float, double2: float, tideSystem: 'TideSystem', doubleArray: typing.List[typing.List[float]], doubleArray2: typing.List[typing.List[float]]) -> 'UnnormalizedSphericalHarmonicsProvider': ...
    @typing.overload
    @staticmethod
    def getUnnormalizedProvider(int: int, int2: int) -> 'UnnormalizedSphericalHarmonicsProvider': ...
    @typing.overload
    @staticmethod
    def getUnnormalizedProvider(normalizedSphericalHarmonicsProvider: 'NormalizedSphericalHarmonicsProvider') -> 'UnnormalizedSphericalHarmonicsProvider': ...
    @staticmethod
    def readGravityField(int: int, int2: int) -> 'PotentialCoefficientsReader': ...

class GravityFields:
    def getConstantNormalizedProvider(self, int: int, int2: int) -> 'NormalizedSphericalHarmonicsProvider': ...
    def getConstantUnnormalizedProvider(self, int: int, int2: int) -> 'UnnormalizedSphericalHarmonicsProvider': ...
    def getNormalizedProvider(self, int: int, int2: int) -> 'NormalizedSphericalHarmonicsProvider': ...
    def getOceanTidesWaves(self, int: int, int2: int) -> java.util.List['OceanTidesWave']: ...
    def getUnnormalizedProvider(self, int: int, int2: int) -> 'UnnormalizedSphericalHarmonicsProvider': ...

class OceanLoadDeformationCoefficients(java.lang.Enum['OceanLoadDeformationCoefficients']):
    IERS_1996: typing.ClassVar['OceanLoadDeformationCoefficients'] = ...
    IERS_2003: typing.ClassVar['OceanLoadDeformationCoefficients'] = ...
    IERS_2010: typing.ClassVar['OceanLoadDeformationCoefficients'] = ...
    GEGOUT: typing.ClassVar['OceanLoadDeformationCoefficients'] = ...
    def getCoefficients(self) -> typing.List[float]: ...
    _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(class_: typing.Type[_valueOf_0__T], string: str) -> _valueOf_0__T: ...
    @typing.overload
    @staticmethod
    def valueOf(string: str) -> 'OceanLoadDeformationCoefficients': ...
    @staticmethod
    def values() -> typing.List['OceanLoadDeformationCoefficients']: ...

class OceanTidesReader(org.orekit.data.DataLoader):
    def __init__(self, string: str): ...
    def canAdd(self, int: int, int2: int) -> bool: ...
    def getMaxParseDegree(self) -> int: ...
    def getMaxParseOrder(self) -> int: ...
    def getSupportedNames(self) -> str: ...
    def getWaves(self) -> java.util.List['OceanTidesWave']: ...
    def setMaxParseDegree(self, int: int) -> None: ...
    def setMaxParseOrder(self, int: int) -> None: ...
    def stillAcceptsData(self) -> bool: ...

class OceanTidesWave:
    def __init__(self, int: int, int2: int, int3: int, doubleArray: typing.List[typing.List[typing.List[float]]]): ...
    def addContribution(self, bodiesElements: org.orekit.data.BodiesElements, doubleArray: typing.List[typing.List[float]], doubleArray2: typing.List[typing.List[float]]) -> None: ...
    def getDoodson(self) -> int: ...
    def getMaxDegree(self) -> int: ...
    def getMaxOrder(self) -> int: ...

class PotentialCoefficientsReader(org.orekit.data.DataLoader):
    def getMaxAvailableDegree(self) -> int: ...
    def getMaxAvailableOrder(self) -> int: ...
    def getMaxParseDegree(self) -> int: ...
    def getMaxParseOrder(self) -> int: ...
    def getProvider(self, boolean: bool, int: int, int2: int) -> 'RawSphericalHarmonicsProvider': ...
    def getSupportedNames(self) -> str: ...
    def loadData(self, inputStream: java.io.InputStream, string: str) -> None: ...
    def missingCoefficientsAllowed(self) -> bool: ...
    def setMaxParseDegree(self, int: int) -> None: ...
    def setMaxParseOrder(self, int: int) -> None: ...
    def stillAcceptsData(self) -> bool: ...

class TideSystem(java.lang.Enum['TideSystem']):
    TIDE_FREE: typing.ClassVar['TideSystem'] = ...
    ZERO_TIDE: typing.ClassVar['TideSystem'] = ...
    UNKNOWN: typing.ClassVar['TideSystem'] = ...
    _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(class_: typing.Type[_valueOf_0__T], string: str) -> _valueOf_0__T: ...
    @typing.overload
    @staticmethod
    def valueOf(string: str) -> 'TideSystem': ...
    @staticmethod
    def values() -> typing.List['TideSystem']: ...

class TideSystemProvider:
    def getTideSystem(self) -> TideSystem: ...

class EGMFormatReader(PotentialCoefficientsReader):
    @typing.overload
    def __init__(self, string: str, boolean: bool): ...
    @typing.overload
    def __init__(self, string: str, boolean: bool, boolean2: bool): ...
    def getProvider(self, boolean: bool, int: int, int2: int) -> 'RawSphericalHarmonicsProvider': ...
    def loadData(self, inputStream: java.io.InputStream, string: str) -> None: ...

class FESCHatEpsilonReader(OceanTidesReader):
    def __init__(self, string: str, double: float, double2: float, oceanLoadDeformationCoefficients: OceanLoadDeformationCoefficients, map: typing.Union[java.util.Map[int, float], typing.Mapping[int, float]]): ...
    def loadData(self, inputStream: java.io.InputStream, string: str) -> None: ...

class FESCnmSnmReader(OceanTidesReader):
    def __init__(self, string: str, double: float): ...
    def loadData(self, inputStream: java.io.InputStream, string: str) -> None: ...

class GRGSFormatReader(PotentialCoefficientsReader):
    @typing.overload
    def __init__(self, string: str, boolean: bool): ...
    @typing.overload
    def __init__(self, string: str, boolean: bool, timeScale: org.orekit.time.TimeScale): ...
    def getProvider(self, boolean: bool, int: int, int2: int) -> 'RawSphericalHarmonicsProvider': ...
    def loadData(self, inputStream: java.io.InputStream, string: str) -> None: ...

class ICGEMFormatReader(PotentialCoefficientsReader):
    @typing.overload
    def __init__(self, string: str, boolean: bool): ...
    @typing.overload
    def __init__(self, string: str, boolean: bool, timeScale: org.orekit.time.TimeScale): ...
    def getProvider(self, boolean: bool, int: int, int2: int) -> 'RawSphericalHarmonicsProvider': ...
    def loadData(self, inputStream: java.io.InputStream, string: str) -> None: ...

class LazyLoadedGravityFields(GravityFields):
    def __init__(self, dataProvidersManager: org.orekit.data.DataProvidersManager, timeScale: org.orekit.time.TimeScale): ...
    def addDefaultOceanTidesReaders(self) -> None: ...
    def addDefaultPotentialCoefficientsReaders(self) -> None: ...
    def addOceanTidesReader(self, oceanTidesReader: OceanTidesReader) -> None: ...
    def addPotentialCoefficientsReader(self, potentialCoefficientsReader: PotentialCoefficientsReader) -> None: ...
    def clearOceanTidesReaders(self) -> None: ...
    def clearPotentialCoefficientsReaders(self) -> None: ...
    def configureOceanLoadDeformationCoefficients(self, oceanLoadDeformationCoefficients: OceanLoadDeformationCoefficients) -> None: ...
    def getConstantNormalizedProvider(self, int: int, int2: int) -> 'NormalizedSphericalHarmonicsProvider': ...
    def getConstantUnnormalizedProvider(self, int: int, int2: int) -> 'UnnormalizedSphericalHarmonicsProvider': ...
    def getNormalizedProvider(self, int: int, int2: int) -> 'NormalizedSphericalHarmonicsProvider': ...
    def getOceanLoadDeformationCoefficients(self) -> OceanLoadDeformationCoefficients: ...
    def getOceanTidesWaves(self, int: int, int2: int) -> java.util.List[OceanTidesWave]: ...
    def getUnnormalizedProvider(self, int: int, int2: int) -> 'UnnormalizedSphericalHarmonicsProvider': ...
    def readGravityField(self, int: int, int2: int) -> PotentialCoefficientsReader: ...

class PythonGravityFields(GravityFields):
    def __init__(self): ...
    def finalize(self) -> None: ...
    def getConstantNormalizedProvider(self, int: int, int2: int) -> 'NormalizedSphericalHarmonicsProvider': ...
    def getConstantUnnormalizedProvider(self, int: int, int2: int) -> 'UnnormalizedSphericalHarmonicsProvider': ...
    def getNormalizedProvider(self, int: int, int2: int) -> 'NormalizedSphericalHarmonicsProvider': ...
    def getOceanTidesWaves(self, int: int, int2: int) -> java.util.List[OceanTidesWave]: ...
    def getUnnormalizedProvider(self, int: int, int2: int) -> 'UnnormalizedSphericalHarmonicsProvider': ...
    def pythonDecRef(self) -> None: ...
    @typing.overload
    def pythonExtension(self) -> int: ...
    @typing.overload
    def pythonExtension(self, long: int) -> None: ...

class PythonPotentialCoefficientsReader(PotentialCoefficientsReader):
    def finalize(self) -> None: ...
    def getProvider(self, boolean: bool, int: int, int2: int) -> 'RawSphericalHarmonicsProvider': ...
    def loadData(self, inputStream: java.io.InputStream, string: str) -> None: ...
    def pythonDecRef(self) -> None: ...
    @typing.overload
    def pythonExtension(self) -> int: ...
    @typing.overload
    def pythonExtension(self, long: int) -> None: ...

class PythonTideSystemProvider(TideSystemProvider):
    def __init__(self): ...
    def finalize(self) -> None: ...
    def getTideSystem(self) -> TideSystem: ...
    def pythonDecRef(self) -> None: ...
    @typing.overload
    def pythonExtension(self) -> int: ...
    @typing.overload
    def pythonExtension(self, long: int) -> None: ...

class SHMFormatReader(PotentialCoefficientsReader):
    @typing.overload
    def __init__(self, string: str, boolean: bool): ...
    @typing.overload
    def __init__(self, string: str, boolean: bool, timeScale: org.orekit.time.TimeScale): ...
    def getProvider(self, boolean: bool, int: int, int2: int) -> 'RawSphericalHarmonicsProvider': ...
    def loadData(self, inputStream: java.io.InputStream, string: str) -> None: ...

class SphericalHarmonicsProvider(TideSystemProvider):
    def getAe(self) -> float: ...
    def getMaxDegree(self) -> int: ...
    def getMaxOrder(self) -> int: ...
    def getMu(self) -> float: ...
    def getOffset(self, absoluteDate: org.orekit.time.AbsoluteDate) -> float: ...
    def getReferenceDate(self) -> org.orekit.time.AbsoluteDate: ...

class NormalizedSphericalHarmonicsProvider(SphericalHarmonicsProvider):
    def onDate(self, absoluteDate: org.orekit.time.AbsoluteDate) -> 'NormalizedSphericalHarmonicsProvider.NormalizedSphericalHarmonics': ...
    class NormalizedSphericalHarmonics(org.orekit.time.TimeStamped):
        def getNormalizedCnm(self, int: int, int2: int) -> float: ...
        def getNormalizedSnm(self, int: int, int2: int) -> float: ...

class PythonSphericalHarmonicsProvider(SphericalHarmonicsProvider):
    def __init__(self): ...
    def finalize(self) -> None: ...
    def getAe(self) -> float: ...
    def getMaxDegree(self) -> int: ...
    def getMaxOrder(self) -> int: ...
    def getMu(self) -> float: ...
    def getOffset(self, absoluteDate: org.orekit.time.AbsoluteDate) -> float: ...
    def getReferenceDate(self) -> org.orekit.time.AbsoluteDate: ...
    def getTideSystem(self) -> TideSystem: ...
    def pythonDecRef(self) -> None: ...
    @typing.overload
    def pythonExtension(self) -> int: ...
    @typing.overload
    def pythonExtension(self, long: int) -> None: ...

class RawSphericalHarmonicsProvider(SphericalHarmonicsProvider):
    def onDate(self, absoluteDate: org.orekit.time.AbsoluteDate) -> 'RawSphericalHarmonicsProvider.RawSphericalHarmonics': ...
    class RawSphericalHarmonics(org.orekit.time.TimeStamped):
        def getRawCnm(self, int: int, int2: int) -> float: ...
        def getRawSnm(self, int: int, int2: int) -> float: ...

class UnnormalizedSphericalHarmonicsProvider(SphericalHarmonicsProvider):
    def onDate(self, absoluteDate: org.orekit.time.AbsoluteDate) -> 'UnnormalizedSphericalHarmonicsProvider.UnnormalizedSphericalHarmonics': ...
    class UnnormalizedSphericalHarmonics(org.orekit.time.TimeStamped):
        def getUnnormalizedCnm(self, int: int, int2: int) -> float: ...
        def getUnnormalizedSnm(self, int: int, int2: int) -> float: ...

class CachedNormalizedSphericalHarmonicsProvider(NormalizedSphericalHarmonicsProvider):
    def __init__(self, normalizedSphericalHarmonicsProvider: NormalizedSphericalHarmonicsProvider, double: float, int: int, int2: int, double2: float, double3: float): ...
    def getAe(self) -> float: ...
    def getMaxDegree(self) -> int: ...
    def getMaxOrder(self) -> int: ...
    def getMu(self) -> float: ...
    def getOffset(self, absoluteDate: org.orekit.time.AbsoluteDate) -> float: ...
    def getReferenceDate(self) -> org.orekit.time.AbsoluteDate: ...
    def getTideSystem(self) -> TideSystem: ...
    def onDate(self, absoluteDate: org.orekit.time.AbsoluteDate) -> NormalizedSphericalHarmonicsProvider.NormalizedSphericalHarmonics: ...

class PythonNormalizedSphericalHarmonicsProvider(NormalizedSphericalHarmonicsProvider):
    def __init__(self): ...
    def finalize(self) -> None: ...
    def getAe(self) -> float: ...
    def getMaxDegree(self) -> int: ...
    def getMaxOrder(self) -> int: ...
    def getMu(self) -> float: ...
    def getOffset(self, absoluteDate: org.orekit.time.AbsoluteDate) -> float: ...
    def getReferenceDate(self) -> org.orekit.time.AbsoluteDate: ...
    def getTideSystem(self) -> TideSystem: ...
    def onDate(self, absoluteDate: org.orekit.time.AbsoluteDate) -> NormalizedSphericalHarmonicsProvider.NormalizedSphericalHarmonics: ...
    def pythonDecRef(self) -> None: ...
    @typing.overload
    def pythonExtension(self) -> int: ...
    @typing.overload
    def pythonExtension(self, long: int) -> None: ...

class PythonRawSphericalHarmonicsProvider(RawSphericalHarmonicsProvider):
    def __init__(self): ...
    def finalize(self) -> None: ...
    def getAe(self) -> float: ...
    def getMaxDegree(self) -> int: ...
    def getMaxOrder(self) -> int: ...
    def getMu(self) -> float: ...
    def getOffset(self, absoluteDate: org.orekit.time.AbsoluteDate) -> float: ...
    def getReferenceDate(self) -> org.orekit.time.AbsoluteDate: ...
    def getTideSystem(self) -> TideSystem: ...
    def onDate(self, absoluteDate: org.orekit.time.AbsoluteDate) -> RawSphericalHarmonicsProvider.RawSphericalHarmonics: ...
    def pythonDecRef(self) -> None: ...
    @typing.overload
    def pythonExtension(self) -> int: ...
    @typing.overload
    def pythonExtension(self, long: int) -> None: ...

class PythonUnnormalizedSphericalHarmonics(UnnormalizedSphericalHarmonicsProvider.UnnormalizedSphericalHarmonics):
    def __init__(self): ...
    def finalize(self) -> None: ...
    def getDate(self) -> org.orekit.time.AbsoluteDate: ...
    def getUnnormalizedCnm(self, int: int, int2: int) -> float: ...
    def getUnnormalizedSnm(self, int: int, int2: int) -> float: ...
    def pythonDecRef(self) -> None: ...
    @typing.overload
    def pythonExtension(self) -> int: ...
    @typing.overload
    def pythonExtension(self, long: int) -> None: ...

class PythonUnnormalizedSphericalHarmonicsProvider(UnnormalizedSphericalHarmonicsProvider):
    def __init__(self): ...
    def finalize(self) -> None: ...
    def getAe(self) -> float: ...
    def getMaxDegree(self) -> int: ...
    def getMaxOrder(self) -> int: ...
    def getMu(self) -> float: ...
    def getOffset(self, absoluteDate: org.orekit.time.AbsoluteDate) -> float: ...
    def getReferenceDate(self) -> org.orekit.time.AbsoluteDate: ...
    def getTideSystem(self) -> TideSystem: ...
    def onDate(self, absoluteDate: org.orekit.time.AbsoluteDate) -> UnnormalizedSphericalHarmonicsProvider.UnnormalizedSphericalHarmonics: ...
    def pythonDecRef(self) -> None: ...
    @typing.overload
    def pythonExtension(self) -> int: ...
    @typing.overload
    def pythonExtension(self, long: int) -> None: ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.orekit.forces.gravity.potential")``.

    AstronomicalAmplitudeReader: typing.Type[AstronomicalAmplitudeReader]
    CachedNormalizedSphericalHarmonicsProvider: typing.Type[CachedNormalizedSphericalHarmonicsProvider]
    EGMFormatReader: typing.Type[EGMFormatReader]
    FESCHatEpsilonReader: typing.Type[FESCHatEpsilonReader]
    FESCnmSnmReader: typing.Type[FESCnmSnmReader]
    GRGSFormatReader: typing.Type[GRGSFormatReader]
    GravityFieldFactory: typing.Type[GravityFieldFactory]
    GravityFields: typing.Type[GravityFields]
    ICGEMFormatReader: typing.Type[ICGEMFormatReader]
    LazyLoadedGravityFields: typing.Type[LazyLoadedGravityFields]
    NormalizedSphericalHarmonicsProvider: typing.Type[NormalizedSphericalHarmonicsProvider]
    OceanLoadDeformationCoefficients: typing.Type[OceanLoadDeformationCoefficients]
    OceanTidesReader: typing.Type[OceanTidesReader]
    OceanTidesWave: typing.Type[OceanTidesWave]
    PotentialCoefficientsReader: typing.Type[PotentialCoefficientsReader]
    PythonGravityFields: typing.Type[PythonGravityFields]
    PythonNormalizedSphericalHarmonicsProvider: typing.Type[PythonNormalizedSphericalHarmonicsProvider]
    PythonPotentialCoefficientsReader: typing.Type[PythonPotentialCoefficientsReader]
    PythonRawSphericalHarmonicsProvider: typing.Type[PythonRawSphericalHarmonicsProvider]
    PythonSphericalHarmonicsProvider: typing.Type[PythonSphericalHarmonicsProvider]
    PythonTideSystemProvider: typing.Type[PythonTideSystemProvider]
    PythonUnnormalizedSphericalHarmonics: typing.Type[PythonUnnormalizedSphericalHarmonics]
    PythonUnnormalizedSphericalHarmonicsProvider: typing.Type[PythonUnnormalizedSphericalHarmonicsProvider]
    RawSphericalHarmonicsProvider: typing.Type[RawSphericalHarmonicsProvider]
    SHMFormatReader: typing.Type[SHMFormatReader]
    SphericalHarmonicsProvider: typing.Type[SphericalHarmonicsProvider]
    TideSystem: typing.Type[TideSystem]
    TideSystemProvider: typing.Type[TideSystemProvider]
    UnnormalizedSphericalHarmonicsProvider: typing.Type[UnnormalizedSphericalHarmonicsProvider]