package fibonacci;

import org.junit.jupiter.api.Test;
import org.openjdk.jmh.annotations.Benchmark;
import org.openjdk.jmh.annotations.BenchmarkMode;
import org.openjdk.jmh.annotations.Mode;

import static org.junit.jupiter.api.Assertions.*;

interface FibonacciTest {
  Fibonacci createFibonacci();

  @Test
  @Benchmark
  default void fibonacciPerformance()
  {
    FunctionalFibonacci functionalTest = new FunctionalFibonacci();
    MemoizedRecursionFibonacci memoTest = new MemoizedRecursionFibonacci();
    ImperativeFibonacci imperativeTest = new ImperativeFibonacci();
    RecursiveFibonacci recursiveTest = new RecursiveFibonacci();
  }

  @Test
  default void fibonacciTest() {

    assertAll(
            () -> assertEquals(1, createFibonacci().compute(0)),
            () -> assertEquals(1, createFibonacci().compute(1)),
            () -> assertEquals(1, createFibonacci().compute(2)),
            () -> assertEquals(5, createFibonacci().compute(5))
    );

  }

  @Test
  default void fibonacciForNegativeTest() {
    assertThrows(IllegalArgumentException.class,
    ()-> createFibonacci().compute(-1));
  }


}
