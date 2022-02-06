import java.util
import org.orekit.data
import org.orekit.files.ccsds.ndm
import org.orekit.files.ccsds.section
import org.orekit.files.ccsds.utils
import org.orekit.files.ccsds.utils.lexical
import org.orekit.utils
import typing



_AbstractMessageParser__T = typing.TypeVar('_AbstractMessageParser__T')  # <T>
class AbstractMessageParser(org.orekit.files.ccsds.utils.lexical.MessageParser[_AbstractMessageParser__T], typing.Generic[_AbstractMessageParser__T]):
    def anticipateNext(self, processingState: 'ProcessingState') -> None: ...
    def getCurrent(self) -> 'ProcessingState': ...
    def getFormatVersionKey(self) -> str: ...
    def getSpecialXmlElementsBuilders(self) -> java.util.Map[str, org.orekit.files.ccsds.utils.lexical.XmlTokenBuilder]: ...
    def parseMessage(self, dataSource: org.orekit.data.DataSource) -> _AbstractMessageParser__T: ...
    def process(self, parseToken: org.orekit.files.ccsds.utils.lexical.ParseToken) -> None: ...
    def setEndTagSeen(self, boolean: bool) -> None: ...
    def setFallback(self, processingState: 'ProcessingState') -> None: ...
    def wasEndTagSeen(self) -> bool: ...

class ProcessingState:
    def processToken(self, parseToken: org.orekit.files.ccsds.utils.lexical.ParseToken) -> bool: ...

_AbstractConstituentParser__T = typing.TypeVar('_AbstractConstituentParser__T', bound=org.orekit.files.ccsds.ndm.NdmConstituent)  # <T>
_AbstractConstituentParser__P = typing.TypeVar('_AbstractConstituentParser__P', bound='AbstractConstituentParser')  # <P>
class AbstractConstituentParser(AbstractMessageParser[_AbstractConstituentParser__T], typing.Generic[_AbstractConstituentParser__T, _AbstractConstituentParser__P]):
    def finalizeData(self) -> bool: ...
    def finalizeHeader(self) -> bool: ...
    def finalizeMetadata(self) -> bool: ...
    def getConventions(self) -> org.orekit.utils.IERSConventions: ...
    def getDataContext(self) -> org.orekit.data.DataContext: ...
    def getHeader(self) -> org.orekit.files.ccsds.section.Header: ...
    def getParsedUnitsBehavior(self) -> org.orekit.files.ccsds.ndm.ParsedUnitsBehavior: ...
    def inData(self) -> bool: ...
    def inHeader(self) -> bool: ...
    def inMetadata(self) -> bool: ...
    def isSimpleEOP(self) -> bool: ...
    def prepareData(self) -> bool: ...
    def prepareHeader(self) -> bool: ...
    def prepareMetadata(self) -> bool: ...

class ErrorState(ProcessingState):
    def __init__(self): ...
    def processToken(self, parseToken: org.orekit.files.ccsds.utils.lexical.ParseToken) -> bool: ...

_PythonAbstractMessageParser__T = typing.TypeVar('_PythonAbstractMessageParser__T')  # <T>
class PythonAbstractMessageParser(AbstractMessageParser[_PythonAbstractMessageParser__T], typing.Generic[_PythonAbstractMessageParser__T]):
    def build(self) -> _PythonAbstractMessageParser__T: ...
    def finalize(self) -> None: ...
    def pythonDecRef(self) -> None: ...
    @typing.overload
    def pythonExtension(self) -> int: ...
    @typing.overload
    def pythonExtension(self, long: int) -> None: ...
    def reset(self, fileFormat: org.orekit.files.ccsds.utils.FileFormat) -> None: ...

_PythonAbstractConstituentParser__T = typing.TypeVar('_PythonAbstractConstituentParser__T', bound=org.orekit.files.ccsds.ndm.NdmConstituent)  # <T>
_PythonAbstractConstituentParser__P = typing.TypeVar('_PythonAbstractConstituentParser__P', bound=AbstractConstituentParser)  # <P>
class PythonAbstractConstituentParser(AbstractConstituentParser[_PythonAbstractConstituentParser__T, _PythonAbstractConstituentParser__P], typing.Generic[_PythonAbstractConstituentParser__T, _PythonAbstractConstituentParser__P]):
    def build(self) -> _PythonAbstractConstituentParser__T: ...
    def finalize(self) -> None: ...
    def finalizeData(self) -> bool: ...
    def finalizeHeader(self) -> bool: ...
    def finalizeMetadata(self) -> bool: ...
    def getHeader(self) -> org.orekit.files.ccsds.section.Header: ...
    def inData(self) -> bool: ...
    def inHeader(self) -> bool: ...
    def inMetadata(self) -> bool: ...
    def prepareData(self) -> bool: ...
    def prepareHeader(self) -> bool: ...
    def prepareMetadata(self) -> bool: ...
    def pythonDecRef(self) -> None: ...
    @typing.overload
    def pythonExtension(self) -> int: ...
    @typing.overload
    def pythonExtension(self, long: int) -> None: ...
    def reset(self, fileFormat: org.orekit.files.ccsds.utils.FileFormat) -> None: ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.orekit.files.ccsds.utils.parsing")``.

    AbstractConstituentParser: typing.Type[AbstractConstituentParser]
    AbstractMessageParser: typing.Type[AbstractMessageParser]
    ErrorState: typing.Type[ErrorState]
    ProcessingState: typing.Type[ProcessingState]
    PythonAbstractConstituentParser: typing.Type[PythonAbstractConstituentParser]
    PythonAbstractMessageParser: typing.Type[PythonAbstractMessageParser]