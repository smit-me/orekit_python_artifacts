import java.util
import org.orekit.gnss.metric.messages.ssr
import org.orekit.models.earth.ionosphere
import typing



class SsrIm201(org.orekit.gnss.metric.messages.ssr.SsrMessage['SsrIm201Header', 'SsrIm201Data']):
    def __init__(self, int: int, ssrIm201Header: 'SsrIm201Header', list: java.util.List['SsrIm201Data']): ...
    def getIonosphericModel(self) -> org.orekit.models.earth.ionosphere.SsrVtecIonosphericModel: ...

class SsrIm201Data(org.orekit.gnss.metric.messages.ssr.SsrData):
    def __init__(self): ...
    def getCnm(self) -> typing.List[typing.List[float]]: ...
    def getHeightIonosphericLayer(self) -> float: ...
    def getSnm(self) -> typing.List[typing.List[float]]: ...
    def getSphericalHarmonicsDegree(self) -> int: ...
    def getSphericalHarmonicsOrder(self) -> int: ...
    def setCnm(self, doubleArray: typing.List[typing.List[float]]) -> None: ...
    def setHeightIonosphericLayer(self, double: float) -> None: ...
    def setSnm(self, doubleArray: typing.List[typing.List[float]]) -> None: ...
    def setSphericalHarmonicsDegree(self, int: int) -> None: ...
    def setSphericalHarmonicsOrder(self, int: int) -> None: ...

class SsrIm201Header(org.orekit.gnss.metric.messages.ssr.SsrHeader):
    def __init__(self): ...
    def getNumberOfIonosphericLayers(self) -> int: ...
    def getVtecQualityIndicator(self) -> float: ...
    def setNumberOfIonosphericLayers(self, int: int) -> None: ...
    def setVtecQualityIndicator(self, double: float) -> None: ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.orekit.gnss.metric.messages.ssr.subtype")``.

    SsrIm201: typing.Type[SsrIm201]
    SsrIm201Data: typing.Type[SsrIm201Data]
    SsrIm201Header: typing.Type[SsrIm201Header]