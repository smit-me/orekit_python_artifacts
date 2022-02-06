import org.hipparchus
import org.hipparchus.analysis.polynomials
import typing



_FieldHansenTesseralLinear__T = typing.TypeVar('_FieldHansenTesseralLinear__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldHansenTesseralLinear(typing.Generic[_FieldHansenTesseralLinear__T]):
    def __init__(self, int: int, int2: int, int3: int, int4: int, int5: int, field: org.hipparchus.Field[_FieldHansenTesseralLinear__T]): ...
    def computeInitValues(self, t: _FieldHansenTesseralLinear__T, t2: _FieldHansenTesseralLinear__T, t3: _FieldHansenTesseralLinear__T) -> None: ...
    def getDerivative(self, int: int, t: _FieldHansenTesseralLinear__T) -> _FieldHansenTesseralLinear__T: ...
    def getValue(self, int: int, t: _FieldHansenTesseralLinear__T) -> _FieldHansenTesseralLinear__T: ...

_FieldHansenThirdBodyLinear__T = typing.TypeVar('_FieldHansenThirdBodyLinear__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldHansenThirdBodyLinear(typing.Generic[_FieldHansenThirdBodyLinear__T]):
    def __init__(self, int: int, int2: int, field: org.hipparchus.Field[_FieldHansenThirdBodyLinear__T]): ...
    def computeInitValues(self, t: _FieldHansenThirdBodyLinear__T, t2: _FieldHansenThirdBodyLinear__T, t3: _FieldHansenThirdBodyLinear__T) -> None: ...
    def getDerivative(self, int: int, t: _FieldHansenThirdBodyLinear__T) -> _FieldHansenThirdBodyLinear__T: ...
    def getValue(self, int: int, t: _FieldHansenThirdBodyLinear__T) -> _FieldHansenThirdBodyLinear__T: ...

_FieldHansenZonalLinear__T = typing.TypeVar('_FieldHansenZonalLinear__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldHansenZonalLinear(typing.Generic[_FieldHansenZonalLinear__T]):
    def __init__(self, int: int, int2: int, field: org.hipparchus.Field[_FieldHansenZonalLinear__T]): ...
    def computeInitValues(self, t: _FieldHansenZonalLinear__T) -> None: ...
    def getDerivative(self, int: int, t: _FieldHansenZonalLinear__T) -> _FieldHansenZonalLinear__T: ...
    def getValue(self, int: int, t: _FieldHansenZonalLinear__T) -> _FieldHansenZonalLinear__T: ...

class HansenTesseralLinear:
    def __init__(self, int: int, int2: int, int3: int, int4: int, int5: int): ...
    def computeInitValues(self, double: float, double2: float, double3: float) -> None: ...
    def getDerivative(self, int: int, double: float) -> float: ...
    def getValue(self, int: int, double: float) -> float: ...

class HansenThirdBodyLinear:
    def __init__(self, int: int, int2: int): ...
    def computeInitValues(self, double: float, double2: float, double3: float) -> None: ...
    def getDerivative(self, int: int, double: float) -> float: ...
    def getValue(self, int: int, double: float) -> float: ...

class HansenUtilities:
    ONE: typing.ClassVar[org.hipparchus.analysis.polynomials.PolynomialFunction] = ...
    ZERO: typing.ClassVar[org.hipparchus.analysis.polynomials.PolynomialFunction] = ...
    @staticmethod
    def buildIdentityMatrix2() -> 'PolynomialFunctionMatrix': ...
    @staticmethod
    def buildIdentityMatrix4() -> 'PolynomialFunctionMatrix': ...
    @staticmethod
    def buildZeroMatrix2() -> 'PolynomialFunctionMatrix': ...
    @staticmethod
    def buildZeroMatrix4() -> 'PolynomialFunctionMatrix': ...

class HansenZonalLinear:
    def __init__(self, int: int, int2: int): ...
    def computeInitValues(self, double: float) -> None: ...
    def getDerivative(self, int: int, double: float) -> float: ...
    def getValue(self, int: int, double: float) -> float: ...

class PolynomialFunctionMatrix:
    def add(self, polynomialFunctionMatrix: 'PolynomialFunctionMatrix') -> 'PolynomialFunctionMatrix': ...
    def getElem(self, int: int, int2: int) -> org.hipparchus.analysis.polynomials.PolynomialFunction: ...
    def getMatrixLine(self, int: int) -> typing.List[org.hipparchus.analysis.polynomials.PolynomialFunction]: ...
    def multiply(self, polynomialFunctionMatrix: 'PolynomialFunctionMatrix') -> 'PolynomialFunctionMatrix': ...
    def setElem(self, int: int, int2: int, polynomialFunction: org.hipparchus.analysis.polynomials.PolynomialFunction) -> None: ...
    def setMatrix(self, polynomialFunctionArray: typing.List[typing.List[org.hipparchus.analysis.polynomials.PolynomialFunction]]) -> None: ...
    def setMatrixLine(self, int: int, polynomialFunctionArray: typing.List[org.hipparchus.analysis.polynomials.PolynomialFunction]) -> None: ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.orekit.propagation.semianalytical.dsst.utilities.hansen")``.

    FieldHansenTesseralLinear: typing.Type[FieldHansenTesseralLinear]
    FieldHansenThirdBodyLinear: typing.Type[FieldHansenThirdBodyLinear]
    FieldHansenZonalLinear: typing.Type[FieldHansenZonalLinear]
    HansenTesseralLinear: typing.Type[HansenTesseralLinear]
    HansenThirdBodyLinear: typing.Type[HansenThirdBodyLinear]
    HansenUtilities: typing.Type[HansenUtilities]
    HansenZonalLinear: typing.Type[HansenZonalLinear]
    PolynomialFunctionMatrix: typing.Type[PolynomialFunctionMatrix]