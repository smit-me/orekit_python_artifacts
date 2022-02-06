import org.orekit.gnss.metric.messages.rtcm
import org.orekit.gnss.metric.messages.rtcm.ephemeris.utils
import org.orekit.propagation.analytical.gnss.data
import org.orekit.time
import typing



class RtcmEphemerisData(org.orekit.gnss.metric.messages.rtcm.RtcmData):
    def __init__(self): ...
    def getAccuracyProvider(self) -> org.orekit.gnss.metric.messages.rtcm.ephemeris.utils.AccuracyProvider: ...
    def getSatelliteID(self) -> int: ...
    def setAccuracyProvider(self, accuracyProvider: org.orekit.gnss.metric.messages.rtcm.ephemeris.utils.AccuracyProvider) -> None: ...
    def setSatelliteID(self, int: int) -> None: ...

_RtcmEphemerisMessage__D = typing.TypeVar('_RtcmEphemerisMessage__D', bound=RtcmEphemerisData)  # <D>
class RtcmEphemerisMessage(org.orekit.gnss.metric.messages.rtcm.RtcmMessage[_RtcmEphemerisMessage__D], typing.Generic[_RtcmEphemerisMessage__D]):
    def __init__(self, int: int, d: _RtcmEphemerisMessage__D): ...
    def getEphemerisData(self) -> _RtcmEphemerisMessage__D: ...

class Rtcm1019(RtcmEphemerisMessage['Rtcm1019Data']):
    def __init__(self, int: int, rtcm1019Data: 'Rtcm1019Data'): ...

class Rtcm1019Data(RtcmEphemerisData):
    def __init__(self): ...
    def getGpsCodeOnL2(self) -> int: ...
    def getGpsFitInterval(self) -> int: ...
    def getGpsL2PDataFlag(self) -> bool: ...
    @typing.overload
    def getGpsNavigationMessage(self) -> org.orekit.propagation.analytical.gnss.data.GPSNavigationMessage: ...
    @typing.overload
    def getGpsNavigationMessage(self, timeScales: org.orekit.time.TimeScales) -> org.orekit.propagation.analytical.gnss.data.GPSNavigationMessage: ...
    def getGpsToc(self) -> float: ...
    def setGpsCodeOnL2(self, int: int) -> None: ...
    def setGpsFitInterval(self, int: int) -> None: ...
    def setGpsL2PDataFlag(self, boolean: bool) -> None: ...
    def setGpsNavigationMessage(self, gPSNavigationMessage: org.orekit.propagation.analytical.gnss.data.GPSNavigationMessage) -> None: ...
    def setGpsToc(self, double: float) -> None: ...

class Rtcm1020(RtcmEphemerisMessage['Rtcm1020Data']):
    def __init__(self, int: int, rtcm1020Data: 'Rtcm1020Data'): ...

class Rtcm1020Data(RtcmEphemerisData):
    def __init__(self): ...
    def areAdditionalDataAvailable(self) -> bool: ...
    def getBN(self) -> int: ...
    def getDeltaTN(self) -> float: ...
    def getEn(self) -> int: ...
    def getFT(self) -> int: ...
    @typing.overload
    def getGlonassNavigationMessage(self) -> org.orekit.propagation.analytical.gnss.data.GLONASSNavigationMessage: ...
    @typing.overload
    def getGlonassNavigationMessage(self, timeScales: org.orekit.time.TimeScales) -> org.orekit.propagation.analytical.gnss.data.GLONASSNavigationMessage: ...
    def getLNFifthString(self) -> int: ...
    def getLNThirdString(self) -> int: ...
    def getM(self) -> int: ...
    def getN4(self) -> int: ...
    def getNA(self) -> int: ...
    def getNt(self) -> int: ...
    def getP(self) -> int: ...
    def getP1(self) -> int: ...
    def getP2(self) -> int: ...
    def getP3(self) -> int: ...
    def getP4(self) -> int: ...
    def getTauC(self) -> float: ...
    def getTauGps(self) -> float: ...
    def getTk(self) -> float: ...
    def isHealthAvailable(self) -> bool: ...
    def setAreAdditionalDataAvailable(self, boolean: bool) -> None: ...
    def setBN(self, int: int) -> None: ...
    def setDeltaTN(self, double: float) -> None: ...
    def setEn(self, int: int) -> None: ...
    def setFT(self, int: int) -> None: ...
    def setGlonassNavigationMessage(self, gLONASSNavigationMessage: org.orekit.propagation.analytical.gnss.data.GLONASSNavigationMessage) -> None: ...
    def setHealthAvailabilityIndicator(self, boolean: bool) -> None: ...
    def setLNFifthString(self, int: int) -> None: ...
    def setLNThirdString(self, int: int) -> None: ...
    def setM(self, int: int) -> None: ...
    def setN4(self, int: int) -> None: ...
    def setNA(self, int: int) -> None: ...
    def setNt(self, int: int) -> None: ...
    def setP(self, int: int) -> None: ...
    def setP1(self, int: int) -> None: ...
    def setP2(self, int: int) -> None: ...
    def setP3(self, int: int) -> None: ...
    def setP4(self, int: int) -> None: ...
    def setTauC(self, double: float) -> None: ...
    def setTauGps(self, double: float) -> None: ...
    def setTk(self, double: float) -> None: ...

class Rtcm1042(RtcmEphemerisMessage['Rtcm1042Data']):
    def __init__(self, int: int, rtcm1042Data: 'Rtcm1042Data'): ...

class Rtcm1042Data(RtcmEphemerisData):
    def __init__(self): ...
    @typing.overload
    def getBeidouNavigationMessage(self) -> org.orekit.propagation.analytical.gnss.data.BeidouNavigationMessage: ...
    @typing.overload
    def getBeidouNavigationMessage(self, timeScales: org.orekit.time.TimeScales) -> org.orekit.propagation.analytical.gnss.data.BeidouNavigationMessage: ...
    def getBeidouToc(self) -> float: ...
    def getSvHealth(self) -> float: ...
    def setBeidouNavigationMessage(self, beidouNavigationMessage: org.orekit.propagation.analytical.gnss.data.BeidouNavigationMessage) -> None: ...
    def setBeidouToc(self, double: float) -> None: ...
    def setSvHealth(self, double: float) -> None: ...

class Rtcm1044(RtcmEphemerisMessage['Rtcm1044Data']):
    def __init__(self, int: int, rtcm1044Data: 'Rtcm1044Data'): ...

class Rtcm1044Data(RtcmEphemerisData):
    def __init__(self): ...
    def getQzssCodeOnL2(self) -> int: ...
    def getQzssFitInterval(self) -> int: ...
    @typing.overload
    def getQzssNavigationMessage(self) -> org.orekit.propagation.analytical.gnss.data.QZSSNavigationMessage: ...
    @typing.overload
    def getQzssNavigationMessage(self, timeScales: org.orekit.time.TimeScales) -> org.orekit.propagation.analytical.gnss.data.QZSSNavigationMessage: ...
    def getQzssToc(self) -> float: ...
    def setQzssCodeOnL2(self, int: int) -> None: ...
    def setQzssFitInterval(self, int: int) -> None: ...
    def setQzssNavigationMessage(self, qZSSNavigationMessage: org.orekit.propagation.analytical.gnss.data.QZSSNavigationMessage) -> None: ...
    def setQzssToc(self, double: float) -> None: ...

class Rtcm1045(RtcmEphemerisMessage['Rtcm1045Data']):
    def __init__(self, int: int, rtcm1045Data: 'Rtcm1045Data'): ...

class Rtcm1045Data(RtcmEphemerisData):
    def __init__(self): ...
    def getGalileoDataValidityStatus(self) -> int: ...
    @typing.overload
    def getGalileoNavigationMessage(self) -> org.orekit.propagation.analytical.gnss.data.GalileoNavigationMessage: ...
    @typing.overload
    def getGalileoNavigationMessage(self, timeScales: org.orekit.time.TimeScales) -> org.orekit.propagation.analytical.gnss.data.GalileoNavigationMessage: ...
    def getGalileoToc(self) -> float: ...
    def setGalileoDataValidityStatus(self, int: int) -> None: ...
    def setGalileoNavigationMessage(self, galileoNavigationMessage: org.orekit.propagation.analytical.gnss.data.GalileoNavigationMessage) -> None: ...
    def setGalileoToc(self, double: float) -> None: ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.orekit.gnss.metric.messages.rtcm.ephemeris")``.

    Rtcm1019: typing.Type[Rtcm1019]
    Rtcm1019Data: typing.Type[Rtcm1019Data]
    Rtcm1020: typing.Type[Rtcm1020]
    Rtcm1020Data: typing.Type[Rtcm1020Data]
    Rtcm1042: typing.Type[Rtcm1042]
    Rtcm1042Data: typing.Type[Rtcm1042Data]
    Rtcm1044: typing.Type[Rtcm1044]
    Rtcm1044Data: typing.Type[Rtcm1044Data]
    Rtcm1045: typing.Type[Rtcm1045]
    Rtcm1045Data: typing.Type[Rtcm1045Data]
    RtcmEphemerisData: typing.Type[RtcmEphemerisData]
    RtcmEphemerisMessage: typing.Type[RtcmEphemerisMessage]
    utils: org.orekit.gnss.metric.messages.rtcm.ephemeris.utils.__module_protocol__