import java.io
import java.lang
import java.util
import org.hipparchus.random
import org.hipparchus.stat.descriptive
import org.hipparchus.stat.ranking
import org.hipparchus.util
import typing



class Max(org.hipparchus.stat.descriptive.AbstractStorelessUnivariateStatistic, org.hipparchus.stat.descriptive.AggregatableStatistic['Max'], java.io.Serializable):
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, max: 'Max'): ...
    @typing.overload
    def aggregate(self, iterable: typing.Union[java.lang.Iterable[typing.Any], typing.Sequence[typing.Any], typing.Set[typing.Any]]) -> None: ...
    @typing.overload
    def aggregate(self, tArray: typing.List[typing.Any]) -> None: ...
    @typing.overload
    def aggregate(self, max: 'Max') -> None: ...
    def clear(self) -> None: ...
    def copy(self) -> 'Max': ...
    @typing.overload
    def evaluate(self, doubleArray: typing.List[float]) -> float: ...
    @typing.overload
    def evaluate(self, doubleArray: typing.List[float], int: int, int2: int) -> float: ...
    def getN(self) -> int: ...
    def getResult(self) -> float: ...
    def increment(self, double: float) -> None: ...

class Median(org.hipparchus.stat.descriptive.AbstractUnivariateStatistic, java.io.Serializable):
    def __init__(self): ...
    def copy(self) -> 'Median': ...
    @typing.overload
    def evaluate(self, doubleArray: typing.List[float]) -> float: ...
    @typing.overload
    def evaluate(self) -> float: ...
    @typing.overload
    def evaluate(self, doubleArray: typing.List[float], int: int, int2: int) -> float: ...
    def getEstimationType(self) -> 'Percentile.EstimationType': ...
    def getKthSelector(self) -> org.hipparchus.util.KthSelector: ...
    def getNaNStrategy(self) -> org.hipparchus.stat.ranking.NaNStrategy: ...
    def withEstimationType(self, estimationType: 'Percentile.EstimationType') -> 'Median': ...
    def withKthSelector(self, kthSelector: org.hipparchus.util.KthSelector) -> 'Median': ...
    def withNaNStrategy(self, naNStrategy: org.hipparchus.stat.ranking.NaNStrategy) -> 'Median': ...

class Min(org.hipparchus.stat.descriptive.AbstractStorelessUnivariateStatistic, org.hipparchus.stat.descriptive.AggregatableStatistic['Min'], java.io.Serializable):
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, min: 'Min'): ...
    @typing.overload
    def aggregate(self, iterable: typing.Union[java.lang.Iterable[typing.Any], typing.Sequence[typing.Any], typing.Set[typing.Any]]) -> None: ...
    @typing.overload
    def aggregate(self, tArray: typing.List[typing.Any]) -> None: ...
    @typing.overload
    def aggregate(self, min: 'Min') -> None: ...
    def clear(self) -> None: ...
    def copy(self) -> 'Min': ...
    @typing.overload
    def evaluate(self, doubleArray: typing.List[float]) -> float: ...
    @typing.overload
    def evaluate(self, doubleArray: typing.List[float], int: int, int2: int) -> float: ...
    def getN(self) -> int: ...
    def getResult(self) -> float: ...
    def increment(self, double: float) -> None: ...

class PSquarePercentile(org.hipparchus.stat.descriptive.AbstractStorelessUnivariateStatistic, org.hipparchus.stat.descriptive.StorelessUnivariateStatistic, java.io.Serializable):
    @typing.overload
    def __init__(self, double: float): ...
    @typing.overload
    def __init__(self, pSquarePercentile: 'PSquarePercentile'): ...
    def clear(self) -> None: ...
    def copy(self) -> 'PSquarePercentile': ...
    def equals(self, object: typing.Any) -> bool: ...
    def getN(self) -> int: ...
    def getQuantile(self) -> float: ...
    def getResult(self) -> float: ...
    def hashCode(self) -> int: ...
    def increment(self, double: float) -> None: ...
    @staticmethod
    def newMarkers(list: java.util.List[float], double: float) -> 'PSquarePercentile.PSquareMarkers': ...
    def quantile(self) -> float: ...
    def toString(self) -> str: ...
    class PSquareMarkers: ...

class Percentile(org.hipparchus.stat.descriptive.AbstractUnivariateStatistic, java.io.Serializable):
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, double: float): ...
    @typing.overload
    def __init__(self, percentile: 'Percentile'): ...
    def copy(self) -> 'Percentile': ...
    @typing.overload
    def evaluate(self, doubleArray: typing.List[float]) -> float: ...
    @typing.overload
    def evaluate(self) -> float: ...
    @typing.overload
    def evaluate(self, double: float) -> float: ...
    @typing.overload
    def evaluate(self, doubleArray: typing.List[float], double2: float) -> float: ...
    @typing.overload
    def evaluate(self, doubleArray: typing.List[float], int: int, int2: int) -> float: ...
    @typing.overload
    def evaluate(self, doubleArray: typing.List[float], int: int, int2: int, double2: float) -> float: ...
    def getEstimationType(self) -> 'Percentile.EstimationType': ...
    def getKthSelector(self) -> org.hipparchus.util.KthSelector: ...
    def getNaNStrategy(self) -> org.hipparchus.stat.ranking.NaNStrategy: ...
    def getPivotingStrategy(self) -> org.hipparchus.util.PivotingStrategy: ...
    def getQuantile(self) -> float: ...
    @typing.overload
    def setData(self, doubleArray: typing.List[float]) -> None: ...
    @typing.overload
    def setData(self, doubleArray: typing.List[float], int: int, int2: int) -> None: ...
    def setQuantile(self, double: float) -> None: ...
    def withEstimationType(self, estimationType: 'Percentile.EstimationType') -> 'Percentile': ...
    def withKthSelector(self, kthSelector: org.hipparchus.util.KthSelector) -> 'Percentile': ...
    def withNaNStrategy(self, naNStrategy: org.hipparchus.stat.ranking.NaNStrategy) -> 'Percentile': ...
    class EstimationType(java.lang.Enum['Percentile.EstimationType']):
        LEGACY: typing.ClassVar['Percentile.EstimationType'] = ...
        R_1: typing.ClassVar['Percentile.EstimationType'] = ...
        R_2: typing.ClassVar['Percentile.EstimationType'] = ...
        R_3: typing.ClassVar['Percentile.EstimationType'] = ...
        R_4: typing.ClassVar['Percentile.EstimationType'] = ...
        R_5: typing.ClassVar['Percentile.EstimationType'] = ...
        R_6: typing.ClassVar['Percentile.EstimationType'] = ...
        R_7: typing.ClassVar['Percentile.EstimationType'] = ...
        R_8: typing.ClassVar['Percentile.EstimationType'] = ...
        R_9: typing.ClassVar['Percentile.EstimationType'] = ...
        def evaluate(self, doubleArray: typing.List[float], double2: float, kthSelector: org.hipparchus.util.KthSelector) -> float: ...
        _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
        @typing.overload
        @staticmethod
        def valueOf(class_: typing.Type[_valueOf_0__T], string: str) -> _valueOf_0__T: ...
        @typing.overload
        @staticmethod
        def valueOf(string: str) -> 'Percentile.EstimationType': ...
        @staticmethod
        def values() -> typing.List['Percentile.EstimationType']: ...

class RandomPercentile(org.hipparchus.stat.descriptive.AbstractStorelessUnivariateStatistic, org.hipparchus.stat.descriptive.StorelessUnivariateStatistic, org.hipparchus.stat.descriptive.AggregatableStatistic['RandomPercentile'], java.io.Serializable):
    DEFAULT_EPSILON: typing.ClassVar[float] = ...
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, double: float): ...
    @typing.overload
    def __init__(self, double: float, randomGenerator: org.hipparchus.random.RandomGenerator): ...
    @typing.overload
    def __init__(self, randomGenerator: org.hipparchus.random.RandomGenerator): ...
    @typing.overload
    def __init__(self, randomPercentile: 'RandomPercentile'): ...
    @typing.overload
    def aggregate(self, iterable: typing.Union[java.lang.Iterable[typing.Any], typing.Sequence[typing.Any], typing.Set[typing.Any]]) -> None: ...
    @typing.overload
    def aggregate(self, tArray: typing.List[typing.Any]) -> None: ...
    @typing.overload
    def aggregate(self, randomPercentile: 'RandomPercentile') -> None: ...
    def clear(self) -> None: ...
    def copy(self) -> 'RandomPercentile': ...
    @typing.overload
    def evaluate(self, doubleArray: typing.List[float]) -> float: ...
    @typing.overload
    def evaluate(self, double: float, doubleArray: typing.List[float]) -> float: ...
    @typing.overload
    def evaluate(self, double: float, doubleArray: typing.List[float], int: int, int2: int) -> float: ...
    @typing.overload
    def evaluate(self, doubleArray: typing.List[float], int: int, int2: int) -> float: ...
    def getAggregateN(self, collection: typing.Union[java.util.Collection['RandomPercentile'], typing.Sequence['RandomPercentile'], typing.Set['RandomPercentile']]) -> float: ...
    def getAggregateQuantileRank(self, double: float, collection: typing.Union[java.util.Collection['RandomPercentile'], typing.Sequence['RandomPercentile'], typing.Set['RandomPercentile']]) -> float: ...
    def getAggregateRank(self, double: float, collection: typing.Union[java.util.Collection['RandomPercentile'], typing.Sequence['RandomPercentile'], typing.Set['RandomPercentile']]) -> float: ...
    def getN(self) -> int: ...
    def getQuantileRank(self, double: float) -> float: ...
    def getRank(self, double: float) -> float: ...
    @typing.overload
    def getResult(self) -> float: ...
    @typing.overload
    def getResult(self, double: float) -> float: ...
    def increment(self, double: float) -> None: ...
    @staticmethod
    def maxValuesRetained(double: float) -> int: ...
    def reduce(self, double: float, collection: typing.Union[java.util.Collection['RandomPercentile'], typing.Sequence['RandomPercentile'], typing.Set['RandomPercentile']]) -> float: ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.hipparchus.stat.descriptive.rank")``.

    Max: typing.Type[Max]
    Median: typing.Type[Median]
    Min: typing.Type[Min]
    PSquarePercentile: typing.Type[PSquarePercentile]
    Percentile: typing.Type[Percentile]
    RandomPercentile: typing.Type[RandomPercentile]