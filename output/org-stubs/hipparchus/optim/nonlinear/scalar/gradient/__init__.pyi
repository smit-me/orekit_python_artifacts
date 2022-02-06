import java.lang
import org.hipparchus.optim
import org.hipparchus.optim.nonlinear.scalar
import typing



class Preconditioner:
    def precondition(self, doubleArray: typing.List[float], doubleArray2: typing.List[float]) -> typing.List[float]: ...

class NonLinearConjugateGradientOptimizer(org.hipparchus.optim.nonlinear.scalar.GradientMultivariateOptimizer):
    @typing.overload
    def __init__(self, formula: 'NonLinearConjugateGradientOptimizer.Formula', convergenceChecker: org.hipparchus.optim.ConvergenceChecker[org.hipparchus.optim.PointValuePair]): ...
    @typing.overload
    def __init__(self, formula: 'NonLinearConjugateGradientOptimizer.Formula', convergenceChecker: org.hipparchus.optim.ConvergenceChecker[org.hipparchus.optim.PointValuePair], double: float, double2: float, double3: float): ...
    @typing.overload
    def __init__(self, formula: 'NonLinearConjugateGradientOptimizer.Formula', convergenceChecker: org.hipparchus.optim.ConvergenceChecker[org.hipparchus.optim.PointValuePair], double: float, double2: float, double3: float, preconditioner: Preconditioner): ...
    @typing.overload
    def optimize(self) -> typing.Any: ...
    @typing.overload
    def optimize(self, optimizationDataArray: typing.List[org.hipparchus.optim.OptimizationData]) -> org.hipparchus.optim.PointValuePair: ...
    class Formula(java.lang.Enum['NonLinearConjugateGradientOptimizer.Formula']):
        FLETCHER_REEVES: typing.ClassVar['NonLinearConjugateGradientOptimizer.Formula'] = ...
        POLAK_RIBIERE: typing.ClassVar['NonLinearConjugateGradientOptimizer.Formula'] = ...
        _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
        @typing.overload
        @staticmethod
        def valueOf(class_: typing.Type[_valueOf_0__T], string: str) -> _valueOf_0__T: ...
        @typing.overload
        @staticmethod
        def valueOf(string: str) -> 'NonLinearConjugateGradientOptimizer.Formula': ...
        @staticmethod
        def values() -> typing.List['NonLinearConjugateGradientOptimizer.Formula']: ...
    class IdentityPreconditioner(Preconditioner):
        def __init__(self): ...
        def precondition(self, doubleArray: typing.List[float], doubleArray2: typing.List[float]) -> typing.List[float]: ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.hipparchus.optim.nonlinear.scalar.gradient")``.

    NonLinearConjugateGradientOptimizer: typing.Type[NonLinearConjugateGradientOptimizer]
    Preconditioner: typing.Type[Preconditioner]